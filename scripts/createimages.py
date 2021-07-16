from os import listdir
from os.path import isfile, join
import os.path

import os

imagesroot = "./newimages/"

onlydirs = [f for f in listdir(imagesroot) if not isfile(join(imagesroot, f))]

for dir in onlydirs:

    pathofdir = imagesroot + dir + "/"

    allfiles = [f for f in listdir(pathofdir) if isfile(join(pathofdir, f))]

    print(allfiles[0])

    for file in allfiles:

        fileid = int(file.split(".")[0]) - 1
        os.rename(pathofdir + file, pathofdir + dir + "_" + str(fileid) + ".png")
