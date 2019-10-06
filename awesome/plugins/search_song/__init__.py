import nonebot
from utils.work import *
from .data_source import *

bot = nonebot.get_bot()


songs = []
flagLoaded = False

@bot.on_message('private')
async def add_song_private(context):
    global flagLoaded, songs
    if context['user_id'] == creator and context['message'] == '更新曲库':
        songs = loadSongs()
        flagLoaded = True


@bot.on_message('group')
async def add_song_group(context):
    global flagLoaded, songs
    if context['user_id'] == creator and context['message'] == '更新曲库':
        songs = loadSongs()
        flagLoaded = True


@bot.on_message('group')
async def search_song_group(context):
    global flagLoaded, songs
    msg = str(context['message'])
    msgBlank = msg.split(' ', 1)
    if len(msgBlank) > 1:
        if msgBlank[0] in ['搜歌', '找歌']:
            if not flagLoaded:
                songs = loadSongs()
                flagLoaded = True
            msgSearch = findSong(msgBlank[1], songs, 10)
            await bot.send(context, msgSearch)


@bot.on_message('private')
async def search_song_private(context):
    global flagLoaded, songs
    msg = str(context['message'])
    msgBlank = msg.split(' ', 1)
    if len(msgBlank) > 1:
        if msgBlank[0] in ['搜歌', '找歌']:
            if not flagLoaded:
                songs = loadSongs()
                flagLoaded = True
            msgSearch = findSong(msgBlank[1], songs, 10)
            await bot.send(context, msgSearch)
