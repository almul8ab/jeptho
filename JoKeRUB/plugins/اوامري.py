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


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Ntk")))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر الـنطق 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .تكلم ar ) 
 بالرد على النص لتحويله الى مقطع صوتي للغة  يه 

- ( .تكلم en ) 
 بالرد على النص لتحوليه الى مقطع صوتي للغه الانكليزية

- ( .احجي ar ) 
 بالرد على مقطع صوتي او بصمة لتحوليه الى نص للغه  ية

- ( .احجي en ) 
 بالرد على مقطع صوتي او بصمة لتحوليه الى نص للغه الانكليزية

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Down")))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن امـر التحمـيل
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر

- (.بحث + اسم الاغنية)
بكتابة اسم الاغنية مع الامر لارسال الاغنيه مباشرا واذا ما اشتغل جرب اوامر التحميل الاخرى
- مثـال : .بحث ماهر زين

- (.يوت + اسم الفيديو او الاغنية)
كتابة الامر مع اسم الفيديو او الاغنية ليعطيك نتائج البحث وروابط من يوتيوب تستخدم مع اوامر التحميل
- مثـال : .يوت ماهر زين

- (.تحميل ص + رابط الاغنية)
لتحميل اغنيه من خلال وضع الرابط مع الامر
- مثـال : .تحميل ص https://youtube.com/...

- (.فيديو + اسم الاغنية)
كتابة الامر مع اسم المقطع لتحميله وارساله
- مثـال : .فيديو باسم الكربلائي

- (.انستا + الرابط )
يستخدم هذا الامر لتحميل من الانستا فقط اكتب الامر مع رابط الفيديو ليحمله
- مثـال : .انستا https://instagram.com/jdisjejjd...

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Trans")))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر الترجمة 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .ترجمة ar ) 

 بالرد على النص لترجمته للغه  ية

- ( .ترجمة en ) 
 بالرد على النص لترجمته للغه الانكليزية

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Download")))
@check_owner
async def _(event):
	Home = [
    [
     Button.inline("( النطق )", data="Ntk"),Button.inline('( التحميل )',data='Down')],Button.inline('( الترجمة )',data='Trans')];await event.edit('''
قائمة اوامر التحميل والترجمه :
 ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( .اوامر النطق )
- ( .اوامر التحميل )
- ( .اوامر الترجمة ) 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=Home)

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

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Telegraph')))
@check_owner
async def _(event):
	Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر التلكراف 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .تلكراف ميديا ) 

 لاستخراج رابط من الصورة على شكل رابط تلكراف  

- ( .تلكراف نص ) 
 بالرد على النص او المقالة لصنع رابط تلكراف للنص

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Sec1")))
@check_owner
async def _(event):
	Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر الـخاص 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .الحماية تشغيل/تعطيل ) 
 لتشغيل امر الحمايه او تعطيله في الـخاص 

- ( .سماح ) 
 بالرد على الشخص للسماح له بالتكلم في الخاص

- ( .رفض ) 
 بالرد على الشخص لرفضه من الخاص 

- ( .المسموح لهم )
 فقط ارسل الامر لاظهار الاشخاص المسموح لهم والمرفوضين

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Securty")))
@check_owner
async def _(event):
	Home = [[Button.inline('( الحماية )',data='Sec1'),Button.inline('( التلكراف )',data='Telegraph')],
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
قائمة اوامر حـماية الخاص والتلكراف :
 ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( .اوامر الحماية )
- ( .اوامر التلكراف ) 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=Home)

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

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Group')))
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


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"TargetU")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("( الانتحال )", data="TarU"),
     Button.inline("( التقليد )", data="LikU")],[Button.inline('( المنشن )',data='mention')],[Button.inline('( القائمة الرئيسة )',data='Home')]]
    
    await event.edit('''
قائمة اوامر الـمنشن والانتحال :
 ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( .اوامر الانتحال )
- ( .اوامر التقليد )
- ( .اوامر المنشن ) 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"TarU")))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر الانتحال 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .انتحال ) 

 بالرد على الشخص لنسخ حسابه بالكامل من صورة واسم وبايو  

- ( .اعادة ) 
 لارجاع الحساب الى وضعه الطبيعي لما كان سابقا

- ( .انتحال_الدردشه ) 
 قم بكتابة الامر مع معرف المجموعة او القناة بدون @

- ( .اعادة_الدردشه ) 
 لارجاع الدردشه الى وضعه الطبيعي لما كان سابقا

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"LikU")))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر الـتقليـد 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .تقليد ) 
 بالرد على الشخص لتقليد جميع رسائله في الدردشه 

- ( .الغاء التقليد ) 
 بالرد على الشخص لايقاف التقليد

- ( .المقلدهم ) 
لاظهـار قائمه الاشخاص الذي فعـلت عليهم امر التقليد ولمسحهم ارسل  (.مسح المقلدهم) 

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'mention')))
@check_owner
async def _(event):
    Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر الـمنشن 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- (.منشن + المسج)
قم بكتابة الامر في المجموعة لعمل تاك مفرد للاعظاء الموجودين
- (.الغاء منشن)
لألغاء التاك 

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
