import os
import time
import zipfile

def createZipFile(mylist):
    date = time.strftime('%Y%m%d', time.gmtime())
    os.chdir('build/')
    zf = zipfile.ZipFile("FMPA" + date + ".zip", mode='w')
    try:
        os.chdir('../docs/')
        for x in mylist:
            zf.write(x)
    finally:
        os.chdir('../build')
        print('closing')
        zf.close()
    return zf