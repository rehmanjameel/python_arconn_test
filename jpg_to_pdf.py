import glob

import img2pdf

with open("name.pdf", "wb") as f:
    f.write(img2pdf.convert(glob.glob("/home/arehman/Desktop/Radio/BCRM/*.jpg")))
    