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


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from bot import (
    AKTIFPERINTAH,
    COMMM_AND_PRE_FIX,
    START_COMMAND,
    START_OTHER_USERS_TEXT,
    INPUT_PHONE_NUMBER
)


@Client.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    filters.private
)
async def num_start_message(_, message: Message):
    AKTIFPERINTAH[message.chat.id] = {}
    status_message = await message.reply_text(
        START_OTHER_USERS_TEXT + "\n" + INPUT_PHONE_NUMBER
    )
    AKTIFPERINTAH[message.chat.id]["START"] = status_message
    raise message.stop_propagation()
