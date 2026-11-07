import os
from dotenv import load_dotenv
from typing import Final

# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Bot is now starting up...')

load_dotenv()
API_TOKEN: Final = os.environ['TELEGRAM_BOT_TOKEN']
BOT_HANDLE: Final = '@sariJujaBot'


# Command to start the bot
async def initiate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hi, you good?')

async def fuck_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('behave')    

def generate_response(user_input: str) -> str:
    # Custom logic for response generation

    return user_input

    normalized_input: str = user_input.lower()

    if 'hi' in normalized_input:
        return 'Hello!'

    if 'how are you doing' in normalized_input:
        return 'I am functioning properly!'

    if 'i would like to subscribe' in normalized_input:
        return 'Sure go ahead!'

    return user_input.lower()


async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract details of the incoming message
    chat_type: str = update.message.chat.type
    text: str = update.message.text

    # Logging for troubleshooting
    print(f'User ({update.message.chat.id}) in {chat_type}: "{text}"')

    # Handle group messages only if bot is mentioned
    if chat_type == 'group':
        if BOT_HANDLE in text:
            cleaned_text: str = text.replace(BOT_HANDLE, '').strip()
            response: str = generate_response(cleaned_text)
        else:
            return  # Ignore messages where bot is not mentioned in a group
    else:
        response: str = generate_response(text)

    # Reply to the user
    print('Bot response:', response)
    await update.message.reply_text(response)


# Log errors
async def log_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Start the bot
if __name__ == '__main__':
    app = Application.builder().token(API_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('start', initiate_command))

    # Register command handlers
    app.add_handler(CommandHandler('fuck_you', fuck_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, process_message))

    # Register error handler
    app.add_error_handler(log_error)

    print('Starting polling...')
    # Run the bot
    app.run_polling(poll_interval=0)