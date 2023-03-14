import telebot
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


#токен бота
bot = telebot.TeleBot('Your Token')


print("Бот Запустился")

#команды бота
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<b>Hello</b> <u>{message.from_user.first_name}👋</u>\n type /help to find out all available commands📚'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    print('тебе написал сообщение в бота <start>' + 'username:'+ message.from_user.username, 'firstname:'+ message.from_user.first_name)

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '<b>⬇️⬇️All Comands List⬇️⬇️</b>\n/id-sends you your id\n/factoftheday-sends the fact of the day', parse_mode='html')
    print('тебе написал сообщение в бота <help> ' + 'username:'+ message.from_user.username, 'firstname:'+ message.from_user.first_name)

@bot.message_handler()
def get_user_text(message):
    if message.text == '/id':
        bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
        print('тебе написал сообщение в бота <id> ' + 'username:'+ message.from_user.username, 'firstname:'+ message.from_user.first_name)
    elif message.text == '/factoftheday':
        bot.send_message(message.chat.id, f"<b>fact of the day:</b> What did Dumbledore teach before he became headmaster?", parse_mode='html')
        bot.send_message(message.chat.id, f"<b>Dumbledore is an expert at Transfiguration too, having taught the subject before becoming headmaster.</b>", parse_mode='html')
        print('тебе написал сообщение в бота <factoftheday> ' + 'username:'+ {message.from_user.id} + 'firstname:'+ message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, "I'm sorry, I don't understand you", parse_mode='html')

#чтобы бот всегда работал
bot.polling(none_stop=True)
