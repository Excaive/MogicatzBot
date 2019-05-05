import nonebot
import jieba
import random
from utils.work import *

bot = nonebot.get_bot()


def randomReply():
    randomList = \
        ['喵？',
         '我的主人Excaive最好了。',
         '你有小鱼干吗？',
         '大中华是什么？好吃吗？',
         '好想看你女装呀。',
         '你能把我收掉吗？',
         '来打ufi吧！要玩的在下面扣个0，我统计一下。',
         '夜轮大大简直是天使！啊啊啊啊激动到跑圈！！！！']
    return random.choice(randomList)


def analysis(wordSet):
    if '大吉' in wordSet or '中吉' in wordSet or '小吉' in wordSet:
        return '好的我去收歌去了\n₍₍(づ・∀・)づΩ'
    elif '吉' in wordSet:
        return '今天也可以试着收歌...'
    elif '末吉' in wordSet:
        return '我就是末吉猫（？'
    elif '凶' in wordSet or '大凶' in wordSet:
        return '对，我超凶的\nฅ^•д•^ฅ'
    elif '鸽子' in wordSet:
        return '咕咕咕'
    elif '跑圈' in wordSet:
        return '你也是跑圈人？'
    elif '玩得' in wordSet:
        return 'mp吗？'
    elif {'重复', '复读'} < wordSet:
        return '我复读会上瘾的'
    elif {'你', '女装'} < wordSet:
        return '我头像就是我的女装照哦~'
    elif {'知道', '吗'} < wordSet:
        return '知道！'
    elif {'停', '更'} < wordSet:
        return '哦，我的老伙计，这太可怕了，就像隔壁苏珊太太做的苹果派一样糟糕。'
    elif {'你', '会', '黑白棋', '吗'} < wordSet:
        return '以前会的，但最近我被[数据删除]了，所以忘记怎么下了'
    else:
        return


@bot.on_message('group')
async def be_ated(context):
    msg = str(context['message'])
    if at(cat) in msg and 'CQ:image,file=' not in msg:
        msg = msg.replace(at(cat), '')
        msg = msg.replace(' ', '')
        if 0 < len(msg) <= 256:
            words = jieba.cut(msg, cut_all=False)
            wordSet = {word for word in words}
            msgReply = analysis(wordSet)
            if msgReply:
                await bot.send(context, msgReply)
            else:
                msgReply = randomReply()
                await bot.send(context, str(wordSet)+'\n'+msgReply)
        else:
            msgReply = randomReply()
            await bot.send(context, msgReply)
