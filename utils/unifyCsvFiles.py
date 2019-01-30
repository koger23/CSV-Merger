#!/usr/bin/python3
import os


def unifyCsvFiles(csvFileList, filename, targetpath=None, header=True, encoding=None):

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

        No = 1 # counter for files for progressbar

        target_file = open(targetFullPath, "w", encoding=encode)

        for file in csvFileList:

            f = open(file, 'r', encoding=encode)

            # write all line starting with header
            if countH == 0:
                for i in f:
                    target_file.write(i)
                    countH += 1
            # write starts with second line only
            else:
                lines = f.readlines()[1:]
                for rows in lines:
                    target_file.write(rows)

            No += 1

        target_file.close()

if __name__ == '__main__':

    from utils import getCsvFileList as getFiles

    csvFiles = getFiles.getCsvFiles(r'Y:\Dropbox\Python\Programjaim\DailyStats\utils\raw_datas', '*.csv')

    unifyCsvFiles(csvFiles, "all_csv.csv")
