import nonebot
import random
from utils.work import *

bot = nonebot.get_bot()


@bot.on_message('group')
async def replace(context):
    msg = str(context['message'])
    card = context['sender']['card']
    if (chr(8238) and chr(8237) in card) and (at(cat) not in msg):
        if random.randint(0, 19) == 0:
            suffixBegin = card.index(chr(8238)) + 1
            suffixEnd = card.index(chr(8237))
            suffix = card[suffixBegin : suffixEnd]
            suffix = suffix[::-1]
            if suffixBegin < suffixEnd:
                if len(context['message']) == 1:
                    if context['message'][0]['type'] == 'image':
                        cardNormal = card[: suffixBegin - 2]
                        msgSuffix = cardNormal + ': [图片]' + suffix
                        await bot.send(context, msgSuffix)
                    elif context['message'][0]['type'] == 'text':
                        msgSuffix = msg + suffix
                        await bot.send(context, msgSuffix)
