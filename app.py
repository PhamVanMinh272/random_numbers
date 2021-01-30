from os import system
import time
from random import randint
from datetime import datetime


system('clear')
CHALLENGE_DATA_PATH = 'data.txt' 


def save_challenge(path: str, input: str):
    with open(path, 'a') as f:
        f.writelines(input+'\n')

def read_challenge(path):
    with open(path, 'r') as f:
        data = f.read()
        print(data)

def caculate_row_score(error_pointer: str)->int:
    errors = error_pointer.count('!')
    score = 0
    if errors==0:
        score = 40
    elif errors==1:
        score = 20
    return score

def check_challenge(path):
    with open(path, 'r') as f:
        data = f.readlines()
    total_score = 0
    for index, line in enumerate(data):
        error_index = ''
        line = line[:-3]
        row = input(f"Row {index+1}: ")
        if len(row)<40+39*2:
            row = '  '.join(row)
        if len(row)==len(line):
            if row==line:
                print('Correct')
            else:
                for i, v in enumerate(line):
                    if v != row[i]:
                        error_index += '!'
                    else:
                        error_index += ' '
                
                print('Wrong')
                print('Correct awnser:', line)
                print('               ', error_index)
                print('Your awnser:   ', row)
        else:
            error_index = '!!!'
            print('Wrong')
            print('Correct awnser:', line)
            print('Your awnser:   ', row)
        row_score = caculate_row_score(error_index)
        print('Row score =', row_score)
        total_score += row_score
    print('Total score =', total_score)

def clear_challenge(path):
    with open(path, 'w') as f:
        f.write('')


def generate_challenge_data(n: int, len_row: int=40) -> list:
    challenge_data = []
    row = ''
    for _ in range(n):
        num = randint(0, 9)
        row += str(num)+'  '
        if len(row)>=len_row*3:
            save_challenge(CHALLENGE_DATA_PATH, row)
            challenge_data.append(row)
            row = ''
    if row:
        save_challenge(CHALLENGE_DATA_PATH, row)
        challenge_data.append(row)
    return challenge_data


def start_challenge():
    # clear old data
    clear_challenge(CHALLENGE_DATA_PATH)
    n = input("Number of numbers (Default 80): ")
    # get number of numbers
    if n == '':
        n=80
    else:
        try:
            n = int(n)
        except:
            print('Wrong format. Use default 80 numbers.')
    # wait time to start
    for i in range(1, 3):
        print(i)
        time.sleep(1)
    # generate data challenge and show
    challenge_data = generate_challenge_data(n)
    print('')
    for row in challenge_data:
        print(row)
        print('')
    start = datetime.now()
    input()
    # Recall
    system('clear')
    print('Time =', datetime.now()-start)
    start = datetime.now()
    check_challenge(CHALLENGE_DATA_PATH)
    print('Recall time:', datetime.now()-start)
    clear_challenge(CHALLENGE_DATA_PATH)

start_challenge()
