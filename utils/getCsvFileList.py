import os, fnmatch


def getCsvFiles(path, extension=None):

    if extension:
        fileExtension = extension
    else:
        fileExtension = "*.csv"

    print(fileExtension)

    files = []

    # get all files in folder
    fileList = os.listdir(path)

    # filter on csv files
    for name in fileList:

        if fnmatch.fnmatch(name, fileExtension) == True:

            files.append(os.path.join(path, name))


    return files
