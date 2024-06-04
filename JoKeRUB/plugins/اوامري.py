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
                    
                    [Button.inline("( الانتحال والتقليد ) ⑤", data="TargetU")],[Button.inline("( التحميل ..) ⑥", data="DOO")],
                    
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

@l313l.tgbot.on(CallbackQuery)
@check_owner
async def _(event):
	if event.data == rb'JuSt':
		await event.answer('(•) قريبا ...',alert=True)
	elif event.data == rb'VrAt':
		Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
قائمة اوامر الفارات
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖
᯽︙ اختر احدى هذه الاوامر

- ( .جلب + اسم الفار )
-لجلب قيمة الفار إن وجد
- ( .وضع توقيت )
-بالرد على المنطقة الزمنية 
- ( .وضع رمز الاسم )
- بالرد على الرمز المراد وضعه 
- ( .وضع الكروب )
- بالرد على اسم الكروب الذي تريد وضعهُ 
- ( .وضع البايو )
- بالرد على النبذا المراد وضعها 
 -( .وضع لون وقتي )
- بالرد على اسم اللون بالانجليزي 
- ( .وضع الصورة )
- بالرد على رابط تليجراف الصورة المراد وضعها وكتابة الامر 
- ( .وضع صورة الكروب )
- بالرد على رابط تليجراف الصورة المراد وضعها وكتابة الامر 
- ( .وضع زخرفة الارقام )
- بالرد على الارقام المراد وضعها وكتابة الامر 
- ( .وضع اسم )
- بالرد على الاسم المراد وضعه وكتابة الامر
- ( .وضع كروب التخزين )
- بالرد على الايدي المحادثة المراد جعلها كروب التخزين 
- ( .وضع كروب الحفظ )
-بالرد على الايدي المحادثة المراد جعلها كروب الحفظ 
- ( .وقت العراق )
- لوضع الساعة بتوقيت العراق 
- ( .وقت السعودية )
 - لوضع الساعة بتوقيت السعودية 
- ( .وقت مصر )
 -لوضع الساعة بتوقيت مصر 
- ( .وقت الاردن )
- لوضع الساعة بتوقيت الاردن 
- ( .وقت اليمن )
- لوضع الساعة بتوقيت اليمن 
- ( .وقت سوريا )
- لوضع الساعة بتوقيت سوريا
- تنويه : عندما تريد حذف الفار استعمل الامر (محو) بدل كلمة (وضع)

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖
⌔︙CH : @jepthon
''', buttons=Home)
	elif event.data == rb'Var':
		Home = [[Button.inline('( التخصيص )',data='JuSt'),Button.inline('( الفارات )',data='VrAt')],
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
قائمة التخصيص والفارات :
 ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( .اوامر التخصيص )
 لتغير الصور والكلايش كل من الحماية والفحص والبنك
- ( .اوامر الفارات )
 - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=Home)
	elif event.data == rb'DelT':
		Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر المسـح
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ اختر احدى هذه الاوامر

- ( .مسح  + بالرد على النص )
فقط اكتب الامر بالرد على الرسالة ليقوم بحذفها 

- ( .حذف رسائلي )
اكتب الامر في اي مكان وسيقوم بحذف جميع رسائلك في الدردشه حتى لو لم يكن لديك صلاحيات 

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
	elif event.data == rb'ClR':
		Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر التنظيـف
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر

- ( .تنظيف + عدد الرسائل )
يقوم بحذف الرسائل اكتب الامر وعدد معين من الرسائل سيقوم بحذفها 

- ( .تنظيف  + الاضافة )
 يـجب وضع الشـارحه مع الاضافة (-)
مثـال  :  ( .تنظيف -ح )  <سيقوم بحذف المتحركات في الدردشة>
الاضافات : 
 (-ب) : لحـذف الرسائل الـصوتية
 (-م): لحـذف الملفات
 (-ح): لحـذف المتحـركه
 (-ص): لحـذف الـصور
 (-غ): لحـذف الاغاني
 (-ق): لحـذف الـملصقات
 (-ر): لحـذف الـروابط 
(-ف): لحـذف الفـيديوهـات

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
	elif event.data == rb'Spam':
		Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر السبـام
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ اختر احدى هذه الاوامر

- ( .سبام + كلمـة )
يقوم بتفصيخ احرف الكلمه وارسالها جربه بنفسك

- ( .وسبام + كلـمة )
كتابة الامر مع نص معين يقوم بتفصيخ الجمله كلمه كلمه وارسالها

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
	elif event.data == rb'Agi':
		Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر التـكرار

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ اختر احدى هذه الاوامر

- ( .كرر  +عدد التكرار  +بالرد على الرسالة )
 يقوم بتكرار النصوص والوسائط بالرد على الرسالة او الصورة 
مثال  :  ( بالرد على صورة  .كرر 10 )

- ( .تكرار الملصق + بالرد على ملصق )
 بالرد على الملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها

- (.مكرر  + وقت بالدقائق  + عدد  + بالرد )
 بالرد على نص او صورة او اي شي يقوم بالتكرار  مع وقت معين .
مثال  : بالـرد على نص ( .مكرر 10 2 )  عندها سترسل 10 رسائل نصية ( النص الي رديت عليه ) بفاصل ثانيتين بين كل رسالة

- ( .ضع تكرار + العدد )
لمنع التكرار بالمجموعة الخاصة بك بالعدد الذي وضعته للعودة للوضع الطبيعي ضع 999999.
مثال : ( .ضع تكرار 10 )

- ( .ايقاف التكرار` )
لأيقاف جميع التكرار ومن بينهم النشر التلقائي

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
	elif event.data == rb'Clear':
		Home = [
    [
     Button.inline("( التكرار )", data="Agi"),Button.inline('( السبام )',data='Spam')],[Button.inline('( التنظيف )',data='ClR'),Button.inline('( المسح )',data='DelT')],[Button.inline('( القائمة الرئيسيه )',data='Home')]];await event.edit('''
