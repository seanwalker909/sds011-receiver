# SDS011 Receiver

This server runs on the **Display Pi** to receive air quality data from a sensor Pi over the LAN.

## Setup

1. Clone this repo:
   `git clone https://github.com/seanwalker909/sds011-receiver.git`
2. Navigate to folder:
   `cd sds011-receiver`
3. Create and use a virtual environment:

   **Standard Way:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   **⚠️ Raspberry Pi Workaround (If the standard way hangs):**
   If `python3 -m venv venv` hangs (common on some Raspberry Pi OS versions), use this method to manually bootstrap `pip`:
   ```bash
   # 1. Create the environment without pip
   python3 -m venv venv --without-pip
   
   # 2. Activate it
   source venv/bin/activate
   
   # 3. Manually install pip
   curl https://bootstrap.pypa.io/get-pip.py | python3
   
   # 4. Install dependencies
   pip install -r requirements.txt
   ```

## Running as a Service

1. Move the service file to the systemd directory:
   `sudo cp sds011-receiver.service /etc/systemd/system/`
2. Reload the systemd daemon:
   `sudo systemctl daemon-reload`
3. Enable and start the service:
   `sudo systemctl enable sds011-receiver.service`
   `sudo systemctl start sds011-receiver.service`
