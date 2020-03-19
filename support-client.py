#!/usr/bin/python3
# -*- coding: utf-8 -*-
############################################
# MIT License Copyright 2020 Günter Bailey #
############################################
import tkinter as tk
from tkinter import Menu
from tkinter.ttk import Progressbar
from tkinter import messagebox as mbox
from gettext import gettext as _
from bin import __version__, ABOUTPROGRAM, ABOUTTXT, PROGRAM_NAME
from bin.findenv import get_osname as _osenv
from bin.license import information
from os import curdir, sep, path, mkdir
import threading
from subprocess import Popen, PIPE
import json
from datetime import datetime

try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve

#
# def onlinehelp():
#     import webbrowser
#     webbrowser.open("http://wiki.pratznschutz.com/index.php/Support-Client")
#
#
# def updwebsite():
#     import webbrowser
#     webbrowser.open("http://download.bailey-solution.com/Support-Client")
#

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title(f"{PROGRAM_NAME} {__version__}")
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)
        self.config = dict({'version': __version__, 'tmpdir': curdir + sep + 'tmp',
                            'email': 'office@bailey-solution.com', 'phone': '+43(0)720/517219',
                            'webpage': 'https://www.bailey-solution.com',
                            'remote_app': dict({'server': 'https://download.b2go.cloud/Support-Client/bin/',
                                                'nt': 'TVQS.exe', 'macos': 'TVQS.dmg', 'linux': 'TVQS.exe'}),
                            'test': dict({'ping': dict({'server': 'google.com', 'repeat': 4, 'result': 'no result',
                                                        'ip': '8.8.8.8'})
                                          })
                            })

        self.setup(load=True)
        self.check_folder()
        self.child = None
        # configuration
        self.tmpdir = None
        self.test_ping_server = None
        self.test_ping_ip = None
        self.test_ping_repeat = None
        # start UI
        self.initUI()

    def save_edit_configuration(self):
        self.config.update({'tmpdir': self.tmpdir.get()})
        self.config['test']['ping'].update({'server': self.test_ping_server.get(),
                                            'repeat': int(self.test_ping_repeat.get()),
                                            'ip': self.test_ping_ip.get()})

        if self.setup(write=True):
            mbox.showinfo(title=f"{PROGRAM_NAME} {__version__}", message=_("Configuration saved"))
            self.child.destroy()

    def edit_configuration(self):
        win = tk.Toplevel()
        win.wm_title(_(f"{PROGRAM_NAME} {__version__} Edit Configuration"))
        win.grid_columnconfigure(0, weight=1)
        win.resizable(True, True)
        tk.Label(win, text=f"Version {self.config['version']}").grid(row=0, column=0, columnspan=6)

        self.child = win
        self.tmpdir = tk.StringVar(value=self.config['tmpdir'])
        tk.Label(win, text=_("Download Directory")).grid(row=1, column=0)
        tk.Entry(win, bd=2, textvariable=self.tmpdir).grid(row=1, column=1)

        tk.Label(win, text=_("Connection Check Settings")).grid(row=2, column=1, columnspan=6)

        self.test_ping_server = tk.StringVar(value=self.config['test']['ping']['server'])
        tk.Label(win, text=_("Server")).grid(row=5, column=0)
        tk.Entry(win, bd=2, textvariable=self.test_ping_server).grid(row=5, column=1)

        self.test_ping_ip = tk.StringVar(value=self.config['test']['ping']['ip'])
        tk.Label(win, text=_("IP")).grid(row=10, column=0)
        tk.Entry(win, bd=2, textvariable=self.test_ping_ip).grid(row=10, column=1)

        self.test_ping_repeat = tk.IntVar(value=self.config['test']['ping']['repeat'])
        tk.Label(win, text=_("Ping Repeat min. 2")).grid(row=20, column=0)
        tk.Entry(win, bd=2, textvariable=self.test_ping_repeat).grid(row=20, column=1)

        remote_app_server_url = tk.StringVar(value=self.config['remote_app']['server'])
        remote_app_tv = tk.StringVar(value=self.config['remote_app'][_osenv()])
        tk.Label(win, text=_("Remote Server")).grid(row=30, column=0)
        tk.Entry(win, bd=2, state="readonly", textvariable=remote_app_server_url).grid(row=30, column=1)

        tk.Label(win, text=_("Program")).grid(row=40, column=0)
        tk.Entry(win, bd=2, state="readonly", textvariable=remote_app_tv).grid(row=40, column=1)

        tk.Button(win, width=20, height=2, text=_("Close"), command=win.destroy).grid(row=50, column=0)
        tk.Button(win, width=20, height=2, text=_("Save"), command=self.save_edit_configuration).grid(row=50, column=1)

    def check_folder(self):
        if not path.exists(self.config['tmpdir']):
            mkdir(self.config['tmpdir'])

    def setup(self, load=False, write=False):
        jsonfile = curdir + sep + "config.json"
        if not path.isfile(jsonfile):
            with open(jsonfile, "w") as f:
                f.write(json.dumps(self.config))

        if load:
            with open(jsonfile, "r") as f:
                cfg = json.loads(f.read())
            if self.config['version'] > cfg.get('version', '0.1a'):
                with open(jsonfile, "w") as f:
                    f.write(json.dumps(self.config))
            else:
                self.config.update(cfg)
        elif write:
            with open(jsonfile, "w") as f:
                f.write(json.dumps(self.config))
        return True

    def initUI(self):
        self.windows = []
        label = tk.Label(self, text=PROGRAM_NAME)
        label["font"] = "Courier 14 italic"
        label["height"] = 1
        label["width"] = 25
        label["borderwidth"] = 2
        label["relief"] = "ridge"
        label["fg"] = "#000000"
        label["anchor"] = "center"
        label.grid(row=0, column=0, columnspan=6)

        self.logo = tk.PhotoImage(file=curdir + sep + "bin" + sep + "image" + sep + "support-client.gif")
        self.Artwork = tk.Label(self, compound=tk.TOP,
                                text=_("press the button \nstart remote support and \ntell the support the"
                                       " \nTeamviewer ID and Password.\n"), font="Courier 12", anchor="center",
                                fg="#000000", image=self.logo).grid(row=1, column=0, columnspan=5, sticky="N",
                                                                    rowspan=2)
        tk.Label(self, text=_(f"Tech Support \n Phone: {self.config['phone']}\n E-Mail: {self.config['email']}"),
                 font="Courier 12", anchor="center", fg="#000000").grid(row=4, column=0, columnspan=5, sticky="N")

        menubar = Menu(self.master)
        dateimenu = Menu(menubar)
        supportmenu = Menu(menubar)
        helpmenu = Menu(menubar)
        self.configure(menu=menubar)

        menubar.add_cascade(label=_("File"), menu=dateimenu)
        dateimenu.add_command(label=_("Edit Configuration"), command=self.edit_configuration)
        dateimenu.add_command(label=_("Close"), command=self.quit)

        menubar.add_cascade(label=_("Support"), menu=supportmenu)
        supportmenu.add_command(label=_("Check Internet Connection"), command=self.ping_tool)
        supportmenu.add_command(label=_("Start Remotesupport"), command=self.tw_start)
        supportmenu.add_command(label=_("Download Remotetool"), command=self.download_supporttool)
        supportmenu.add_separator()

        menubar.add_cascade(label=_("Help"), menu=helpmenu)
        helpmenu.add_command(label=_(f"About {PROGRAM_NAME}"), command=self.about_program)
        helpmenu.add_separator()
        helpmenu.add_command(label=_("License"), command=self.show_license)
        helpmenu.add_command(label=_("Manual"), command=self.manual)
        helpmenu.add_command(label=_("Update"), command=self.update_program)

        tk.Label(self, text='').grid(row=5, column=0)

        self.conntestlb = tk.Label(self)
        self.conntestlb["text"] = _("Internet Connection ?")
        self.conntestlb["bg"] = "#ffa500"
        self.conntestlb["font"] = "Courier 12"
        self.conntestlb["height"] = 2
        self.conntestlb["width"] = 22
        self.conntestlb["relief"] = "ridge"
        self.conntestlb["fg"] = "#000000"
        self.conntestlb["anchor"] = "center"
        self.conntestlb.grid(column=0, row=6, columnspan=6)

        tk.Label(self, text='').grid(row=15, column=0)
        self.progressbar = Progressbar(self, orient='horizontal', length=260, mode='indeterminate')
        self.progressbar.grid(row=18, column=0, columnspan=3)
        self.progressbar.grid_forget()

        tk.Label(self, text='').grid(row=20, column=0)
        tk.Button(self, width=20, height=2, text=_("Start Remotesupport"), command=self.tw_start).grid(row=25, column=0)
        tk.Label(self, text='').grid(row=30, column=0)
        tk.Button(self, width=20, height=2, text=_("Close"), command=self.quit).grid(row=50, column=0)
        tk.Label(self, text='').grid(row=60, column=0)

        tk.Label(self, text=f"Bailey-Solution @{datetime.now().year}").grid(row=70, column=0, columnspan=2)

    def download_supporttool(self, parentprocess=True):
        def download():
            if parentprocess:
                self.progressbar.grid(row=18, column=0, columnspan=3)
                self.progressbar.start()
            try:
                self.check_folder()
                urlretrieve(url=f"{self.config['remote_app']['server']}{self.config['remote_app'][_osenv()]}",
                            filename=f"{self.config['tmpdir']}{sep}{self.config['remote_app'][_osenv()]}")
                if parentprocess:
                    mbox.showinfo(title=_("Download"), message=_(f"Image {self.config['remote_app'][_osenv()]} downloaded"))
            except Exception as exp:
                print("exception = ", exp)
                mbox.showwarning(title=_("Download Error"), message=exp)
            if parentprocess:
                self.progressbar.stop()
                self.progressbar.grid_forget()
            return True
        if parentprocess:
            threading.Thread(target=download).start()
        else:
            download()
        return True

    def tw_start(self):
        def start():
            self.progressbar.grid(row=18, column=0, columnspan=3)
            self.progressbar.start()
            try:
                fpath = self.config.get('tmpdir', curdir+sep+'tmp')
                if not path.isfile(f"{fpath}{sep}{self.config['remote_app'][_osenv()]}"):
                    self.download_supporttool(parentprocess=False)
                appstart = None
                if _osenv() == "nt":
                    appstart = [fpath+sep+self.config['remote_app'][_osenv()]]
                elif _osenv() == "macos":
                    appstart = ['open', fpath+sep+self.config['remote_app'][_osenv()]]

                if appstart:
                    Popen(appstart)
                else:
                    mbox.showwarning(title=_("Start Remotesupport"), message=_("Programm not found"))
            except Exception as exp:
                print("error = ", exp)
                mbox.showwarning(title=_("Start Remotesupport"), message=str(exp))
            self.progressbar.stop()
            self.progressbar.grid_forget()
            return True
        threading.Thread(target=start).start()
        return True

    def ping_tool(self):
        def ping():
            self.progressbar.grid(row=18, column=0, columnspan=3)
            self.progressbar.start()
            try:
                self.conntestlb["bg"] = "#00FF00"
                self.conntestlb["text"] = _("Check Running...")
                cmd = ['ping']
                if _osenv() == "nt":
                    cmd.append('-n')
                elif _osenv() in ["linux", "macos"]:
                    cmd.append('-c')
                else:
                    cmd.append('-c')

                cmd1 = cmd
                cmd1.append(str(self.config['test']['ping']['repeat']))
                cmd1.append(self.config['test']['ping']['ip'])
                p1 = Popen(cmd1, stdout=PIPE)
                result, error = p1.communicate()
                if error:
                    self.conntestlb["bg"] = "#FF0000"
                    self.conntestlb["text"] = _("DNS error")

                cmd2 = cmd
                cmd2.append(str(self.config['test']['ping']['repeat']))
                cmd2.append(self.config['test']['ping']['server'])
                p2 = Popen(cmd2, stdout=PIPE)
                result2, error2 = p2.communicate()
                if error2:
                    self.conntestlb["bg"] = "#FF0000"
                    self.conntestlb["text"] = _("no connection")

                if error or error2:
                    mbox.showwarning(title=_("Ping Error"), message=f"{error}\n{error2}")
                else:
                    self.conntestlb["bg"] = "#00FF00"
                    self.conntestlb["text"] = _("connection OK")
                    mbox.showinfo(title=_("Ping Successful"), message=_("Ping Successful"))
            except Exception as exp:
                print("exception = ", exp)
                mbox.showwarning(title=_("Error on PING Command"), message=exp)
            self.progressbar.stop()
            self.progressbar.grid_forget()
            return True
        threading.Thread(target=ping).start()

    def manual(self):
        desc = _("To start the Remoteconnection for Tech Support, klick on Start Remotesupport.")
        mbox.showinfo(title=_("Manual"), message=desc)

    def show_license(self):
        mbox.showinfo(title=_("License"), message=information)

    def about_program(self):
        mbox.showinfo(title=_(f"About {PROGRAM_NAME}"), message=ABOUTPROGRAM)

    def update_program(self):
        # from bin import update
        # update.start_updater()
        mbox.showinfo(title=f"Update {PROGRAM_NAME} {__version__}", message=_("feature is comming soon."))


if __name__ == "__main__":
    app = App()
    app.mainloop()
