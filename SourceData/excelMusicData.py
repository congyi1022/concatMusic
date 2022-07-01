# coding:utf-8
from utils.excel_util import OperationExcel
from conf import data_conf


class GetMusicData:
    """获取表格中的数据"""

    def __init__(self):
        self.open_excel = OperationExcel()  # 初始化excel工具类

    def get_lines(self):
        """获得数据的行数"""
        return self.open_excel.get_lines()

    def get_timbre(self, x):
        """获取音色"""
        y = data_conf.get_timbre()
        timbre = self.open_excel.get_cell_value(x, int(y))
        return timbre

    def get_duration(self, x):
        """获取时长"""
        y = data_conf.get_duration()
        duration = self.open_excel.get_cell_value(x, int(y))
        return duration
