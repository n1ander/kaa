from libs import sortFileByTime, getFileName, createZipFile, sftpConnect 

res = sortFileByTime()
mylist = getFileName(res)
zipFile = createZipFile(mylist)
sftpConnect(zipFile.filename, "CustomerX.zip")