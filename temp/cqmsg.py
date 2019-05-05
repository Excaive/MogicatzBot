class cqMsg():

    def cq_face(id):
        '''
        QQ表情
        {0}为0-170的数字
        举例：[CQ:face,id=14]（发送一个微笑的QQ表情'''
        return "[CQ:face,id={0}]".format(id)

    def cq_emoji(id):
        '''
        emoji表情
        {0}为emoji字符的unicode编号
        举例：[CQ:emoji,id=128513]（发送一个大笑的emoji表情）'''
        return "[CQ:emoji,id={0}]".format(id)

    def cq_bface(id):
        '''
        原创表情
        {0}为该原创表情的ID，存放在酷Q目录的data\bface\下
        '''
        return "[CQ:bface,id={0}]".format(id)

    def cq_sface(id):
        '''
        小表情
        {0}为该小表情的ID
        '''
        return "[CQ:sface,id={0}]".format(id)

    def cq_image(file):
        '''
        发送自定义图片
        {0}为图片文件名称，图片存放在酷Q目录的data\image\下
        举例：[CQ:image,file=1.jpg]（发送data\image\1.jpg）
        '''
        return "[CQ:image,file={0}]".format(file)

    def cq_record(file, magic=False):
        '''
        发送语音
        {1}为音频文件名称，音频存放在酷Q目录的data\record\下
        {2}为是否为变声，若该参数为true则显示变声标记。该参数可被忽略。
        举例：[CQ:record,file=1.silk，magic=true]（发送data\record\1.silk，并标记为变声）
        '''
        magic = str(magic).lower()
        return "[CQ:record,file={0},magic={1}]".format(file, magic)

    def cq_at(fromQQ):
        '''
        @某人
        {0}为被@的群成员QQ。若该参数为all，则@全体成员（次数用尽或权限不足则会转换为文本）。
        举例：[CQ:at,qq=123456]
        '''
        return "[CQ:at,qq={0}]".format(fromQQ)

    def cq_rps(type):
        '''
        发送猜拳魔法表情
        {0}为猜拳结果的类型，暂不支持发送时自定义。该参数可被忽略。
        1 - 猜拳结果为石头
        2 - 猜拳结果为剪刀
        3 - 猜拳结果为布
        '''
        return "[CQ:rps,type={0}]".format(type)

    def cq_dice():
        '''
        发送掷骰子魔法表
        {0}对应掷出的点数，暂不支持发送时自定义。该参数可被忽略。
        暂时不被允许填写参数
        '''
        return "[CQ:dice,type={0}]".format(type)

    def cq_shake():
        '''
        戳一戳（原窗口抖动，仅支持好友消息使用）
        原窗口抖动，仅支持好友消息使用
        '''
        return "[CQ:shake]"

    def cq_anonymous(ignore=False):
        '''
        匿名发消息（仅支持群消息使用）
        本CQ码需加在消息的开头。
        当{0}为true时，代表不强制使用匿名，如果匿名失败将转为普通消息发送。
        当{0}为false或ignore参数被忽略时，代表强制使用匿名，如果匿名失败将取消该消息的发送。
        举例：
        [CQ:anonymous,ignore=true]
        [CQ:anonymous]
        '''
        ignore = str(ignore).lower()
        return "[CQ:anonymous,ignore={0}]".format(ignore)

    def cq_music(type, id):
        '''
        发送音乐
        {0}为音乐平台类型，目前支持qq、163、xiami
        {1}为对应音乐平台的数字音乐id
        注意：音乐只能作为单独的一条消息发送
        举例：
        [CQ:music,type=qq,id=422594]（发送一首QQ音乐的“Time after time”歌曲到群内）
        [CQ:music,type=163,id=28406557]（发送一首网易云音乐的“桜咲く”歌曲到群内）
        '''
        return "[CQ:music,type={0},id={1}]".format(type, id)

    def cq_music_diy(url, audio, title, content="", image=""):
        '''
        发送音乐自定义分享
        {0}为分享链接，即点击分享后进入的音乐页面（如歌曲介绍页）。
        {1}为音频链接（如mp3链接）。
        {2}为音乐的标题，建议12字以内。
        {3}为音乐的简介，建议30字以内。该参数可被忽略。
        {4}为音乐的封面图片链接。若参数为空或被忽略，则显示默认图片。
        注意：音乐自定义分享只能作为单独的一条消息发送
        '''
        return "[CQ:music,type=custom,url={0},audio={1},title={2},content={3},image={4}]".format(
            url, audio, title, content, image)

    def cq_share(url, title, content="", image=""):
        '''
        发送链接分享
        {0}为分享链接。
        {1}为分享的标题，建议12字以内。
        {2}为分享的简介，建议30字以内。该参数可被忽略。
        {3}为分享的图片链接。若参数为空或被忽略，则显示默认图片。
        注意：链接分享只能作为单独的一条消息发送
        '''
        return "[CQ:share,url={0},title={1},content={2},image={3}]".format(
            url, title, content, image)