# 📡 Wifi_Ddos_EvilTwin_Combo

**A combo tool for WiFi jamming and Evil Twin attacks, driven from a single
one-click web interface.**

Includes a built-in captive portal with a D-Link firmware-update page, and can
jam or interrupt other wireless networks in the 2.4GHz range.

> ⚠️ For educational purposes only. Be careful and don't misuse this script —
> only use it against networks you own or have explicit permission to test.

<p>
  <a href="https://www.buymeacoffee.com/kalihackz"><img src="https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=kalihackz&button_colour=FFDD00&font_colour=000000&font_family=Bree&outline_colour=000000&coffee_colour=ffffff" /></a>
</p>

---

## ✨ Features

- **WiFi DDoS / jamming** — interrupt other wireless networks in the 2.4GHz range.
- **Evil Twin** — spins up a fake AP with a captive portal (D-Link firmware-update page) to harvest credentials.
- **One-click web UI** — kick off either attack from a local web interface instead of juggling terminal scripts.

---

## 🧰 Tools & modules used

| Python3 | Bash | Node.js |
|---|---|---|
| flask | airmon-ng | express |
| subprocess | macchanger | body-parser |
| sys | aireplay-ng | nodemon |
| time | airodump-ng | node.js |
| termcolor | dnsspoof | |
| os | hostapd and dnsmasq | |

---

## 📦 Requirements

- **Kali Linux** — some functionality relies on tools only reliably available there.
- **Two wireless adapters** if running both attacks together:
  - `wlan1` — used for the WiFi DDoS.
  - `wlan0` — used for Evil Twin (internal WiFi adapter).

---

## 🚀 Installation

1. Clone or download the repository.
2. If downloaded as a zip, unzip it and open a terminal in the extracted
   folder (e.g. `Wifi_Ddos_EvilTwin_Combo-main`).
3. Make the scripts executable:

   ```bash
   chmod +x Ddos_Wifi/WifiMoniterModeScanner.sh
   chmod +x Ddos_Wifi/wifiDos.sh
   chmod +x Ddos_Wifi/off_wifiDos.sh
   ```

---

## 🕹️ Usage

```bash
sudo python3 comboServer_main.py
```

Then open **http://127.0.0.1:5000** and drive the attack from the web UI.

---

## 📄 Files

| File | Purpose |
|---|---|
| `comboServer_main.py` | One-click web-based tool for WiFi DDoS and Evil Twin attacks |
| `Ddos_Wifi/` | Bash scripts for scanning and running/stopping the WiFi DDoS |
| `FakeAuth_EvilTwin/` | Evil Twin / captive portal implementation |
| `templates/` | Web UI templates |

---

## 🖼️ Screenshots

**Web interface**
![Screenshot of the web interface](https://i.imgur.com/K7a7CEN.png)

**WiFi DDoS**
![Screenshot of WiFi DDoS](https://i.imgur.com/Iv4gHJ7.png)

**Evil Twin**
![Screenshot of Evil Twin](https://i.imgur.com/NX4riD3.png)

---

## ☕ Support

If this tool saved you some time, consider buying me a coffee:

<a href="https://www.buymeacoffee.com/kalihackz"><img src="https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=kalihackz&button_colour=FFDD00&font_colour=000000&font_family=Bree&outline_colour=000000&coffee_colour=ffffff" /></a>
