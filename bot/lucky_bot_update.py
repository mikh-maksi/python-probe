from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import random

img = ["https://mikh-maksi.github.io/probes/img/air.jpg", "https://mikh-maksi.github.io/probes/img/happy.jpg", "https://mikh-maksi.github.io/probes/img/happy2.jpg", "https://mikh-maksi.github.io/probes/img/flowers.jpg", "https://mikh-maksi.github.io/probes/img/morning.jpg"]

async def start(update: Update, context: CallbackContext) -> None:
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Щаслива картка", callback_data="photo")]])
    await update.message.reply_text('Оберіть щастя:', reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    chat = update.effective_chat
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Щаслива картка", callback_data="photo")]])

    if query.data == 'photo':
        photo_img = random.choice(img)
        await context.bot.send_photo(chat_id=chat.id, photo=photo_img ,reply_markup=reply_markup)

def main() -> None:
    application = Application.builder().token("5722992818:AAGS0T-86JnKxqNJIqyebiHYPOzkWn5k5rM").build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))


    application.run_polling()

if __name__ == '__main__':
    main()
