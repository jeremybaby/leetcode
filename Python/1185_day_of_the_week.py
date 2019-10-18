import datetime


class Solution1:
    """使用内置的datetime模块"""
    def dayOfTheWeek(self, day, month, year):
        calendar = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        day = datetime.datetime(year, month, day).weekday()

        return calendar[day]


import datetime


class Solution2:
    """把以下天数进行统计：
      - 从1971年开始，非闰年365天，闰年366天
      - 每个月的天数为
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        其中遇到闰年的二月为29天
      - 1971-1-1为周五"""
    def dayOfTheWeek(self, day, month, year):

        # 判断是否为闰年
        def isLeapYear(year):
            return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

        # 注意，index从Sunday开始,这样保证索引1是周一
        calendar = ['Sunday', 'Monday', 'Tuesday', \
                    'Wednesday', 'Thursday', 'Friday', 'Saturday']

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if isLeapYear(year):
            # 闰年2月29天
            month_days[1] = 29

        year_days = [0] * (year - 1970)

        for i in range(1971, year):
            year_days[i - 1971] = 366 if isLeapYear(i) else 365

        # 1971-1-1 周五
        # 假如'1971-1-1'为周一， 那么对于1971-1-29，29 % 7 = 1，那么29号就是周一
        # 周二的话，就要加1，周五的话，就要加4
        count_days = sum(year_days) + sum(month_days[:month - 1]) + day + 4

        return calendar[count_days % 7]
