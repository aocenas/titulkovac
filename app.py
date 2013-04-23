# -*- coding: utf-8 -*-
import re
import sys

import google as g
import titulky as t
import files as f
import requestWrapper as req
# if true, outputs requesed urls and writes contetnts to log/
req.debug = False

if len(sys.argv) < 2:
    print 'directory or file need to be specified'
else:
    startDir = sys.argv[1]

    videos = f.getVideos(startDir)
    # getFirstLevelLinks changes the passed dict
    videos = g.Google().getFirstLevelLinks(videos)
    t.Titulky().downloadSubtitles(videos, f.saveSubtitles)

