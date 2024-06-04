import re

from telethon import Button, events
from telethon.events import CallbackQuery

from l313l.razan.resources.assistant import *
from l313l.razan.resources.mybot import *
from JoKeRUB import l313l
from ..core import check_owner
from ..Config import Config

JEP_IC = "https://telegra.ph/file/762989c65df81fc2e96d7.jpg"
ROE = "**♰ هـذه هي قائمة اوامـر سـورس الجوكر ♰**"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("اوامري") and event.query.user_id == bot.uid:
            buttons = [
                [Button.inline("( اوامر الادمن  ) ① ", data="Admin")],
                
                    [Button.inline("( المجموعات ) ②", data="Groups"),
                    Button.inline("( الترحيب .. ) ③", data="Tarh"),
                    Button.inline("( الحمايه .. ) ④", data="Securty")],
                    
                    [Button.inline("( الانتحال والتقليد ) ⑤", data="Target")],[Button.inline("( التحميل ..) ⑥", data="Download")],
                    
                [Button.inline("( المنع .. ) ⑦", data="NOT"),
                    Button.inline("( التنظيف .. ) ⑧", data="Clear")],
                    [Button.inline("( الفارات ) ⑨", data="Var")],
                [Button.inline("( الوقتي ..) ⓪①", data="Timer"),
                    Button.inline("( الكشف و ..) ①① )", data="Open")],
                [Button.inline("( المساعده ) ②① ", data="Helper")],
              [Button.inline("( أذكار .. ) ③①", data="Think"),
                    Button.inline("( الملصقات ) ④①", data="Sticker")],
                [Button.inline("( التسليه ميمز ) ⑤①", data="FunY")],
                [
                    Button.inline("( الصيغ ..) ⑥①", data="Contect"),
                    Button.inline(" ( التمبلر ..) ⑦①", data="Tumbler")],[Button.inline("(  الحساب ) ⑧①", data="Account")]
                    ,[Button.inline("( ميوزك ) ⑨①", data="Music"),Button.inline("( بصمات ) ⓪②", data="Voice")],[Button.inline("( التجميع ) ①②", data="r7brz")]
                    ,[Button.inline("( اوامر البوت )", data="rozbot")]
            ]
            if JEP_IC and JEP_IC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    JEP_IC, text=ROE, buttons=buttons
                )
            elif JEP_IC:
                result = builder.document(
                    JEP_IC,
                    title="JoKeRUB",
                    text=ROE,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="JoKeRUB",
                    text=ROE,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="اوامري"))
async def repo(event):
    if event.fwd_from:
        return
    lMl10l = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(lMl10l, "اوامري")
    await response[0].click(event.chat_id)
    await event.delete()


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"l313l0")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("( التالي )", data="jrzst"),
      Button.inline("القائمة الرئيسية", data="ROE"),]]
    await event.edit(ROZADM, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"jrzst")))
@check_owner
async def _(event):
    butze = [
    [
     Button.inline("( التالي )", data="tslrzj"),
     Button.inline("( رجوع )", data="l313l0")]]
    await event.edit(GRTSTI, buttons=butze)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"tslrzj")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( التالي )", data="krrznd"),
     Button.inline("( رجوع )", data="jrzst")]]
    await event.edit(JMAN, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"krrznd")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("( التالي )", data="rozbot"),
      Button.inline("( رجوع )", data="tslrzj")]]
    await event.edit(TKPRZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rozbot")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( التالي )", data="Jmrz"),
     Button.inline("( رجوع )", data="krrznd")]]
    await event.edit(ROZBOT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Jmrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( التالي )", data="r7brz"),
     Button.inline("( رجوع )", data="rozbot")]]
    await event.edit(JROZT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"r7brz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( التالي )", data="sejrz"),
     Button.inline("( رجوع )", data="Jmrz")]]
    await event.edit(JMTRD, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"sejrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( التالي )", data="gro"),
     Button.inline("( رجوع )", data="r7brz")]]
    await event.edit(ROZSEG, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"gro")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( التالي )", data="grrz"),
     Button.inline("( رجوع )", data="sejrz")]]
    await event.edit(JMGR1,buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"grrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( التالي )", data="iiers"),
     Button.inline("( رجوع )", data="gro")]]
    await event.edit(ROZPRV, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"iiers")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( التالي )", data="rfhrz"),
     Button.inline("( رجوع )", data="grrz")]]
    await event.edit(HERP, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rfhrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( التالي )", data="uscuxrz"),
     Button.inline("( رجوع )", data="iiers")]]
    await event.edit(T7SHIZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"uscuxrz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("( رجوع )", data="l313l0"),]]
    await event.edit(CLORN, buttons=buttons)
