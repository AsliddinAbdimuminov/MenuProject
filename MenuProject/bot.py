from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Botni ishga tushirish uchun TOKENni yozing
TOKEN = '6183316106:AAF8TdtHL1eyK3IBkf9cy84ITMhN0j3arLY'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Assalomu alaykum! Botimizga xush kelibsiz.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Uzr, tushunmadim.")

def main():
    # Updater yaratish va TOKEN bilan bog'lash
    updater = Updater(TOKEN, use_context=True)

    # Dispatcher olish
    dispatcher = updater.dispatcher

    # Start komandasiga javob berish
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Yozuvlarga javob berish
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Noma'lum komandalarga javob berish
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Botni ishga tushirish
    updater.start_polling()

    # Dasturni to'xtatish uchun Ctrl+C bosish
    updater.idle()

if __name__ == '__main__':
    main()
