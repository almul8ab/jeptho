import asyncio
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon import events

Aljoker_Asbo3 = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}

Hussein = False

async def main(api_id, api_hash, phone_number):
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            code = input('Enter the code: ')
            await client.sign_in(phone_number, code)

@client.on(events.NewMessage(pattern='.الذاتية تشغيل'))
async def reda(event):
    if Hussein = True
        return await edit_delete(event, "**᯽︙حفظ الذاتيات مفعل وليس بحاجة للتفعيل مجدداً **")
    else:
        Hussein = True
        await edit_delete(event, "**᯽︙تم تفعيل ميزة حفظ الذاتيات بنجاح ✓**")
 
@client.on(events.NewMessage(pattern='.الذاتية تعطيل'))
async def Reda_Is_Here(event):   
        Hussein = False
        return await edit_delete(event, "**᯽︙تم تعطيل حفظت الذاتيات بنجاح ✓**")
    else:
        await edit_delete(event, "**᯽︙انت لم تفعل حفظ الذاتيات لتعطيلها!**")

def joker_unread_media(message):
    return message.media_unread and (message.photo or message.video)

async def Hussein(event, caption):
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    lMl10l_date = event.date.strftime("%Y-%m-%d")
    lMl10l_day = Aljoker_Asbo3[event.date.strftime("%A")]
    await bot.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, lMl10l_date, lMl10l_day),
        parse_mode="markdown"
    )
    os.remove(media)

@client.on(events.NewMessage(func=lambda e: e.is_private and joker_unread_media(e) and e.sender_id != bot.uid))
async def Reda(event):
    if Hussein = True:
        caption = """**
           ♡  غير مبري الذمة اذا استعملته للأبتزاز  ♡
♡ تم حفظ الذاتية بنجاح ✓
♡ تم الصنع : @Jepthon
♡ أسم المرسل : [{0}](tg://user?id={1})
♡  تاريخ الذاتية : `{2}`
♡  أرسلت في يوم `{3}`
       ♡    ALJOKER    ♡
        **"""
        await Hussein(event, caption)

        await client.run_until_disconnected()

async def run():
    api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API Hash: ")

    await main(api_id, api_hash, phone_number)

asyncio.run(run())