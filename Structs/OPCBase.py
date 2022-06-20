from Interfaces.IOPCBase import IOPCBase
import pythoncom


class OPCBase(IOPCBase):
    def __init__(self, comObject):
        self._object = comObject

    @property
    def Parent(self):
        return self._object.Parent


class OPCBaseServer(IOPCBase):
    def __init__(self, comObject):
        pythoncom.CoInitialize()
        self._object = comObject

