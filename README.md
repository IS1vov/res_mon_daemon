# Resource Monitor Daemon

A lightweight Linux system daemon that monitors CPU and RAM usage and sends alerts to Telegram if usage exceeds specified thresholds. Built in Python and installable as a `.deb` package.

## 📦 Features

- Monitors system CPU and RAM every 30 seconds
- Sends alerts via Telegram when thresholds are exceeded
- Runs as a `systemd` service
- Installable via `.deb` package
- Secure: uses environment file for token configuration

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/IS1vov/res_mon_daemon.git
cd res_mon_daemon
2. Configure environment
Create a file at /etc/resource_monitor.env:

TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
Restrict access to root only:

sudo chmod 600 /etc/resource_monitor.env
3. Install the .deb package
./build_deb.sh
sudo dpkg -i resource-monitor.deb
4. Enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable resource_monitor.service
sudo systemctl start resource_monitor.service
🛠 Build .deb package

You can build the .deb package manually using:

./build_deb.sh
This creates resource-monitor.deb in the current directory.


🔐 Security

Sensitive credentials are stored in /etc/resource_monitor.env and are not tracked in Git.
You should never commit real tokens to this repository.
```
