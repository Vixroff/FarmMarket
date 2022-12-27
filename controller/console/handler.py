import sys
import time


from controller.txt import BYE, GUIDE


COMMANDS = ('list', 'find', 'show', 'review', 'guide', 'exit')


def handler(cmd, args):
    if cmd not in COMMANDS:
        print('Wrong command!')
        time.sleep(2)
        sys.exit(1)
    elif cmd == 'exit':
        print(BYE)
        time.sleep(2)
        sys.exit()
    elif cmd == 'guide':
        print(GUIDE)
    else:
        print("Sorryy, it will be soon!")
