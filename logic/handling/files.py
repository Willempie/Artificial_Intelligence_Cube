import os
import wx

__author__ = 'Willem'


class HandleFiles():

    __window = None
    __file_location = None

    def __init__(self, window):
        self.__window = window
        pass

    def open(self, event):
        openFileDialog = wx.FileDialog(self.__window, "Open XML file", "", "",
                                       "XML files (*.xml)|*.xml", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_OK:
            filename = openFileDialog.GetFilename()
            directory = openFileDialog.GetDirectory()
            self.__file_location = directory + "/" + filename
            return self.__file_location
        openFileDialog.Destroy()

    def save(self, event):
        saveFileDialog = wx.FileDialog(self.__window, "Save XML file", "", "",
                                       "XML files (*.xml)|*.xml", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if saveFileDialog.ShowModal() == wx.ID_OK:
            filename = saveFileDialog.GetFilename()
            directory = saveFileDialog.GetDirectory()

            self.__file_location = directory + "/" + filename
            return self.__file_location
        saveFileDialog.Destroy()

    def close(self, event):
        pass