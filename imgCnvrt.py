from PIL import Image
from PIL import EpsImagePlugin
#establish where the binary is, substitute for setting PATH variable
EpsImagePlugin.gs_windows_binary =  r"C:\Program Files\gs\gs9.53.3\bin\gswin64c.exe"

#save images
def convert(img, filename):
    im = Image.open(img)
    im.save(filename, lossless = True)