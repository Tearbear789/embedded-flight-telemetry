import csv
from pathlib import Path

class CSVLogger:
    def __init__(self, filename="logs/telemetry_log.csv"):
        self.file_path = Path(filename)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        self.file = open(self.file_path, mode="w", newline="")
        self.writer = csv.writer(self.file)

        self.writer.writerow([
            "time",
            "altitude",
            "battery",
            "pitch",
            "roll"
        ])

    def log(self, timestamp, data):
        self.writer.writerow([
            round(timestamp, 2),
            round(data["altitude"], 2),
            round(data["battery"], 2),
            round(data["pitch"], 2),
            round(data["roll"], 2)
        ])

        self.file.flush()

    def close(self):
        self.file.close()