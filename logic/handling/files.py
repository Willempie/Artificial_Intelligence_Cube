import wx

__author__ = 'Willem'


class HandleFiles():

    __window = None

    def __init__(self, window):
        self.__window = window
        pass

    def open(self, event):
        openFileDialog = wx.FileDialog(self.__window, "Open XML file", "", "",
                                       "XML files (*.xml)|*.xml", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        pass

    def save(self, event):
        print("save")
        pass

    def close(self, event):
        pass