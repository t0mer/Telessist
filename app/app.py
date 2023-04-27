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
















if __name__ == '__main__':
    logger.debug("Starting")
    logger.debug("I'm running and wating for commands")
    bot.infinity_polling()