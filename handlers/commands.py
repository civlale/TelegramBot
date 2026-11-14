from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Log errors
async def log_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

    
# Command to start the bot
async def initiate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hellow, what can I do for you?',reply_markup=menu)
    

profile_button = InlineKeyboardButton("پروفایل من", callback_data="profile")
about_button = InlineKeyboardButton("درباره ما", callback_data="about")
contact_button = InlineKeyboardButton("ارتباط با ما", callback_data="contact")
keyboard = [
    [profile_button],
    [about_button],
    [contact_button],
    [InlineKeyboardButton("بالا", callback_data="test_inline")],
    [InlineKeyboardButton("پایین", callback_data="test_reply")],
]


menu = InlineKeyboardMarkup(keyboard)

#async def fuck_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    await update.message.reply_text('behave') 

