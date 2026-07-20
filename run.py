import time
import sys
from src.monitor import gather_network_metrics
from src.exporter import stream_json_metrics


def main():
    """Main execution loop for the net-pulse performance exporter."""
    # Production-ready interval (e.g., every 10 seconds)
    interval = 10

    try:
        while True:
            # 1. Gather raw low-level metrics
            metrics = gather_network_metrics()

            # 2. Stream structured JSON to stdout
            stream_json_metrics(metrics)

            # 3. Rest until the next collection cycle
            time.sleep(interval)

    except KeyboardInterrupt:
        # Catch standard Ctrl+C interrupts to exit cleanly
        sys.exit(0)
    except Exception as e:
        # Catch top-level unexpected failures to log them to stderr
        import json

        error_msg = {
            "status": "FATAL",
            "message": f"Unexpected runtime error: {str(e)}",
        }
        sys.stderr.write(json.dumps(error_msg) + "\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
