from nonebot.plugin import on_message
from nonebot.adapters import Bot, Event
from nonebot.matcher import Matcher

blacklist = on_message(priority=1, block=False)

#reject user in blacklist
@blacklist.handle()
async def handle(matcher: Matcher, event: Event, bot: Bot):
    
    usrid = str(event.get_user_id())
    
    if usrid in bot.config.blacklist:
        matcher.stop_propagation()