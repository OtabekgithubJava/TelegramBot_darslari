from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to Elnurfood TG bot")


async def xabarlar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text

    if message.lower() == "elnurbek":
        await update.message.reply_text("Elnurbek -> Real")
    elif message.lower() == "sanjarbek1":
        await update.message.reply_text("Sanjarbek1 -> Real")
    elif message.lower() == "sanjarbek2":
        await update.message.reply_text("Sanjarbek2 -> MYU")
    elif message.lower() == "dilshoda":
        await update.message.reply_text("Dilshoda -> Arsenal")
    elif message.lower() == "abduvali":
        await update.message.reply_text("Man City")
    elif message.lower() == "muhammadaziz":
        await update.message.reply_text("Liverpool")
    else:
        await update.message.reply_text("Noto'g'ri TEXT")


app = ApplicationBuilder().token("7716195960:AAF7Psfoj_xdXNfockgHKEDAex7F-hLIiKk").build()

app.add_handler(CommandHandler("start", start))

app.add_handler(MessageHandler(filters.TEXT, xabarlar))

print("Bot ishga tushdi...")
app.run_polling()