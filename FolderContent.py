import sys
import os

class FolderContent:

    path = ''
    extension = ''
    pattern = ''

    def __init__(self, path):
        self.path = path

    def resetFilter(self):
        self.extension = ''
        self.pattern = ''

    def filterToExtension(self, extension):
        self.extension = extension

    def filterToPatterninFileName(self, pattern):
        self.pattern = pattern

    def doesFolderExist(self):
        return os.path.exists(self.path)

    def ignore(self, filename):

        if self.extension != '':
            if not str(filename).lower().endswith(self.extension.lower()):
                return True

        if self.pattern != '':
            if str(filename).find(self.pattern) < 0:
                return True

        return False

    def getListOfFiles(self):

        fileList = []

        if self.doesFolderExist() == False:
            return fileList

        for file in os.scandir(self.path):

            fileFullPath = os.path.join(self.path, file.name)

            if self.ignore(file.name):
                continue

            fileList.append(fileFullPath)

        return fileList

    def workOnFiles(self, task):

        fileList = []

        if self.doesFolderExist() == False:
            return fileList

        for file in os.scandir(self.path):

            fileFullPath = os.path.join(self.path, file.name)

            if self.ignore(file.name):
                continue

            task(fileFullPath)


    def getListOfFilesInSubdirectories(self):

        fileList = []

        if self.doesFolderExist() == False:
            return fileList

        for root, subdirectories, files in os.walk(self.path):

            for subdirectory in subdirectories:
                # print(os.path.join(root, subdirectory))
                continue

            for file in files:

                fileFullPath = os.path.join(root, file)
                # print(self.ignore(file), ":", file)

                if self.ignore(file):
                    continue

                fileList.append(fileFullPath)

        return fileList

    def workOnFilesIncludingSubdirectories(self, task):

        fileList = []

        if self.doesFolderExist() == False:
            return fileList

        for root, subdirectories, files in os.walk(self.path):

            for subdirectory in subdirectories:
                # print(os.path.join(root, subdirectory))
                continue

            for file in files:

                fileFullPath = os.path.join(root, file)

                if self.ignore(file):
                    continue

                task(fileFullPath)