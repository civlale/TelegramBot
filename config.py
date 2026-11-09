import os
from dotenv import load_dotenv
from typing import Final

load_dotenv()
API_TOKEN: Final = os.environ['TELEGRAM_BOT_TOKEN']
BOT_HANDLE: Final = '@sariJujaBot'