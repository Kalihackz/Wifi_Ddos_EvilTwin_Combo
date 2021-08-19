<img src="https://via.placeholder.com/1270x120/0d1117/fffff?text=Wifi+DDos+EvilTwin+Combo" />

```html
This is a combo script of Wifi Hijacking and Jamming.Includes builtin captive portal with
a dlink firmware update page.It can jam or interrupt working of other wireless networks in
2.4Ghz range.So be careful and don't misuse this script.Its only for education purpose.
```
<img src="https://via.placeholder.com/1000x100/0d1117/BFFF00?text=Tools+and+Modules+used" />

| Python3  | Bash | Node JS |
| ------------- | ------------- | -------- |
| flask | airmon-ng | express |
| subprocess | macchanger | body-parser |
| sys  | aireplay-ng | nodemon |
| time | airodump-ng | node.js |
| termcolor | dnsspoof |   |
| os | hostapd and dnsmasq  |   |

-------------------------------------------------------------------------------------------------------------------------------------------------
<img src="https://via.placeholder.com/1270x120/0d1117/BFFF00?text=INSTALLATIONS and CONFIGURATION" />

Installation :
=============
* Clone or Download the repository.
* Unzip the zip.
* Open a terminal in the unzipped folder namely : `Wifi_Ddos_EvilTwin_Combo-main`
* Now enter the following commands in the terminal :

| Commands  |
| ------------- |
| chmod +x Ddos_Wifi/WifiMoniterModeScanner.sh |
| chmod +x Ddos_Wifi/wifiDos.sh |
| chmod +x Ddos_Wifi/off_wifiDos.sh |

Assumptions :
===========

We need two Wireless Adapters if two attacks are done together.
* `wlan1` - here is used for Wifi Ddos.
* `wlan0` - here is used for Evil Twin purposes. [wlan0 - internal wifi adapter]

We need Kali Linux OS else somethings may not work.

Start Attack :
============

* Command : `sudo python3 comboServer_main.py`.
* Navigate to http://127.0.0.1:5000 .

-------------------------------------------------------------------------------------------------------------------------------------------------
<img src="https://via.placeholder.com/1270x120/0d1117/BFFF00?text=FUNCTIONALITIES" />

* **comboServer_main.py** - One click web based Wifi Attacking Tool for DDosing and Evil Twin.
------------------------------------------------------------------------------------------------------------------------------------------------

<img src="https://via.placeholder.com/1270x120/0d1117/BFFF00?text=SCREENSHOT+OF+THE+SCRIPT" />

Web Interface :
==============
![Screenshot Of Wifi_Combo_Tool Date: Sun April 04 06:50:25 PM](https://i.imgur.com/K7a7CEN.png)
Wifi DDos :
==============
![Screenshot Of Wifi_Combo_Tool Date: Sun April 04 06:50:25 PM](https://i.imgur.com/Iv4gHJ7.png)
Evil Twin :
==============
![Screenshot Of Wifi_Combo_Tool Date: Sun April 04 06:50:25 PM](https://i.imgur.com/NX4riD3.png)
