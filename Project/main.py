from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters

users = []
super_admin = 5091219046
admins = {
    5091219046 : "@Creative_007_O"
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id = update.effective_user.id
    
    if id not in users:
        users.append(id)
        
    buttons = [
        [KeyboardButton("Register"), KeyboardButton("Login")]
    ]
    
    marks = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    
    await update.message.reply_text(
        text=f'Hello {update.effective_user.first_name}', 
        reply_markup=marks
        )
    
    
async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    xabar = update.message.text
    id = update.effective_user.id
    
    if xabar == "Login":
        if id in admins.keys():
            await admin_panel(update, context)
        else:
            await update.message.reply_text(
                text="Siz admin emassiz!"
            )
    elif xabar == "Register":
        button = [
            [KeyboardButton("Share Contact", request_contact=True)]
        ]
        
        marks = ReplyKeyboardMarkup(button, resize_keyboard=True)
        
        await update.message.reply_text(
            text="Admin bo'lish uchun telefon raqamni jo'nating!",
            reply_markup=marks
        )
    elif update.message.contact:
        telefon = update.message.contact.phone_number
        
        id = update.effective_user.id
        username = update.effective_user.username
        
        with open("txt.txt", "a", encoding="utf-8") as file:
            file.write(f"{telefon}\n")
            
        await update.message.reply_text(
            text="So'rov jo'natildi!"
        )
        
        inlines = [
            [
                InlineKeyboardButton("Accept ✅", callback_data=f"accept:{id}:{username}"),
                InlineKeyboardButton("Reject ❌", callback_data=f"reject:{id}:{username}")
            ]
        ]
        
        marks = InlineKeyboardMarkup(inlines)
        
        await context.bot.send_message(
            chat_id=super_admin,
            text=f"Yangi so'rov\n\nID: {id}\nUsername: @{username}",
            reply_markup=marks
        )
    elif xabar == "Say Hi" and id in admins.keys():
        for i in users:
            await context.bot.send_message(
                chat_id=i,
                text="Hi!"
            )
        
        

async def queries(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    info = update.callback_query.data
    
    natija, user_id, username = info.split(":")
    
    if natija == "reject":
        await context.bot.send_message(
            chat_id=super_admin,
            text=f"Foydalanuvchi rad etildi"
        )
        
        await context.bot.send_message(
            chat_id=user_id,
            text="Sizni so'roviz rad etildi!"
        )
    elif natija == "accept":
        admins.update({int(user_id): f"@{username}"})  # Convert user_id to integer
        
        await context.bot.send_message(
            chat_id=super_admin,
            text="Admin qo'shildi!"
        )
        
        await context.bot.send_message(
            chat_id=int(user_id),
            text="So'rov qabul qilindi va siz endi adminsiz!"
        )

        
        
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tugmacha = [
        [KeyboardButton("Say Hi")]
    ]
    tugmacha2 = ReplyKeyboardMarkup(tugmacha, resize_keyboard=True)
    
    await update.message.reply_text(
        text="Admin Panelga xush kelibsiz! \n\nTugmacha tanlang!",
        reply_markup=tugmacha2
    )


app = ApplicationBuilder().token("7716195960:AAG5iLkrknVx74CutKLTm0GDApX1rlIznXo").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT | filters.CONTACT, text))
app.add_handler(CallbackQueryHandler(queries))

print("Bot ishladi!")
app.run_polling()