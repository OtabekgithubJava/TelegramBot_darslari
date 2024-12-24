from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id = update.effective_user.id
    name = update.effective_user.full_name
    username = update.effective_user.username
    
    await update.message.reply_text(f"🥷 Yangi foydalanuvchi: \n🆔 ID: {id}\n🚹 Name: {name}\n📱 Username: @{username}")
    
    
async def send_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_sticker("https://telegrambots.github.io/book/docs/sticker-fred.webp")
    
    
    
async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_video("video.mp4")
    
    
async def send_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_photo("abduvali.jpg")


app = ApplicationBuilder().token("7716195960:AAF7Psfoj_xdXNfockgHKEDAex7F-hLIiKk").build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("sticker", send_sticker))
app.add_handler(CommandHandler("photo", send_photo))
app.add_handler(CommandHandler("video", send_video))


app.run_polling()
