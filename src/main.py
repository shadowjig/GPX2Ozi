#!/usr/bin/env python
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import sys
import platform
import os
import gpxpy

#Hard coded output filename.  Path will be the same as input file.
outputfilename = 'ozi.wpt'

class LoadDialog(FloatLayout):
    #Default path based on OS
    if platform.uname()[0] == 'Linux':
        default_path = os.path.abspath('/storage/emulated/0/Download')
    elif platform.uname()[0] == 'Windows':
        default_path = os.path.abspath('c:\\temp')
    else:
        default_path = ''
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    path = ''
    filename = ''
    #uname = platform.uname()[0]

    def dismiss_popup(self):
        self._popup.dismiss()
        
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.path = path
        self.filename = filename
        self.ids['message1'].text = 'File Loaded:\n{0}'.format(os.path.join(path, filename[0]))
        self.dismiss_popup()

    def convert(self):
        if (self.filename == '') or (self.path == ''):
            self.ids['message1'].text = 'Load a GPX file first!!'
            return
        
        infile = os.path.join(self.path, self.filename[0])
        gpx_file = open(infile, 'r')
        outfile = os.path.join(self.path, outputfilename)
        try:
            ozi_file = open(outfile, 'w')
        except Exception as e:
            # Catch any error, e.g. non-writable directory, etc.
            self.ids['message2'].text = str(e).encode('utf-8')
            self.ids['message3'].text = 'If you got a permissions error.\nTry moving the file a folder that\'s writeable.\nOn Android try: /storage/emulated/0/Download'
            return
        
        gpx = gpxpy.parse(gpx_file)

        #Next 4 lines are defaults.  WGS 84 is default datum of GPX file so it's hard coded.
        #http://www.oziexplorer3.com/eng/help/fileformats.html  -  describes ozi wpt file format  
        ozi_file.write('OziExplorer Waypoint File Version 1.1\n')
        ozi_file.write('OziExplorer Waypoint File Version 1.1\n')
        ozi_file.write('WGS 84\n')
        ozi_file.write('Reserved - future use\n')
        ozi_file.write('Reserved - future use\n')
        count = 0
        for waypoint in gpx.waypoints:
            count += 1
            ozi_file.write('{0},{1},{2},{3},{4},0,1,3,0,65535,{1},0,0,0,-777,6,0,17\n'.\
                format(count, waypoint.name, waypoint.latitude, waypoint.longitude,waypoint.time))
        self.ids['message1'].text =  '{0} waypoints exported to:\n{1}'.format(count,os.path.join(self.path, outputfilename))
        return

class Editor(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    Editor().run()
