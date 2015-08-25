#!/usr/bin/python
# -*- coding: utf-8 -*-

#Todo: Testing alpha status, it changes the icon from program on Mac OSX

def changeicon(image, file):
    import Cocoa,sys
    Cocoa.NSWorkspace.sharedWorkspace().setIcon_forFile_options_(Cocoa.NSImage.alloc().initWithContentsOfFile_(image.decode('utf-8')), file.decode('utf-8'), 0) or sys.exit("Unable to set file icon")

# Cocoa.NSWorkspace.sharedWorkspace().setIcon_forFile_options_(Cocoa.NSImage.alloc().initWithContentsOfFile_(sys.argv[1].decode('utf-8')), sys.argv[2].decode('utf-8'), 0) or sys.exit("Unable to set file icon")
