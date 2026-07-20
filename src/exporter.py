import json
import sys


def stream_json_metrics(metrics_data):
    """Formats and streams network metrics to standard output.

    Ensures immediate write flushes for real-time pipeline integration.
    """
    try:
        # Serialize the python dictionary to a compact JSON string
        json_output = json.dumps(metrics_data, separators=(",", ":"))

        # Stream directly to stdout followed by an immediate system flush
        sys.stdout.write(json_output + "\n")
        sys.stdout.flush()

    except (TypeError, ValueError) as e:
        error_log = {
            "timestamp": metrics_data.get("timestamp"),
            "status": "CRITICAL",
            "error": f"Failed to serialize metrics data: {str(e)}",
        }
        sys.stderr.write(json.dumps(error_log) + "\n")
        sys.stderr.flush()
