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
			
print "%s Current directory for file access and modification is " % (dirwalk())
accessNMod(dirwalk())				
	
def dirwalk(top):
	for root, folders, files in walk(top, topdown = true, oneerror=walkerror):
		yield root, folders, files

def walkerror(oserror):		
	sys.stderr.write(str(oserror))
	sys.stderr.write('\n')
	return 0
	
def accessNMod(st):
ctime,atime,mtime = st 

	print "Created: ", time.ctime(ctime)
	print "Last accessed: ", time.ctime(atime)
	print "Last modified: ", time.ctime(mtime)

st = os.stat(dirwalk())

def get_filepath(directory):
filePaths = [] 

for root, directories, files in scandir.walk(directory):
	for filename in files:
		filepath = os.path.join(root, filename)
		filePaths.append(filepath)
FullFilePaths = get_filepaths()	

sys.exit(main())
	
