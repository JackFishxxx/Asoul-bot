from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

tts = on_command("说", aliases={"转语音"}, rule=to_me(), priority=5, block=True)

@tts.handle()
async def handle_first_receive(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    usrmsg = str(event.get_message())
    if usrmsg[0] == "说":
        usrmsg = usrmsg[1:]
    elif usrmsg[0] == "转":
        usrmsg = usrmsg[3:]
    group = int(event.get_session_id().split("_")[1])

    if usrmsg != "" and len(usrmsg) <= 30:
        reply = "[CQ:tts,text={}]".format(usrmsg)
    elif len(usrmsg) > 30:
        reply = "😄发这么长一串让我读是不是嫌自己的太短了啊，啥比"
    else:
        reply = "格式错误，应为：转语音/说 内容"
    
    await bot.send_group_msg(group_id=group, message=reply)
    