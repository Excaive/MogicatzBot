# -*- coding: utf-8 -*-
import xlrd
import re


class Song:
    def __init__(self, name, source, rank, votes):
        self.name = name
        self.source = source
        self.rank = rank
        self.votes = votes

    def info(self):
        print(f'【NAME】 {self.name}  【SOURCE】 {self.source}  【RANK】 {self.rank}  【VOTES】 {self.votes}')


def loadSongs():
    workbook = xlrd.open_workbook(r'files/search_song/songlist.xlsx')
    sheet = workbook.sheet_by_index(0)
    songs = []
    for i in range(sheet.nrows):
        if sheet.cell(i, 0).ctype == 1:
            newSong = Song(sheet.cell_value(i, 0), sheet.cell_value(i, 1), int(sheet.cell_value(i, 2)), int(sheet.cell_value(i, 3)))
            songs.append(newSong)
        elif sheet.cell(i, 0).ctype == 2:
            newSong = Song(str(int(sheet.cell_value(i, 0))), sheet.cell_value(i, 1), int(sheet.cell_value(i, 2)), int(sheet.cell_value(i, 3)))
            songs.append(newSong)
    return songs


def sameSong(songName1, songName2):
    if len(songName1) == len(songName2):
        songName1 = songName1.upper()
        songName2 = songName2.upper()
        for i in range(len(songName1)):
            if songName1[i] != '*':
                if songName1[i] != songName2[i]:
                    return False
        return True
    return False


def findSong(songName, songs, max=10):
    sameSongs = []
    for i in range(len(songs)):
        if sameSong(songName, songs[i].name):
            sameSongs.append(songs[i])
    if len(sameSongs) != 0:
        sameSongs = sorted(sameSongs, key=lambda song: song.rank)
        msg = '找到了以下歌曲：\n'
        for i in range(min(len(sameSongs), max)):
            msg = msg + '------------------------------\n'
            msg = msg + f'曲名：{sameSongs[i].name}\n' \
                        f'来源：{sameSongs[i].source}\n' \
                        f'排名：{sameSongs[i].rank}\n'
        msg = msg + '------------------------------'
        return msg
    else:
        return '没有找到对应歌曲'


def sameSongRe(songName1, songName2):
    songName1 = rf'^{songName1}$'
    songMatch = re.match(songName1.upper(), songName2.upper())
    if songMatch is not None:
        return True
    else:
        return False


def findSongRe(songName, songs, max=5):
    sameSongs = []
    for i in range(len(songs)):
        if sameSongRe(songName, songs[i].name):
            sameSongs.append(songs[i])
    if len(sameSongs) != 0:
        sameSongs = sorted(sameSongs, key=lambda song: song.rank)
        msg = '找到了以下歌曲：\n'
        for i in range(min(len(sameSongs), max)):
            msg = msg + '------------------------------\n'
            msg = msg + f'曲名：{sameSongs[i].name}\n' \
                        f'来源：{sameSongs[i].source}\n' \
                        f'排名：{sameSongs[i].rank}\n'
        msg = msg + '------------------------------'
        return msg
    else:
        return '没有找到对应歌曲'
