import datetime
import re


class Ccr:
    def __init__(self):
        self.female = {'0M': 3.2,
                       '1M': 4.81,
                       '2M': 5.74,
                       '3M': 6.22,
                       '4M': 7.01,
                       '5M': 7.53,
                       '6M': 8,
                       '8M': 8.65,
                       '10M': 9.09,
                       '12M': 9.52,
                       '15M': 10.09,
                       '18M': 10.65,
                       '21M': 11.25,
                       '2岁': 12.04,
                       '2.5岁': 12.97,
                       '3岁': 14.01,
                       '3.5岁': 14.94,
                       '4岁': 15.81,
                       '4.5岁': 16.8,
                       '5岁': 17.84,
                       '5.5岁': 18.8,
                       '6岁': 20.36,
                       '7岁': 22.32,
                       '8岁': 24.58,
                       '9岁': 27.45,
                       '10岁': 31.11,
                       '11岁': 35.76,
                       '12岁': 40.18,
                       '13岁': 44.45,
                       '14岁': 46.73,
                       '15岁': 48.7,
                       '16岁': 49.97,
                       '17岁': 50.37,
                       '18岁': 50.37}
        self.male = {'0M': 3.3,
                     '1M': 5.1,
                     '2M': 6.16,
                     '3M': 6.74,
                     '4M': 7.56,
                     '5M': 8.02,
                     '6M': 8.62,
                     '8M': 9.19,
                     '10M': 9.65,
                     '12M': 10.16,
                     '15M': 10.7,
                     '18M': 11.25,
                     '21M': 11.83,
                     '2岁': 12.57,
                     '2.5岁': 13.56,
                     '3岁': 14.42,
                     '3.5岁': 15.37,
                     '4岁': 16.23,
                     '4.5岁': 17.24,
                     '5岁': 18.34,
                     '5.5岁': 19.38,
                     '6岁': 20.97,
                     '7岁': 23.35,
                     '8岁': 25.73,
                     '9岁': 28.66,
                     '10岁': 31.88,
                     '11岁': 35.69,
                     '12岁': 39.74,
                     '13岁': 45.96,
                     '14岁': 50.83,
                     '15岁': 54.11,
                     '16岁': 56.8,
                     '17岁': 58.25,
                     '18岁': 58.25}
        self.recipe_time_str = '2019-06-25'
        self.birthday_str = '2015-02-28'
        self.y, self.age = self.calculate_age(self.recipe_time_str, self.birthday_str)

    # 根据出生日期计算年龄
    # 门诊   recipe_time - birthday
    # 住院   birthday
    def calculate_age(self, recipe_time_str, birthday_str):
        recipe_time = datetime.datetime.strptime(recipe_time_str, '%Y-%m-%d')
        birthday = datetime.datetime.strptime(birthday_str, '%Y-%m-%d')
        y = 0
        age = ''
        if recipe_time.month < birthday.month:
            y = recipe_time.year - birthday.year - 1
            if y == 0:
                if recipe_time.day < birthday.day:
                    age = str(12 - (birthday.month - recipe_time.month) - 1) + 'M'
                else:
                    age = str(12 - (birthday.month - recipe_time.month)) + 'M'
            else:
                age = str(y) + '岁'
        if recipe_time.month > birthday.month:
            y = recipe_time.year - birthday.year
            if y == 0:
                if recipe_time.day < birthday.day:
                    age = str(12 - (birthday.month - recipe_time.month) - 1) + 'M'
                else:
                    age = str(12 - (birthday.month - recipe_time.month)) + 'M'
            else:
                age = str(y) + '岁'
        if recipe_time.month == birthday.month and recipe_time.day < birthday.day:
            y = recipe_time.year - birthday.year - 1
            if y == 0:
                if recipe_time.day < birthday.day:
                    age = str(12 - (birthday.month - recipe_time.month) - 1) + 'M'
                else:
                    age = str(12 - (birthday.month - recipe_time.month)) + 'M'
            else:
                age = str(y) + '岁'
        if recipe_time.month == birthday.month and recipe_time.day > birthday.day:
            y = recipe_time.year - birthday.year
            if y == 0:
                if recipe_time.day < birthday.day:
                    age = str(12 - (birthday.month - recipe_time.month) - 1) + 'M'
                else:
                    age = str(12 - (birthday.month - recipe_time.month)) + 'M'
            else:
                age = str(y) + '岁'
        return y, age

    # 计算年龄默认值
    def get_default_weight(self, sex):
        num = self.age[0:-1]
        str = self.age[-1]
        weight = 0
        if sex == '男':
            if str == '岁' and int(num) > 18:
                weight = 60
            else:
                for k in self.male:
                    if k == self.age:
                        weight = self.male[k]
        else:
            if str == '岁' and int(num) > 18:
                weight = 50
            else:
                for k in self.female:
                    if k == self.age:
                        weight = self.female[k]
        return weight

    # 不传ccr只传scr时，根据scr计算ccr
    def ccr_calculate(self, sex, unit, age, weight, scr, default):

        if default == 0:  # 不使用默认身高体重
            if age == '' or weight == '' or sex == '':
                ccr = str(90) + '预设值'
            else:
                if unit == 'mg/dl':
                    c = ((140 - age) * weight) / (72 * scr)
                else:
                    c = ((140 - age) * weight) / (0.818 * scr)
                if sex == '男':
                    ccr = c
                else:
                    ccr = 0.85 * c
        # 使用默认身高体重
        else:
            if age == '' or sex == '':
                ccr = str(90) + '(预设值)'
            else:
                if sex == '男':
                    weight = self.get_default_weight('男')
                    if unit == 'mg/dl':
                        ccr = ((140 - age) * weight) / (72 * scr)
                    else:
                        ccr = ((140 - age) * weight) / (0.818 * scr)
                else:
                    weight = self.get_default_weight('女')
                    if unit == 'mg/dl':
                        ccr = ((140 - age) * weight) / (72 * scr) * 0.85
                    else:
                        ccr = ((140 - age) * weight) / (0.818 * scr) * 0.85
        return ccr


cal_ccr = Ccr()
we = cal_ccr.get_default_weight('男')
print(we)
print(cal_ccr.age)
test = cal_ccr.ccr_calculate(sex='男', unit='mg/dl', age=cal_ccr.y, weight='', scr=2, default=1)
print(test)
