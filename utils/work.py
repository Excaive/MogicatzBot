import re
from utils.info import *


def at(user_id):
    return '[CQ:at,qq=%d]' % user_id


def unescape(string):
    string = string.replace('&#91;', '[')
    string = string.replace('&#93;', ']')
    string = string.replace('&amp;', '&')
    return string


def safe(msg, information):
    banedList = [{'message': r'^给.*(禁言|烟上|上烟|递烟|上大烟|抽大烟|上大中华)$', 'admin': [marigold, tairitsu]},
                 {'message': r'^(认输)$', 'admin': [tairitsu]},
                 {'message': r'^(烟我|别[CQ:emoji,id=128014]复读了|你要知道我对复读的忍耐是有限度的。)$', 'admin': [marigold]},
                 {'message': r'^(测试)$', 'admin': [creator]}]

    adminList = [admin['user_id'] for admin in information['admins']]
    for baned in banedList:
        msg_match = re.match(baned['message'], msg)
        if msg_match is not None:
            has_admin = list(set(adminList) & set(baned['admin']))
            if has_admin:
                return False
    return True
