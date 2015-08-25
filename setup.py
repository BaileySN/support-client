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
from distutils.core import setup
from lang import de_DE as ltrans
from bin import version
import os
from os import curdir,sep
import py2exe

imgdir = (curdir+sep+"bin"+sep+"image"+sep)
excludes = ['email']

Mydata_files = []
for files in os.listdir(imgdir):
    f1 = imgdir + files
    if os.path.isfile(f1): # skip directories
        f2 = (curdir+sep+"bin"+sep+"image"), [f1]
        Mydata_files.append(f2)

setup(
    name='Support-Client',
    version=str(version.versionnum),
    packages=['bin', 'conf', 'lang'],
    url='http://wiki.pratznschutz.com/index.php/Support-Client',
    license='GPLv3',
    author='guenter',
    author_email='office@bailey-solution.com',
    description=ltrans.aboutprogram,
	data_files = Mydata_files,
    options = {"py2exe": {"optimize": 2,
						  "packages": ['bin', 'lang', 'conf'],
						  "excludes": excludes,
                          }
    },
    windows=['support-client.py'],
	zipfile="sclib.zip",
)
