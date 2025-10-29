import telebot
import os
from flask import Flask, request

# توکن ربات
bot = telebot.TeleBot("8348534439:AAEwFZjAxvQ7FjF7RVgJsWuLfCYrIV8J3_I")
app = Flask(__name__)

# کیبورد اصلی
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard1.add("ارتباط گرفتن با من", "رزومه", "پروژه ها")

@bot.message_handler(commands=["start"])
def hi(message):
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

@app.route('/')
def home():
    return "🤖 Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        return 'Invalid content type', 403

if __name__ == '__main__':
    # حذف هرگونه webhook قبلی
    bot.remove_webhook()
    
    # تنظیم webhook جدید
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_URL', '')}/webhook"
    if webhook_url.startswith('https://'):
        bot.set_webhook(url=webhook_url)
        print(f"✅ Webhook set to: {webhook_url}")
    
    # اجرای سرور
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    print("🤖 ربات با webhook اجرا شد!")
