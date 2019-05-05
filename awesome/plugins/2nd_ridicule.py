import nonebot
import random
from utils.work import *


def collect_msg_info(group, msg, sex):
    msgDict[group] = {'msg': msg, 'sex': sex}

def ridicule(group, msg):
    if group in msgDict.keys():
        if msgDict[group]['msg'].replace('我', '你') == msg \
                or msgDict[group]['msg'].replace('我', '您') == msg:
            return True
        else:
            return False
    else:
        return False


msgDict = {}
bot = nonebot.get_bot()


@bot.on_message('group')
async def second_ridicule(context):
    msg = str(context['message'])
    if '我' in msg:
        group = context['group_id']
        sex = context['sender']['sex']
        collect_msg_info(group, msg, sex)
    elif '你' in msg or '您' in msg:
        group = context['group_id']
        if ridicule(group, msg):
            if random.randint(0, 2) == 0:
                if msgDict[group]['sex'] == 'female':
                    msg_second_ridicule = msgDict[group]['msg'].replace('我', '她')
                else:
                    msg_second_ridicule = msgDict[group]['msg'].replace('我', '他')
                await bot.send(context, msg_second_ridicule)
