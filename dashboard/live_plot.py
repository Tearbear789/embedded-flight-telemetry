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

fig, (ax_status, ax_altitude, ax_battery, ax_attitude, ax_faults) = plt.subplots(
    5,
    1,
    figsize=(10, 11),
    gridspec_kw={"height_ratios": [1, 2, 2, 2, 1]}
)

def update_plot(current_time, data, faults):

    time_data.append(current_time)
    altitude_data.append(data["altitude"])
    battery_data.append(data["battery"])
    pitch_data.append(data["pitch"])
    roll_data.append(data["roll"])

    ax_status.clear()
    ax_status.axis("off")
    status_text = (
        f"Altitude: {data['altitude']:.2f} m\n"
        f"Battery: {data['battery']:.2f} V\n"
        f"Pitch: {data['pitch']:.2f}°\n"
        f"Roll: {data['roll']:.2f}°"
    )

    ax_status.text(
        0.02,
        0.5,
        status_text,
        fontsize=12,
        verticalalignment="center",
        family="monospace"
    )

    ax_altitude.clear()
    ax_altitude.plot(time_data, altitude_data, label="Altitude")
    ax_altitude.set_title("Altitude")
    ax_altitude.set_ylabel("Meters (m)")
    ax_altitude.legend()

    ax_battery.clear()
    ax_battery.plot(time_data, battery_data, label="Battery")
    ax_battery.set_title("Battery")
    ax_battery.set_ylabel("Volts (V)")
    ax_battery.legend()

    ax_attitude.clear()
    ax_attitude.plot(time_data, pitch_data, label="Pitch")
    ax_attitude.plot(time_data, roll_data, label="Roll")
    ax_attitude.set_title("Attitude")
    ax_attitude.set_ylabel("Degrees (°)")
    ax_attitude.set_xlabel("Time (s)")
    ax_attitude.legend()


    ax_faults.clear()
    ax_faults.axis("off")
    ax_faults.set_title("Fault Indicators")

    indicators = [
        "HIGH ALTITUDE",
        "LOW BATTERY",
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
    plt.pause(0.1)