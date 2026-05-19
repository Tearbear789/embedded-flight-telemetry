import time
import random

while True:
    altitude = random.uniform(100, 120)
    battery = random.uniform(11.5, 12.6)
    pitch = random.uniform(-10, 10)
    roll = random.uniform(-10, 10)

    print(f"Altitude: {altitude:.2f} m")
    print(f"Battery: {battery:.2f} V")
    print(f"Pitch: {pitch:.2f} deg")
    print(f"Roll: {roll:.2f} deg")
    print("-" * 30)

    time.sleep(1)