import telebot
import qrcode


token = '6141703674:AAFK7UVUymBLONej8Tywuis8_zJxm62WBDo'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Пришлите ссылку для генерации QR ")


@bot.message_handler()
def messages(message):
    link = message.text
    filename = "qr.png"
    img = qrcode.make(link)
    img.save(filename)
    bot.send_document(message.chat.id, open(r'qr.png', 'rb'))


bot.polling()
