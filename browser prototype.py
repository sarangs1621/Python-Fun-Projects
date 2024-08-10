
import tkinter as tk
import webbrowser

class Check:
    """ create checkbuttons for links """
    def __init__(self, master, site):
        self.var = tk.IntVar()
        self.site = site
        self = tk.Checkbutton(
            master,
            text = self.site,
            variable = self.var,
            command = self.check).pack()
 
    def check(self):
        v = self.var.get() # 1 checked 0 unchecked
        if v:
            checked.append(self.site)
        else:
            if self.site in checked:
                checked.remove(self.site)
 
class App:
    def __init__(self, sites):
        """creates the window"""
        c = []
        master = tk.Tk()
        for site in sites:
            c.append(Check(master, site))
        tk.Button(
            master,
            text = "Launch",
            command = self.start).pack()
        master.mainloop()
 
    def start(self):
        chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        w = webbrowser.get(chrome)
        for checked_site in checked:
            w.open(checked_site)
 
checked = []

app = App([
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://twitter.com/login",
    "https://www.instagram.com/",
    "https://web.whatsapp.com/",
    ])
