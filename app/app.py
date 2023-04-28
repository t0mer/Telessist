import os
from pathlib import Path
from loguru import logger
from telebot import types, TeleBot
from commandhandler import CommandHandler
from telebot.custom_filters import AdvancedCustomFilter
from telebot.callback_data import CallbackData, CallbackDataFilter

BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_IDS = os.getenv("ALLOWED_IDS")
audio_dir = Path.cwd() / "audio/"
audio_dir.mkdir(parents=True, exist_ok=True)
data_dir = Path.cwd() / "data/"
data_dir.mkdir(parents=True, exist_ok=True)
commandHandler = CommandHandler()

bot = TeleBot(BOT_TOKEN)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    result = commandHandler.execute_command(message.text)
    if message.text.startswith("/d") and result.lower().endswith(".png"):
        photo = open(str(result),'rb')
        bot.send_photo(message.chat.id,photo)
        os.remove(str(result))
    else:
        bot.reply_to(message,result, parse_mode='Markdown')


# Handles Voice messages
@bot.message_handler(content_types=['voice'])
def handle_docs_audio(message):
    file_info = bot.get_file(message.voice.file_id)
    file_path = audio_dir / f'{message.voice.file_unique_id}.ogg'
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = commandHandler.transcript(str(file_path))
    bot.reply_to(message,result)

# Handles Audio messages
@bot.message_handler(content_types=['audio'])
def handle_docs_audio(message):
    file_info = bot.get_file(message.audio.file_id)
    file_path = audio_dir / message.audio.file_name
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = commandHandler.transcript(str(file_path))
    bot.reply_to(message,result)

	

	













if __name__ == '__main__':
    logger.debug("Starting")
    logger.debug("I'm running and wating for commands")
    bot.infinity_polling()