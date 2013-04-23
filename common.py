import string

videoTypes = ('mkv', 'mp4', 'avi')

def videoToDict(dirpath, name, tokenList):
    return {
            'dirpath': dirpath,
            'name': name,
            'tokens': tokenList
            }

def tokenize(name):
    translated = name.translate(string.maketrans(' -', '..'))
    return translated.split('.')
