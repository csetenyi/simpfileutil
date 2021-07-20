from FolderContent import FolderContent as FC

fc = FC('/Users/csetenyizoltan/Documents/(6.a) Programozosdi - Python/language - Python Core/[ps] Core Python - Getting Started/pythonProject')
fc.filterToExtension("py")
fc.filterToPatterninFileName('in')
list = fc.getListOfFiles()

fc.workOnFiles(print)
print(list)
listSub = fc.getListOfFilesInSubdirectories()
print(listSub)

fc.workOnFilesIncludingSubdirectories(print)
