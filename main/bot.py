import telebot
from django.shortcuts import render
from main import models


bot = telebot.TeleBot('1850642993:AAFamhHLH6JPxJhFXiayyCQ7Us7_wDvuYL4')

bot.send_message(221464302, "Bot запущен")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.from_user.id == 221464302:
        user = int(message.text.split("\n")[0].strip())
        text = ""
        for i in message.text.split("\n")[1:]:
            text += i + '\n'
        bot.send_message(
            user,
            text
        )
    elif message.text == "/start":
        bot.send_message(
            message.from_user.id,
            "Здравствуйте, расскажите о своей проблеме, и наша команда Вам поможет! (Диалог анонимный)"
        )
    elif message.text.lower() == "привет":
        bot.send_message(
            message.from_user.id,
            "Здравствуйте, расскажите о своей проблеме, и наша команда Вам поможет! (Диалог анонимный)"
        )
    else:
        bot.send_message(221464302, f"Сообщение от: {message.from_user.id}\n{message.text}")
        bot.send_message(message.from_user.id, "Наши специалисты, скоро Вам ответят\nComing soon")

bot.polling(none_stop=True, interval=0)