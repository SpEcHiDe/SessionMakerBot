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
    SESSION_GENERATED_USING
)


@Client.on_message(
    filters.text &
    filters.private,
    group=3
)
async def recv_tg_tfa_message(_, message: Message):
    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    signed_in = w_s_dict.get("SIGNED_IN")
    phone_number = w_s_dict.get("PHONE_NUMBER")
    loical_ci = w_s_dict.get("USER_CLIENT")
    if not signed_in or not phone_number:
        return
    await w_s_dict.get("MESSAGE").delete()
    del w_s_dict["MESSAGE"]
    tfa_code = message.text
    await loical_ci.check_password(tfa_code)
    saved_message_ = await message.reply_text(
        str(await loical_ci.export_session_string()),
        quote=True
    )
    await saved_message_.reply_text(
        SESSION_GENERATED_USING,
        quote=True
    )
