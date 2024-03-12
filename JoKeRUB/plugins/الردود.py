import re

from JoKeRUB import l313l
from io import BytesIO
from ..core.managers import edit_or_reply
from ..sql_helper.filter_sql import (
    add_filter,
    get_filters,
    remove_all_filters,
    remove_filter,
)
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "utils"
ROZTEXT = "عـذرا لا يمكـنك اضافـة رد هـنا" 


@l313l.ar_cmd(incoming=True)
async def filter_incoming_handler(handler):
    if handler.sender_id == handler.client.uid:
        return

    name = handler.raw_text
    filters = get_filters(handler.chat_id)
    if not filters:
        return
    a_user = await handler.get_sender()
    is_private = handler.is_private
    if not is_private:
        chat = await handler.get_chat()
        me = await handler.client.get_me()
        title = chat.title or "this chat"
        participants = await handler.client.get_participants(chat)
        count = len(participants)
        mention = f"[{a_user.first_name}](tg://user?id={a_user.id})"
        my_mention = f"[{me.first_name}](tg://user?id={me.id})"
        first = a_user.first_name
        last = a_user.last_name
        fullname = f"{first} {last}" if last else first
        username = f"@{a_user.username}" if a_user.username else mention
        userid = a_user.id
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
    else:
        title = "Private Chat"
        me = await handler.client.get_me()

    for trigger in filters:
        pattern = r"( |^|[^\w])" + re.escape(trigger.keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            if trigger.f_mesg_id:
                msg_o = await handler.client.get_messages(
                    entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id)
                )
                if isinstance(msg_o.entities, list) and any(isinstance(entity, MessageEntityCustomEmoji) for entity in msg_o.entities):
                    emoji_bytes = await handler.client.download_media(msg_o)
                    emoji_io = BytesIO(emoji_bytes)
                    await handler.client.send_file(handler.chat_id, file=emoji_io)
                    return
                await handler.reply(
                    msg_o.message.format(
                        mention=f"[{a_user.first_name}](tg://user?id={a_user.id})",
                        title=title,
                        count="",
                        first=a_user.first_name,
                        last=a_user.last_name,
                        fullname=f"{a_user.first_name} {a_user.last_name}" if a_user.last_name else a_user.first_name,
                        username=f"@{a_user.username}" if a_user.username else f"[{a_user.first_name}](tg://user?id={a_user.id})",
                        userid=a_user.id,
                        my_first=me.first_name,
                        my_last=me.last_name,
                        my_fullname=f"{me.first_name} {me.last_name}" if me.last_name else me.first_name,
                        my_username=f"@{me.username}" if me.username else f"[{me.first_name}](tg://user?id={me.id})",
                        my_mention=f"[{me.first_name}](tg://user?id={me.id})",
                    ),
                    file=msg_o.media,
                )
            elif trigger.reply:
                await handler.reply(
                    trigger.reply.format(
                        mention=f"[{a_user.first_name}](tg://user?id={a_user.id})",
                        title=title,
                        count="",
                        first=a_user.first_name,
                        last=a_user.last_name,
                        fullname=f"{a_user.first_name} {a_user.last_name}" if a_user.last_name else a_user.first_name,
                        username=f"@{a_user.username}" if a_user.username else f"[{a_user.first_name}](tg://user?id={a_user.id})",
                        userid=a_user.id,
                        my_first=me.first_name,
                        my_last=me.last_name,
                        my_fullname=f"{me.first_name} {me.last_name}" if me.last_name else me.first_name,
                        my_username=f"@{me.username}" if me.username else f"[{me.first_name}](tg://user?id={me.id})",
                        my_mention=f"[{me.first_name}](tg://user?id={me.id})",
                    ),
                )

@l313l.ar_cmd(
    pattern="رد ([\s\S]*)",
    command=("رد", plugin_category),
    info={
        "header": "To save filter for the given keyword.",
        "description": "If any user sends that filter then your bot will reply.",
        "option": {
            "{mention}": "To mention the user",
            "{title}": "To get chat name in message",
            "{count}": "To get group members",
            "{first}": "To use user first name",
            "{last}": "To use user last name",
            "{fullname}": "To use user full name",
            "{userid}": "To use userid",
            "{username}": "To use user username",
            "{my_first}": "To use my first name",
"{my_fullname}": "To use my full name",
            "{my_last}": "To use my last name",
            "{my_mention}": "To mention myself",
            "{my_username}": "To use my username.",
        },
        "note": "For saving media/stickers as filters you need to set PRIVATE_GROUP_BOT_API_ID.",
        "usage": "{tr}filter <keyword>",
    },
)
async def add_new_filter(new_handler):
    "To save the filter"
    keyword = new_handler.pattern_match.group(1)
    string = new_handler.text.partition(keyword)[2]
    msg = await new_handler.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if isinstance(msg.entities, list) and any(isinstance(entity, MessageEntityCustomEmoji) for entity in msg.entities):
            emoji_bytes = await new_handler.client.download_media(msg)
            emoji_io = BytesIO(emoji_bytes)
            await new_handler.client.send_file(new_handler.chat_id, file=emoji_io)
            return
        if BOTLOG:
            await new_handler.client.send_message(
                BOTLOG_CHATID,
                f"#الــرد\
            \nايدي الدردشه: {new_handler.chat_id}\
            \nالـكيبورد: {keyword}\
            \n\nالرسالة التالية حفظت كرد ارسل معلومات الرد لرؤية الرد  ،  لاتقم بحذف ارسالة !!",
            )
            msg_o = await new_handler.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=new_handler.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                new_handler,
                "⌯︙يتطلب حفظ الوسائط كرد  تعيين PRIVATE_GROUP_BOT_API_ID\n قـم بعمل مجموعه وقم باخذ ايدي المجموعه عبر اي بوت بعدها ارسل\n .set var PRIVATE_GROUP_BOT_API_ID + ايدي المجموعة ",
            )
            return
    elif new_handler.reply_to_msg_id and not string:
        rep_msg = await new_handler.get_reply_message()
        string = rep_msg.text
    success = "**᯽︙ الـرد {} تـم اضـافتة بنـجـاح ✓**"
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(new_handler, success.format(keyword, "added"))
    remove_filter(str(new_handler.chat_id), keyword)
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(new_handler, success.format(keyword, "Updated"))
    await edit_or_reply(new_handler, f"Error while setting filter for {keyword}")

