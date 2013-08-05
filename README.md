nsconf-video-file-renamer
=========================

Quick hack to rename the NSConf video files to have useful, well-ordered names.

The NSConf video file naming is a complete mess:

* the .m4v file names have neither the subject nor the author in them
* the number of the video in that year's session is first in the filename - useless for sorting purposes if all videos are together
* the names aren't even consistent in their crapness: sometimes you'll see "Five", sometimes you'll see "05", for example

Also see comments in the .py file.

If you're from NSConf and you want to use my renamed file scheme on your site, please feel free (and give me a name credit if you do).

Usage
=====

Once you've cloned the repo, created a folder inside named allVidsUnzipped. Inside that dir please unzip all of the NSConf videos.
Run the python script, and then look in the allVidsRenamed folder for renamed copies of all the videos.

Note: the original videos are copied, not renamed in-place.

Before and After
================

Example of filenames before:

```01NSConf03March2011.m4v
01NSConf04March2012.m4v
01NSConfFiveMarch2013.m4v
01NSConfMain032009.m4v
01NSConfMiniJune2010.m4v
01NSConfMiniSept2012.m4v
01NSConfTwoMarch2010.m4v
02NSConf03March2011.m4v
02NSConf04March2012.m4v
02NSConf05March2013.m4v```

And after:

```NSConf01 - 01 Designing and Developing Custom Controls (Matt Gemmell).m4v
NSConf01 - 02 Integrating With The Photography Eco System (Fraser Spiers).m4v
NSConf01 - 03 New Cocoa Programming SuperPowers (Philippe Mougin).m4v
NSConf01 - 04 The Foundations of Objective C (Andre Pang).m4v
NSConf01 - 05 Pimp My App (Mike Lee).m4v
NSConf01 - 06 What a Performance (Drew McCormack).m4v
NSConf01 - 07 Building A Secure Cocoa Program (Graham Lee).m4v
NSConf01 - 08 Core Animation Animating Your UI (Bill Dudney).m4v
NSConf01 - 09 Spotlight and Quicklook vs Core Data (Marcus Zarra).m4v
NSConf01 - 10 The Very First Cocoa Face Off (Misc).m4v
NSConf02 - 01 Engineering Life (Mike Lee).m4v
NSConf02 - 02 Spelunking OS X (Johnathan Rentzch).m4v
NSConf02 - 03 Clean Code (Dave Dribin).m4v```

