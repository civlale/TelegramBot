from telegram import Update
from telegram.ext import ContextTypes

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    print(query.data)
    
    if query.data == "profile":
        user = query.from_user
        await query.message.reply_text(f"we know who you are {user.id}\n" f"Username: {user.username or '...'}\n" f"I see you {user.first_name or 'HA HA'} {user.last_name or 'HA HA'}")
    if query.data == "about":
        await query.message.reply_text("So as you know I’m trying to learn a few things\nIn other words,you’re my guinea pig")
    if query.data == "contact":
        await query.message.reply_text("We don’t offer that service yet, maybe later?")

    