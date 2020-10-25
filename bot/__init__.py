#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from bot.get_config import get_config

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")

# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)

# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
#
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
# start command
START_COMMAND = get_config("START_COMMAND", "start")
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "SessionMakerBot.log")
# a dictionary to store the currently running processes
AKTIFPERINTAH = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)


# /start message when other users start your bot
START_OTHER_USERS_TEXT = get_config(
    "START_OTHER_USERS_TEXT",
    (
        "Hi. ☺️\n"
        "Thank you for using me 😬\n\n"
        "This is an Open Source Project available on "
        "https://github.com/SpEcHIDe/SessionMakerBot\n\n\n"
        "ℹ️ Subscribe @SpEcHlDe if you 😍 using this bot❗️❣️"
    )
)
INPUT_PHONE_NUMBER = (
    "Enter the Phone Number that you want to make awesome."
)
RECVD_PHONE_NUMBER_DBP = (
    "checking received phone number \n\n"
    ">> the Process Takes a Long Time,\n"
    ">>> Please be Patient,\n\n"
    "<b>Never Submit Again</b>"
    "<b><i><u>It'll ruin the System</u></i></b>"
)
ALREADY_REGISTERED_PHONE = (
    "This number is registered on Telegram. "
    "Please input the verification code that you receive "
    "from <a href='tg://user?id=777000'>Telegram</a> "
    "seperated by space, "
    "else a PhoneCodeInvalidError would be raised."
)
RECVD_PHONE_CODE = (
    "checking received phone code \n\n"
    ">> the Process Takes a Long Time,\n"
    ">>> Please be Patient,\n\n"
    "<b>Never Submit Again</b>"
    "<b><i><u>It'll ruin the System</u></i></b>"
)
NOT_REGISTERED_PHONE = (
    "This number is not registered on Telegram. "
    "Please check your #karma by reading https://t.me/c/1220993104/28753"
)
PHONE_CODE_IN_VALID_ERR_TEXT = "Invalid Code Received. Please re /start"
ACC_PROK_WITH_TFA = (
    "The entered Telegram Number is protected with 2FA. "
    "Please enter your second factor authentication code.\n"
    "__This message will only be used for generating your "
    "string session, and will never be used for any other purposes "
    "than for which it is asked.__\n\n"
    ""
)
SESSION_GENERATED_USING = (
    "Thank you for using me 😬\n\n"
    "This is an Open Source Project available on "
    "https://github.com/SpEcHIDe/SessionMakerBot\n\n\n"
    "👆👆👆 String Session successfully generated 👆👆👆"
)
