from os import listdir
from os.path import isfile, join
import os.path
from types import coroutine

from PIL import Image


mypath = "./annotations/"

labelpath = "./labels/"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

for mathfile in onlyfiles:
    lines = []
    with open(mypath + mathfile) as f:
        lines = [line.rstrip() for line in f]
    
    templines = []

    maxisize = -1

    for line in lines:
        commasep = line.split(',')
        temp = []
        for x in commasep:
            temp.append(int(x))
        templines.append(temp)
        maxisize = max(maxisize, temp[0])

    lines = templines

    namewithdotmath = mathfile.split('.')[0]

    outputfilename = labelpath + namewithdotmath + ".txt"

    # if not os.path.isfile(outputfilename):

    for line in lines:
        outputfilename = labelpath + namewithdotmath + "_" +str(line[0]) +".txt"

        if not os.path.exists("./images/"+namewithdotmath+"_"+str(line[0]) + ".png"):
            continue

        im = Image.open("./images/"+namewithdotmath+"_"+str(line[0]) + ".png")

        f= open(outputfilename,"a+")
        coord = line[1:]

        # image = PIL.Image.open("./images/"+namewithdotmath+"_"+str(line[0]) + ".png")

        
        # width, height = im.size

        # temp =  [0,0,0,0,0]

        # xmin = coord[0]
        # xmax = coord[2]
        # ymin = coord[1]
        # ymax = coord[3]

        # xcen = float((xmin + xmax)) / 2 / width
        # ycen = float((ymin + ymax)) / 2 / height

        # w = float((xmax - xmin)) / width
        # h = float((ymax - ymin)) / height

        # temp[1] = xcen
        # temp[2] = ycen
        # temp[3] = w
        # temp[4] = h

        temp =  [0,0,0,0]

        xmin = coord[0]
        xmax = coord[2]
        ymin = coord[1]
        ymax = coord[3]

        xcen = float((xmin + xmax)) / 2
        ycen = float((ymin + ymax)) / 2

        w = float((xmax - xmin))
        h = float((ymax - ymin))

        temp[0] = xcen
        temp[1] = ycen
        temp[2] = w
        temp[3] = h

        coord = temp

        coord = map(str, coord)
        f.write(" ".join(coord))
        f.write("\n")
        f.close()

