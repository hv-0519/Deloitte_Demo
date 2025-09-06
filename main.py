import json
from datetime import datetime

# -------------------------------------------------
# Helper: Convert ISO8601 timestamp into milliseconds
# -------------------------------------------------
def iso_to_millis(iso_str: str) -> int:
    """
    Convert ISO8601 timestamp into milliseconds since epoch.
    Example: "2020-01-01T12:34:56.789Z" -> 1577882096789
    """
    # Some ISO timestamps may end with "Z" (UTC) → Python needs it explicit
    if iso_str.endswith("Z"):
        iso_str = iso_str[:-1] + "+00:00"

    dt = datetime.fromisoformat(iso_str)
    millis = int(dt.timestamp() * 1000)
    return millis


# -------------------------------------------------
# IMPLEMENT: Convert format #1 → unified format
# -------------------------------------------------
def convert_from_format1(entry: dict) -> dict:
    """
    Input example (data-1.json):
    {
      "ts": "2020-01-01T12:34:56.789Z",
      "reading": {
        "temperature": 21.2,
        "humidity": 34.5
      }
    }

    Output (data-result.json style):
    {
      "timestamp": 1577882096789,
      "temperature": 21.2,
      "humidity": 34.5
    }
    """
    return {
        "timestamp": iso_to_millis(entry["ts"]),
        "temperature": entry["reading"]["temperature"],
        "humidity": entry["reading"]["humidity"],
    }


# -------------------------------------------------
# IMPLEMENT: Convert format #2 → unified format
# -------------------------------------------------
def convert_from_format2(entry: dict) -> dict:
    """
    Input example (data-2.json):
    {
      "time": 1577882096789,
      "temp": 21.2,
      "hum": 34.5
    }

    Output (data-result.json style):
    {
      "timestamp": 1577882096789,
      "temperature": 21.2,
      "humidity": 34.5
    }
    """
    return {
        "timestamp": entry["time"],
        "temperature": entry["temp"],
        "humidity": entry["hum"],
    }


# -------------------------------------------------
# The rest of the project will already call these
# functions during the tests.
# -------------------------------------------------

if __name__ == "__main__":
    # Debug run (not required for tests)
    with open("data-1.json") as f1, open("data-2.json") as f2:
        d1 = json.load(f1)
        d2 = json.load(f2)

    print("Format1 →", [convert_from_format1(e) for e in d1])
    print("Format2 →", [convert_from_format2(e) for e in d2])
