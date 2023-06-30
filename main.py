# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater
from MiddlewareCMD.keyboardBTN import MiddlewareBTN


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


BTN = MiddlewareBTN()


# Define a command handler
async def start(update, context):
    reply_markup = BTN.get_keyboard_mark_up()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Choose an option:',
        reply_markup=reply_markup)


app = ApplicationBuilder().token("5863336169:AAG6gtEOuGtUxzEI4TXzCUlefP_d27DKOX4").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))

app.run_polling()
