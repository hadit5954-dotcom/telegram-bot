import os
import threading
from flask import Flask
import telebot
import sqlite3

# ایجاد سرور وب برای نگه‌داری آنلاین
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# اجرای سرور وب در ترد جداگانه
web_thread = threading.Thread(target=run_web)
web_thread.daemon = True
web_thread.start()

# بقیه کد ربات...
bot = telebot.TeleBot("8348534439:AAEwFZjAxvQ7FjF7RVgJsWuLfCYrIV8J3_I")

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard1.add("ارتباط گرفتن با من", "رزومه", "پروژه ها")

def init_db():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            name TEXT,
            username TEXT
        )
    ''')
    conn.commit()
    conn.close()

@bot.message_handler(commands=["start"])
def hi(message):
    user = message.from_user
    print(f"کاربر جدید: {user.first_name}")
    
    try:
        conn = sqlite3.connect('bot.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE user_id = ?", (user.id,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO users (user_id, name, username) VALUES (?, ?, ?)", (user.id, user.first_name, user.username))
            conn.commit()
        conn.close()
    except Exception as e:
        print(f"خطا: {e}")
    
    bot.send_message(message.chat.id, "سلام من محمد هادی ترابی هستم👋", reply_markup=keyboard1)

@bot.message_handler(func=lambda message: True)
def keyboard(message):
    if message.text == "ارتباط گرفتن با من":
        keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard2.add("آیدی تلگرام", "شماره تلفن", "پیج اینستاگرام", "ایمیل", "بازگشت")
        bot.send_message(message.chat.id, "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=keyboard2)

    elif message.text == "آیدی تلگرام":
        bot.send_message(message.chat.id, "@Haditorabi2006")
    elif message.text == "شماره تلفن":
        bot.send_message(message.chat.id, "09030174385")
    elif message.text == "پیج اینستاگرام":
        bot.send_message(message.chat.id, "mohamadhadi194")
    elif message.text == "ایمیل":
        bot.send_message(message.chat.id, "mohamadhadi20071385@gmail.com")

    elif message.text == "رزومه":
        keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard3.add("پایتون جامع", "پایتون پیشرفته", "شبکه های کامپیوتری", "بازگشت")
        bot.send_message(message.chat.id, "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=keyboard3)

    elif message.text == "پایتون جامع":
        bot.send_message(message.chat.id, "🎓 گواهی نامه دوره جامع پایتون مکتب خونه")
    elif message.text == "پایتون پیشرفته":
        bot.send_message(message.chat.id, "گواهی به زودی بارگذاری میشود")
    elif message.text == "شبکه های کامپیوتری":
        bot.send_message(message.chat.id, "🎓 گواهی نامه دوره شبکه مکتب خونه")

    elif message.text == "پروژه ها":
        keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard4.add("پروژه لیست خرید", "پروژه مکان شماره تلفن", "پروژه ماشین حساب", "بازگشت")
        bot.send_message(message.chat.id, "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=keyboard4)

    elif message.text == "پروژه لیست خرید":
        bot.send_message(message.chat.id, "🛒 پروژه لیست خرید")
    elif message.text == "پروژه ماشین حساب":
        bot.send_message(message.chat.id, "🧮 پروژه ماشین حساب")
    elif message.text == "پروژه مکان شماره تلفن":
        bot.send_message(message.chat.id, "📱 پروژه مکان شماره تلفن")

    elif message.text == "بازگشت":
        bot.send_message(message.chat.id, "به منوی اصلی بازگشتی 👇", reply_markup=keyboard1)

init_db()
print("ربات اجرا شد!")
bot.infinity_polling()

