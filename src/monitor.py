import socket
import time


def measure_dns_resolution(host):
    """Measures the time taken to resolve a hostname
    to an IP address.
    """
    metrics = {
        "host": host,
        "ip": None,
        "resolution_ms": 0.0,
        "status": "FAIL",
    }

    start_time = time.perf_counter()
    try:
        # Per Canonical standards: Direct low-level OS socket resolution
        metrics["ip"] = socket.gethostbyname(host)
        duration = time.perf_counter() - start_time
        metrics["resolution_ms"] = round(duration * 1000, 2)
        metrics["status"] = "PASS"
    except socket.gaierror:
        # Handles host unreachable / offline states cleanly
        metrics["status"] = "FAIL"

    return metrics


def check_tcp_port(host, port, timeout=2.0):
    """Performs a raw TCP handshake to check port availability."""
    metrics = {"port": port, "latency_ms": 0.0, "status": "FAIL"}

    start_time = time.perf_counter()
    # Use a context manager to ensure the descriptor closes immediately
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            duration = time.perf_counter() - start_time
            metrics["latency_ms"] = round(duration * 1000, 2)
            metrics["status"] = "PASS"
        except (socket.timeout, ConnectionRefusedError, OSError):
            metrics["status"] = "FAIL"

    return metrics


def gather_network_metrics():
    """Aggregates low-level network performance metrics."""
    # Target infrastructure mirrors frequently used by Ubuntu tools
    target_host = "changelogs.ubuntu.com"

    dns_report = measure_dns_resolution(target_host)

    # Check standard production endpoints: HTTP (80) and HTTPS (443)
    http_report = check_tcp_port(target_host, 80)
    https_report = check_tcp_port(target_host, 443)

    return {
        "timestamp": int(time.time()),
        "target": target_host,
        "dns": dns_report,
        "ports": {"80": http_report, "443": https_report},
    }
