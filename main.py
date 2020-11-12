from libs import sortFileByTime, getFileName, getHarmony, getTaylorCreek

res = sortFileByTime()
mylist = getFileName(res)

harmony = getHarmony(mylist)
tc = getTaylorCreek(mylist)
print(harmony)
print(tc)