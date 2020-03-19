#!/usr/bin/env bash

sfile="support-client.command"
ver="1.0a"
sfcontent="""
##############################################################################################################################
# Support-Client <http://wiki.pratznschutz.com/index.php/Support-Client>.                                                    #
# Copyright @ 2020  [Guenter Bailey]                                                                                     #
#                                                                                                                            #
# This program is free software;                                                                                             #
# you can redistribute it and/or modify it under the terms of the GNU General Public License                                 #
# as published by the Free Software Foundation;                                                                              #
# either version 3 of the License, or (at your option) any later version.                                                    #
#                                                                                                                            #
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;                                  #
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                                  #
# See the GNU General Public License for more details.                                                                       #
#                                                                                                                            #
# You should have received a copy of the GNU General Public License along with this program;                                 #
# if not, see <http://www.gnu.org/licenses/>.                                                                                #
##############################################################################################################################
"""

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
    echo """
Erstelle die Start Datei $sfile
Die Sie nachher mit dem Desktop verknuepfen koennen (Alias), oder Kopieren

create the start file $sfile
after that step you can link this with the Desktop (Alias) or copy
------------------------------------------------------------------------------------
Support-Client Pfad $PWD

Support-Client path $PWD
    """
    echo "#!/bin/bash" >> $sfile
    echo "$sfcontent" >> $sfile
    echo "cd $PWD &&python ./support-client.py" >> $sfile
    echo "osascript -e 'tell application "'"Terminal"'" to quit'" >> $sfile
    echo "exit" >> $sfile
    sleep 1
    chmod +x $PWD/$sfile
    sleep 1
    echo """
Datei $sfile erstellt

file $sfile created

Konfiguration erfolgreich, Sie koennen nun das Programm mit klick auf $sfile starten.

configuration successfull, you can now starting the program with double click.

    """

fi
