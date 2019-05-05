import jieba

msg = '''
重复复读可不是好习惯
'''

def analysis(wordSet):
    if {'重复的', '复读'} < wordSet:
        return '我复读会上瘾的'
    return

words = jieba.cut(msg, cut_all=False)
wordSet = {word for word in words}

msgReply = analysis(wordSet)
print(msgReply)
if not msgReply:
    print(2)

# print(wordSet)
# print(type(wordSet))
#
# if '今日' in wordSet:
#     print(True)
# else:
#     print(False)


# # print("Full Mode: " + "/ ".join(seg_list))
# # print(type(seg_list))
#
# for i in seg_list:
#     print(i)

# import jieba.posseg as pseg
# words = pseg.cut(msg)
# for word, flag in words:
#     print('%s %s' % (word, flag))

