import time
from telemetry_sources.fake_data import get_telemetry
from csv_logger import CSVLogger
from live_plot import update_plot
from faults import check_faults

logger = CSVLogger()
start_time = time.time()

try:
    while True:
        current_time = time.time() - start_time
        data = get_telemetry()
        
        faults = check_faults(data)

        if faults:
            print("FAULTS:", ", ".join(faults))
        else:
            print("System nominal")

        # print(f"Altitude: {data['altitude']}")
        # print(f"Battery: {data['battery']}")
        # print(f"Pitch: {data['pitch']}")
        # print(f"Roll: {data['roll']}")

        logger.log(current_time, data)
        update_plot(current_time, data, faults)
        
        # print("-" * 40)

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Telemetry stopped.")
    logger.close()
