# coding:utf_8
import xlrd


class OperationExcel:
    def __init__(self, filename=None, sheet_id=None):
        if filename:
            self.file_name = filename
            self.sheet_id = sheet_id
        else:
            self.file_name = '../musicExcel/musicData.xls'
            self.sheet_id = 0

        self.data = self.get_data()

    def get_data(self):
        """获取sheets内容"""
        data = xlrd.open_workbook_xls(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """获取单元格的行数"""
        return self.data.nrows

    def get_cell_value(self, row, col):
        """获取单元格的内容"""
        return self.data.cell_value(row, col)

    def get_rows_values(self, row):
        """根据行号，找到该行找到对应内容"""
        tables = self.data
        values = tables.row_values(row)
        return values

    def get_col_values(self, col_id=None):
        """根据列号,找到该列对应的内容"""
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

