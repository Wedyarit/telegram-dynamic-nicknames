import random
import urllib.request

import logger


class EmojiParser:
    def __init__(self, unicode_url):
        logger.Logger.emoji_parsing()

        self.sequence = None
        self.unicode_url = unicode_url
        self.emojis = []

        self.download()
        self.parse()

    def download(self):
        response = urllib.request.urlopen(self.unicode_url)
        data = response.read()
        self.sequence = data.decode('utf-8')

    def parse(self):
        for line in [l for l in self.sequence.split('\n') if not l.startswith('#') and len(l) > 0]:
            self.emojis.append(line[line.find('#') + 2])

    def emoji(self):
        return random.choice(self.emojis)
