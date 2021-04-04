clear
echo -e "Starting the \e[91m\e[5mJamming of Wifi Network Attack \e[25m"
echo -e "                         \e[93m\e[1m-Made by Kalihackz\e[21m\e[97m"
echo -e "\e[35mPlease Wait...\e[0m"
sleep 3
printf "\n"
echo -e "Changing Wifi Mode to \e[91mMoniter Mode from \e[93mManaged Mode"
sleep 1
ifconfig wlan1 down
iwconfig wlan1 mode moniter
ifconfig wlan1 up
airmon-ng check kill
echo -e -n "\e[91m"
echo -e "Moniter\e[95m Mode Started.."
sleep 3
airodump-ng wlan1
