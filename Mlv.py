import telebot
import subprocess

TOKEN = "YOURBOTTOKEN"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def terminal(message):

    command = message.text

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    output = result.stdout or result.stderr

    bot.reply_to(message, output)


bot.polling()
