# import nonebot.permission as perm
# from nonebot import on_natural_language, NLPSession
# from nonebot.helpers import context_id
#
# from utils.info import *


# @on_natural_language(only_to_me=False, permission=perm.GROUP)
# async def _(session: NLPSession):
#     bot = session.bot
#     msg = session.msg_text
#     group_ctx_id = context_id(session.ctx, mode='group')
#     if msg == '喵':
#         await bot.send_private_msg(user_id=creator, message='喵～')



# def safe(msg):
#     msgBanedList = [r'^给.*(禁言|烟上|上烟|递烟|上大烟|抽大烟|上大中华)$',
#                     r'^(烟我|认输)$'
#                     r'^(别[CQ:emoji,id=128014]复读了|你要知道我对复读的忍耐是有限度的。)$']
#     for msgBaned in msgBanedList:
#         m = re.match(msgBaned, msg)
#         if m is not None:
#             return False
#     return True

import random

def randomReply():
    randomList = \
        ['喵？',
         '我的主人Excaive最好了。',
         '你有小鱼干吗？',
         '大中华是什么？好吃吗？',
         '好想看你女装呀。',
         '你能把我收掉吗？',
         '来打ufi吧！要玩的在下面扣个0，我统计一下。']
    return random.choice(randomList)

print(randomReply())