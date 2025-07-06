import glfw
from OpenGL.GL import *
from OpenGL.GL.ARB.texture_float import *
from OpenGL.GL.ARB.framebuffer_object import *
import numpy as np

class GlStateManager:
    class AlphaState:
        def __init__(self):
            self.alphaTest = GlStateManager.BooleanState(3008)
            self.func = 519
            self.ref = -1.0

    class BlendState:
        def __init__(self):
            self.blend = GlStateManager.BooleanState(3042)
            self.srcFactor = 1
            self.dstFactor = 0
            self.srcFactorAlpha = 1
            self.dstFactorAlpha = 0

    class BooleanState:
        def __init__(self, capability_in):
            self.capability = capability_in
            self.current_state = False

        def setDisabled(self):
            self.setState(False)

        def setEnabled(self):
            self.setState(True)

        def setState(self, state):
            if state != self.current_state:
                self.current_state = state
                if state:
                    glEnable(self.capability)
                else:
                    glDisable(self.capability)

    class ClearState:
        def __init__(self):
            self.depth = 1.0
            self.color = GlStateManager.Color(0.0, 0.0, 0.0, 0.0)
            self.field_179204_c = 0

    class Color:
        def __init__(self, red_in=1.0, green_in=1.0, blue_in=1.0, alpha_in=1.0):
            self.red = red_in
            self.green = green_in
            self.blue = blue_in
            self.alpha = alpha_in

    class ColorLogicState:
        def __init__(self):
            self.colorLogicOp = GlStateManager.BooleanState(3058)
            self.opcode = 5379

    class ColorMask:
        def __init__(self):
            self.red = True
            self.green = True
            self.blue = True
            self.alpha = True

    class ColorMaterialState:
        def __init__(self):
            self.colorMaterial = GlStateManager.BooleanState(2903)
            self.face = 1032
            self.mode = 5634

    class CullState:
        def __init__(self):
            self.cullFace = GlStateManager.BooleanState(2884)
            self.mode = 1029

    class DepthState:
        def __init__(self):
            self.depthTest = GlStateManager.BooleanState(2929)
            self.maskEnabled = True
            self.depthFunc = 513

    class FogState:
        def __init__(self):
            self.fog = GlStateManager.BooleanState(2912)
            self.mode = 2048
            self.density = 1.0
            self.start = 0.0
            self.end = 1.0

    class PolygonOffsetState:
        def __init__(self):
            self.polygonOffsetFill = GlStateManager.BooleanState(32823)
            self.polygonOffsetLine = GlStateManager.BooleanState(10754)
            self.factor = 0.0
            self.units = 0.0

    class StencilFunc:
        def __init__(self):
            self.field_179081_a = 519
            self.field_179079_b = 0
            self.field_179080_c = -1

    class StencilState:
        def __init__(self):
            self.field_179078_a = GlStateManager.StencilFunc()
            self.field_179076_b = -1
            self.field_179077_c = 7680
            self.field_179074_d = 7680
            self.field_179075_e = 7680

    class TexGen:
        S = 0
        T = 1
        R = 2
        Q = 3

    class TexGenCoord:
        def __init__(self, p_i46254_1_, p_i46254_2_):
            self.coord = p_i46254_1_
            self.textureGen = GlStateManager.BooleanState(p_i46254_2_)
            self.param = -1

    class TexGenState:
        def __init__(self):
            self.s = GlStateManager.TexGenCoord(8192, 3168)
            self.t = GlStateManager.TexGenCoord(8193, 3169)
            self.r = GlStateManager.TexGenCoord(8194, 3170)
            self.q = GlStateManager.TexGenCoord(8195, 3171)

    class TextureState:
        def __init__(self):
            self.texture2DState = GlStateManager.BooleanState(3553)
            self.textureName = 0

    alphaState = AlphaState()
    lightingState = BooleanState(2896)
    
    lightState = []
    for i in range(8):
        lightState.append(BooleanState(16384 + i))

    colorMaterialState = ColorMaterialState()
    blendState = BlendState()
    depthState = DepthState()
    fogState = FogState()
    cullState = CullState()
    polygonOffsetState = PolygonOffsetState()
    colorLogicState = ColorLogicState()
    texGenState = TexGenState()
    clearState = ClearState()
    stencilState = StencilState()
    normalizeState = BooleanState(2977)
    activeTextureUnit = 0
    textureState = []
    for i in range(8):
        textureState.append(TextureState(16384 + i))

    activeShadeModel = 7425
    rescaleNormalState = BooleanState(32826)
    colorMaskState = ColorMask()
    colorState = Color()

    @staticmethod
    def pushAttrib():
        glPushAttrib(8256)

    @staticmethod
    def popAttrib():
        glPopAttrib()

    @staticmethod
    def disableAlpha():
        GlStateManager.alphaState.alphaTest.setDisabled()

    @staticmethod
    def enableAlpha():
        GlStateManager.alphaState.alphaTest.setEnabled()

    @staticmethod
    def alphaFunc(func, ref):
        if func != GlStateManager.alphaState.func or ref != GlStateManager.alphaState.ref:
            GlStateManager.alphaState.func = func
            GlStateManager.alphaState.ref = ref
            glAlphaFunc(func, ref)

    @staticmethod
    def enableLighting():
        GlStateManager.lightingState.setEnabled()

    @staticmethod
    def disableLighting():
        GlStateManager.lightingState.setDisabled()

    @staticmethod
    def enableLight(light):
        GlStateManager.lightState[light].setEnabled()

    @staticmethod
    def disableLight(light):
        GlStateManager.lightState[light].setDisabled()

    @staticmethod
    def enableColorMaterial():
        GlStateManager.colorMaterialState.colorMaterial.setEnabled()

    @staticmethod
    def disableColorMaterial():
        GlStateManager.colorMaterialState.colorMaterial.setDisabled()

    @staticmethod
    def colorMaterial(face, mode):
        if face != GlStateManager.colorMaterialState.face or mode != GlStateManager.colorMaterialState.mode:
            GlStateManager.colorMaterialState.face = face
            GlStateManager.colorMaterialState.mode = mode
            glColorMaterial(face, mode)

    @staticmethod
    def disableDepth():
        GlStateManager.depthState.depthTest.setDisabled()

    @staticmethod
    def enableDepth():
        GlStateManager.depthState.depthTest.setEnabled()

    @staticmethod
    def depthFunc(depthFunc):
        if depthFunc != GlStateManager.depthState.depthFunc:
            GlStateManager.depthState.depthFunc = depthFunc
            glDepthFunc(depthFunc)

    @staticmethod
    def depthMask(flag_in):
        if flag_in != GlStateManager.depthState.maskEnabled:
            GlStateManager.depthState.maskEnabled = flag_in
            glDepthMask(flag_in)

    @staticmethod
    def disableBlend():
        GlStateManager.blendState.blend.setDisabled()

    @staticmethod
    def enableBlend():
        GlStateManager.blendState.blend.setEnabled()

    @staticmethod
    def blendFunc(srcFactor, dstFactor):
        if srcFactor != GlStateManager.blendState.srcFactor or dstFactor != GlStateManager.blendState.dstFactor:
            GlStateManager.blendState.srcFactor = srcFactor
            GlStateManager.blendState.dstFactor = dstFactor
            glBlendFunc(srcFactor, dstFactor)

    @staticmethod
    def tryBlendFuncSeparate(srcFactor, dstFactor, srcFactorAlpha, dstFactorAlpha):
        if srcFactor != GlStateManager.blendState.srcFactor or dstFactor != GlStateManager.blendState.dstFactor or srcFactorAlpha != GlStateManager.blendState.srcFactorAlpha or dstFactorAlpha != GlStateManager.blendState.dstFactorAlpha:
            GlStateManager.blendState.srcFactor = srcFactor
            GlStateManager.blendState.dstFactor = dstFactor
            GlStateManager.blendState.srcFactorAlpha = srcFactorAlpha
            GlStateManager.blendState.dstFactorAlpha = dstFactorAlpha
            glBlendFuncSeparate(srcFactor, dstFactor, srcFactorAlpha, dstFactorAlpha)

    @staticmethod
    def enableFog():
        GlStateManager.fogState.fog.setEnabled()

    @staticmethod
    def disableFog():
        GlStateManager.fogState.fog.setDisabled()

    @staticmethod
    def setFog(param):
        if param != GlStateManager.fogState.mode:
            GlStateManager.fogState.mode = param
            glFogi(GL_FOG_MODE, param)

    @staticmethod
    def setFogDensity(param):
        if param != GlStateManager.fogState.density:
            GlStateManager.fogState.density = param
            glFogf(GL_FOG_DENSITY, param)

    @staticmethod
    def setFogStart(param):
        if param != GlStateManager.fogState.start:
            GlStateManager.fogState.start = param
            glFogf(GL_FOG_START, param)

    @staticmethod
    def setFogEnd(param):
        if param != GlStateManager.fogState.end:
            GlStateManager.fogState.end = param
            glFogf(GL_FOG_END, param)

    @staticmethod
    def enableCull():
        GlStateManager.cullState.cullFace.setEnabled()

    @staticmethod
    def disableCull():
        GlStateManager.cullState.cullFace.setDisabled()

    @staticmethod
    def cullFace(mode):
        if mode != GlStateManager.cullState.mode:
            GlStateManager.cullState.mode = mode
            glCullFace(mode)

    @staticmethod
    def enablePolygonOffset():
        GlStateManager.polygonOffsetState.polygonOffsetFill.setEnabled()

    @staticmethod
    def disablePolygonOffset():
        GlStateManager.polygonOffsetState.polygonOffsetFill.setDisabled()

    @staticmethod
    def doPolygonOffset(factor, units):
        if factor != GlStateManager.polygonOffsetState.factor or units != GlStateManager.polygonOffsetState.units:
            GlStateManager.polygonOffsetState.factor = factor
            GlStateManager.polygonOffsetState.units = units
            glPolygonOffset(factor, units)

    @staticmethod
    def enableColorLogic():
        GlStateManager.colorLogicState.colorLogicOp.setEnabled()

    @staticmethod
    def disableColorLogic():
        GlStateManager.colorLogicState.colorLogicOp.setDisabled()

    @staticmethod
    def colorLogicOp(opcode):
        if opcode != GlStateManager.colorLogicState.opcode:
            GlStateManager.colorLogicState.opcode = opcode
            glLogicOp(opcode)

    @staticmethod
    def enableTexGenCoord(p_179087_0_):
        texGenCoord = GlStateManager.texGenCoord(p_179087_0_)
        texGenCoord.textureGen.setEnabled()

    @staticmethod
    def disableTexGenCoord(p_179100_0_):
        texGenCoord = GlStateManager.texGenCoord(p_179100_0_)
        texGenCoord.textureGen.setDisabled()

    @staticmethod
    def texGen(p_179105_0_, param):
        texGenCoord = GlStateManager.texGenCoord(p_179105_0_)
        if param != texGenCoord.param:
            texGenCoord.param = param
            glTexGeni(texGenCoord.coord, GL_TEXTURE_GEN_MODE, param)

    @staticmethod
    def texGen(p_179105_0_, pname, params):
        texGenCoord = GlStateManager.texGenCoord(p_179105_0_)
        if isinstance(params, int):
            glTexGeni(texGenCoord.coord, pname, params)
        elif isinstance(params, (list, tuple, np.ndarray)):
            if pname in [GL_TEXTURE_GEN_MODE, GL_OBJECT_PLANE, GL_EYE_PLANE]:
                if len(params) == 4:
                    if isinstance(params[0], float):
                        glTexGenfv(texGenCoord.coord, pname, params)
                    elif isinstance(params[0], int):
                        glTexGeniv(texGenCoord.coord, pname, params)
                    else:
                        raise TypeError("Params must be of type float or int")
                else:
                    raise ValueError("Params must be a list, tuple, or numpy array of length 4")
            else:
                raise ValueError("Invalid pname for texGen")
        else:
            raise TypeError("Params must be of type int, list, tuple, or numpy array")

    @staticmethod
    def texGenCoord(p_179125_0_):
        if p_179125_0_ == GlStateManager.TexGen.S:
            return GlStateManager.texGenState.s
        elif p_179125_0_ == GlStateManager.TexGen.T:
            return GlStateManager.texGenState.t
        elif p_179125_0_ == GlStateManager.TexGen.R:
            return GlStateManager.texGenState.r
        elif p_179125_0_ == GlStateManager.TexGen.Q:
            return GlStateManager.texGenState.q
        else:
            return GlStateManager.texGenState.s

    @staticmethod
    def setActiveTexture(texture):
        if GlStateManager.activeTextureUnit != texture - GL_TEXTURE0:
            GlStateManager.activeTextureUnit = texture - GL_TEXTURE0
            glActiveTexture(texture)

    @staticmethod
    def enableTexture2D():
        GlStateManager.textureState[GlStateManager.activeTextureUnit].texture2DState.setEnabled()

    @staticmethod
    def disableTexture2D():
        GlStateManager.textureState[GlStateManager.activeTextureUnit].texture2DState.setDisabled()

    @staticmethod
    def generateTexture():
        texture = glGenTextures(1)
        return texture

    @staticmethod
    def deleteTexture(texture):
        glDeleteTextures(texture)
        for state in GlStateManager.textureState:
            if state.textureName == texture:
                state.textureName = -1

    @staticmethod
    def bindTexture(texture):
        if texture != GlStateManager.textureState[GlStateManager.activeTextureUnit].textureName:
            GlStateManager.textureState[GlStateManager.activeTextureUnit].textureName = texture
            glBindTexture(GL_TEXTURE_2D, texture)

    @staticmethod
    def enableNormalize():
        GlStateManager.normalizeState.setEnabled()

    @staticmethod
    def disableNormalize():
        GlStateManager.normalizeState.setDisabled()

    @staticmethod
    def shadeModel(mode):
        if mode != GlStateManager.activeShadeModel:
            GlStateManager.activeShadeModel = mode
            glShadeModel(mode)

    @staticmethod
    def enableRescaleNormal():
        GlStateManager.rescaleNormalState.setEnabled()

    @staticmethod
    def disableRescaleNormal():
        GlStateManager.rescaleNormalState.setDisabled()

    @staticmethod
    def viewport(x, y, width, height):
        glViewport(x, y, width, height)

    @staticmethod
    def colorMask(red, green, blue, alpha):
        if red != GlStateManager.colorMaskState.red or green != GlStateManager.colorMaskState.green or blue != GlStateManager.colorMaskState.blue or alpha != GlStateManager.colorMaskState.alpha:
            GlStateManager.colorMaskState.red = red
            GlStateManager.colorMaskState.green = green
            GlStateManager.colorMaskState.blue = blue
            GlStateManager.colorMaskState.alpha = alpha
            glColorMask(red, green, blue, alpha)

    @staticmethod
    def clearDepth(depth):
        if depth != GlStateManager.clearState.depth:
            GlStateManager.clearState.depth = depth
            glClearDepth(depth)

    @staticmethod
    def clearColor(red, green, blue, alpha):
        if red != GlStateManager.clearState.color.red or green != GlStateManager.clearState.color.green or blue != GlStateManager.clearState.color.blue or alpha != GlStateManager.clearState.color.alpha:
            GlStateManager.clearState.color.red = red
            GlStateManager.clearState.color.green = green
            GlStateManager.clearState.color.blue = blue
            GlStateManager.clearState.color.alpha = alpha
            glClearColor(red, green, blue, alpha)

    @staticmethod
    def clear(mask):
        glClear(mask)

    @staticmethod
    def matrixMode(mode):
        glMatrixMode(mode)

    @staticmethod
    def loadIdentity():
        glLoadIdentity()

    @staticmethod
    def pushMatrix():
        glPushMatrix()

    @staticmethod
    def popMatrix():
        glPopMatrix()

    @staticmethod
    def getFloat(pname, params):
        glGetFloatv(pname, params)

    @staticmethod
    def ortho(left, right, bottom, top, zNear, zFar):
        glOrtho(left, right, bottom, top, zNear, zFar)

    @staticmethod
    def rotate(angle, x, y, z):
        glRotatef(angle, x, y, z)

    @staticmethod
    def scale(x, y, z):
        glScalef(x, y, z)

    @staticmethod
    def scale(x, y, z):
        glScaled(x, y, z)

    @staticmethod
    def translate(x, y, z):
        glTranslatef(x, y, z)

    @staticmethod
    def translate(x, y, z):
        glTranslated(x, y, z)

    @staticmethod
    def multMatrix(matrix):
        if matrix.dtype == np.float32:
            glMultMatrixf(matrix)
        elif matrix.dtype == np.float64:
            glMultMatrixd(matrix)
        else:
            raise TypeError("Matrix must be of type float32 or float64")

    @staticmethod
    def color(color_red, color_green, color_blue, color_alpha):
        if color_red != GlStateManager.colorState.red or color_green != GlStateManager.colorState.green or color_blue != GlStateManager.colorState.blue or color_alpha != GlStateManager.colorState.alpha:
            GlStateManager.colorState.red = color_red
            GlStateManager.colorState.green = color_green
            GlStateManager.colorState.blue = color_blue
            GlStateManager.colorState.alpha = color_alpha
            glColor4f(color_red, color_green, color_blue, color_alpha)

    @staticmethod
    def color(color_red, color_green, color_blue):
        GlStateManager.color(color_red, color_green, color_blue, 1.0)

    @staticmethod
    def resetColor():
        GlStateManager.colorState.red = GlStateManager.colorState.green = GlStateManager.colorState.blue = GlStateManager.colorState.alpha = -1.0

    @staticmethod
    def callList(list_):
        glCallList(list_)