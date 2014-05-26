import os
import wx
from objects.xml.xml_move import XmlObject
from logic.xml_parser import XmlParser

class HandleFiles():

    def __init__(self, display):
        self.display = display
        self.__window = display.cube_gui.get_window_frame()
        self.current_xml = XmlObject("Some1", self.display._storage.cube_size)
        self._xml_parser = XmlParser()

        self.isset = False

    def __set(self):
        if not self.isset:
            self.current_xml.set_start(self.display._storage._start_cube)
            self.current_xml.set_result(self.display._storage._result_cube)
            self.current_xml.set_code(self.display._storage._code_cube)

            self.current_xml.set_code(self.display._panels.action.steps)
            self.isset = True

    def open(self, event):
        self.__set()
        openFileDialog = wx.FileDialog(self.__window, "Open XML file", self._xml_parser.CONST_XML_LOCATION, "",
                                       "XML files (*.xml)|*.xml", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_OK:
            filename = openFileDialog.GetFilename()
            directory = openFileDialog.GetDirectory()

            self.current_xml = self._xml_parser.read_file(directory + "/" + filename)
        openFileDialog.Destroy()

    def save(self, event):
        self.__set()
        saveFileDialog = wx.FileDialog(self.__window, "Save XML file", self._xml_parser.CONST_XML_LOCATION, "",
                                       "XML files (*.xml)|*.xml", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if saveFileDialog.ShowModal() == wx.ID_OK:
            filename = saveFileDialog.GetFilename()
            directory = saveFileDialog.GetDirectory()

            self._xml_parser.new_file(directory + "/" + filename, self.current_xml)
        saveFileDialog.Destroy()

    def close(self, event):
        pass