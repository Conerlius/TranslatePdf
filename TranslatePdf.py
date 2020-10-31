#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx
import Scripts.MainWindow as MainWindow

def Start():
    app = wx.App()
    main_windows = MainWindow.Create(None)
    main_windows.Show()
    app.MainLoop()

if __name__ == '__main__':
    Start()