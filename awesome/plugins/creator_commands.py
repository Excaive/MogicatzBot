import nonebot
from utils.work import *

bot = nonebot.get_bot()


@bot.on_message('private')
async def forward(context):
    if context['user_id'] == creator:
        msg = str(context['message'])
        splitList = msg.split(' ', 1)
        msgForwardSucceed = '已经帮你转发过去了喵~'
        msgForward = splitList[1]

        msgForward = msgForward.replace('/c', at(cat))
        msgForward = msgForward.replace('/e', at(creator))
        msgForward = msgForward.replace('/b', at(beryl))
        msgForward = msgForward.replace('/m', at(marigold))
        msgForward = msgForward.replace('/t', at(tairitsu))
        msgForward = msgForward.replace('//', '/')

        if splitList[0] == '猫群':
            await bot.send_group_msg(group_id=catRoom, message=str(msgForward))
            await bot.send(context, msgForwardSucceed)
        elif splitList[0] == '烟群':
            await bot.send_group_msg(group_id=debugRoom, message=str(msgForward))
            await bot.send(context, msgForwardSucceed)


@bot.on_message('private')
async def test(context):
    if context['user_id'] == creator:
        msg = str(context['message'])

        if msg == '喵':
            await bot.send(context, '喵')
        elif msg == 'at':
            await bot.send_group_msg(group_id=catRoom, message='haha %s' % at(creator))
        elif msg == '信息':
            information = await bot._get_group_info(group_id=debugRoom)
            await bot.send(context, str(information))
        elif msg == '下棋':
            board = \
'''　ＡＢＣＤＥＦＧＨ　
１□□□□□□□□１
２□□□□□□□□２
３□□□□□□□□３
４□□□◎●□□□４
５□□□●◎□□□５
６□□□□□□□□６
７□□□□□□□□７
８□□□□□□□□８
　ＡＢＣＤＥＦＧＨ　
◈ [● 50]         ◎ 14  ◈'''
            await bot.send_group_msg(group_id=catRoom, message=board)
