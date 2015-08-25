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
from sys import platform as _platform


class osenv(object):
    def __init__(self):
        self.text="Text"

    def __new__(self):
        env=()
        if _platform == "linux" or _platform == "linux2":
            env=("linux")
        elif _platform == "darwin" or _platform == "mac":
            env=("macos")
        elif _platform == "win32" or _platform == "win64":
            env=("nt")
        elif _platform == "nt" or _platform == "win":
            env=("nt")
        else:
            env=("linux")
        return (env)
