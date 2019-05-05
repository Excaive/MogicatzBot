import nonebot
from utils.work import *


def collect_repeat_info(group, msg):
    if group not in msgDict.keys():
        msgDict[group] = {'msg': msg, 'num': 1}
    elif msg == msgDict[group]['msg']:
        num = msgDict[group]['num'] + 1
        msgDict[group] = {'msg': msg, 'num': num}
    else:
        msgDict[group] = {'msg': msg, 'num': 1}


msgDict = {}
bot = nonebot.get_bot()


@bot.on_message('group')
async def repeat(context):
    group = context['group_id']
    msg = str(context['message'])
    collect_repeat_info(group, msg)
    if msgDict[group]['num'] in [3, 6, 9]:
        information = await bot._get_group_info(group_id=group)
        if safe(msg, information):
            await bot.send(context, msg)
