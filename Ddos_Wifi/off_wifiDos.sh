printf "Reverting back to original MAC Address\nPlease Wait..."
ifconfig wlan1 down
sudo macchanger -p wlan1 | grep "Permanent MAC"
iwconfig wlan1 mode managed
ifconfig wlan1 up
service NetworkManager restart
