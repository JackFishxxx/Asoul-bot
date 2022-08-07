from nonebot import on_command
from nonebot.adapters import Bot, Event

qtitle = on_command("设置头衔", priority=5, block=True)

@qtitle.handle()
async def handle_first_receive(bot: Bot, event: Event):

    
    group = int(event.get_session_id().split("_")[1])
    usrid = str(event.get_user_id())
    title_usr = str(event.get_message()).split("=")[0].split("]")[0]  #
    title = str(event.get_message()).split("]")[1].strip(" ")  #

    if event.sender.role == "admin" or event.sender.role == "owner":
        print(group)
        await bot.send_group_msg(group_id=group, message="设置成功！")
        await bot.set_group_special_title(group_id=str(group), user_id=title_usr, special_title=title)

admin = on_command("设置管理", priority=5, block=True)
@admin.handle()
async def handle_first_receive(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])
    usrid = str(event.get_user_id())
    admin_usr = str(event.get_message()).split("=")[1].split("]")[0]  #
        
    await bot.send_group_msg(group_id=group, message="设置成功！")
    await bot.set_group_admin(group_id=group, user_id=admin_usr, enable=True)

notadmin = on_command("取消管理", priority=5, block=True)
@notadmin.handle()
async def handle_first_receive(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])
    usrid = str(event.get_user_id())
    admin_usr = str(event.get_message()).split("=")[1].split("]")[0]  #
        
    await bot.send_group_msg(group_id=group, message="取消成功！")
    await bot.set_group_admin(group_id=group, user_id=admin_usr, enable=False)