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
    ALREADY_REGISTERED_PHONE,
    CONFIRM_SENT_VIA,
    RECVD_PHONE_NUMBER_DBP
)
from bot.user import User


@Client.on_message(
    filters.text &
    filters.private,
    group=1
)
async def recvd_ph_no_message(_, message: Message):
    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    status_message = w_s_dict.get("START")
    if not status_message:
        return
    del w_s_dict["START"]
    status_message = await message.reply_text(
        RECVD_PHONE_NUMBER_DBP
    )
    loical_ci = User()
    w_s_dict["PHONE_NUMBER"] = message.text
    await loical_ci.connect()
    w_s_dict["SENT_CODE_R"] = await loical_ci.send_code(
        w_s_dict["PHONE_NUMBER"]
    )
    w_s_dict["USER_CLIENT"] = loical_ci

    status_message = await status_message.edit_text(
        ALREADY_REGISTERED_PHONE + "\n\n" + CONFIRM_SENT_VIA.format(
            w_s_dict["SENT_CODE_R"].type.value
        )
    )
    w_s_dict["MESSAGE"] = status_message
    AKTIFPERINTAH[message.chat.id] = w_s_dict
    raise message.stop_propagation()
