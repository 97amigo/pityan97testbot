import telebot
import vk_api
from vk_api import audio

def vk_case(i, id):
    REQUEST_STATUS_CODE = 200
    login = '+79163914689'  # Номер телефона
    password = '12832pit28!'  # Пароль

    vk_session = vk_api.VkApi(login=login, password=password)
    vk_session.auth()
    vk = vk_session.get_api()
    vk_audio = audio.VkAudio(vk_session)

    return (vk_audio.get(owner_id = int(id))[i]['url'])

mybot_TOKEN = '974770884:AAFkEr5EmeElm4DlGXAns1CgNtaFKrHgK-k'

bot = telebot.TeleBot(mybot_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "I just give you first five your vk tracks?")
    bot.send_message(message.chat.id, "Enter the id of page you want to get tracks(it should be opened)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    for i in range(5):
        bot.send_audio(chat_id = message.chat.id, audio = vk_case(i, message.text))

bot.polling()
