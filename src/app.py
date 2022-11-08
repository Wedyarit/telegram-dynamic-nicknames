import asyncio
import os

from dotenv import load_dotenv
from pathlib import Path

from telegram_dynamic_nickname import TelegramDynamicNicknames
import config

# -----------------
# Load the ENV file
# -----------------
env_file = '.env' if os.path.isfile('.env') else '../.env'
dotenv_path = Path(env_file)
load_dotenv(dotenv_path=dotenv_path)

if __name__ == '__main__':
    telegram_dynamic_nicknames = TelegramDynamicNicknames(
        unicode_url=os.environ['UNICODE_URL'],
        emojis_enabled=config.emojis_enabled,
        config_nicknames=config.nicknames,
        api_id=os.environ['API_ID'],
        api_hash=os.environ['API_HASH'],
        change_interval=config.change_interval,
        emoji_symbol=config.emoji_symbol
    )

    asyncio.run(telegram_dynamic_nicknames.loop())
