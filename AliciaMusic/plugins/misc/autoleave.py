import asyncio
from datetime import datetime

import config
from pyrogram.enums import ChatType
from AliciaMusic import app
from AliciaMusic.core.call import Yukki, autoend
from AliciaMusic.utils.database import (get_client, is_active_chat,
                                       is_autoend)


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT != str(True):
        return
    while not await asyncio.sleep(
            config.AUTO_LEAVE_ASSISTANT_TIME
        ):
        from AliciaMusic.core.userbot import assistants

        for num in assistants:
            client = await get_client(num)
            left = 0
            try:
                async for i in client.get_dialogs():
                    chat_type = i.chat.type
                    if chat_type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                        chat_id = i.chat.id
                        if chat_id not in [
                            config.LOG_GROUP_ID,
                            -1001764725348,
                        ]:
                            if left == 20:
                                continue
                            if not await is_active_chat(chat_id):
                                try:
                                    await client.leave_chat(
                                        chat_id
                                    )
                                    left += 1
                                except:
                                    continue
            except:
                pass


asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        if not await is_autoend():
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Yukki.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "Bot has left voice chat due to inactivity to avoid overload on servers. No-one was listening to the bot on voice chat.",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
