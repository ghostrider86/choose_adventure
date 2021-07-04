import json
import os
import game_1 as g1
import game_2 as g2
def get_file():
    print('what adventure do you want?')
    file_n = input()
    return file_n

def read_intro(file_n):
    with open(file_n) as f:
        data = json.load(f)
        print(f"{data['intro']}")
        return data

file_n = ""
while not os.path.exists(file_n):
    file_n = get_file()
    print(file_n)
text = read_intro(file_n)

if file_n == 'adventure_1.json':
    g1.game_1()
elif file_n == 'adventure_2.json':
    g2.game_2()
else:
    print("That adventure is not written yet.")
