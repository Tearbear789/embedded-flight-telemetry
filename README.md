# embedded-flight-telemetry
Embedded avionics telemetry platform utilizing ESP32-based sensors, real-time data streaming, and Python visualization tools.

---

# Overview

This project is an embedded telemetry and avionics learning platform designed to simulate core aerospace system concepts including:

- real-time sensor acquisition
- telemetry streaming
- environmental monitoring
- motion/orientation tracking
- flight-style data visualization
- embedded communication systems

The long-term goal of this project is to evolve into a modular autonomous aerospace systems platform.

---

## Current Status

The current version uses simulated telemetry data to test the dashboard pipeline before hardware integration.

Implemented:
- simulated telemetry source
- live plotting
- CSV logging
- fault detection
- warning display

Below is a preview:

## Dashboard Preview
![Telemetry Dashboard](docs/dashboard_preview.png)

# Features

Current Features:
- Python telemetry dashboard
- CSV flight-data logging

Planned Features:
- ESP32-based embedded controller
- serial telemetry streaming
- real-time sensor monitoring
- IMU orientation tracking
- barometric altitude estimation
- wireless telemetry
- flight-state logic
- PCB integration
- autonomous UAV subsystem support

---

# Hardware

## Current Hardware
- Computer and code

## Planned Hardware
- ESP32 DevKit
- MPU6050 IMU
- BME280 environmental sensor
- GPS module
- telemetry radio
- custom PCB
- battery monitoring system

---

# Software Stack

- C++
- Python
- PlatformIO
- VS Code
- Git/GitHub

---

# System Architecture

```
Sensors → ESP32 → Telemetry Stream → Python Dashboard → Logging/Visualization
```

---

# Project Goals

This repository is intended to document the progression from:
- embedded systems fundamentals
to:
- aerospace telemetry systems
- avionics concepts
- autonomous UAV subsystem integration

---

# Learning Objectives

Key engineering topics explored in this project:
- embedded systems
- UART/I2C/SPI communication
- telemetry systems
- sensor integration
- debugging workflows
- data visualization
- avionics concepts
- systems engineering

---

# Current Status

Phase 0 — Setup and Infrastructure

Current focus:
- development environment setup
- GitHub workflow
- telemetry architecture planning
- repository structure
- embedded systems tooling

---

# Repository Structure

```text
/docs          -> documentation
/firmware      -> ESP32 firmware
/dashboard     -> Python visualization tools
/hardware       -> schematics and PCB files
/logs          -> captured telemetry logs
```

---

# Future Roadmap

- [ ] basic telemetry output
- [ ] IMU integration
- [ ] live dashboard visualization
- [ ] sensor filtering
- [ ] wireless telemetry
- [ ] PCB revision
- [ ] UAV systems integration

---

# Author

Electrical Engineering student focused on:
- embedded systems
- avionics
- autonomy
- aerospace systems engineering