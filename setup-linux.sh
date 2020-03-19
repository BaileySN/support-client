#!/usr/bin/env bash
sfile="Support-Client.desktop"
lsfile="start.sh"
ver="1.0a"

echo """
##############################################################################################
#                                  Support-Client setup v$ver                                 #
#--------------------------------------------------------------------------------------------#
#                                         by BS @2020                                        #
#--------------------------------------------------------------------------------------------#
#    this tool configure the $sfile for easy starting the program     #
##############################################################################################
"""

echo """
###########################################################################################
# Support-Client v$ver  Copyright (C) 2020  Guenter Bailey                                 #
# This program comes with ABSOLUTELY NO WARRANTY.                                         #
# This is free software, and you are welcome to redistribute it under certain conditions. #
###########################################################################################
"""

if [ -f $sfile ]; then
    echo "Datei $sfile vorhanden"
    echo "file $sfile exists"
else
    echo "Starte Installation von Abhaengigkeiten"
    apt-get install python3.6 python3 python3-tk
    echo """
Erstelle die Desktop Datei $sfile
Die Sie nachher auf den Desktop kopieren koennen.

create the desktop file $sfile
after then, you can copy this file to the desktop
------------------------------------------------------------------------------------
Support-Client Pfad $PWD

Support-Client path $PWD
"""
echo "[Desktop Entry]" >> $sfile
echo "Version=1.0" >> $sfile
echo "Type=Application" >> $sfile
echo "Name=Support-Client" >> $sfile
echo "Comment=Dieses Programm wurde Entwickelt damit Kunden einfach zur Zeit ein Fernwartungstool downloaden koennen und falls es ist auch noch zu starten." >> $sfile
echo "Exec=python support-client.py" >> $sfile
echo "Icon=$PWD/bin/image/support-client.PNG" >> $sfile
echo "Path=$PWD/" >> $sfile
echo "Terminal=false" >> $sfile
echo "StartupNotify=true" >> $sfile
echo "GenericName=" >> $sfile
sleep 1
chmod +x $PWD/$sfile
sleep 1
echo """
Desktop Datei $sfile erstellt

desktop file $sfile created

Konfiguration erfolgreich, Sie koennen nun das Programm mit klick auf $sfile starten.

configuration successfull, you can now starting the program with double click.
"""
fi
