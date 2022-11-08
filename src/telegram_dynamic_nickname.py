import time

from nickname_generator import NicknameGenerator
import logger
from tg_client import TGClient


class TelegramDynamicNicknames:
    def __init__(self,
                 unicode_url,
                 emojis_enabled,
                 config_nicknames,
                 api_id,
                 api_hash,
                 change_interval,
                 emoji_symbol):
        logger.Logger.banner()
        # ------------------
        # Instance variables
        # ------------------
        self.generator = NicknameGenerator(
            unicode_url=unicode_url,
            emojis_enabled=emojis_enabled,
            config_nicknames=config_nicknames,
            emoji_symbol=emoji_symbol
        )
        self.tg_client = TGClient(
            api_id=api_id,
            api_hash=api_hash,
        )
        self.change_interval = change_interval

    async def loop(self):
        await self.tg_client.start()

        while True:
            nickname = self.generator.nickname()
            logger.Logger.nickname(nickname)
            await self.tg_client.update_nickname(nickname)
            time.sleep(self.change_interval)
