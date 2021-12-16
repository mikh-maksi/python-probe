from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import random
# список картинок для випадкового вибоору однієї з них
img = ["https://mikh-maksi.github.io/probes/img/air.jpg", "https://mikh-maksi.github.io/probes/img/happy.jpg", "https://mikh-maksi.github.io/probes/img/happy2.jpg", "https://mikh-maksi.github.io/probes/img/flowers.jpg", "https://mikh-maksi.github.io/probes/img/morning.jpg"]

# кнопка із написом "Щаслива картинка"
keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Щаслива картка", callback_data="photo")]])

# обробка команди /start
def start(update, context):
    update.message.reply_text('Оберіть щастя:', reply_markup=keyboard)

# обробка нажаття на кнопку
def button(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=random.choice(img) ,reply_markup=keyboard)

# підключення до боту
updater = Updater("")

# обробка команди /start
updater.dispatcher.add_handler(CommandHandler('start', start))
# обробка нажаття кнопки
updater.dispatcher.add_handler(CallbackQueryHandler(button))

# команди запуску бота
updater.start_polling()
updater.idle()
