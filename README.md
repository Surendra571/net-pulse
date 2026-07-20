# net-pulse 🚀
> **Lightweight Network Telemetry Pipeline**

A high-performance, zero-dependency network performance streaming engine designed for Linux environment pipeline integration. `net-pulse` interacts directly with system-native sockets using only the Python Standard Library to gather ultra-low-level network metrics, streaming them as structured JSON data optimized for tools like `jq`.


## Features

- **Zero-Dependency Architecture:** Built entirely on the Python Standard Library (`socket`, `json`, `time`, `sys`). No external package overhead.
- **Low-Level Telemetry:** Measures true OS-level DNS resolution performance and raw TCP handshake latencies.
- **Stream-Optimized Output:** Emits compact JSON strings with instant standard output flushes, ensuring seamless integration with standard Unix pipelines.
- **Enterprise Hygiene:** 100% compliant with PEP 8 standards, verified by `black` and `flake8`.


  

## Installation & Setup

Clone the repository and navigate into the project root:

```bash
git clone [https://github.com/Surendra571/net-pulse.git](https://github.com/Surendra571/net-pulse.git)
cd net-pulse

```




*(Optional) Install development tools if you wish to run formatting or linting checks:*

```bash
pip install -r requirements.txt

```


## Usage

### Real-Time Streaming (Human Readable)

Pipe the engine's stream directly into `jq` for beautifully formatted, real-time JSON metrics:

```bash
python run.py | jq

```



### Production Data Pipeline Output Example

When active, the stream provides structural insights into connection states, latency spikes, and OS-level optimizations (such as DNS caching):

```json
{
  "timestamp": 1784529478,
  "target": "changelogs.ubuntu.com",
  "dns": {
    "host": "changelogs.ubuntu.com",
    "ip": "185.125.190.49",
    "resolution_ms": 8.17,
    "status": "PASS"
  },
  "ports": {
    "80": {
      "port": 80,
      "latency_ms": 1230.66,
      "status": "PASS"
    },
    "443": {
      "port": 443,
      "latency_ms": 256.4,
      "status": "PASS"
    }
  }
}
{
  "timestamp": 1784529488,
  "target": "changelogs.ubuntu.com",
  "dns": {
    "host": "changelogs.ubuntu.com",
    "ip": "185.125.190.49",
    "resolution_ms": 0.46,
    "status": "PASS"
  },
  "ports": {
    "80": {
      "port": 80,
      "latency_ms": 207.9,
      "status": "PASS"
    },
    "443": {
      "port": 443,
      "latency_ms": 218.55,
      "status": "PASS"
    }
  }
}

```



## Development & Code Quality

Maintain codebase hygiene using the integrated workspace tooling:

```bash
# Auto-format codebase
black src/ run.py

# Lint compliance validation
flake8 src/ run.py
```




This provides a comprehensive summary of the project's engineering choices while embedding the pipeline output to demonstrate its functionality instantly.
