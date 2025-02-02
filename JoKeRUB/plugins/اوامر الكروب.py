#aljoker 2024
from asyncio import sleep
import asyncio
import requests
import random
import re
from re import match
from datetime import datetime
import time
from telethon.tl import types
from telethon.tl.types import Channel, Chat, User, ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import ChannelPrivateError
from telethon.tl.custom import Message
from ..Config import Config
from telethon.errors import (
    ChatAdminRequiredError,
    FloodWaitError,
    MessageNotModifiedError,
    UserAdminInvalidError,
)
from telethon.tl import functions
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.channels import EditBannedRequest, LeaveChannelRequest
from telethon.tl.functions.channels import EditAdminRequest
from telethon import events
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantCreator,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
    InputPeerChat,
    MessageEntityCustomEmoji,
)
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from datetime import datetime
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from ..core.logger import logging
from ..helpers.utils import reply_id
from ..sql_helper.locks_sql import *
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import readable_time
from . import BOTLOG, BOTLOG_CHATID
LOGS = logging.getLogger(__name__)
plugin_category = "admin"
spam_chats = []
aljoker_time = None
BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

from datetime import datetime

marriage = []
joker_marriage = []
marriage_details = {}
marriage_contracts = {}
dowry_per_message = 10 
min_dowry = 1000  
joker_balance = 20000  # تخزين رصيد البوت

@l313l.ar_cmd(pattern="نزوج(?: |$)(.*)")
async def handle_marriage_request(event):
    sender_id = event.sender_id
    message = event.pattern_match.group(1).strip()
    
    try:
        requested_dowry = int(message)
    except ValueError:
        await event.edit('الرجاء إدخال مبلغ صالح للمهر')
        return
    
    if requested_dowry < min_dowry:
        await event.edit(f'عذرًا، المهر يجب أن يكون على الأقل {min_dowry}$')
        return
    
    if requested_dowry > joker_balance:
        await event.edit('عذرًا، رصيد البوت غير كافي لقبول الزواج')
        return

    if event.is_reply:
        replied_message = await event.get_reply_message()
        if replied_message.sender_id:
            if len(joker_marriage) < 4:
                if replied_message.sender_id not in joker_marriage:
                    marriage_details[replied_message.sender_id] = {'dowry': requested_dowry}
                    marriage.append(replied_message.sender_id)
                    await event.edit('هل تريد الزواج مني؟ (نعم/لا)')
                else:
                    await event.edit('عذرًا، أنتم متزوجان بالفعل!')
            else:
                await event.edit('عذرًا، لقد وصلنا إلى الحد الأقصى للزواجيات')
    else:
        await event.edit('يجب الرد على رسالة المستخدم لتنفيذ الأمر')

@l313l.on(events.NewMessage(outgoing=True))  # تحديث الرسالة الصادرة
async def handle_outgoing_message(event):
    global joker_balance
    joker_balance += dowry_per_message  # زيادة رصيد البوت بقيمة الرسالة

@l313l.on(events.NewMessage(outgoing=True, pattern=r'\.رصيدي'))
async def check_bot_balance(event):
    global joker_balance
    await event.reply(f"رصيد البوت الحالي: {joker_balance}$")

@l313l.ar_cmd(pattern="طالق")
async def handle_divorce(event):
    if event.is_reply:
        replied_message = await event.get_reply_message()
        if replied_message.sender_id in joker_marriage:
            joker_marriage.remove(replied_message.sender_id)
            contracts_to_remove = [contract_id for contract_id, contract in marriage_contracts.items() if contract['husband'] == replied_message.sender_id or contract['wife'] == replied_message.sender_id]
            for contract_id in contracts_to_remove:
                del marriage_contracts[contract_id]
            await event.edit('تمت طلاق الزوجة وارجاعها الى اهلها 😂')
        else:
            await event.edit('الزوجة ماموجوده وية زوجاتك البقية')
    else:
        await event.edit('يجب الرد على رسالة المستخدم لتنفيذ الأمر')
    
@l313l.on(events.NewMessage(incoming=True))
async def handle_incoming_message(event):
    global joker_balance, marriage_contracts
    sender_id = event.sender_id
    if sender_id in marriage:
        if event.text.lower() in ['نعم', 'لا']:
            if event.text.lower() == 'نعم':
                aljoker_entity = await event.client.get_entity(sender_id)
                replied_sender_entity = await event.client.get_entity('me')
                aljoker_profile = f"[{aljoker_entity.first_name}](tg://user?id={aljoker_entity.id})"
                replied_sender_profile = f"[{replied_sender_entity.first_name}](tg://user?id={replied_sender_entity.id})"
                dowry = marriage_details[sender_id]['dowry']  # استخدام المهر المحدد كقيمة المهر
                if dowry <= joker_balance:
                    joker_balance -= dowry  # خصم المهر من الرصيد الكلي
                    marriage_date = datetime.now()
                    marriage_contracts[sender_id] = {
                        'husband': replied_sender_entity.id,
                        'wife': aljoker_entity.id,
                        'dowry': dowry,
                        'date': marriage_date
                    }
                    await event.reply(f'الف مبروووك الى {replied_sender_profile} و {aljoker_profile} اصبحا زوجاً وزوجة\nالمهر: {dowry}$\nالرصيد المتبقي: {joker_balance}$')
                    joker_marriage.append(sender_id)
                else:
                    await event.reply('عذرًا، رصيد البوت غير كافي لإتمام الزواج')
                marriage.remove(sender_id)
            else:
                await event.reply('تم رفض طلب الزواج')
                marriage.remove(sender_id)
    elif sender_id in joker_marriage:
        if event.text.strip().lower() == 'زوجي':
            await event.reply('ها يعمري اني موجود لا تخافي ❤️😍')

