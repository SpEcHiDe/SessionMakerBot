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
from pyrogram.errors import (
    SessionPasswordNeeded,
    BadRequest
)
from bot import (
    ACC_PROK_WITH_TFA,
    AKTIFPERINTAH,
    RECVD_PHONE_CODE
)


@Client.on_message(
    filters.text &
    filters.private,
    group=2
)
async def recv_tg_code_message(_, message: Message):
    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    sent_code = w_s_dict.get("SENT_CODE_R")
    phone_number = w_s_dict.get("PHONE_NUMBER")
    loical_ci = w_s_dict.get("USER_CLIENT")
    if not sent_code or not phone_number:
        return
    await w_s_dict.get("MESSAGE").delete()
    del w_s_dict["MESSAGE"]
    status_message = await message.reply_text(
        RECVD_PHONE_CODE,
        quote=True
    )
    phone_code = "".join(message.text.split(" "))
    try:
        w_s_dict["SIGNED_IN"] = await loical_ci.sign_in(
            phone_number,
            sent_code.phone_code_hash,
            phone_code
        )
    except BadRequest as e:
        await status_message.edit_text(e.MESSAGE)
        del AKTIFPERINTAH[message.chat.id]
    except SessionPasswordNeeded as e:
        print(e.MESSAGE)
        await status_message.edit_text(
            ACC_PROK_WITH_TFA
        )
    w_s_dict["MESSAGE"] = status_message
    AKTIFPERINTAH[message.chat.id] = w_s_dict
