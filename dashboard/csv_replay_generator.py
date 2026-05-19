import csv

# Parses telemetry logs and returns data in dictionary format
def telemetry_generator(filename="dashboard/telemetry_logs/telemetry_log.csv"):

    with open(filename, mode="r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            data = {
                "time": float(row["time"]),
                "altitude": float(row["altitude"]),
                "battery": float(row["battery"]),
                "pitch": float(row["pitch"]),
                "roll": float(row["roll"]),
            }

            yield data