from telemetry_sources.serial_data import SerialTelemetry

telemetry = SerialTelemetry(port="COM5", baud_rate=115200)

while True:
    data = telemetry.get_telemetry()

    if data is not None:
        print(data)