# Green House IoT

## Overview
Green House IoT is a project designed to automate and monitor various aspects of a greenhouse environment using IoT devices. This project integrates sensors, actuators, and control systems to ensure optimal conditions for plant growth.

## Features
- **Temperature and Humidity Monitoring**: Real-time monitoring of greenhouse temperature and humidity levels.
- **Light Controls**: Automated control of lighting systems to simulate natural light cycles.
- **Motion Detection**: Security features to detect unauthorized access.
- **RGB Controls**: Customizable RGB lighting for aesthetic or functional purposes.
- **Servo Mechanisms**: Automated control of vents or other mechanical systems.
- **Keypad Input**: User interface for manual control and configuration.
- **Buzzer Alerts**: Audible alerts for critical conditions or security breaches.

## Files
- `main.py`: The main script to run the IoT system.
- `temp_hum.py`: Handles temperature and humidity monitoring.
- `light_controls.py`: Manages lighting systems.
- `motion.py`: Implements motion detection.
- `rgb_controls.py`: Controls RGB lighting.
- `servo.py`: Operates servo mechanisms.
- `keypad.py`: Processes keypad inputs.
- `buzzer.py`: Controls the buzzer for alerts.
- `rel.py`: Additional relay controls.
- `diagram.json`: JSON file containing the system's wiring diagram.

## Setup
1. Clone the repository.
2. Install necessary dependencies.
3. Connect the hardware components as per `diagram.json`.
4. Run `main.py` to start the system.

## Usage
- Monitor environmental conditions in real-time.
- Configure settings using the keypad.
- Receive alerts for critical conditions.