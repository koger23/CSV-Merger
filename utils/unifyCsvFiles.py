#!/usr/bin/python3
import os


def unifyCsvFiles(csvFileList, filename, targetpath=None, header=True, encoding=None, progBar=None):

    """
    Unifying text files based on given file list and save it in given path with given filename.

    :param csvFileList: list
    :param filename: string - target filename for saving
    :param targetpath: string - target file path for saving the file
    :param header: boolean - for keeping header of csv files
    :param encoding: string - encoding of text files
    :param progBar: QProgressbar object
    :return: nothing
    """

    if encoding:
        encode = encoding
    else:
        encode = "ISO8859-3"

    if targetpath:
        targetFullPath = os.path.join(targetpath, filename)
    else:
        targetFullPath = filename

    if header is True:
        countH = 0
    else:
        countH = 1

    numOfFiles = len(csvFileList)

    if numOfFiles > 0:

        if progBar:
            progBar.setMaximum(numOfFiles)

        No = 1 # counter for files for progressbar

        try:
            target_file = open(targetFullPath, "w", encoding=encode)
        except PermissionError as e:
                    errorMsg = "Permission denied:\n\n" + \
                               str(e) + \
                               "\n\nProbably you do not have the permission to create a file in the target folder."
                    return errorMsg


        for file in csvFileList:

            f = open(file, 'r', encoding=encode)

            # write all line starting with header
            if countH == 0:
                for i in f:
                    target_file.write(i)
                    countH += 1
            # write starts with second line only
            else:
                try:
                    lines = f.readlines()[1:]
                except UnicodeDecodeError as e:
                    errorMsg = "Decoding error:\n\n" + \
                               str(e) + \
                               "\n\nProbably the selected encoding is not proper."
                    return errorMsg

                for rows in lines:
                    target_file.write(rows)

            if progBar:
                progBar.increaseValue(No)

            No += 1

        target_file.close()

if __name__ == '__main__':

    from utils import getCsvFileList as getFiles

    csvFiles = getFiles.getCsvFiles(r'Y:\Dropbox\Python\Programjaim\DailyStats\utils\raw_datas', '*.csv')

    unifyCsvFiles(csvFiles, "all_csv.csv")
