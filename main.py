from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6308921798:AAG8F_KMPTiDusQwMUwJLxnZlpxXxPhCGqc'
BOT_USERNAME: Final = '@Mobodybot'


async def start_Command(Update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text('Hello! thanks for chating with me! i am mobodybot')

async def help_Command(Update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text('i am mobodybot! please type something so that i can respond')

async def custom_Command(Update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text('This is a custom command!')


def handle_response(text: str) -> str:
    processed: str = text.lower()


    if 'hello' in processed:
        return'Hey there'
    
    if 'how are you' in processed:
        return'i am good'
    
    if 'i love python' in processed:
        return' remember to subscribe'
    
    return 'i do not understand what you wrote..... '



async def handle_message (update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text


    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)

        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')




if __name__ == '__main__':
    print('starting bot...')
    app = Application.builder().token(TOKEN).build()


    #commands
    app.add_handler(CommandHandler('start', start_Command))
    app.add_handler(CommandHandler('help', help_Command))
    app.add_handler(CommandHandler('custom', custom_Command))


    #message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)


    #polls
    print('polling....')
    app.run_polling(poll_interval=3)


