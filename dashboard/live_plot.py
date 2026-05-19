import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from collections import deque

# Store recent telemetry
time_data = deque(maxlen=50)
altitude_data = deque(maxlen=50)
battery_data = deque(maxlen=50)
pitch_data = deque(maxlen=50)
roll_data = deque(maxlen=50)

plt.ion()

fig, ax = plt.subplots()


def update_plot(current_time, data, faults):

    time_data.append(current_time)
    altitude_data.append(data["altitude"])
    battery_data.append(data["battery"])
    pitch_data.append(data["pitch"])
    roll_data.append(data["roll"])

    ax.clear()

    ax.plot(time_data, altitude_data, label="Altitude")
    ax.plot(time_data, battery_data, label="Battery")
    ax.plot(time_data, pitch_data, label="Pitch")
    ax.plot(time_data, roll_data, label="Roll")

    ax.set_title("Flight Telemetry")
    ax.set_xlabel("Time (s)")
    ax.legend()

    if not faults:
        fault_text = "SYSTEM NOMINAL"
        box_color = "lightgray"
    else:
        fault_text = "Faults: " + ", ".join(faults)
        box_color = "red"
    ax.text(
        0.02,
        0.95,
        fault_text,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor=box_color, alpha=0.7)
    )

    plt.pause(0.01)