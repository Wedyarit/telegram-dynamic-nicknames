
import logger
from src.emoji_parser import EmojiParser


class NicknameGenerator:
    def __init__(self, emojis_enabled, unicode_url, config_nicknames, emoji_symbol):
        logger.Logger.nickname_generator_initiating()

        # ------------------
        # Instance variables
        # ------------------
        self.nicknames_iterator = None
        self.emoji_parser = None
        self.unicode_url = unicode_url
        self.config_nicknames = config_nicknames
        self.nicknames_iterator = iter(self.config_nicknames)
        self.emojis_enabled = emojis_enabled
        self.emoji_symbol = emoji_symbol

        # ------------------
        # Init emoji parser
        # ------------------
        if self.emojis_enabled:
            self.init_emoji_parser()

    def init_emoji_parser(self):
        self.emoji_parser = EmojiParser(self.unicode_url)

    def nickname(self):
        nickname = next(self.nicknames_iterator, None)
        if nickname is None:
            self.nicknames_iterator = iter(self.config_nicknames)
            nickname = next(self.nicknames_iterator)
        while self.emoji_symbol in nickname:
            nickname = nickname.replace(self.emoji_symbol, self.emoji_parser.emoji(), 1)

        return nickname
