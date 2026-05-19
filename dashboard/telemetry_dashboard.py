import time
from telemetry_sources.fake_data import get_telemetry
from csv_logger import CSVLogger

logger = CSVLogger()
start_time = time.time()

try:
    while True:
        current_time = time.time() - start_time
        data = get_telemetry()

        print(f"Altitude: {data['altitude']}")
        print(f"Battery: {data['battery']}")
        print(f"Pitch: {data['pitch']}")
        print(f"Roll: {data['roll']}")

        if data["battery"] < 11.3:
            print("Warning: Low Battery")

        if data["altitude"] < 118:
            print("Warning: HIGH ALTITUDE")

        logger.log(current_time, data)
        
        print("-" * 40)

        time.sleep(1)

except KeyboardInterrupt:
    print("Telemetry stopped.")
    logger.close()
