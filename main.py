import os
from dotenv import load_dotenv
from typing import Final

# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

from config import API_TOKEN, BOT_HANDLE
from handlers.commands import initiate_command, log_error
from handlers.callbacks import handle_button
from handlers.messages import process_message

from services.responses import generate_response

print('Bot is now starting up...')


# Start the bot
if __name__ == '__main__':
    app = Application.builder().token(API_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('start', initiate_command))

    # Register command handlers
    # app.add_handler(CommandHandler('fuck_you', fuck_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

    # Register error handler
    app.add_error_handler(log_error)

    #Callback Query یعنی خبری که تلگرام بعد از کلیک کاربر روی دکمهٔ Inline به بات می‌فرستد.
    app.add_handler(CallbackQueryHandler(handle_button))

    print('Starting polling...')
    # Run the bot
    app.run_polling(poll_interval=0)