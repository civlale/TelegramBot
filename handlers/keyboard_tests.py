"""Small keyboard demonstrations, separate from existing bot responses."""

from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ContextTypes

REPLY_TEST_TEXT = "بالا"
CLOSE_KEYBOARD_TEXT = "پایین"

reply_test_keyboard = ReplyKeyboardMarkup(
    [[KeyboardButton(REPLY_TEST_TEXT)], [KeyboardButton(CLOSE_KEYBOARD_TEXT)]],
    resize_keyboard=True,
)



async def handle_reply_test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Return whether this message belongs to the reply keyboard demo."""
    message = update.message
    if message is None:
        return False
    if message.text == REPLY_TEST_TEXT:
        await message.reply_text("تست Reply")
        return True
    if message.text == CLOSE_KEYBOARD_TEXT:
        await message.reply_text("کیبورد تست بسته شد.", reply_markup=ReplyKeyboardRemove())
        return True
    return False
