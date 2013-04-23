# -*- coding: utf-8 -*-
import requestWrapper as req
import re
import time

class Titulky(object):
    urlPart = 'http://www.titulky.com/'
    downloadLinkExpression = re.compile(r'idown.php(?:(?!\").)+')
    filenameRe = re.compile(r'filename=(.+)')

    def downloadSubtitles(self, videos, cb):
        for video in videos:
            contents, filename = self.getSubtitles(video['firstLink'])
            cb(contents, video, filename)
            #with open(filename, 'w') as f:
                #f.write(r.content)
    
    def getSubtitles(self, link):
        r = req.get(link)
        firstDownloadLink = self.downloadLinkExpression.search(r.text).group(0)
        r = req.get(domainPart + firstDownloadLink)
        secondDownloadLink = self.downloadLinkExpression.search(r.text).group(0)
        # arbitrary timer until you can download the subtitles
        time.sleep(10)
        r = req.get(domainPart + secondDownloadLink)
        filename = self.filenameRe.search(
                r.headers['content-disposition']).group(1)
        return r.content, filename


