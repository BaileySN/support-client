#!/usr/bin/python
# -*- coding: utf-8 -*-
#######################################################################################################################
# Support-Client <https://github.com/BaileySN/Support-Client>.                                                        #
# Copyright (C) [2015]  [Guenter Bailey]                                                                              #
#                                                                                                                     #
# This program is free software;                                                                                      #
# you can redistribute it and/or modify it under the terms of the GNU General Public License                          #
# as published by the Free Software Foundation;                                                                       #
# either version 3 of the License, or (at your option) any later version.                                             #
#                                                                                                                     #
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;                           #
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                           #
# See the GNU General Public License for more details.                                                                #
#                                                                                                                     #
# You should have received a copy of the GNU General Public License along with this program;                          #
# if not, see <http://www.gnu.org/licenses/>.                                                                         #
#######################################################################################################################
import os
import Tkinter as tk
from os import curdir, sep
from subprocess import Popen, PIPE
from tkMessageBox import showinfo
from lang import de_DE, en_EN
from conf import setlang, dlsource
from conf import check as _check
from bin import osenv as _osenv

# set language
ltrans = ()
if setlang.langn == "de_DE":
    ltrans = de_DE()
elif setlang.langn == "en_EN":
    ltrans = en_EN()
else:
    ltrans = de_DE()

programmtxt = ltrans.programm_name
savfilent = (curdir + sep + "temp" + sep + dlsource.twsafe_nt)
savfilelinux = (curdir + sep + "temp" + sep + dlsource.twsafe_linux)
savfilemacos = (curdir + sep + "temp" + sep + dlsource.twsafe_macos)
twstart_linux = (curdir + sep + "temp" + sep + "teamviewerqs" + sep + "teamviewer")

def update_program():
    from bin import update
    update.start_updater()
    ende()

def editconfiguration():
    editor = ''
    if _osenv() == "nt":
        editor = 'notepad'
    elif _osenv() == "linux":
        editor = 'notepad'
    elif _osenv == "macos":
        editor = 'notepad'
    else:
        editor = 'notepad'

    confopen = [editor, 'conf/config.py']
    p7 = Popen(confopen, stdout=PIPE)
    cmdt = p7.communicate()[0]

def aboutprogram():
    uebertxt = ltrans.aboutprogram
    showinfo(programmtxt, uebertxt)

def onlinehelp():
    import webbrowser

    webbrowser.open("http://wiki.pratznschutz.com/index.php/Support-Client")

def updwebsite():
    import webbrowser
    webbrowser.open("http://download.bailey-solution.com/Support-Client")

def dlfernwartung():
    import urllib

    tempdir = (curdir + sep + "temp")
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)

    if _osenv() == "nt":
        showinfo(ltrans.button_support_teamviewer_download, ltrans.label_shortdesc_teamviewer_download)
        urllib.urlretrieve(dlsource.twclient_nt, savfilent)
        showinfo(ltrans.button_support_teamviewer_download, ltrans.label_shortdesc_teamviewer_download_fertig)
    elif _osenv() == "linux":
        showinfo(ltrans.button_support_teamviewer_download, ltrans.label_shortdesc_teamviewer_download)
        urllib.urlretrieve(dlsource.twclient_linux, savfilelinux)
        os.system("tar xfz " + savfilelinux + " -C " + curdir + sep + "temp" + sep)
        showinfo(ltrans.button_support_teamviewer_download, ltrans.label_shortdesc_teamviewer_download_fertig)
    elif _osenv() == "macos":
        showinfo(ltrans.button_support_teamviewer_download, ltrans.label_shortdesc_teamviewer_download)
        urllib.urlretrieve(dlsource.twclient_macos, savfilemacos)
        showinfo(ltrans.button_support_teamviewer_download, ltrans.label_shortdesc_teamviewer_download_fertig)
    return 0

def twstart():
    if _osenv() == "nt":
        # appstart = [savfilent]
        p1 = Popen(savfilent)

    elif _osenv() == "linux":
        # appstart = twstart_linux
        p1 = Popen(twstart_linux)

    elif _osenv() == "macos":
        appstart = ['open', savfilemacos]
        p1 = Popen(appstart)
    return 0

def ende():
    main.destroy()

