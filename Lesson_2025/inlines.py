from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
import requests

link1 = "https://t.me/alo_xashar"
link2 = "https://t.me/+h43gS6kc3axjOGIy"

ch1 = -1002315557332
ch2 = -1002201963688

TOKEN = "7716195960:AAG5iLkrknVx74CutKLTm0GDApX1rlIznXo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tekshiruv1 = await is_subscribed(update, context, ch1)
    tekshiruv2 = await is_subscribed(update, context, ch2)
    
    if tekshiruv1 and tekshiruv2:
        await context.bot.send_message(
            chat_id=update.effective_user.id,
            text="Obuna bo'ldingiz!")
    else:
        tugmachalar = [
            [InlineKeyboardButton("Channel 1", url=f"{link1}")],
            [InlineKeyboardButton("Channel 2", url=f"{link2}")],
            [InlineKeyboardButton("✅ Tekshiring", callback_data="tekshirish")]
        ]
        
        buttons = InlineKeyboardMarkup(tugmachalar)
        
        
        await context.bot.send_message(
            chat_id=update.effective_user.id,
            text="Welcome!\n\nKanallarga obuna bo'ling!",
            reply_markup=buttons
        )
    
async def is_subscribed(update: Update,context: ContextTypes.DEFAULT_TYPE, kanal_link) -> bool:
    user_id = update.effective_user.id
    url = f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={kanal_link}&user_id={user_id}"
    response = requests.get(url).json()
    print(f"{kanal_link} : {response}")

    if response.get("ok", False):
        status = response.get("result", {}).get("status")
        return status in ("member","adminstrator","creator")
    return False
    

async def texts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tekshiruv1 = await is_subscribed(update, context, ch1)
    tekshiruv2 = await is_subscribed(update, context, ch2)
    
    if not tekshiruv1 and tekshiruv2:
        await start(update, context)
    else:
        text = update.message.text
        await update.message.reply_text(f"You sent:\n\n{text}")
        
        
async def callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tugma_xabar = update.callback_query.data
    
    if tugma_xabar == "tekshirish":
        await start(update, context)
        

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, texts))
app.add_handler(CallbackQueryHandler(callbacks))

print("Bot is running...")
app.run_polling()