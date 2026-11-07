import logging

# task 1
logging.basicConfig(
    level=logging.INFO,
    filename='app_session.log',
    encoding='utf-8',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)d'
)

variable = 10

logging.debug("Отладка: %s", variable)
logging.info("Информация")
logging.critical("КРИТИЧЕСКАЯ ошибка!")

# task 2
# def repeat_string(text, count):
#     assert isinstance(text, str), 'Text is not a string'
#     assert isinstance(count, int), 'Count is not int'
#     return text*count
#
# print(repeat_string('Aliona', 10))

# task 3
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# file_1_handler = logging.FileHandler('combined.log', encoding='utf-8')
# file_1_handler.setLevel(logging.INFO)
#
# file_2_handler = logging.FileHandler('crit_errors.log', encoding='utf-8')
# file_2_handler.setLevel(logging.ERROR)
#
# formatter = logging.Formatter(
# '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)d'
# )
#
# file_1_handler.setFormatter(formatter)
# file_2_handler.setFormatter(formatter)
#
# logger.addHandler(file_1_handler)
# logger.addHandler(file_2_handler)
#
# variable = 20
#
# logger.debug("Отладка: %s", variable)
# logger.info("Информация")
# logger.warning("Предупреждение!")
# logger.error("Ошибка!")
# logger.critical("КРИТИЧЕСКАЯ ошибка!")


# task 4
# logger = logging.getLogger(__name__)
# logger.addHandler(logging.StreamHandler())
#
# user_data = {"name": "Alice"}
#
# try:
#     print(user_data['age'])
# except KeyError:
#     logger.exception('Ключ age не найден в user_data')


# task 5
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)d'
# )
#
# logger = logging.getLogger(__name__)
#
# def process_payment(amount):
#     try:
#         assert amount > 0, 'Amount cannot be <= 0'
#     except AssertionError:
#         logger.exception('Некорректная сумма платежа: %s', amount)
#         return False
#     logger.info('Платеж на сумму %s проведен успешно', amount)
#     return True
#
# print(process_payment(-5))