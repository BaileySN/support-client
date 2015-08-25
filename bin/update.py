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
import os,zipfile,shutil
from os import curdir,sep
from tkMessageBox import showinfo,showerror
from bin import osenv as _osenv
from lang import de_DE, en_EN
from conf import setlang
from conf import check as _check

support_cldir = "support-client"

ltrans = ()
if setlang.langn == "de_DE":
    ltrans = de_DE()
elif setlang.langn == "en_EN":
    ltrans = en_EN()
else:
    ltrans = de_DE()

def chk_connection():
    pingopt = ''
    stat = ""
    if _osenv() == "nt":
        pingopt = '-n'
    elif _osenv() == "linux":
        pingopt = '-c'
    elif _osenv() == "macos":
        pingopt = '-c'
    else:
        pingopt = '-c'

    if os.system("ping " + pingopt + " " + _check.rate + " " + _check.pingurl) == 0:
        stat = "OK"
    else:
        stat = "Error"
    return stat

def forceMergeFlatDir(srcDir, dstDir):
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)
    for item in os.listdir(srcDir):
        srcFile = os.path.join(srcDir, item)
        dstFile = os.path.join(dstDir, item)
        forceCopyFile(srcFile, dstFile)

def forceCopyFile (sfile, dfile):
    if os.path.isfile(sfile):
        shutil.copy2(sfile, dfile)

def isAFlatDir(sDir):
    for item in os.listdir(sDir):
        sItem = os.path.join(sDir, item)
        if os.path.isdir(sItem):
            return False
    return True

def copyTree(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isfile(s):
            if not os.path.exists(dst):
                os.makedirs(dst)
            forceCopyFile(s,d)
        if os.path.isdir(s):
            isRecursive = not isAFlatDir(s)
            if isRecursive:
                copyTree(s, d)
            else:
                forceMergeFlatDir(s, d)

def msdelupdate(srcDir):
    try:
        os.system("rmdir /s /q "+srcDir+sep)
    except:
        print("fehler bei update delete")

def mscopy(srcDir, dstDir):
    try:
        os.system("xcopy "+srcDir+sep+"*"+" "+dstDir+" /Y /E")
    except IOError:
        print("xcopy fehler")

def extract(fpath, fname):
    ext = (fpath+sep+fname)
    try:
        with zipfile.ZipFile(ext, 'r') as z:
            z.extractall(fpath+sep)
        os.remove(ext)
        if _osenv() == "nt":
            mscopy(fpath, curdir)
            msdelupdate(fpath)
        else:
            copyTree(fpath, curdir)
            shutil.rmtree(fpath)
    except IOError:
        print("extract error")


class start_updater():
    def __init__(self):
        if _osenv() == "nt":
            updname = "scupdate_win.zip"
        else:
            updname = "scupdate_linux.zip"

        self.url = ("http://download.bailey-solution.com/Support-Client/"+updname)
        self.dldir = (curdir+sep+"temp"+sep+"update")
        self.fname = self.url.split('/')[-1]
        if chk_connection() == "OK":
            try:
                self.dlprogram()
                extract(self.dldir, self.fname)
                showinfo(ltrans.programm_name, ltrans.label_update_finish)
            except IOError:
                print("cant run")
        else:
            showerror(ltrans.programm_name, ltrans.label_update_error)

    def dlprogram(self):
        import urllib2
        if not os.path.exists(self.dldir):
            os.makedirs(self.dldir)

        try:
            u = urllib2.urlopen(self.url)
            file_path = (self.dldir+sep+self.fname)
            f = open(file_path, 'wb')
            meta = u.info()

            file_size = int(meta.getheaders("Content-Length")[0])
            print("Downloading Update: '%s' Bytes: '%s'" %(self.fname, file_size))

            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break

                file_size_dl += len(buffer)
                f.write(buffer)
                status = r"%10d    [%3.2f%%]" %(file_size_dl, file_size_dl * 100. /file_size)
                status = status + chr(8)*(len(status)+1)
                print(status)
            f.close()
        except IOError:
            print("cant download update")
