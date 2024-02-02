# Reda - Hussein
# © JoKeRUB Team 2023
# ها شعدك داخل ع الملف تريد تخمط ؟ ابو زربة لهل درجة فاشل
import pytz
from datetime import datetime
from telethon import events
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete
from telethon import functions
from telethon.errors.rpcerrorlist import MessageIdInvalidError
@l313l.on(admin_cmd(pattern="(خط الغامق|خط غامق)"))
async def btext(event):
    isbold = gvarstatus("bold")
    if not isbold:
        addgvar ("bold", "on")
        await edit_delete(event, "**᯽︙ تم تفعيل خط الغامق بنجاح ✓**")
        return

    if isbold:
        delgvar("bold")
        await edit_delete(event, "**᯽︙ تم اطفاء خط الغامق بنجاح ✓ **")
        return

@l313l.on(admin_cmd(pattern="(خط المشطوب|خط مشطوب)"))
async def btext(event):
    istshwesh = gvarstatus("tshwesh")
    if not istshwesh:
        addgvar ("tshwesh", "on")
        await edit_delete(event, "**᯽︙ تم تفعيل خط المشطوب بنجاح ✓**")
        return

    if istshwesh:
        delgvar("tshwesh")
        await edit_delete(event, "**᯽︙ تم اطفاء خط المشطوب بنجاح ✓ **")
        return

@l313l.on(admin_cmd(pattern="(خط رمز|خط الرمز)"))
async def btext(event):
    isramz = gvarstatus("ramz")
    if not isramz:
        addgvar ("ramz", "on")
        await edit_delete(event, "**᯽︙ تم تفعيل خط الرمز بنجاح ✓**")
        return

    if isramz:
        delgvar("ramz")
        await edit_delete(event, "**᯽︙ تم اطفاء خط الرمز بنجاح ✓ **")
        return
        
@l313l.on(admin_cmd(pattern="(رسالة وقتية|رساله وقتية|رسالة وقتية|رساله وقتيه)"))
async def btext(event):
    istw8et = gvarstatus("tw8et")
    if not istw8et:
        addgvar ("tw8et", "on")
        await edit_delete(event, "**᯽︙ تم تفعيل الرسالة الوقتية بنجاح ✓**")
        return

    if istw8et:
        delgvar("tw8et")
        await edit_delete(event, "**᯽︙ تم اطفاء الرسالة الوقتية بنجاح ✓ **")
        return
        
@l313l.on(events.NewMessage(outgoing=True))
async def reda(event):
    if event.message.text and not event.message.media and "." not in event.message.text:
        isbold = gvarstatus("bold")
        isramz = gvarstatus("ramz")
        istshwesh = gvarstatus("tshwesh")
        istw8et = gvarstatus("tw8et")
        time_zone = pytz.timezone('Asia/Baghdad')
        current_time = datetime.now(time_zone).strftime('%I:%M')
        if isbold:
            try:
                await event.edit(f"**{event.message.text}**")
            except MessageIdInvalidError:
                pass
        if isramz:
            try:
                await event.edit(f"`{event.message.text}`")
            except MessageIdInvalidError:
                pass
        if istshwesh:
            try:
                await event.edit(f"~~{event.message.text}~~")
            except MessageIdInvalidError:
                pass
        if istw8et:
            try:
                await event.edit(f"{event.message.text}\n\n- **{current_time}**")
            except MessageIdInvalidError:
                pass
