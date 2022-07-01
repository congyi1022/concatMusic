# coding:utf-8
from SourceData.excelMusicData import GetMusicData
from utils.music_unit import ConcatMusic


class RunMain:
    def __init__(self):
        self.data = GetMusicData()
        self.concat = ConcatMusic()

    def go_run(self):
        lines = self.data.get_lines()  # 获得Excel行数
        total_music_list = []
        for i in range(1, lines):
            timbre = self.data.get_timbre(i)
            print("音色：" + timbre)
            duration = self.data.get_duration(i)
            print("时长：" + str(duration))
            total_music_list = self.concat.concatMusicList(timbre, duration, total_music_list)

        self.concat.concatTotalMusic(total_music_list)


if __name__ == '__main__':
    run = RunMain()
    run.go_run()
