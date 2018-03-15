#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import os
class background(object):
    class folder:
        def __init__(self, folder, type = [".svg"]):
            self.default = "/usr/share/backgrounds"
            self.pl = ["Gtk", "Gnome"]
            self.folder = folder
            self.type = type
        def platform(self):
            os.system("update-alternatives --set desktop-login-background /usr/share/backgrounds/Lock.png")
        def pictures(self, list=[]):
            pictures = os.listdir(self.folder)
            for l in pictures:
                for t in self.type:
                    if l.endswith(t) is True:
                        list.append(l)
            return list
        def random(self):
            return random.choice(self.pictures())
                

get = background.folder(".",  [".png", ".jpg", ".jpeg", ".svg"])
print get.random()
