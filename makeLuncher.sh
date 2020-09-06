#!/bin/sh

# Here checking for root access
if [ "$(id -u)" -ne "0" ]
then
    echo "Requiers root access."
    exit 1
fi

# Require paths
icon="$(pwd)/icon/icon.png"

echo "Creating the Luncher..."

echo "
[Desktop Entry]
Version=1.0
Type=Application
Name=Announcements Settings
Comment=University of Piraeus Notifications Settings
Exec=sh $(pwd)/shellScripts/runUI.sh
Icon=$icon
Terminal=false
StartupNotify=true
" > announcementsSettings.desktop

echo "
[Desktop Entry]
Version=1.0
Type=Application
Name=Announcements
Comment=University of Piraeus Notifications
Exec=sh $(pwd)/shellScripts/autostart.sh
Icon=$icon
Terminal=false
StartupNotify=false
" > autostart/autostart.desktop 

echo "
cd $(pwd)/utils
python3 UIHandler.py

" > shellScripts/runUI.sh

echo "
cd $(pwd)
python3 main.py

" > shellScripts/autostart.sh

chmod 555 shellScripts/runUI.sh
chmod 555 shellScripts/autostart.sh
cp announcementsSettings.desktop /usr/share/applications/
cp autostart/autostart.desktop /usr/share/applications/announcements.desktop
echo "Clean up..."
rm announcementsSettings.desktop
echo "Done."
