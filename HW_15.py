import json
import yaml
import xml.etree.ElementTree as ET

# 1. JSON
# 1.1
results = {'test_suite': 'api_tests', 'total': 10, 'passed': 8, 'failed': 2}

with open('test_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# 1.2
# results = [{"id": 1, "name": "Sasha", "role": "admin"}]
#
# with open('users.json', 'w', encoding='utf-8') as f:
#     json.dump(results, f, indent=2, ensure_ascii=False)

# 1.3
# with open('test_results.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#
# total = data['total']
# passed = data['passed']
# passed_percent = (passed* 100)/total
#
# print(passed_percent)

# 1.4
# my_user = {"id": 2, "name": "Aliona", "role": "user"}
#
# with open('users.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#
# print(data)
# data.append(my_user)
# print(data)
#
# with open('users.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=2, ensure_ascii=False)

# 1.5
# def dummy_test(data):
#     if data <= 5:
#         return True
#     else:
#         return False
#
# tests = [
# (dummy_test(5), True),
# (dummy_test(7), True),
# (dummy_test(6), False),
# (dummy_test(2), True),
# (dummy_test(4), False),
# (dummy_test(8), True),
# (dummy_test(1), False),
# ]
#
# count_passed = 0
# count_failed = 0
# error_messages = []
#
# for result, expected in tests:
#     try:
#         assert result == expected
#         count_passed +=1
#     except AssertionError as e:
#         print(f"Тест не пройден! Ожидается что пароль результат {expected}, " +
#               f"но фактический результат {result}")
#         count_failed +=1
#         error_messages.append(f'Тест не пройден! Ожидается что пароль результат {expected}, но фактический результат {result}')
#         continue
#     print("Тест прошёл!")
#
# print(count_passed)
# print(count_failed)
#
# total = count_passed + count_failed
# passed_percent = count_passed*100/total if total else 0
#
# print(f'{passed_percent:.2f}')
#
# test_results = {}
# test_results['total'] = total
# test_results['passed_tests'] = count_passed
# test_results['failed_tests'] = count_failed
# test_results['passed_percent'] = round(passed_percent, 2)
# test_results['error_messages'] = error_messages
# print(test_results)
#
#
# with open('dummy_test_results.json', 'w', encoding='utf-8') as f:
#     json.dump(test_results, f, indent=2, ensure_ascii=False)

# 2. YAML
# 2.1
# results = {'test_suite': 'api_tests', 'total': 10, 'passed': 8, 'failed': 2}
#
# with open('test_results.yaml', 'w', encoding='utf-8') as f:
#     yaml.safe_dump(results, f, default_flow_style=False, sort_keys=False)

# 2.2
# results = [{"id": 1, "name": "Sasha", "role": "admin"}]
#
# with open('users.yaml', 'w', encoding='utf-8') as f:
#     yaml.safe_dump(results, f, default_flow_style=False, sort_keys=False)


# 2.3
# with open('test_results.yaml', 'r', encoding='utf-8') as f:
#     test_results = yaml.safe_load(f)
#
# passed_percent = test_results['passed']*100 / test_results['total']
# print(passed_percent)

# 2.4
# my_user = {"id": 2, "name": "Aliona", "role": "user"}
#
# with open('users.yaml', 'r', encoding='utf-8') as f:
#     users = yaml.safe_load(f)
#
# users.append(my_user)
# print(users)
#
# with open('users.yaml', 'w') as f:
#     yaml.safe_dump(users, f, default_flow_style=False, sort_keys=False)

# 2.5
# def dummy_test(data):
#     if data <= 5:
#         return True
#     else:
#         return False
#
# tests = [
# (dummy_test(5), True),
# (dummy_test(7), True),
# (dummy_test(6), False),
# (dummy_test(2), True),
# (dummy_test(4), False),
# (dummy_test(8), True),
# (dummy_test(1), False),
# ]
#
# count_passed = 0
# count_failed = 0
# error_messages = []
#
# for result, expected in tests:
#     try:
#         assert result == expected
#         count_passed +=1
#     except AssertionError as e:
#         print(f"Тест не пройден! Ожидается что пароль результат {expected}, " +
#               f"но фактический результат {result}")
#         count_failed +=1
#         error_messages.append(f'Тест не пройден! Ожидается что пароль результат {expected}, но фактический результат {result}')
#         continue
#     print("Тест прошёл!")
#
# print(count_passed)
# print(count_failed)
#
# total = count_passed + count_failed
# passed_percent = count_passed*100/total if total else 0
#
# print(f'{passed_percent:.2f}')
#
# test_results = {}
# test_results['total'] = total
# test_results['passed_tests'] = count_passed
# test_results['failed_tests'] = count_failed
# test_results['passed_percent'] = round(passed_percent, 2)
# test_results['error_messages'] = error_messages
# print(test_results)
#
#
# with open('dummy_test_results.yaml', 'w', encoding='utf-8') as f:
#     yaml.safe_dump(test_results, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

# 3. XML
# 3.1
# tree = ET.parse('employees.xml')
# root = tree.getroot()
#
# employees = root.findall('employee')
# count_employees = len(employees)
#
# employee_salaries = [elem.text for elem in root.findall('.//salary')]
#
# converted_employee_salaries = []
# for item in employee_salaries:
#     s = int(item)
#     converted_employee_salaries.append(s)
#
# total_salary = sum(converted_employee_salaries)
#
# print(f"Количество сотрудников: {count_employees}")
# print(f"Суммарная зарплата: {total_salary}")


# 3.2
# def dummy_test(data):
#     if data <= 5:
#         return True
#     else:
#         return False
#
# tests = [
# (dummy_test(5), True),
# (dummy_test(7), True),
# (dummy_test(6), False),
# (dummy_test(2), True),
# (dummy_test(4), False),
# (dummy_test(8), True),
# (dummy_test(1), False),
# ]
#
# count_passed = 0
# count_failed = 0
# error_messages = []
#
# for result, expected in tests:
#     try:
#         assert result == expected
#         count_passed +=1
#     except AssertionError as e:
#         print(f"Тест не пройден! Ожидается что пароль результат {expected}, " +
#               f"но фактический результат {result}")
#         count_failed +=1
#         error_messages.append(f'Тест не пройден! Ожидается что пароль результат {expected}, но фактический результат {result}')
#         continue
#     print("Тест прошёл!")
#
# print(count_passed)
# print(count_failed)
#
# total = count_passed + count_failed
# passed_percent = count_passed*100/total if total else 0
#
# print(f'{passed_percent:.2f}')
#
# root = ET.Element('test_results')
# ET.SubElement(root, 'total').text = str(total)
# ET.SubElement(root, 'passed_tests').text = str(count_passed)
# ET.SubElement(root, 'failed_tests').text = str(count_failed)
# ET.SubElement(root, 'passed_percent').text = str(round(passed_percent, 2))
# error_mess_xml = ET.SubElement(root, 'error_messages')
# for message in error_messages:
#     ET.SubElement(error_mess_xml, 'error').text = message
#
#
# tree = ET.ElementTree(root)
# ET.indent(tree, space='    ')
# tree.write('dummy_test_results.xml', encoding='utf-8', xml_declaration=True)