import os
import os.path as path
import common

def getVideos(root):
    ''' get all videos in the root directory and all its subdirectories or the 
    root if it is a video file'''
    videos = []
    if path.isfile(root):
        dirpath, nameWithExt = path.split(root)
        name, ext = path.splitext(nameWithExt)
        if ext[1:] in common.videoTypes:
            videos.append(
                    common.videoToDict(dirpath, name, common.tokenize(name)))
        else:
            raise Exception('File is not a known video format')
    else:
        for (dirpath, dirname, filenames) in os.walk(root):
            # get all files with extension from videoTypes, leading dot is 
            # stripped from the extension
            for f in filenames:
                name, ext = path.splitext(f)
                if ext[1:] in common.videoTypes:
                    videos.append(common.videoToDict(
                            dirpath, name, common.tokenize(name)))
    if len(videos) == 0:
        raise Exception(
                'No file with known video format found in the directory')
    return videos

def saveSubtitles(contents, video, filename):
    with open(path.join(video['dirpath'], filename), 'w') as f:
        f.write(contents)