@l313l.ar_cmd(pattern="عقد الزواج")
async def show_marriage_contracts(event):
    user_id = event.sender_id
    user_contracts = [contract for contract in marriage_contracts.values() if contract['husband'] == user_id or contract['wife'] == user_id]
    
    if user_contracts:
        reply_message = "عقود الزواج:\n\n"
        for contract in user_contracts:
            husband = await event.client.get_entity(contract['husband'])
            wife = await event.client.get_entity(contract['wife'])
            dowry = contract['dowry']
            date = contract['date'].strftime('%Y-%m-%d')
            time = contract['date'].strftime('%I:%M %p')
            meridiem = "صباحًا" if int(contract['date'].strftime('%H')) < 12 else "مساءًا"  # تحديد الفترة (صباحًا / مساءًا)
            reply_message += f"الزوج: [{husband.first_name}](tg://user?id={husband.id})\n"
            reply_message += f"الزوجة: [{wife.first_name}](tg://user?id={wife.id})\n"
            reply_message += f"المهر: {dowry}$\n"
            reply_message += f"تاريخ الزواج: {date}\n"
            reply_message += f"الساعة: {time} {meridiem}\n\n"
        await event.reply(reply_message)
    else:
        await event.reply("لا يوجد عقود زواج مسجلة لك.")
@l313l.ar_cmd(pattern="نسواني")
async def handle_call_wife(event):
    mentions = []
    for wife_id in joker_marriage:
        wife_entity = await event.client.get_entity(wife_id)
        mentions.append(f"[{wife_entity.first_name}](tg://user?id={wife_id})")
    if mentions:
        if len(mentions) == 1:
            await event.edit(f'تعالي حبيبتي زوجج يريدج ❤️: {mentions[0]}')
        else:
            await event.edit(f'تعالن حبيباتي رجلچن يريدچن ❤️: {" ,".join(mentions)}')
    else:
        await event.reply('لا يوجد زوجات متزوجات حالياً.')
async def ban_user(chat_id, i, rights):
    try:
        await l313l(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)        
@l313l.ar_cmd(pattern="ارسل")
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("تم الارسال الرسالة الى الرابط الذي وضعتة")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("تم ارسال الرساله الى الرابط الذي وضعتة")
    except BaseException:
        await event.edit("** عذرا هذا ليست مجموعة **")
@l313l.ar_cmd(
    pattern="اطردني$",
    command=("اطردني", plugin_category),
    info={
        "header": "To kick myself from group.",
        "usage": [
            "{tr}kickme",
        ],
    },
    groups_only=True,
)
async def kickme(leave):
    "to leave the group."
    await leave.edit("᯽︙  حسنا سأغادر المجموعه وداعا ")
    await leave.client.kick_participant(leave.chat_id, "me")

@l313l.ar_cmd(
    pattern="تفليش بالطرد$",
    command=("تفليش بالطرد", plugin_category),
    info={
        "header": "To kick everyone from group.",
        "description": "To Kick all from the group except admins.",
        "usage": [
            "{tr}kickall",
        ],
    },
    require_admin=True,
)
async def _(event):
    "To kick everyone from group."
    await event.delete()
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, event.client.uid)
    )
    if not result.participant.admin_rights.ban_users:
        return await edit_or_reply(
            event, "᯽︙ - يبدو انه ليس لديك صلاحيات الحذف في هذه الدردشة "
        )
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client.kick_participant(event.chat_id, user.id)
                success += 1
                await sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await sleep(0.5)
    await event.reply(
        f"᯽︙  تم بنجاح طرد من {total} الاعضاء ✅ "
    )

@l313l.ar_cmd(
    pattern="تفليش$",
    command=("تفليش", plugin_category),
    info={
        "header": "To ban everyone from group.",
        "description": "To ban all from the group except admins.",
        "usage": [
            "{tr}kickall",
        ],
    },
    require_admin=True,
)
async def _(event):
    "To ban everyone from group."
    await event.delete()

    try:
        # Check if it's a channel
        chat = await event.client.get_entity(event.chat_id)
        if chat:
            # For channels
            participants = await event.client(GetParticipantRequest(event.chat_id, event.client.uid))
            admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        else:
            # For groups
            full_chat = await event.client(GetFullChatRequest(event.chat_id))
            participants = full_chat.full_chat.participants
            admins = [admin for admin in participants if admin.admin_rights]

        admins_id = [i.id for i in admins]
        total = 0
        success = 0
        for user in participants:
            total += 1
            try:
                if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
                    success += 1
                    await asyncio.sleep(0.5) # for avoiding any flood waits
            except Exception as e:
                LOGS.info(str(e))
        await event.reply(f"تم بنجاح حظر {success} من اصل {total} اعضاء.")
    except Exception as e:
        LOGS.info(str(e))
        await event.reply("حدث خطأ أثناء تنفيذ الأمر.")



