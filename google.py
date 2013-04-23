# -*- coding: utf-8 -*-
import requestWrapper as req
import re
import time
import random

class Google(object):
    searchUrl = 'https://www.google.sk/search?q=site%3Atitulky.com+{0}'
    searchExpression = re.compile(r'www.titulky.com/(?:(?!\.).)+\.htm')

    def getFirstLevelLinks(self, videos):
        lastVid = len(videos) - 1
        for i, video in enumerate(videos):
            url = self.searchUrl.format(video['name'])
            r = req.get(url)
            ''' get the first link, as we trust the wisdom of google'''
            link = self.searchExpression.search(r.text)
            if not link:
                raise Exception('No suitable link found, go manual')
            video['firstLink'] = 'http://' + link.group(0)
            if i != lastVid:
                time.sleep(random.randint(5, 15))
        return videos

