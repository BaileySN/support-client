#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################################################################################################
# Support-Client <http://wiki.pratznschutz.com/index.php/Support-Client>.                                                    #
# Copyright (C) [2015]  [Guenter Bailey]                                                                                     #
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
from bin import version

class de_DE():
    programm_name=("Support Client v"+version.versionnum)
    programm_shortdesc="""
1. Prüfe Internet Verbindung
2. Download Teamviewer
3. Starte Teamviewer
"""
    label_update_error="Fehler, konnte nicht updaten"
    programm_description="""Falls Sie das Programm noch nicht verwendet haben gehen Sie bitte folgende Punkte nach der
Reihe durch:

1.) Prüfe Internet Verbindung
2.) Download Teamviewer
3.) Starte Teamviewer

Falls Teamviewer schon Heruntergeladen wurde, können Sie auch gleich mit Punkt 3 beginnen."""

    # Menu Datei
    button_filemenu_label="Datei"
    button_filemenu_end="Beenden"

    # Menu Konfiguration
    button_config_label="Konfiguration"
    button_config_editconf="Einstellungen"

    # Menu Support
    button_support_label="Support"
    button_support_teamviewer_download="Download Teamviewer"
    label_shortdesc_teamviewer_download="""Lade Teamviewer herunter.\nDies kann eine kurze Zeit dauern.

Während des Downloads kann man das Programm nicht verwenden.

Mit OK schließen Sie das Fenster"""
    label_shortdesc_teamviewer_download_fertig="Download von Teamviewer Beendet.\nWeiter mit Punkt 3."
    button_support_teamviewer_start="Starte Fernwartung"
    label_update="Nach dem Bestätigen startet der Update Prozess"
    label_update_finish="Update Beendet, Bitte starten Sie das Programm neu"


    # Menu Help
    button_help_label="Hilfe"
    button_help_steps="Abblauf"
    button_help_online="Online Hilfe"
    button_help_aboutus="Über Uns"
    button_update="Update"
    button_to_update_url="Update Webseite"
    aboutprogram=("""               Support Client

Dieses Programm wurde Entwickelt damit Kunden einfach zur Zeit ein Fernwartungstool downloaden können und falls es ist auch noch zu starten.

Copyright © 2015  Günter Bailey
""")

    # Display
    button_connection="Prüfe Internet Verbindung"
    display_connection="Internet Verbindung ?"
    display_connection_true="Verbindung OK"
    display_connection_false="Keine Verbindung"






class en_EN():
    programm_name=de_DE.programm_name
    programm_shortdesc=("""

Check Internet Connection
Download Teamviewer
Start Teamviewer
""")

    programm_description=("""If you have not used the program, please go to the following points after the
Series by:

1.) Check Internet connection
2.) Download TeamViewer
3.) Start TeamViewer

If TeamViewer was already downloaded, you might as well start with step 3.""")

    # Menu Datei
    button_filemenu_label="File"
    button_filemenu_end="Quit"

    # Menu Konfiguration
    button_config_label="Configuration"
    button_config_editconf="Settings"

    # Menu Support
    button_support_label="Support"
    button_support_teamviewer_download="Download Teamviewer"
    label_shortdesc_teamviewer_download=("""Downloading Teamviewer.\nThis may take a while.

During the download, you can not use the program.

Click OK to close the window""")
    label_shortdesc_teamviewer_download_fertig="Download TeamViewer Completed.\nClick to Point 3"
    label_update="After Accepts starting the update progress"
    button_support_teamviewer_start="Start Teamviewer"

    label_update_error="Fehler, konnte nicht updaten"
    label_update_finish="Update finish, please restart the program"
    # Menu Help
    button_help_label="Help"
    button_help_steps="Proceeding"
    button_help_online="Online Help"
    button_help_aboutus="About Us"
    button_update="Update"
    button_to_update_url="update website"
    aboutprogram=("""               Support client

This program was developed so that customers can easily download at the time a remote maintenance tool and if it is yet to be launched.

Copyright © 2015  Günter Bailey
""")

    # Display
    button_connection="Check Internet Connection"
    display_connection="I-Net connection is ?"
    display_connection_true="Connection OK"
    display_connection_false="Connection fails"
