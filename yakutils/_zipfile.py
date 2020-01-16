import os
from zipfile import ZipFile, ZIP_DEFLATED

def zipdir(src, dst):
    os.chdir(src)
    with ZipFile(dst, 'w', compression=ZIP_DEFLATED) as zfh:
        for root, _, files in os.walk(src):
            for file in files:
                zfh.write(os.path.join(root, file))
    return dst
