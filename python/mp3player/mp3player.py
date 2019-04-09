#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import wx


class Mp3Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}

        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 100), style=wx.LC_REPORT | wx.BORDER_SUNKEN)

        self.list_ctrl.InsertColumn(0, 'Artist', width=140)
        self.list_ctrl.InsertColumn(1, 'Album', width=140)
        self.list_ctrl.InsertColumn(2, 'Title', width=200)

        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        edit_button = wx.Button(self, label='Edit')
        edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        main_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(main_sizer)

    @staticmethod
    def on_edit(event):
        print('in on_edit')

    @staticmethod
    def update_mp3_listing(folder_path):
        print(folder_path)


class Mp3Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Mp3 Tag Editor')
        self.panel = Mp3Panel(self)
        self.create_menu()
        self.Show()

    def create_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_folder_menu_item = file_menu.Append(wx.ID_ANY, 'Open Folder',
                                                 'Open a folder with MP3s')
        menu_bar.Append(file_menu, '&File')
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_open_folder,
            source=open_folder_menu_item,
        )
        self.SetMenuBar(menu_bar)

    def on_open_folder(self, event):
        title = "Choose a directory:"
        dlg = wx.DirDialog(self, title, style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.panel.update_mp3_listing(dlg.GetPath())
        dlg.Destroy()


if __name__ == '__main__':
    app = wx.App(False)
    frame = Mp3Frame()
    app.MainLoop()
