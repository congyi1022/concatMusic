# coding:utf-8
from utils.excel_util import OperationExcel
from pydub import AudioSegment


class globar_var:
    """数据配置项"""

    timbre = '0'  # 音色
    duration = '1'  # 时长


def get_timbre():
    return globar_var.timbre


def get_duration():
    return globar_var.duration


# 响板声音1s
def applause():
    return AudioSegment.from_wav("../sourceMp3/applause.wav")


# 空白声音1s
def blank():
    return AudioSegment.from_wav("../sourceMp3/blank.wav")