@l313l.ar_cmd(
    pattern="حذف المحظورين$",
    command=("حذف المحظورين", plugin_category),
    info={
        "header": "To unban all banned users from group.",
        "usage": [
            "{tr}unbanall",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To unban all banned users from group."
    catevent = await edit_or_reply(
        event, "**᯽︙ يتـم الـغاء حـظر الجـميع فـي هذه الـدردشـة**"
    )
    succ = 0
    total = 0
    flag = False
    chat = await event.get_chat()
    async for i in event.client.iter_participants(
        event.chat_id, filter=ChannelParticipantsKicked, aggressive=True
    ):
        total += 1
        rights = ChatBannedRights(until_date=0, view_messages=False)
        try:
            await event.client(
                functions.channels.EditBannedRequest(event.chat_id, i, rights)
            )
        except FloodWaitError as e:
            LOGS.warn(f"لقد حدث عمليه تكرار كثير ارجو اعادة الامر او انتظر")
            await catevent.edit(
                f"أنتـظر لـ {readable_time(e.seconds)} تحتاط لاعادة الامر لاكمال العملية"
            )
            await sleep(e.seconds + 5)
        except Exception as ex:
            await catevent.edit(str(ex))
        else:
            succ += 1
            if flag:
                await sleep(2)
            else:
                await sleep(1)
            try:
                if succ % 10 == 0:
                    await catevent.edit(
                        f"᯽︙  الغاء حظر جميع الحسابات\nتم الغاء حظر جميع الاعضاء بنجاح ✅"
                    )
            except MessageNotModifiedError:
                pass
    await catevent.edit(f"᯽︙ الغاء حظر :__{succ}/{total} في الدردشه {chat.title}__")

# Ported by ©[NIKITA](t.me/kirito6969) and ©[EYEPATCH](t.me/NeoMatrix90)
@l313l.ar_cmd(
    pattern="المحذوفين ?([\s\S]*)",
    command=("المحذوفين", plugin_category),
    info={
        "header": "To check deleted accounts and clean",
        "description": "Searches for deleted accounts in a group. Use `.zombies clean` to remove deleted accounts from the group.",
        "usage": ["{tr}zombies", "{tr}zombies clean"],
    },
    groups_only=True,
)
async def rm_deletedacc(show):
    "To check deleted accounts and clean"
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "᯽︙  لم يتم العثور على حسابات متروكه او حسابات محذوفة الكروب نظيف"
    if con != "اطردهم":
        event = await edit_or_reply(
            show, "᯽︙  يتم البحث عن حسابات محذوفة او حسابات متروكة انتظر"
        )
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(0.5)
        if del_u > 0:
            del_status = f"᯽︙ تـم العـثور : **{del_u}** على حسابات محذوفة ومتروكه في هذه الدردشه من الحسابات في هذه الدردشه,\
                           \nاطردهم بواسطه  `.المحذوفين اطردهم`"
        await event.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(show, "أنا لسـت مشرف هـنا", 5)
        return
    event = await edit_or_reply(
        show, "᯽︙ جاري حذف الحسابات المحذوفة"
    )
    del_u = 0
    del_a = 0
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client.kick_participant(show.chat_id, user.id)
                await sleep(0.5)
                del_u += 1
            except ChatAdminRequiredError:
                await edit_delete(event, "᯽︙  ليس لدي صلاحيات الحظر هنا", 5)
                return
            except UserAdminInvalidError:
                del_a += 1
    if del_u > 0:
        del_status = f"التنظيف **{del_u}** من الحسابات المحذوفة"
    if del_a > 0:
        del_status = f"التنظيف **{del_u}** من الحسابات المحذوف \
        \n**{del_a}** لا يمكنني حذف حسابات المشرفين المحذوفة"
    await edit_delete(event, del_status, 5)
    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            f"#تنـظيف الـمحذوفات\
            \n{del_status}\
            \nالـدردشة: {show.chat.title}(`{show.chat_id}`)",
        )

@l313l.ar_cmd(pattern="حظر_الكل(?:\s|$)([\s\S]*)")
async def banall(event):
     chat_id = event.chat_id
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "حظر"
     is_admin = False
     try:
         partici_ = await l313l(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in l313l.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await l313l.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@l313l.ar_cmd(pattern="كتم_الكل(?:\s|$)([\s\S]*)")
async def muteall(event):
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "كتم"
     is_admin = False
     try:
         partici_ = await l313l(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in l313l.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await l313l.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@l313l.ar_cmd(pattern="طرد_الكل(?:\s|$)([\s\S]*)")
async def kickall(event):
     chat_id = event.chat_id
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "طرد"
     is_admin = False
     try:
         partici_ = await l313l(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in l313l.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await l313l.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@l313l.ar_cmd(pattern="الغاء التفليش")
async def ca_sp(event):
  if not event.chat_id in spam_chats:
    return await edit_or_reply(event, "** ᯽︙ 🤷🏻 لا يوجد طرد او حظر او كتم لأيقافه**")
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await edit_or_reply(event, "** ᯽︙ تم الغاء العملية بنجاح ✓**")
@l313l.ar_cmd(
    pattern="احصائيات الاعضاء ?([\s\S]*)",
    command=("احصائيات الاعضاء", plugin_category),
    info={
        "header": "To get breif summary of members in the group",
        "description": "To get breif summary of members in the group . Need to add some features in future.",
        "usage": [
            "{tr}ikuck",
        ],
    },
    groups_only=True,
)
async def _(event):  # sourcery no-metrics
    "To get breif summary of members in the group.1 11"
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not chat.admin_rights and not chat.creator:
            await edit_or_reply(event, " انت لست مشرف هنا ⌔︙")
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    et = await edit_or_reply(event, "يتم البحث في القوائم ⌔︙")
    async for i in event.client.iter_participants(event.chat_id):
        p += 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(until_date=None, view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y += 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastMonth):
            m += 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastWeek):
            w += 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusOffline):
            o += 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusOnline):
            q += 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusRecently):
            r += 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if i.bot:
            b += 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("᯽︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        elif i.deleted:
            d += 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
        elif i.status is None:
            n += 1
    if input_str:
        required_string = """الـمطرودين {} / {} الأعـضاء
الحـسابـات المـحذوفة: {}
حـالة المستـخدم الفـارغه: {}
اخر ظهور منذ شـهر: {}
اخر ظـهور منـذ اسبوع: {}
غير متصل: {}
المستخدمين النشطون: {}
اخر ظهور قبل قليل: {}
البوتات: {}
مـلاحظة: {}"""
        await et.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await sleep(5)
    await et.edit(
        """: {} مـجموع المـستخدمين
الحـسابـات المـحذوفة: {}
حـالة المستـخدم الفـارغه: {}
اخر ظهور منذ شـهر: {}
اخر ظـهور منـذ اسبوع: {}
غير متصل: {}
المستخدمين النشطون: {}
اخر ظهور قبل قليل: {}
البوتات: {}
مـلاحظة: {}""".format(
            p, d, y, m, w, o, q, r, b, n
        )
    )
##Reda is here 


@l313l.ar_cmd(pattern="مغادرة الكروبات")
async def Reda (event):
    await event.edit("**᯽︙ جارِ مغادرة جميع الكروبات الموجوده في حسابك ...**")
    gr = []
    dd = []
    num = 0
    try:
        async for dialog in event.client.iter_dialogs():
         entity = dialog.entity
         if isinstance(entity, Channel) and not entity.megagroup:
             continue
         elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
            ):
                 gr.append(entity.id)
                 if entity.creator or entity.admin_rights:
                  dd.append(entity.id)
        dd.append(188653089)
        dd.append(1629927549)
        for group in gr:
            if group not in dd:
                await l313l.delete_dialog(group)
                num += 1
                await sleep(1)
        if num >=1:
            await event.edit(f"**᯽︙ تم المغادرة من {num} كروب بنجاح ✓**")
        else:
            await event.edit("**᯽︙ ليس لديك كروبات في حسابك لمغادرتها !**")
    except BaseException as er:
     await event.reply(f"حدث خطأ\n{er}\n{entity}")

DevJoker = [705475246]
@l313l.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("اطلع") and event.sender_id in DevJoker:
        message = event.message
        channel_username = None
        if len(message.text.split()) > 1:
            channel_username = message.text.split()[1].replace("@", "")
        if channel_username:
            try:
                entity = await l313l.get_entity(channel_username)
                if isinstance(entity, Channel) and entity.creator or entity.admin_rights:
                    response = "**᯽︙ لا يمكنك الخروج من هذه القناة. أنت مشرف أو مالك فيها!**"
                else:
                    await l313l(LeaveChannelRequest(channel_username))
                    response = "**᯽︙ تم الخروج من القناة بنجاح!**"
            except ValueError:
                response = "خطأ في العثور على القناة. يرجى التأكد من المعرف الصحيح"
        else:
            response = "**᯽︙ يُرجى تحديد معرف القناة أو المجموعة مع الخروج يامطوري ❤️**"
        #await event.reply(response)
        
@l313l.ar_cmd(pattern="مغادرة القنوات")
async def Hussein (event):
    await event.edit("**᯽︙ جارِ مغادرة جميع القنوات الموجوده في حسابك ...**")
    gr = []
    dd = []
    num = 0
    try:
        async for dialog in event.client.iter_dialogs():
         entity = dialog.entity
         if isinstance(entity, Channel) and entity.broadcast:
             gr.append(entity.id)
             if entity.creator or entity.admin_rights:
                 dd.append(entity.id)
        dd.append(1527835100)
        for group in gr:
            if group not in dd:
                await l313l.delete_dialog(group)
                num += 1
                await sleep(1)
        if num >=1:
            await event.edit(f"**᯽︙ تم المغادرة من {num} قناة بنجاح ✓**")
        else:
            await event.edit("**᯽︙ ليس لديك قنوات في حسابك لمغادرتها !**")
    except BaseException as er:
     await event.reply(f"حدث خطأ\n{er}\n{entity}")

@l313l.ar_cmd(pattern="تصفية الخاص")
async def hussein(event):
    await event.edit("**᯽︙ جارِ حذف جميع الرسائل الخاصة الموجودة في حسابك ...**")
    dialogs = await event.client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_user:
            try:
                await event.client(DeleteHistoryRequest(dialog.id, max_id=0, just_clear=True))
            except Exception as e:
                print(f"حدث خطأ أثناء حذف المحادثة الخاصة: {e}")
    await event.edit("**᯽︙ تم تصفية جميع محادثاتك الخاصة بنجاح ✓ **")

@l313l.ar_cmd(pattern="تصفية البوتات")
async def Hussein(event):
    await event.edit("**᯽︙ جارٍ حذف جميع محادثات البوتات في الحساب ...**")
    result = await event.client(GetContactsRequest(0))
    bots = [user for user in result.users if user.bot]
    for bot in bots:
        try:
            await event.client(DeleteHistoryRequest(bot.id, max_id=0, just_clear=True))
        except Exception as e:
            print(f"حدث خطأ أثناء حذف محادثات البوت: {e}")
    await event.edit("**᯽︙ تم حذف جميع محادثات البوتات بنجاح ✓ **")

# الكود من كتابة فريق الجوكر بس تسرقة تنشر بقناة الفضايح انتَ وقناتك 🖤
@l313l.ar_cmd(pattern=r"ذكاء(.*)")
async def hussein(event):
    await event.edit("**᯽︙ جارِ الجواب على سؤالك انتظر قليلاً ...**")
    text = event.pattern_match.group(1).strip()
    if text:
        url = f'http://api.itdevo.uz/ChatGPT/api/index.php?text={text}'
        response = requests.get(url).text
        await event.edit(response)
    else:
        await event.edit("يُرجى كتابة رسالة مع الأمر للحصول على إجابة.")
is_Reham = False
No_group_Joker = "@jepthonsupport"
# يا يلفاشل هم الك نيه تاخذه وتنشره بسورسك 🤣
active_aljoker = []

@l313l.ar_cmd(pattern=r"الذكاء تفعيل")
async def enable_bot(event):
    global is_Reham
    if not is_Reham:
        is_Reham = True
        active_aljoker.append(event.chat_id)
        await event.edit("**᯽︙ تم تفعيل امر الذكاء الاصطناعي سيتم الرد على اسئلة الجميع عند الرد علي.**")
    else:
        await event.edit("**᯽︙ الزر مُفعّل بالفعل.**")
@l313l.ar_cmd(pattern=r"الذكاء تعطيل")
async def disable_bot(event):
    global is_Reham
    if is_Reham:
        is_Reham = False
        active_aljoker.remove(event.chat_id)
        await event.edit("**᯽︙ تم تعطيل امر الذكاء الاصطناعي.**")
    else:
        await event.edit("**᯽︙ الزر مُعطّل بالفعل.**")
@l313l.on(events.NewMessage(incoming=True))
async def reply_to_hussein(event):
    if not is_Reham:
        return
    if event.is_private or event.chat_id not in active_aljoker:
        return
    message = event.message
    if message.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.sender_id == event.client.uid:
            text = message.text.strip()
            if event.chat.username == No_group_Joker:
                return
            response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text
            await asyncio.sleep(4)
            await event.reply(response)
#ها هم تريد تخمط بمحرم ؟ روح شوفلك موكب واضرب زنجيل احسن من ماتخمط
Ya_Hussein = False
active_joker = []
@l313l.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if not Ya_Hussein:
        return
    if event.is_private or event.chat_id not in active_joker:
        return
    sender_id = event.sender_id
    if sender_id != 705475246:
        if isinstance(event.message.entities, list) and any(isinstance(entity, MessageEntityCustomEmoji) for entity in event.message.entities):
            await event.delete()
            sender = await event.get_sender()
            aljoker_entity = await l313l.get_entity(sender.id)
            aljoker_profile = f"[{aljoker_entity.first_name}](tg://user?id={aljoker_entity.id})"
            await event.reply(f"**᯽︙ عذرًا {aljoker_profile}، يُرجى عدم إرسال الرسائل التي تحتوي على إيموجي المُميز**")
@l313l.ar_cmd(pattern="المميز تفعيل")
async def disable_emoji_blocker(event):
    global Ya_Hussein
    Ya_Hussein = True
    active_joker.append(event.chat_id)
    await event.edit("**᯽︙ ✓ تم تفعيل امر منع الايموجي المُميز بنجاح**")
@l313l.ar_cmd(pattern="المميز تعطيل")
async def disable_emoji_blocker(event):
    global Ya_Hussein
    Ya_Hussein = False
    active_joker.remove(event.chat_id)
    await event.edit("**᯽︙ تم تعطيل امر منع الايموجي المُميز بنجاح ✓ **")
remove_admins_aljoker = {}
#الكود تمت كتابته من قبل مطورين الجوكر اذا الك نية تخمطه اذكر حقوق السورس @jepthon
@l313l.on(events.ChatAction)
async def Hussein(event):
    if gvarstatus("Mn3_Kick"):
        if event.user_kicked:
            user_id = event.action_message.from_id
            chat = await event.get_chat()
            if chat and user_id:
                now = datetime.now()
                if user_id in remove_admins_aljoker:
                    if (now - remove_admins_aljoker[user_id]).seconds < 60:
                        admin_info = await event.client.get_entity(user_id)
                        joker_link = f"[{admin_info.first_name}](tg://user?id={admin_info.id})"
                        await event.reply(f"**᯽︙ تم تنزيل المشرف {joker_link} بسبب قيامه بعملية تفليش فاشلة 🤣**")
                        await event.client.edit_admin(chat, user_id, change_info=False)
                    remove_admins_aljoker.pop(user_id)
                    remove_admins_aljoker[user_id] = now
                else:
                    remove_admins_aljoker[user_id] = now

@l313l.ar_cmd(pattern="منع_التفليش", require_admin=True)
async def Hussein_aljoker(event):
    addgvar("Mn3_Kick", True)
    await event.edit("**᯽︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")

@l313l.ar_cmd(pattern="سماح_التفليش", require_admin=True)
async def Hussein_aljoker(event):
    delgvar("Mn3_Kick")
    await event.edit("**᯽︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")
message_counts = {}
enabled_groups = []
Ya_Abbas = False
@l313l.ar_cmd(pattern="النشر تعطيل")
async def enable_code(event):
    global Ya_Abbas
    Ya_Abbas = True
    enabled_groups.append(event.chat_id)
    await event.edit("**᯽︙ ✓ تم تفعيل امر منع النشر التلقائي بنجاح**")
@l313l.ar_cmd(pattern="النشر تفعيل")
async def disable_code(event):
    global Ya_Abbas
    Ya_Abbas = False
    enabled_groups.remove(event.chat_id)
    await event.edit("**᯽︙ تم تعطيل امر منع النشر التلقائي بنجاح ✓ **")

@l313l.on(events.NewMessage)
async def handle_new_message(event):
    if not Ya_Abbas:
        return
    if event.is_private or event.chat_id not in enabled_groups:
        return
    user_id = event.sender_id
    message_text = event.text
    if user_id not in message_counts:
        message_counts[user_id] = {'last_message': None, 'count': 0}
    if message_counts[user_id]['last_message'] == message_text:
        message_counts[user_id]['count'] += 1
    else:
        message_counts[user_id]['last_message'] = message_text
        message_counts[user_id]['count'] = 1
    if message_counts[user_id]['count'] >= 3:
        try:
            await l313l.edit_permissions(event.chat_id, user_id, send_messages=False)
            sender = await event.get_sender()
            aljoker_entity = await l313l.get_entity(sender.id)
            aljoker_profile = f"[{aljoker_entity.first_name}](tg://user?id={aljoker_entity.id})"
            explanation_message = f"**᯽︙ تم تقييد {aljoker_profile} من إرسال الرسائل بسبب تفعيله نشر التلقائي**"
            await event.reply(explanation_message)
            del message_counts[user_id]
        except ChatAdminRequiredError:
            explanation_message = "عذرًا، ليس لدينا الصلاحيات الكافية لتنفيذ هذا الأمر. يرجى من مشرفي المجموعة منحنا صلاحيات مشرف المجموعة."
            await event.reply(explanation_message)
aljoker_Menu = set()
afk_start_time = datetime.now()
@l313l.on(events.NewMessage)
async def handle_messages(event):
    if gvarstatus("5a9_dis"):
        sender_id = event.sender_id
        current_user_id = await l313l.get_me()
        if event.is_private and sender_id != current_user_id.id:
            await event.delete()
            if sender_id not in aljoker_Menu:
                aljoker_time = aljoker_waqt()
                aljoker_message = gvarstatus("aljoker_message") or f"صاحب الحساب قافل خاصة قبل يلا دعبل"
                aljoker_url = gvarstatus("aljoker_url") or "https://telegra.ph/file/ee30cda28bd1346e54cb3.jpg"
                await l313l.send_file(sender_id, aljoker_url, caption=f'**{aljoker_message}**\n**مدة الغياب: {aljoker_time}**')
                aljoker_Menu.add(sender_id)
@l313l.ar_cmd(pattern="الخاص تعطيل")
async def joker5a9(event: Message):
    global afk_start_time
    addgvar("5a9_dis", True)
    afk_start_time = datetime.now()
    await event.edit('**᯽︙ تم قفل الخاص بنجاح الان لا احد يمكنهُ مراسلتك**')
@l313l.ar_cmd(pattern="الخاص تفعيل")
async def joker5a9(event: Message):
    global afk_start_time
    delgvar("5a9_dis")
    afk_start_time = None
    aljoker_Menu.clear()
    await event.edit('**᯽︙ تم تفعيل الخاص بنجاح الان يمكنهم مراسلتك**')
def aljoker_waqt():
    global afk_start_time
    if afk_start_time:
        current_time = datetime.now()
        duration = current_time - afk_start_time
        days, seconds = duration.days, duration.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if days > 0:
            return f"{days} يوم {hours} ساعة {minutes} دقيقة {seconds} ثانية"
        elif hours > 0:
            return f"{hours} ساعة {minutes} دقيقة {seconds} ثانية"
        else:
            return f"{minutes} دقيقة {seconds} ثانية" if minutes > 0 else f"{seconds} ثانية"
    return "N/A"
points = {}
is_game_started = False
is_word_sent = False
word = ''
async def get_bot_entity():
    return await l313l.get_entity('me')

@l313l.ar_cmd(pattern="اسرع")
async def handle_start(event):
    global is_game_started, is_word_sent, word, bot_entity
    is_game_started = True
    is_word_sent = False
    word = event.text.split(maxsplit=1)[1]
    await event.edit(f"**اول من يكتب ( {word} ) سيفوز**")

@l313l.on(events.NewMessage(incoming=True))
async def handle_winner(event):
    global is_game_started, is_word_sent, winner_id, word, points
    if is_game_started and not is_word_sent and word.lower() in event.raw_text.lower():
        bot_entity = await get_bot_entity()
        if bot_entity and event.sender_id != bot_entity.id:
            is_word_sent = True
            winner_id = event.sender_id
            if winner_id not in points:
                points[winner_id] = 0
            points[winner_id] += 1
            sender = await event.get_sender()
            sender_first_name = sender.first_name if sender else 'مجهول'
            sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)
            points_text = '\n'.join([f'{i+1}• {(await l313l.get_entity(participant_id)).first_name}: {participant_points}' for i, (participant_id, participant_points) in enumerate(sorted_points)])
            await l313l.send_message(event.chat_id, f'الف مبرووووك 🎉 الاعب ( {sender_first_name} ) فاز! \n اصبحت نقاطة: {points[winner_id]}\nنقاط المشاركين:\n{points_text}')
