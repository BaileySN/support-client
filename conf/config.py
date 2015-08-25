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


class setlang():
    """
    langn="de_DE" oder "en_EN"
    de_DE => Deutsch (German)
    en_EN => Englisch (US)
    """
    langn="de_DE"

class dlsource():
    """
    Verschiedene downloads für verschiedene OS Systeme
    """
    twclient_nt = "http://download.teamviewer.com/download/TeamViewerQS_de-hse.exe"
    twsafe_nt = "teamviewer-quick-support.exe"
    twclient_linux = "http://download.teamviewer.com/download/teamviewer_qs.tar.gz"
    twsafe_linux = "teamviewer_qs.tar.gz"
    twclient_macos = "http://download.teamviewer.com/download/TeamViewerQS.dmg"
    twsafe_macos = "TeamViewerQS.dmg"


class check():
    # Minimal Ping bei Windows ab 1
    pingurl='www.google.at'
    rate="2"
