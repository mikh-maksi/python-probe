from telegram.ext import Application, Updater, MessageHandler, filters

async def echo(update, context):
    string_in = update.message.text
    string_out = string_in
    await update.message.reply_text(string_out)

application = Application.builder().token("").build()

application.add_handler(MessageHandler(filters.TEXT, echo))

application.run_polling()
