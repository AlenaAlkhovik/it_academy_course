import datetime

now = datetime.datetime.now()

# task 1
print(now)

# # task 2
# birthday_time = datetime.datetime.strptime('26-06-1994 00:00:00', '%d-%m-%Y %H:%M:%S')
# print(birthday_time)
#
# # task 3
# print(now.year, now.month, now.day)
#
# # task 4
# formatted_date = now.strftime('%d-%m-%Y')
# print(formatted_date)
#
# # task 5
# parsed_date = datetime.datetime.strptime('31/12/2025 23:59:59', '%d/%m/%Y %H:%M:%S')
# print(parsed_date)
#
# # task 6
# in_ten_days = now + datetime.timedelta(days=10)
# print(in_ten_days)
#
# # task 7
# start = datetime.date(now.year, 1, 1)
# end = datetime.date.today()
# time_difference = end - start
# print(time_difference.days)
#
# # task 8
# def weekends_determination(date):
#     try:
#         parsed_date = datetime.date.strptime(date, '%Y-%m-%d')
#         day_order = parsed_date.weekday()
#         if day_order in [5, 6]:
#             return 'Дата является выходным днем'
#         else:
#             return 'Дата является рабочим днем'
#     except ValueError:
#         return 'Ошибка ввода'
#
# print(weekends_determination(input('Введите дату в формате YYYY-MM-DD: ')))
#
# # task 9
# tz = datetime.timezone(datetime.timedelta(hours=3))
# print(datetime.datetime.now(tz))
#
# # task 10
# year = lambda d: d.year
# try:
#     input_date = input('Введите дату в формате YYYY-MM-DD: ')
#     parsed_date = datetime.date.strptime(input_date, '%Y-%m-%d')
#     print(year(parsed_date))
# except ValueError:
#     print('ощибка ввода')
