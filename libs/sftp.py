import pysftp
import time

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

def sftpConnect(localFile, remoteFile):
    try:
        with pysftp.Connection('localhost', username='tester', password='password', cnopts=cnopts) as sftp:
            sftp.put(localFile, remoteFile)
            print("Successfully connected to SFTP...")
    except:
        print("SFTP connection failed!")

