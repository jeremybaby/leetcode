class Solution:
    def dayOfYear(self, date):

        # 是否为闰年
        def isLeapYear(year):
            return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

        res = 0

        # 注意，这里都是字符串，需要进行转换
        year, month, day = date.split('-')

        # 这里第一个位置用0填充，保证1月的索引是1
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if isLeapYear(int(year)):
            month_days[2] = 29

        res += sum(month_days[:int(month)]) + int(day)

        return res

class Solution_Promote:
    """ 比上面做了一些简单的优化 """
    def dayOfYear(self, date: str) -> int:
        
        def isLeapYear(year):
            return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
                
        year, month, day = map(int, date.split('-'))
        
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if isLeapYear(year):
            month_days[2] = 29
        
        return sum(month_days[:month]) + day

        
        