import requests
import os
import os.path as path

defaultUserAgent = ''.join([
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) ',
        'AppleWebKit/537.31 (KHTML, like Gecko) ',
        'Chrome/26.0.1410.65 Safari/537.31'
        ])
defaultRequestHeaders = {'User-Agent': defaultUserAgent}
debug = False


def _ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def get(url):
    print 'geting url: ' + url
    r = requests.get(url, headers=defaultRequestHeaders)
    r.raise_for_status()
    if debug:
        log_file = path.join('logs/', url.replace('/', ''))
        _ensure_dir(log_file)
        print 'response status: ', r.status_code
        with open(log_file, 'w') as f:
            f.write(r.text.encode('utf-8'))
    return r

