# coding:utf-8
from pydub import AudioSegment
from conf import data_conf


class ConcatMusic:
    """音频拼接类"""

    def concatTimbreMusic(self, timbre, duration):
        """拼接单个音色的音频"""
        timbre_music = timbre
        while (duration != 1):
            timbre_music = timbre_music + timbre
            duration = duration - 1
        return timbre_music

    def concatMusicList(self, timbre, duration, total_music_list):
        """生成需要拼接的musicList"""
        if timbre == "响板":
            total_applause = self.concatTimbreMusic(data_conf.applause(), duration)
            total_music_list.append(total_applause)
        elif timbre == "空白":
            total_blank = self.concatTimbreMusic(data_conf.blank(), duration)
            total_music_list.append(total_blank)

        return total_music_list

    def concatTotalMusic(self, music_list):
        """拼接整个音频"""
        total_music = music_list[0]  # 因为初始化类型只能是固定的格式（貌似是某个音频格式），所以这里直接赋值第一个音频而不是写的None
        for i in music_list[1:]:  # 上面已经赋值了第一个音频，所以这里从第二个音频开始相加
            total_music = total_music + i
        total_music.export("../targetMp3/concat.wav", format="wav")
        print("拼接成功，请去targetMp3目录下获取")
