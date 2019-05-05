# dict = {}
#
# def collectRepeatInfo(group, msg):
#     if not group in dict.keys():
#         dict[group] = {'msg': msg, 'num': 1}
#     elif msg == dict[group]['msg']:
#         num = dict[group]['num'] + 1
#         dict[group] = {'msg': msg, 'num': num}
#     else:
#         dict[group] = {'msg': msg, 'num': 1}

# dict[1] = 'haha'
# dict[2] = 'jaja'
# dict[3] = 'awee'
# dict[1] = 'gai'





# collectRepeatInfo(1, 'haha')
# collectRepeatInfo(2, 'jaja')
# collectRepeatInfo(1, 'www')
# collectRepeatInfo(3, 'desdfdds')
# collectRepeatInfo(1, 'www')


# print(dict)
# print('msg' in dict[1].keys())
# print(dict[123]['num'])


# dict1 = {'message': '123 456', 'util': '567 890'}
# msg = dict1['message']
# splitList = msg.split(' ')
# print(splitList)
# print(splitList[1])
# print(str(type(dict1)))

import re

# m = re.match(r'(fa{2})', 'fafaaa')
# m = re.match(r'^(foo给\w)s(\w)$','foo给asd')
# print(m)
# print(m[2])

# msgReplace = '给e烟'
# msgBanedList = [r'^给.*(禁言|烟上|上烟|递烟|上大烟|抽大烟|上大中华)$', r'^(烟我)$']

# m = re.match(r'^给.*(禁言|烟上|上烟|递烟|上大烟|抽大烟|上大中华)$','给asddfgds抽大烟')
# m = re.match(r'^(烟我|认输)$','认输')

# m = re.match(b, msgReplace)
# if m is not None:
#     print(m)

# for msgBaned in msgBanedList:
#     m = re.match(msgBaned, msgReplace)
#     if m is not None:
#         print('不能说')
#         break

# marigold = 3304584594
# tairitsu = 2718434132


# def safe(msg, information):
#     banedList = [{'message': r'^给.*(禁言|烟上|上烟|递烟|上大烟|抽大烟|上大中华)$', 'admin': [marigold, tairitsu]},
#                     {'message': r'^(认输)$', 'admin': [tairitsu]},
#                     {'message': r'^(烟我|别[CQ:emoji,id=128014]复读了|你要知道我对复读的忍耐是有限度的。)$', 'admin': [marigold]}]
#     # adminList = []
#     # for admin in information['admins']:
#     #     adminList.append(admin['user_id'])
#
#     adminList = [admin['user_id'] for admin in information['admins']]
#
#     # print(adminList)
#
#     for baned in banedList:
#         msg_match = re.match(baned['message'], msg)
#         if msg_match is not None:
#             has_admin = list(set(adminList) & set(baned['admin']))
#             if has_admin:
#                 return False
#     return True
#
# msg = '给我烟上'
# information = {'admin_count': 5, 'admins': [{'nickname': '消息搬运bot', 'role': 'admin', 'user_id': 562231326}, {'nickname': '今天又是最后一个摸鱼日', 'role': 'owner', 'user_id': 779785756}, {'nickname': 'DN超性能フルグリッチ少年', 'role': 'admin', 'user_id': 1357008522}, {'nickname': 'DN超性能フルバグ少女', 'role': 'admin', 'user_id': 2718434132}, {'nickname': 'marigold', 'role': 'admin', 'user_id': 3304584594}], 'category': 25, 'create_time': 1531315853, 'group_id': 820594943, 'group_name': 'D.N.Debug', 'introduction': 'People and robots in the group can do great things.', 'max_admin_count': 10, 'max_member_count': 200, 'member_count': 62, 'owner_id': 779785756}
#
# # safe(msg, information)
# print(safe(msg, information))

import re
import urllib.request

msg = '|1| [CQ:at，qq=2130638764] [CQ:image，file=BA144C23AA88EEC4BB76435812B092BD.jpg，url=https://gchat.qpic.cn/gchatpic_new/1799306926/794843381-3065347345-BA144C23AA88EEC4BB76435812B092BD/0?vuin=2130638764&amp;term=2]'
searchFile = re.search(r'\[CQ:image，file=(.*)，', msg, re.M)

if searchFile:
    print(searchFile[1])
    fileAddress = 'D:\\_Panda\\酷Q\\CQA-tuling\\酷Q Air\\data\\image\\%s.cqimg' % searchFile.group(1)

    imgFile = open(fileAddress)
    imgFileContent = imgFile.read()
    imgFile.close()

    # searchWidth = re.search(r'width=(.*)', imgFileContent, re.M)
    # searchHeight = re.search(r'height=(.*)', imgFileContent, re.M)
    # searchUrl = re.search(r'url=(.*)', imgFileContent, re.M)
    #
    # imgWidth = int(searchWidth.group(1))
    # imgHeight = int(searchHeight.group(1))
    #
    # print(imgWidth, imgHeight)
    # print(searchUrl.group(1))

    # if max(imgWidth, imgHeight) < 5000:
    #     urllib.request.urlretrieve(searchUrl.group(1), 'D:\_Panda\酷Q\CQA-tuling\酷Q Air\\app\io.github.richardchien.coolqhttpapi\MogicatzBot\\awesome\plugins\magicatz_ocr\catpic.jpg')
