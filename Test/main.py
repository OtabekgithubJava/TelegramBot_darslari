from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes ,filters,MessageHandler,CallbackQueryHandler


admins = []
users = {
    
}
super_admin = 5091219046


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id = update.effective_user.id
    fullname = update.effective_user.full_name
    username = update.effective_user.username
    
    if id in users.keys():
        buttons = [
            [
            InlineKeyboardButton("start", callback_data="start")
            ]
        ]
        btns = InlineKeyboardMarkup(buttons)
        await update.message.reply_text(
            text="testni boshlashingiz mumkin",
            reply_markup=btns
        )
    else:
        buttons = [
            [KeyboardButton("contact 📱", request_contact=True)]
        ]

        btn =ReplyKeyboardMarkup(buttons, resize_keyboard=True)
        await context.bot.send_message(
            chat_id=id,
            text="Welcome register!",
            reply_markup=btn
        )
async def kontakt(update:Update,context:ContextTypes.DEFAULT_TYPE):
    telefon= update.message.contact
    id= update.effective_user.id
    username = update.effective_user.username
    name = update.effective_user.full_name
    users.update({id:[username,name,telefon]}) 
    await start(update,context) 
    
    user = {id:[username,name,telefon]}
    with open("txt.txt","a") as file :
        file.write(f"{user}\n")
        

async def Elnurfod(update:Update,context:ContextTypes.DEFAULT_TYPE):
    info = update.callback_query.data
    if info == "start":
        tugmacha = [
            [InlineKeyboardButton("9",callback_data="test:9"),InlineKeyboardButton("2",callback_data="test:2"), InlineKeyboardButton("4",callback_data="test:4")]
        ]
        
        btn = InlineKeyboardMarkup(tugmacha)

        await context.bot.send_message(
            chat_id=update.effective_user.id,
            text="3*3 nechi",
            reply_markup=btn
        )    
    a, b = info.split(":")
    if a == "test" and b != "9":
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id,
            text="Xato"
        )
    elif a == "test" and b == "9":
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id,
            text="To'g'ri"
        )

    
    

app = ApplicationBuilder().token("7716195960:AAGwCVoGth27y7CkwBmSMVUzdXmbFcBPTYg").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.CONTACT,kontakt))
app.add_handler(CallbackQueryHandler(Elnurfod))

print("Ishladi...")
app.run_polling()