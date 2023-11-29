from dimacs import readSolution
from os import listdir
import time


def runtests(f, dir):
    files = listdir(dir)
    print(f"List of files: {files}")
    final_output = ""
    total_time = 0
    for file in files:
        try:
            path = dir + file
            time_start = time.time()
            my_ans = f(path)
            time_finish = time.time()
            total_time += float(time_finish - time_start)
            good_ans = readSolution(path)
            print('----------------------------')
            print(f'Graph: {file}')
            print(f'My answer: {my_ans}')
            print(f'Expected answer: {good_ans}')
            print(f'Time: {float(time_finish-time_start).__round__(3)}')
            if int(my_ans) == int(good_ans):
                print('Test accepted')
                final_output += "A"
            else:
                print('Test failed')
                final_output += "F"
            print('----------------------------')
        except KeyboardInterrupt:
            print('----------------------------')
            print(f'Graph: {file}')
            print(f'Expected answer: {good_ans}')
            print("Obliczenia przerwane przez operatora")
            final_output += "O"
    print(final_output)
    print(f'Total time: {total_time.__round__(3)}')