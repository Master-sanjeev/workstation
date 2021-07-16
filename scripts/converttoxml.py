import os
import sys
from PIL import Image
from os import listdir
from os.path import isfile, join
import os.path
from types import coroutine
from PIL import Image
from shutil import copyfile



imagesroot = "./images"
mypath = "./annotations/"
labelpath = "./labels/"
outputdir = "./images1"

start = "<annotation>\n\t<folder>{folder}</folder>\n\t<filename>{img}</filename>\n\t<path>/content/workspace/training/images/{img}</path>\n\t<source>\n\t\t<database>Unknown</database>\n\t</source>\n\t<size>\n\t\t<width>{width}</width>\n\t\t<height>{height}</height>\n\t\t<depth>1</depth>\n\t</size>\n\t<segmented>0</segmented>"
data = "\n\t<object>\n\t\t<name>maths</name>\n\t\t<pose>Unspecified</pose>\n\t\t<truncated>0</truncated>\n\t\t<difficult>0</difficult>\n\t\t<bndbox>\n\t\t\t<xmin>{left}</xmin>\n\t\t\t<ymin>{up}</ymin>\n\t\t\t<xmax>{right}</xmax>\n\t\t\t<ymax>{bottom}</ymax>\n\t\t</bndbox>\n\t</object>"
end = "\n</annotation>"



# onlydirs = [f for f in listdir(imagesroot) if not isfile(join(imagesroot, f))]

# for dir in onlydirs:

#     pathofdir = imagesroot + dir + "/"

#     allfiles = [f for f in listdir(pathofdir) if isfile(join(pathofdir, f))]

#     print(allfiles[0])

#     for file in allfiles:

#         fileid = int(file.split(".")[0]) - 1
#         # os.rename(pathofdir + file, pathofdir + dir + "_" + str(fileid) + ".png")
#         copyfile(os.path.join(pathofdir, file),
#                  os.path.join(outputdir, dir + "_" + str(fileid) + ".png"))




onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

done = []

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

    outputfilename = labelpath + namewithdotmath + ".xml"

    # if not os.path.isfile(outputfilename):
    # flag = True
    for line in lines:
        
        outputfilename = labelpath + namewithdotmath + "_" +str(line[0]) +".xml"

        if not os.path.exists("./images/"+namewithdotmath+"_"+str(line[0]) + ".png"):
            continue


            

        im = Image.open("./images/"+namewithdotmath+"_"+str(line[0]) + ".png")

        f= open(outputfilename,"a+")
        if(outputfilename not in done):
            done.append(outputfilename)
            begin = start.format(folder="images", img=namewithdotmath+"_"+str(line[0]) + ".png", width=im.width, height=im.height)
            f.write(begin)


        coord = line[1:]

        middle = data.format(left=coord[0], right=coord[2], up=coord[1], bottom=coord[3])

        # temp =  [0,0,0,0]

        # xmin = coord[0]
        # xmax = coord[2]
        # ymin = coord[1]
        # ymax = coord[3]

        # xcen = float((xmin + xmax)) / 2
        # ycen = float((ymin + ymax)) / 2

        # w = float((xmax - xmin))
        # h = float((ymax - ymin))

        # temp[0] = xcen
        # temp[1] = ycen
        # temp[2] = w
        # temp[3] = h

        # coord = temp

        # coord = map(str, coord)
        # f.write(" ".join(coord))
        f.write(middle)
        f.close()

files = os.listdir(labelpath)
for file in files:
    f = open(labelpath+file, "a+")
    f.write(end)
    f.close()