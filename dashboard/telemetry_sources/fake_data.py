import random

# Creates randomize data to test dashboard
def get_telemetry():

    telemetry = {
        "altitude": random.uniform(100, 120),
        "battery": random.uniform(11.0, 12.6),
        "pitch": random.uniform(-10, 10),
        "roll": random.uniform(-10, 10),
    }

    return telemetry