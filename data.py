#coding=utf-8
import xlrd


class ExcelUnitl:
    def __init__(self, file_path , file_name):
        self.data = xlrd.open_workbook(file_path+'\\'+file_name)
        self.table = self.data.sheet_by_name("Sheet1")
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

    def getName(self):
        name = []
        for name_id in range(1,self.rowNum):
            name.append(self.table.cell(name_id,0).value)
        return name

    def getPwd(self):
        pwd = []
        for p in range(1,self.rowNum):
            pwd.append(self.table.cell(p,1).value)
        return pwd

    def getGrade(self):
        grade = []
        for i in range(1,self.rowNum):
            grade.append(self.table.cell(i,2).value)
        return grade



