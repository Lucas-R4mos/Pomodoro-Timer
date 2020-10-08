from controller import set_timer
from controller import countdown
from controller import alert

working = input('Insert Working turn time: ')
resting = input('Insert Resting turn time: ')

turns = [working, resting]

for turn in turns:
    import time
    if turn == working:
        print('Working time!')
    if turn == resting:
        print('Resting time!')
    finish = set_timer(turn)
    while time.time() < finish:
        remaining = countdown(finish)
        time.sleep(1)
    alert()