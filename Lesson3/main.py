from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    

async def xabarlar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    try:
        if int(message) % 2 == 0:
            await update.message.reply_text("Bu son juft")
        else:
            await update.message.reply_text("Bu son toq")
    except Exception as error:
        await update.message.reply_text("Faqat son kiriting!")
        print(error)
    else:
        print("Ishladi...")
    


app = ApplicationBuilder().token("7716195960:AAF7Psfoj_xdXNfockgHKEDAex7F-hLIiKk").build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(MessageHandler(filters.TEXT, xabarlar))

app.run_polling()