قائمة اوامر التكرار والتنظيف :
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( .اوامر التكرار )
- ( .اوامر السبام )
- ( .اوامر التنظيف ) 
- ( .اوامر المسح ) 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=Home)
	elif event.data == rb'NOT':
		Home = [
    [
     Button.inline("( القفل )", data="Lock"),Button.inline('( الفتح )',data='OpeNed0')],[Button.inline('( المنع )',data='Not0')],Button.inline('( القائمة الرئيسيه )',data='Home')];await event.edit('''
قائمة اوامر القفل والمنع :
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( .اوامر القفل )
- ( .اوامر الفتح )
- ( .اوامر المنع ) 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
⌔︙CH : @jepthon
''', buttons=Home)
	elif event.data == rb'Lock':
		Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر القـفـل 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .قفل + الاضافة ) 
 تكتب الامر مع الاضافة لقفل شي معين في المجموعة 

الاضافات  : 
 - الدردشه  : لقفل ارسال الرسائل 
- الوسائط   : لقفل ارسال الوسائط
 - الملصقات  : لقفل ارسال الملصقات
- الروابط  : لقفل ارسال الروابط
- المتحركه  : لقفل ارسال المتحركه
- الالعاب  : لقفل ارسال الالعاب الانلاين
- الانلاين  : لقفل ارسال البوتات الانلاين
- التصويت  : لقفل ارسال التوصيتات 
- الكل :  لقفل ارسال كل شي

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
	elif event.data == rb'OpeNed0':
		Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر الفـتـح 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .فتح + الاضافة ) 
 تكتب الامر مع الاضافة لفتـح شي معين في المجموعة 

الاضافات  : 
 - الدردشه  : لفتح ارسال الرسائل 
- الوسائط   : لفتح ارسال الوسائط
 - الملصقات  : لفتح ارسال الملصقات
- الروابط  : لفتح ارسال الروابط
- المتحركه  : لفتح ارسال المتحركه
- الالعاب  : لفتح ارسال الالعاب الانلاين
- الانلاين  : لفتح ارسال البوتات الانلاين
- التصويت  : لفتح ارسال التوصيتات 
- الكل :  لفتح ارسال كل شي

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
	elif event.data == rb'Not0':
		Home = [
    [
     Button.inline("( القائمة الرئيسية )", data="Home")]];await event.edit('''
شـرح عـن اوامـر الـمنـع 
★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه الاوامر 

- ( .منع + الكلمة ) 
 لمـنع الـكلمة في الـدردشة وسيتم حذفها عند ارسالها من اي شخص 

- ( .الغاء منع + الكلمة ) 
 لالغاء منع الكلمة والسماح للجميع بأرسالها في الدردشة

- ( .قائمة المنع ) 
لاظهـار قائمه الكـلمات الـتي منعـتها في الـدردشـه 

★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
᯽︙ CH : @jepthon
''', buttons=Home)
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

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Do2")))
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
                    
                    [Button.inline("( الانتحال والتقليد ) ⑤", data="TargetU")],[Button.inline("( التحميل ..) ⑥", data="DOO")],
                    
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

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'DOO')))
@check_owner
async def _(event):
	Home = [
    [
     Button.inline("( النطق )", data="Ntk"),Button.inline('( التحميل )',data='Do2')]
     ,[Button.inline('( الترجمة )',data='Trans')],[Button.inline('( القائمة الرئيسيه )',data='Home')]];await event.edit('''
قائمة اوامر التحميل والترجمه :
 ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★
 ᯽︙ اختر احدى هذه القوائم

- ( .اوامر النطق )
- ( .اوامر التحميل )
- ( .اوامر الترجمة ) 
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

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Group2")))
@check_owner
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

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb'Groups')))
@check_owner
async def _(event):
    Gr = [
    [
     Button.inline("( التفليش )", data="Bom"),
     Button.inline("( المحذوفين )", data="Deleted")],[Button.inline("( الكروب )",data='Group2')],[Button.inline("( القائمة الرئيسيه )",data='Home')]]
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
