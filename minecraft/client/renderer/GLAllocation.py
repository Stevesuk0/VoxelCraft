import ctypes
from OpenGL.GL import *
from OpenGL.GLU import gluErrorString
import numpy as np

class GLAllocation:

    @staticmethod
    def generateDisplayLists(range_):
        i = glGenLists(range_)
        if i == 0:
            err = glGetError()
            s = "No error code reported"
            if err != 0:
                s = gluErrorString(err).decode('utf-8')
            raise RuntimeError(f"glGenLists returned 0 for count {range_}, GL error ({err}): {s}")
        return i

    @staticmethod
    def deleteDisplayLists(list_, range_=1):
        glDeleteLists(list_, range_)

    @staticmethod
    def createDirectByteBuffer(capacity):
        return (ctypes.c_ubyte * capacity)()

    @staticmethod
    def createDirectIntBuffer(capacity):
        buf = (ctypes.c_int * capacity)()
        return buf

    @staticmethod
    def createDirectFloatBuffer(capacity):
        buf = (ctypes.c_float * capacity)()
        return buf
