import nonebot
import random

bot = nonebot.get_bot()


@bot.on_message('group')
async def g24_group(context):
    msg = str(context['message'])
    if msg == '分组':
        noters = ['AGhost', 'bar2ianerman', '晨', '叉叉', 'DSCH',
                  'EDTA', 'EggJuan', 'Excaive', '古手梨花', 'guvle',
                  'Hara', 'HMillion', '幻月', 'Laplaze', '保登心愛',
                  'ShadowNier', '洞洞', 'SaturnKiller', 'Sevicy', '斯诺格',
                  'Snowy', 'sιgmα', 'Trarizon', 'World Rejecter', '小耳朵',
                  '小咩兔', '宇夜', 'Likey']
        msgGroup = ''
        for groupNum in range(1, 11):
            noterNum = 3 if groupNum in range(1, 9) else 2
            group = random.sample(noters, noterNum)
            noters = [i for i in noters if i not in group]
            msgGroup = msgGroup + 'group%d: %s\n' % (groupNum, str(group))
        msgGroup = msgGroup[:-1]
        await bot.send(context, msgGroup)
        