@l313l.ar_cmd(pattern="تصفير")
async def Husssein(event):
    global points
    points = {}
    await event.respond('**تم تصفير نقاط المشاركين بنجاح!**')

joker = [
    "تلعب وخوش تلعب 👏🏻",
    "لك عاش يابطل استمر 💪🏻",
    "على كيفك ركزززز انتَ كدها 🤨",
    "لك وعلي ذيييب 😍",
]

correct_answer = None
game_board = [["👊", "👊", "👊", "👊", "👊", "👊"]]
numbers_board = [["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]]
original_game_board = [["👊", "👊", "👊", "👊", "👊", "👊"]]
joker_player = None
is_game_started2 = False
group_game_status = {}
points = {}
jokerr = 'انا'
async def handle_clue(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id not in group_game_status or not group_game_status[chat_id]:
        group_game_status[chat_id] = {
            'is_game_started2': False,
            'joker_player': None
        }
    if not group_game_status[chat_id]['is_game_started2']:
        group_game_status[chat_id]['is_game_started2'] = True
        group_game_status[chat_id]['joker_player'] = None
        correct_answer = random.randint(1, 6)
        await event.edit(f"**اول من يرسل كلمة (انا) سيشارك في لعبة المحيبس\nملاحظة : لفتح العضمة ارسل طك ورقم العضمة لأخذ المحبس أرسل جيب ورقم العضمة**")

@l313l.ar_cmd(pattern="محيبس")
async def restart_game(event):
    global group_game_status
    chat_id = event.chat_id
    if chat_id in group_game_status:
        group_game_status[chat_id]['is_game_started2'] = False
    await handle_clue(event)

@l313l.on(events.NewMessage(pattern=r'\طك (\d+)'))
async def handle_strike(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id in group_game_status and group_game_status[chat_id]['is_game_started2'] and event.sender_id == group_game_status[chat_id]['joker_player']:
        strike_position = int(event.pattern_match.group(1))
        if strike_position == correct_answer:
            game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
            await event.reply(f"** خسرت شبيك مستعجل وجه الچوب 😒\n{format_board(game_board, numbers_board)}**")
            game_board = [row[:] for row in original_game_board]
            group_game_status[chat_id]['is_game_started2'] = False
            group_game_status[chat_id]['joker_player'] = None
        else:
            game_board[0][strike_position - 1] = '🖐️'
            lMl10l = random.choice(joker)
            await event.reply(f"**{lMl10l}**\n{format_board(game_board, numbers_board)}")

@l313l.on(events.NewMessage(pattern=r'\جيب (\d+)'))
async def handle_guess(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id in group_game_status and group_game_status[chat_id]['is_game_started2'] and event.sender_id == group_game_status[chat_id]['joker_player']:
        guess = int(event.pattern_match.group(1))
        if 1 <= guess <= 6:
            if guess == correct_answer:
                winner_id = event.sender_id
                if winner_id not in points:
                    points[winner_id] = 0
                points[winner_id] += 1
                sender = await event.get_sender()
                sender_first_name = sender.first_name if sender else 'مجهول'
                sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)
                points_text = '\n'.join([f'{i+1}• {(await l313l.get_entity(participant_id)).first_name}: {participant_points}' for i, (participant_id, participant_points) in enumerate(sorted_points)])
                game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
                await l313l.send_message(event.chat_id, f'الف مبروووك 🎉 الاعب ( {sender_first_name} ) وجد المحبس 💍!\n{format_board(game_board, numbers_board)}')
                game_board = [row[:] for row in original_game_board]
                await l313l.send_message(event.chat_id, f'نقاط الاعب : {points[winner_id]}\nنقاط المشاركين:\n{points_text}')
            else:
                game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
                await event.reply(f"**ضاع البات ماضن بعد تلگونة ☹️\n{format_board(game_board, numbers_board)}**")
                game_board = [row[:] for row in original_game_board]
            group_game_status[chat_id]['is_game_started2'] = False
            group_game_status[chat_id]['joker_player'] = None

@l313l.on(events.NewMessage(pattern=r'\انا'))
async def handle_incoming_message(event):
    global group_game_status
    chat_id = event.chat_id
    bot_entity = await event.get_input_chat()
    if chat_id not in group_game_status:
        group_game_status[chat_id] = {
            'is_game_started2': False,
            'joker_player': None
        }
    if group_game_status[chat_id]['is_game_started2'] and not group_game_status[chat_id]['joker_player']:
        group_game_status[chat_id]['joker_player'] = event.sender_id
        await event.reply(f"**تم تسجيلك في المسابقة روح لحسين بظهرك\n{format_board(game_board, numbers_board)}**")
def format_board(game_board, numbers_board):
    formatted_board = ""
    formatted_board += " ".join(numbers_board[0]) + "\n"
    formatted_board += " ".join(game_board[0]) + "\n"
    return formatted_board


@l313l.on(events.NewMessage(pattern=r'.ستوري'))
async def aljoker(joker):
    A = 0
    await joker.edit('**᯽︙ يتم الان تنزيل ستوريات المستخدم الاخيرة وإرسالها الى الرسائل المحفوظة**')
    match = re.match(r'.ستوري (.+)$', joker.text)
    if match:
        Mes = match.group(1).strip()
        if Mes.isdigit():
            Mesg = int(Mes)
        else:
            Mesg = Mes
        
        try:
            story = await l313l(functions.stories.GetPeerStoriesRequest(Mesg))
            if not story.stories.stories:
                await joker.edit('**᯽︙ المستخدم لم ينشر ستوري بعد** ')
            else:
                for StoRy in story.stories.stories:
                    A += 1
                    S = await l313l.download_media(StoRy.media)
                    await l313l.send_file('me', file=S, caption=f'**᯽︙ سورس الجوكر 🤡 .. {A} **')
        except Exception as e:
            await joker.edit(f'**᯽︙ حدث خطأ: {str(e)}**')
    else:
        await joker.edit('**᯽︙ لم يتم تحديد مستخدم أو معرّف بشكل صحيح**')
source_channel_id = None
destination_channel_id = None
@l313l.on(events.NewMessage(pattern=r'.ستوريات'))
async def Aljoker(joker):
    A = 0
    await joker.edit('**᯽︙ يتم الان تنزيل جميع ستوريات المستخدم وإرسالها الى الرسائل المحفوظة**')
    if match(".ستوريات (.*?)$", joker.text):
        Mes = str(joker.text).split('.ستوريات ')[1].strip()
        Number = any(char in set('1234567890') for char in str(Mes))
        if Number:
            Mesg = int(Mes)
        else:
            Mesg = Mes
        stoRy = await l313l(functions.stories.GetPinnedStoriesRequest(Mesg, offset_id=42, limit=100))
        if stoRy.count == 0:
            await joker.edit('**᯽︙ المستخدم لم يثبت ستوريات بعد**')
        else:
            for StoRy in stoRy.stories:
                A += 1
                S = await l313l.download_media(StoRy.media)
                await l313l.send_file('me', file=S, caption=f'**᯽︙ سورس الجوكر 🤡 .. {A} **')
@l313l.on(events.NewMessage(pattern=r'\.تلقائي (.+)'))
async def set_source_channel(event):
    global source_channel_id, destination_channel_id
    source_channel_input = event.pattern_match.group(1)
    if source_channel_input.startswith('@'):
        source_channel_id = source_channel_input
    elif source_channel_input.startswith('-100') and source_channel_input[4:].isdigit():
        source_channel_id = int(source_channel_input)
    else:
        match = re.match(r'https://t\.me/(.+)', source_channel_input)
        if match:
            source_channel_id = match.group(1)
        else:
            await event.reply("المعرف غير صحيح. يرجى استخدام @username أو ID أو رابط القناة.")
            return
    destination_channel_id = event.chat_id
    await event.reply(f'تم تعيين معرف القناة المصدر: {source_channel_id} وسيتم إعادة إرسال الرسائل إلى هذه القناة.')

@l313l.on(events.NewMessage)
async def forward_message(event):
    global source_channel_id, destination_channel_id
    if source_channel_id and destination_channel_id:
        source_entity = await l313l.get_entity(source_channel_id)
        if event.chat_id == source_entity.id:
            if event.text:
                await client.send_message(destination_channel_id, event.text)
            if event.media:
                await client.send_file(destination_channel_id, event.media, caption=event.message.message if event.message else '')