async def add_private_filter(new_handler):
    "To save the private chat filter"
    keyword = new_handler.pattern_match.group(1)
    string = new_handler.text.partition(keyword)[2]
    msg = await new_handler.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if msg.entities:
            for entity in msg.entities:
                if isinstance(entity, MessageEntityCustomEmoji):
                    emoji_bytes = await new_handler.client.download_media(msg)
                    emoji_io = BytesIO(emoji_bytes)
                    await new_handler.reply(file=emoji_io)
                    return
        if BOTLOG:
            await new_handler.client.send_message(
                BOTLOG_CHATID,
                f"#الــرد\
            \nايدي الدردشه: {new_handler.chat_id}\
            \nالـكيبورد: {keyword}\
            \n\nالرسالة التالية حفظت كرد ارسل معلومات الرد لرؤية الرد  ،  لاتقم بحذف ارسالة !!",
            )
            msg_o = await new_handler.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=new_handler.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                new_handler,
                "⌯︙يتطلب حفظ الوسائط كرد  تعيين PRIVATE_GROUP_BOT_API_ID\n قـم بعمل مجموعه وقم باخذ ايدي المجموعه عبر اي بوت بعدها ارسل\n .set var PRIVATE_GROUP_BOT_API_ID + ايدي المجموعة ",
            )
            return
    elif new_handler.reply_to_msg_id and not string:
        rep_msg = await new_handler.get_reply_message()
        string = rep_msg.text
    filters = get_filters(new_handler.chat_id)
    for filter in filters:
        if filter.keyword == keyword:
            add_filter(str(new_handler.chat_id), keyword, string, msg_id)
            success = "**᯽︙ الـرد {} تـم اضـافتة بنـجـاح ✓**"
            await edit_or_reply(new_handler, success.format(keyword))
            return

    await edit_or_reply(
        new_handler,
        "⌯︙ لا يمكنك استخدام هذا الأمر في المجموعات. يرجى استخدام أمر آخر لإضافة ردود في المجموعات.",
    )
        
@l313l.ar_cmd(
    pattern="الردود$",
    command=("الردود", plugin_category),
    info={
        "header": "To list all filters in that chat.",
        "description": "Lists all active (of your userbot) filters in a chat.",
        "usage": "{tr}filters",
    },
)
async def on_snip_list(event):
    "To list all filters in that chat."
    OUT_STR = "**᯽︙لا توجد ردود مضافة في هذه الدردشه  🔍**"
    filters = get_filters(event.chat_id)
    for filt in filters:
        if OUT_STR == "**᯽︙لا توجد ردود مضافة في هذه الدردشة  🔍**":
            OUT_STR = "**᯽︙الردود التي تم اضافتها في هذه الدردشة**\n"
        OUT_STR += "⌯︙{}\n".format(filt.keyword)
    await edit_or_reply(
        event,
        OUT_STR,
        caption="Available Filters in the Current Chat",
        file_name="filters.text",
    )


@l313l.ar_cmd(
    pattern="حذف رد ([\s\S]*)",
    command=("حذف رد", plugin_category),
    info={
        "header": "To delete that filter . so if user send that keyword bot will not reply",
        "usage": "{tr}stop <keyword>",
    },
)
async def remove_a_filter(r_handler):
    "Stops the specified keyword."
    filt = r_handler.pattern_match.group(1)
    if not remove_filter(r_handler.chat_id, filt):
        await r_handler.edit("**᯽︙الـرد {} غير موجود **".format(filt))
    else:
        await r_handler.edit("**᯽︙ الـرد {} تـم حـذفة بنـجـاح ✓**".format(filt))


@l313l.ar_cmd(
    pattern="حذف الردود$",
    command=("حذف الردود", plugin_category),
    info={
        "header": "To delete all filters in that group.",
        "usage": "{tr}rmfilters",
    },
)
async def on_all_snip_delete(event):
    "To delete all filters in that group."
    filters = get_filters(event.chat_id)
    if filters:
        remove_all_filters(event.chat_id)
        await edit_or_reply(event, f"**᯽︙ تم حذف الردود في الدردشة الحالية بنجاح ✓**")
    else:
        await edit_or_reply(event, f"᯽︙لا توجد ردود في هذه المجموعة  ")
