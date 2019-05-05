import nonebot
from utils.work import *

bot = nonebot.get_bot()


@bot.on_message('group')
async def replace(context):
    msg = str(context['message'])
    group = context['group_id']

    msgBlank = msg.replace('\r\n', ' ')
    splitList = msgBlank.split(' ')

    if splitList[0] == '替换':
        while '' in splitList:
            splitList.remove('')

        if len(splitList) >= 4:
            if len(splitList) % 2 == 0:
                msgReplaceNum = len(splitList) - 1
            else:
                msgReplaceNum = len(splitList) - 2
            msgReplace = splitList[msgReplaceNum]

            for i in range(1, (msgReplaceNum + 1) // 2):
                msgReplace = msgReplace.replace(splitList[i * 2 - 1], splitList[i * 2])
                if len(msgReplace) > 256:
                    await bot.send(context, '好烫啊，要溢出了哦！')
                    return 0

            information = await bot._get_group_info(group_id=group)
            if not safe(msgReplace, information):
                await bot.send(context, '我们换个地方说吧，这里群管理带打火机了。')
                return 0

            await bot.send(context, msgReplace)
            return 0
