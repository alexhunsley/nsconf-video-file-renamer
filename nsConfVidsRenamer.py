# NSConf videos renamer
# Alex Hunsley 2013
#
# This quick hack fixes the WTF that is the file naming of the NSConf videos.
# Note that the files are renamed by making copies, rather than
# renamed in place, to avoid annoying irreversible screwups.
#

import csv
import os.path
import sys
import string
import shutil

# source vid files
vidsFolder = "allVidsUnzipped"
# destination vid files (look here for the renamed goodness)
renamedVidsFolder = "allVidsRenamed"

if os.path.exists(renamedVidsFolder):
    shutil.rmtree(renamedVidsFolder)
os.makedirs(renamedVidsFolder)

# This file should have been provided alongside this script.
# It's metadata created from the NSConf vids download page. Which is itself
# inconsistent in the format of data it provides, and some stuff near the end
# is in the wrong order. What do I look like to you, the unix sort command?
csvfile = open('NSConfVidsSummary1.csv', 'rb')

validFilenameChars = "-_.() %s%s" % (string.ascii_letters, string.digits)

reader = csv.reader(csvfile, delimiter=',', quotechar='"')
firstRow = True
for row in reader:
	if (firstRow):
		firstRow = False
		continue

	vidFilename = row[8]

	description = row[0]
	vidIndex = vidFilename[:2]
	authors = row[1]
	baseName = row[9]

	if (len(authors) == 0):
		authors = "Misc"

	fullFilename = "%s - %02d %s (%s).%s" % (baseName, int(vidIndex), description, authors, "m4v")

	fullFilename = ''.join(c for c in fullFilename if c in validFilenameChars)

	fullDestinationFilename = "%s/%s" % (renamedVidsFolder, fullFilename)

	fullSourceFilename = "%s/%s.m4v" % (vidsFolder, vidFilename)

	print "%s --> %s" % (fullSourceFilename, fullDestinationFilename)

	try:
		shutil.copyfile(fullSourceFilename, fullDestinationFilename)
	except IOError:
		print "****** Warning: file not found: %s" % fullSourceFilename


