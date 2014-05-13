import os
import wx
from objects.xml.xml_move import XmlObject
from logic.xml_parser import XmlParser

class HandleFiles():

    def __init__(self, window):
        self.__window = window
        self.current_xml = XmlObject()
        self._xml_parser = XmlParser()

    def open(self, event):
        openFileDialog = wx.FileDialog(self.__window, "Open XML file", self._xml_parser.CONST_XML_LOCATION, "",
                                       "XML files (*.xml)|*.xml", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_OK:
            filename = openFileDialog.GetFilename()
            directory = openFileDialog.GetDirectory()

            self.current_xml = self._xml_parser.read_file(directory + "/" + filename)
        openFileDialog.Destroy()

    def save(self, event):
        saveFileDialog = wx.FileDialog(self.__window, "Save XML file", self._xml_parser.CONST_XML_LOCATION, "",
                                       "XML files (*.xml)|*.xml", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if saveFileDialog.ShowModal() == wx.ID_OK:
            filename = saveFileDialog.GetFilename()
            directory = saveFileDialog.GetDirectory()

            self._xml_parser.new_file(directory + "/" + filename, self.current_xml)
        saveFileDialog.Destroy()

    def close(self, event):
        pass