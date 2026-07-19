# SDS011 Receiver

This server runs on the **Display Pi** to receive air quality data from a sensor Pi over the LAN.

## Setup

1. Clone this repo:
   `git clone https://github.com/seanwalker909/sds011-receiver.git`
2. Navigate to folder:
   `cd sds011-receiver`
3. Install dependencies:
   `pip install -r requirements.txt`

## Running as a Service

1. Move the service file to systemd directory:
   `sudo cp sds011.service /etc/systemd/system/`
2. Enable and start:
   `sudo systemctl enable sds011.service`
   `sudo systemctl start sds011-receiver.service`