def inetcon():
    pingopt = ''

    if _osenv() == "nt":
        pingopt = '-n'
    elif _osenv() == "linux":
        pingopt = '-c'
    elif _osenv() == "macos":
        pingopt = '-c'
    else:
        pingopt = '-c'

    if os.system("ping " + pingopt + " " + _check.rate + " " + _check.pingurl) == 0:
        lb2["text"] = ltrans.display_connection_true
        lb2["bg"] = "#00FF00"
    else:
        lb2["text"] = ltrans.display_connection_false
        lb2["bg"] = "#FF0000"
    return 0

def helpsteps():
    showinfo(ltrans.button_help_steps, ltrans.programm_description)


# Main Window
main = tk.Tk()
# window Title
main.wm_title(ltrans.programm_name)

main.grid_columnconfigure(0, weight=1)
main.resizable(True, True)

# dropdown Menu
menu = tk.Menu(main)
main.config(menu=menu)
dateimenu = tk.Menu(menu)
menu.add_cascade(label=ltrans.button_filemenu_label, menu=dateimenu)

if _osenv() != 'nt':
    dateimenu.add_command(label=ltrans.button_config_editconf, command=editconfiguration)

dateimenu.add_separator()
dateimenu.add_command(label=ltrans.button_filemenu_end, command=ende)

toolmenu = tk.Menu(menu)
menu.add_cascade(label=ltrans.button_support_label, menu=toolmenu)
toolmenu.add_command(label=ltrans.button_connection, command=inetcon)
toolmenu.add_separator()
toolmenu.add_command(label=ltrans.button_support_teamviewer_download, command=dlfernwartung)
toolmenu.add_command(label=ltrans.button_support_teamviewer_start, command=twstart)

hilfemenu = tk.Menu(menu)
menu.add_cascade(label=ltrans.button_help_label, menu=hilfemenu)
hilfemenu.add_command(label=ltrans.button_help_steps, command=helpsteps)
hilfemenu.add_command(label=ltrans.button_help_online, command=onlinehelp)
hilfemenu.add_command(label=ltrans.button_update, command=update_program)
hilfemenu.add_separator()
hilfemenu.add_command(label=ltrans.button_help_aboutus, command=aboutprogram)
hilfemenu.add_command(label=ltrans.button_to_update_url, command=updwebsite)

#Image
imglogo = tk.PhotoImage(file=curdir + sep + "bin" + sep + "image" + sep + "support-client.gif")

# Label
lbapp = tk.Label(main, text=programmtxt)
lbapp["font"] = "Courier 14 italic"
lbapp["height"] = 1
lbapp["width"] = 25
lbapp["borderwidth"] = 2
lbapp["relief"] = "ridge"
lbapp["fg"] = "#000000"
lbapp["anchor"] = "center"
lbapp.grid(column=0, row=0, columnspan=6)

lbspace = tk.Label(main, compound=tk.TOP, text=ltrans.programm_shortdesc, font="Courier 12", anchor="center",
                   fg="#000000", image=imglogo).grid(column=0, row=3, columnspan=6)

lb2 = tk.Label(main)
lb2["text"] = ltrans.display_connection
lb2["bg"] = "#ffa500"
lb2["font"] = "Courier 12"
lb2["height"] = 2
lb2["width"] = 22
lb2["relief"] = "ridge"
lb2["fg"] = "#000000"
lb2["anchor"] = "center"
lb2.grid(column=0, row=6, columnspan=6)

b_ende = tk.Button(main, text=ltrans.button_filemenu_end, command=ende, height=3, width=12).grid(column=0, row=12,
                                                                                                 columnspan=6)
b_chkdb = tk.Button(main, text=ltrans.button_connection, command=inetcon, height=3, width=25).grid(column=0, row=7,
                                                                                                   columnspan=6)
b_dlremotecontrol = tk.Button(main, text=ltrans.button_support_teamviewer_download, command=dlfernwartung, height=3,
                              width=25).grid(column=0, row=9, columnspan=6)
b_startremotecontrol = tk.Button(main, text=ltrans.button_support_teamviewer_start, command=twstart, height=3,
                                 width=25).grid(column=0, row=11, columnspan=6)

main.mainloop()
