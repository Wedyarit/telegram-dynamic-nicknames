from telethon.tl.functions.account import UpdateProfileRequest
from telethon import TelegramClient

import logger


class TGClient:
    def __init__(self, api_id, api_hash):
        logger.Logger.tg_client_initiating()

        # ------------------
        # Instance variables
        # ------------------
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient("telegram-dynamic-nickname", self.api_id, self.api_hash)

    async def start(self):
        await self.client.start()

    async def update_nickname(self, nickname):
        return await self.client(UpdateProfileRequest(first_name=nickname))
