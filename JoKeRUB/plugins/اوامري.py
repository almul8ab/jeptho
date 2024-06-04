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
                    ,[Button.inline("( ميوزك ) ⑨①", data="Music"),Button.inline("( بصمات ) ⓪②", data="Voice")],[Button.inline("( التجميع ) ②①", data="r7brz")]
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

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Home")))
@check_owner
async def _(event):
	Home = [
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
                    ,[Button.inline("( ميوزك ) ⑨①", data="Music"),Button.inline("( بصمات ) ⓪②", data="Voice")],[Button.inline("( التجميع ) ②①", data="r7brz")]
                    ,[Button.inline("( اوامر البوت )", data="rozbot")]
            ]
	await event.edit(ROE, buttons=Home)
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Admin")))
@check_owner
async def _(event):
    buttons = [
    [Button.inline("( الحظر )",data='Block'),Button.inline('( الكتم )',data='Mute')],[Button.inline('( التثبيت )',data='Pin'),Button.inline('( الاشراف )',data='Admins')],
      [Button.inline("( القائمة الرئيسيه )", data="Home")]
      ]
    await event.edit('''
قائمة اوامر الادمن لسورس الجوكر :
 ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( `.اوامر الحظر` )
- ( `.اوامر الكتم` )
- ( `.اوامر التثبيت` )
- ( `.اوامر الاشراف` )
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Block')))
@check_owner
async def _(event):
    butze = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]]
    await event.edit('''
 شـرح عـن اوامـر الحـظر 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

( .حظر ) 
-  تقوم بالرد على شخص او وضع معرفه مع الامر وسيحظره من المجموعة

( .الغاء حظر )
 - بالرد على الشخص او كتابة معرفه مع الامر لالغاء حظره
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
 ''', buttons=butze)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Mute')))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]]
    await event.edit('''
شـرح عـن اوامـر الكـتم 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

( .كتم ) 
-  تقوم بالرد على شخص او وضع معرفه مع الامر وسيكتمه من المجموعة

( .الغاء كتم )
 - بالرد على الشخص او كتابة معرفه مع الامر لالغاء كتمه

( .كتم_مؤقت+عدد الساعات او الدقائق+السبب )
 - بالرد على الشخص او كتابة معرفه مع الامر لتقيدة من المجموعة مؤقتا
مثال : كتم_مؤقت 1h مخالف القوانين
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=Home)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Admins')))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]]
    await event.edit('''
شـرح عـن اوامـر الاشراف 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

( .رفع مشرف ) 
-  تقوم بالرد على الشخص مع الامر و سيرفع مشرفا في المجموعة

( .تك )
 - بالرد على الشخص مع الامر لإنزاله من الاشراف في المجموعة

( .ارفع ) 
- لرفع المستخدم في جميع المجموعات مع كافة الصلاحيات مع لقب مخفي

( .نزل ) 
-لتنزيل الشخص من رتبة الاشراف في جميع المجموعات
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖
⌔︙CH : @jepthon
    ''', buttons=Home)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Pin')))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]]
    await event.edit('''
شـرح عـن اوامـر التثبيت 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

( .تثبيت ) 
-  تقوم بالرد على الرسالة مع الامر وستثبت في المجموعة

( .الغاء التثبيت )
 - بالرد على الرسالة مع الامر لإلغاء تثبيتها
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=Home)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Groups')))
@check_owner
async def _(event):
    Gr = [
    [
     Button.inline("( التفليش )", data="Bom"),
     Button.inline("( المحذوفين )", data="Deleted")],[Button.inline("( المجموعه )",data='Group')],[Button.inline("( القائمة الرئيسيه )",data='Home')]]
    await event.edit('''
قائمة اوامر المجـموعه لسورس الجوكر :
 ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( .اوامر التفليش )
- ( .اوامر المحذوفين )
- ( .اوامر الكروب )
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=Gr)
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Deleted')))
async def _(event):
	Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر الكروب 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .الاحداث ) 
 كتابة  الامـر في الكروب لعرض احداث الكروب

- ( .الاعضاء ) 
 فقـط ارسل الامر في المجموعة لعرض اعضاء المجموعة

- ( .المشرفين ) 
 ارسل الامر في المجموعه لعرض حسابات المشرفين

- ( .البوتات )
 ارسل الامر في المجموعه لعرض البوتات

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
     
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Deleted')))
async def _(event):
	Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر المـحذوفين 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .حذف المحظورين ) 
 كتابة  الامـر في الكروب لالغاء حظر جميع الاعضاء 

- ( .اطردني ) 
 فقـط ارسل الامر في المجموعة لمغادرة المجموعه التي تم ارسال الامر فيها

- ( .المحذوفين ) 
 لعرض الحسابات المحذوفة في مجمـوعة معيـنة ولحذفهم ارسل .المحذوفين اطردهم

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Bom')))
async def _(event):
	Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر التفليـش 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .تفليش بالطرد ) 
 ارسل  الامـر لطرد جميع الاعضاء من المجموعه 

- ( .تفليش ) 
 كتابة  الامـر فقط في المجموعه لحظر جميع الاعضاء

- ( .حظر_الكل ) 
 كتابة  الامـر فقط في المجموعه لحظر جميع الاعضاء بدون صلاحيات عن طريق بوت الحماية 

- ( .طرد_الكل ) 
 كتابة  الامـر فقط في المجموعه ليقوم بطرد جميع الاعضا بدون صلاحيات عن طريق بوت الحماية 

- ( .كتم_الكل ) 
 كتابة  الامـر فقط في المجموعه ليقوم بكتم جميع الاعضاء بدون صلاحيات اشراف عن طريق بوت الحماية

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Tarh")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( الترحيب )", data="Trh"),
     Button.inline("( الردود )", data="Reply")],[Button.inline('( القائمة الرئيسيه )',data='Home')]]
    await event.edit('''
قائمة اوامر الـترحيب والـردود :
 ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( .اوامر الترحيب )
- ( .اوامر الردود )
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Trh")))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]]
    await event.edit('''
شـرح عـن اوامـر الترحيب 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

--( .ترحيب + ترحيبك )
 اكتب الامر مع ترحيب في المجموعه ليرحب بالاعضاء الجدد

- ( .حذف الترحيب ) 
 فقـط ارسل الامر في المجموعة لحذف الترحيبات

- ( .الترحيب )
 ارسل الامر في المجموعه لعرض ترحيبات المجموعة

- ( .الترحيب السابق ايقاف/تشغيل )
 لتعطيل اخر ترحيب وضعته في المجموعة او تشغيل

- ( .رحب + ترحيبك )
 لوضع ترحيب في عند دخول الاعضاء للمجموعة سوف يرحب بهم في الخاص

- ( .حذف رحب )
 لحذف الترحيب في الخاص
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Reply")))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]]
    await event.edit('''
شـرح عـن اوامـر الـردود 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .رد + ردك ) 

 لوضع رد معين في المجموعة اكتب الامر وردك

- ( .حذف الردود ) 
 فقـط ارسل الامر في المجموعة لحذف الردود المضافة

- ( .الردود ) 
 ارسل الامر في المجموعه لعرض ردود المجموعة

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''',buttons=Home)


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
