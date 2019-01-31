import os, fnmatch


def getCsvFiles(path, extension=None):

    """
    Listing files with given extension in a folder.

    :param path: string - folder in which the files are
    :param extension: string - format: "*.csv" file extension what it looks for
    :return: list - list of csv files in from the path
    """

    if extension:
        fileExtension = extension
    else:
        fileExtension = "*.csv"

    files = []

    # get all files in folder
    fileList = os.listdir(path)

    # filter on csv files
    for name in fileList:

        if fnmatch.fnmatch(name, fileExtension) == True:

            files.append(os.path.join(path, name))


    return files
