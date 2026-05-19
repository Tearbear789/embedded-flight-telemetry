import time
from telemetry_sources.fake_data import get_telemetry
from live_plot import update_plot
from faults import check_faults
from csv_replay_generator import telemetry_generator

start_time = time.time()
generator = telemetry_generator()

try:
    while True:
        current_time = time.time() - start_time
        data = next(generator)
        faults = check_faults(data)

        if faults:
            print("FAULTS:", ", ".join(faults))
        else:
            print("System nominal")

        print(f"Altitude: {data['altitude']}")
        print(f"Battery: {data['battery']}")
        print(f"Pitch: {data['pitch']}")
        print(f"Roll: {data['roll']}")

        update_plot(current_time, data, faults)

        print("-" * 40)

        time.sleep(0.2)

except StopIteration:
    print("Replay Ended.")

except KeyboardInterrupt:
    print("Replay Stopped by User.")

except:
    print("Crash.")
