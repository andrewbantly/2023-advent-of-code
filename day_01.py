import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://adventofcode.com/2023/day/1/input'
cookies = {
    'session': os.getenv('SESSION'),
        }
response = requests.get(url, cookies=cookies)

raw_data = response.content.decode('utf-8')

data_arr = [line for line in raw_data.split('\n') if line]

sum = 0

num_words = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

for line in data_arr:
    first_num = 0
    second_num = 0
    number_str = ''
    for char in line:
        if char.isdigit():
            number_str = ''
            if first_num == 0:
                first_num = char
            else:
                second_num = char
        else:
            number_str += char
            matches = 0
            for key, value in num_words.items():
                if len(number_str) > len(key):
                    continue
                match = True
                for i in range(len(number_str)):
                    if key[i] != number_str[i]:
                        match = False
                if match:
                    matches += 1
                    if key == number_str:
                        if first_num == 0:
                            first_num = str(num_words[number_str])
                            number_str = char
                        else:
                            second_num = str(num_words[number_str])
                            number_str = char
            if matches == 0:
                number_str = char
        if second_num == 0:
            second_num = first_num

    calibration_value_str = first_num + second_num
    calibration_value = int(calibration_value_str)
    sum += calibration_value

print(f'count {sum}')

