import threading
from playsound import playsound
import time

bpm = 60

def start():
    global bpm
    while True:
        time.sleep(60/bpm)
        playsound('A4c.mp3')

def commands():
    global bpm
    command = [x for x in input(f'| CRNT BPM:{bpm} | >>> ').split()]
    if command[0].upper() == 'UP':
        bpm += int(command[1])
        bpm = handle_bpm(bpm)
    if command[0].upper() == 'DOWN':
        bpm -= int(command[1])
    commands()

def handle_bpm(bpm):
    if bpm < 15:
        print("Whoops! Too low!")
        return 15
    elif bpm > 200:
        print("Whoops! Too high!")
        return 200
    return bpm

    commands()
def main():
    print("--- You can control the bpm like this: <up/down> <change in bpm> for example: up 20 ---")
    time.sleep(1)
    s = threading.Thread(target=start)
    c = threading.Thread(target=commands)
    s.start()
    c.start()

if __name__ == '__main__':
    main()
