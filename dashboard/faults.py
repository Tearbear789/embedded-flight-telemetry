# Output fault if data is outside threshold
def check_faults(data):
    faults = []

    if data["battery"] < 11.3:
        faults.append("LOW BATTERY")

    if data["altitude"] > 118:
        faults.append("HIGH ALTITUDE")

    if abs(data["pitch"]) > 8:
        faults.append("HIGH PITCH ANGLE")

    if abs(data["roll"]) > 8:
        faults.append("HIGH ROLL ANGLE")

    return faults