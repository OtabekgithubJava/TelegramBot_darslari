from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import requests

url_1 = "https://t.me/+h43gS6kc3axjOGIy"
url_2 = "https://t.me/alo_xashar"
id_1 =  -1002201963688
id_2 =  -1002315557332
token = "7716195960:AAG5iLkrknVx74CutKLTm0GDApX1rlIznXo"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id = update.effective_user.id
    name = update.effective_user.full_name
    username = update.effective_user.username
    
    await context.bot.send_message(
        chat_id=-1002201963688,
        text=f"New user:\n\nID: {id}\nName: {name}\nUsername: @{username}"
    )
    
    channel_1 = await is_subscribed(update, context, id_1)
    channel_2 = await is_subscribed(update, context, id_2)
        
    if not channel_1 and channel_2:
    
        buttons = [
            [InlineKeyboardButton("Channel 1", url=f"{url_1}")],
            [InlineKeyboardButton("Channel 2", url=f"{url_2}")],
            [InlineKeyboardButton("Check ✅", callback_data="tekshiruv")]
        ]
        
        btns = InlineKeyboardMarkup(buttons)
        
        await update.message.reply_text(
            text="Botdan foydalanish uchun kanallarga <b>a'zo bo'ling</b>!",
            reply_markup=btns,
            parse_mode="HTML"
        )
    else:
        btns = [[InlineKeyboardButton("Davom etish", callback_data="tekshiruv")]]
        
        markup_btns = InlineKeyboardMarkup(btns)
        
        await update.message.reply_text(
            text="Welcome",
            reply_markup=markup_btns
        )
        
        
    
async def is_subscribed(update: Update,context: ContextTypes.DEFAULT_TYPE, kanal_link) -> bool:
    user_id = update.effective_user.id
    url = f"https://api.telegram.org/bot{token}/getChatMember?chat_id={kanal_link}&user_id={user_id}"
    response = requests.get(url).json()
    print(f"{kanal_link} : {response}")

    if response.get("ok", False):
        status = response.get("result", {}).get("status")
        return status in ("member","adminstrator","creator")
    return False


async def tugmachalar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    btns = [
        [InlineKeyboardButton("1", callback_data="1"), InlineKeyboardButton("2", callback_data="2"), InlineKeyboardButton("3", callback_data="3")],
        
        [InlineKeyboardButton("4", callback_data="4"), InlineKeyboardButton("5", callback_data="5"), InlineKeyboardButton("6", callback_data="6")],
        
        [InlineKeyboardButton("7", callback_data="7"), InlineKeyboardButton("8", callback_data="8"), InlineKeyboardButton("9", callback_data="9")],
    ]
    
    btns_markup = InlineKeyboardMarkup(btns)
    
    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text="Tugmacha tanlab, bosing!",
        reply_markup=btns_markup
    )

    
async def queries(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    info = update.callback_query.data
    
    if info == "tekshiruv":
        channel_1 = await is_subscribed(update, context, id_1)
        channel_2 = await is_subscribed(update, context, id_2)
        
        if not channel_1 and channel_2:
            await start(update, context)   
        else:
            await tugmachalar(update, context)
    else:
        await context.bot.send_message(
            chat_id=update.effective_user.id,
            text=f"Siz {info}-tugmani bosdiz!"
        )


app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(queries))

print("Bot is running...")
app.run_polling()