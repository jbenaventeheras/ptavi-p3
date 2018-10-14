import sys
import json
import urllib.request
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

tag_names = ('root-layout', 'region', 'img', 'audio', 'textstream')


class KaraokeLocal:

    def __init__(self, file_name):

        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file_name))
        self.tags = cHandler.get_tags()


    def to_json(self, filesmil, filejson=''):

        if filejson == '':
            filejson = filesmil.replace('.smil', '.json')

        with open(filejson, 'w') as jsonfile:
            json.dump(self.tags, jsonfile, indent=3)


if __name__ == '__main__':


    try:
        file_name = sys.argv[1]
    except IndexError:
        sys.exit('usage error: python3 karaoke.py file.smil')
    karaoke = KaraokeLocal(file_name)
    print(karaoke)
    karaoke.to_json(file_name)
    karaoke.do_local()
    karaoke.to_json(file_name, 'local.json')
    "print(karaoke)"
