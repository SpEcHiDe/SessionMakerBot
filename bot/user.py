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

""" MtProto User """

from ast import parse
from pyrogram import (
    Client,
    __version__,
    enums
)
from bot import (
    API_HASH,
    APP_ID,
    LOGGER,
    TG_BOT_WORKERS
)


class User(Client):
    """ modded client for SessionMakerUser """

    def __init__(self):
        super().__init__(
            name="tu",
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=TG_BOT_WORKERS,
            in_memory=True,
            parse_mode=enums.ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
