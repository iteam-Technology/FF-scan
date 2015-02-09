# Script to find access time and modification of files and folders
# Author:Vlad
# Date: February 2015

import os, sys, time

try:
	from scandir import walk
except:
	print('importing os.walk instead of scandir.walk) #scandir.walk is much faster than os.walk
	from os import walk
	
class KeyboardinterruptError(Exception): pass

def main
	
	currdir = os.getcwd()
	
	print('\n Scanning folders %s for files and %s folders' % (args.files, args.folder))
	for root, folders, files in dirwalk(args.files, args.folder)
		try:
			if os.path.exists()
			print "The directory is found "
		except:
			print "The directory was not found. "
			
FullFilePaths = get_fullpaths(directory)

print "%s Current directory for file access and modification is " % (FullFilePaths)
accessNMod(FullFilePaths):				
	
def dirwalk(top):
	for root, folders, files in walk(top, topdown = true, oneerror=walkerror):
		yield root, folders, files

def walkerror(oserror):		
	sys.stderr.write(str(oserror))
	sys.stderr.write('\n')
	return 0
	
def accessNMod(st, directory):
ctime,atime,mtime = st
	
	def get_fullpath(directory):
		filePaths = [] 
		folderPaths = []

		for root, dir, files in dirwalk(directory):
			for filename in files:
				filepath = os.path.join(root, filename)
				filePaths.append(filepath)
			
			for folders in dir:
				folderpath = os.path.join(root, folders)
				folderPaths.append(folderpaths)

FullFilePaths = get_fullpaths(directory)

while (FullFilePaths = true)
	print "Created: ", time.ctime(ctime)
	print "Last accessed: ", time.ctime(atime)
	print "Last modified: ", time.ctime(mtime)

st = os.stat(FullFilePaths)


		
sys.exit(main())
	
