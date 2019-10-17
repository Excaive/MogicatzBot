import nonebot
import urllib.request
from utils.work import *
from .ocr import recognize


def change_flag(group, msg):
    if at(cat) in msg:
        flagDict[group] = 3
    elif group in flagDict.keys():
        if flagDict[group] > 0:
            flagDict[group] = flagDict[group] - 1
    else:
        flagDict[group] = 0


bot = nonebot.get_bot()
flagDict = {}


@bot.on_message('group')
async def magicatz_ocr(context):
    group = context['group_id']
    msg = str(context['message'])
    change_flag(group, msg)

    if flagDict[group] > 0:
        searchFile = re.search(r'CQ:image,file=(.*),', msg, re.M)
        searchUrl = re.search(r'url=(.*)]', msg, re.M)
        fileAddress = r'../../../data/image/%s.cqimg' % searchFile.group(1)

        imgFile = open(fileAddress)
        imgFileContent = imgFile.read()
        imgFile.close()

        searchWidth = re.search(r'width=(.*)', imgFileContent, re.M)
        searchHeight = re.search(r'height=(.*)', imgFileContent, re.M)
        imgWidth = int(searchWidth.group(1))
        imgHeight = int(searchHeight.group(1))

        if max(imgWidth, imgHeight) < 5000:
            urllib.request.urlretrieve(searchUrl.group(1), r'files/magicatz_ocr/catpic.jpg')

        # await bot.send(context, '|test| ' + str(imgWidth)+', '+str(imgHeight))

        amount, FCAC = recognize()

        if [amount, FCAC] in [[1, 1]]:
            msgMagicatzPic = '只是easy谱面而已啦，我不信你能收掉我的hard谱。'
        elif [amount, FCAC] in [[1, 2]]:
            msgMagicatzPic = '只是easy谱面而已啦，我不信你能FC我的hard谱。'
        elif [amount, FCAC] in [[1, 3]]:
            msgMagicatzPic = '欢迎高素质萌新，我的hard谱也很好玩的！'
        elif [amount, FCAC] in [[2, 1]]:
            msgMagicatzPic = '还好不是hard，我快要看不到你的素质了。'
        elif [amount, FCAC] in [[2, 2]]:
            msgMagicatzPic = '只是normal谱面而已啦，我不信你能FC我的hard谱。'
        elif [amount, FCAC] in [[2, 3]]:
            msgMagicatzPic = '悄悄说一句，我的hard谱更好玩哦！'
        elif [amount, FCAC] in [[3, 1]]:
            msgMagicatzPic = '您真是毫无素质，烟了吧！'
        elif [amount, FCAC] in [[3, 2]]:
            msgMagicatzPic = '您太强啦！'
        elif [amount, FCAC] in [[3, 3]]:
            msgMagicatzPic = '怎么样，拿我没办法吧？'
        else:
            msgMagicatzPic = 'Error'

        if msgMagicatzPic != 'Error':
            await bot.send(context, msgMagicatzPic)
