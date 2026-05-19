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

fig, (ax_plot, ax_faults) = plt.subplots(
    2,
    1,
    figsize=(10, 7),
    gridspec_kw={"height_ratios": [3, 1]}
)

def update_plot(current_time, data, faults):

    time_data.append(current_time)
    altitude_data.append(data["altitude"])
    battery_data.append(data["battery"])
    pitch_data.append(data["pitch"])
    roll_data.append(data["roll"])

    ax_plot.clear()

    ax_plot.plot(time_data, altitude_data, label="Altitude")
    ax_plot.plot(time_data, battery_data, label="Battery")
    ax_plot.plot(time_data, pitch_data, label="Pitch")
    ax_plot.plot(time_data, roll_data, label="Roll")

    ax_plot.set_title("Flight Telemetry")
    ax_plot.set_xlabel("Time (s)")
    ax_plot.legend()

    ax_faults.clear()
    ax_faults.axis("off")
    ax_faults.set_title("Fault Indicators")

    indicators = [
        "LOW BATTERY",
        "HIGH ALTITUDE",
        "HIGH PITCH ANGLE",
        "HIGH ROLL ANGLE"
    ]

    for i, fault_name in enumerate(indicators):
            is_active = fault_name in faults

            color = "red" if is_active else "lightgray"

            ax_faults.text(
                0.1 + i * 0.22,
                0.5,
                fault_name,
                ha="center",
                va="center",
                fontsize=10,
                bbox=dict(
                    boxstyle="round,pad=0.5",
                    facecolor=color,
                    edgecolor="black"
                )
            )

    plt.tight_layout()
    plt.pause(0.01)