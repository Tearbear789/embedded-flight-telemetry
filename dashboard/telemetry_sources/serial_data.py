import serial


class SerialTelemetry:
    def __init__(self, port="COM5", baud_rate=115200):
        self.ser = serial.Serial(port, baud_rate, timeout=1)

    def get_telemetry(self):
        line = self.ser.readline().decode("utf-8").strip()

        if not line or line.startswith("altitude"):
            return None

        altitude, battery, pitch, roll = line.split(",")

        return {
            "altitude": float(altitude),
            "battery": float(battery),
            "pitch": float(pitch),
            "roll": float(roll),
        }