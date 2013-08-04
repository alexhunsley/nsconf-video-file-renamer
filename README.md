nsconf-video-file-renamer
=========================

Quick hack to rename the NSConf video files to have useful, well-ordered names.

The NSConf video file naming is a complete mess:

* the .m4v file names have neither the subject nor the author in them
* the number of the video in that year's session is first in the filename - useless for sorting purposes if all videos are together
* the names aren't even consistent in their crapness: sometimes you'll see "Five", sometimes you'll see "05", for example

Also see comments in the .py file.


Usage
=====

Once you've cloned the repo, created a folder inside named allVidsUnzipped. Inside that dir please unzip all of the NSConf videos.
Run the python script, and then look in the allVidsRenamed folder for renamed copies of all the videos.

Note: the original videos are copied, not renamed in-place.
