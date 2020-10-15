from controller import set_timer
from controller import countdown
from controller import alert

working = input('Insert Working turn time: ')
resting = input('Insert Resting turn time: ')

turns = [working, resting]

print('\n', end='\r')

while True:
    for turn in turns:
        import time
        finish = set_timer(turn)
        while time.time() < finish:
            remaining = countdown(finish)
            if turn == working:
                print('   Working time! ' + remaining, end='\r')
            if turn == resting:
                print('   Resting time! ' + remaining, end='\r')
            time.sleep(1)
        alert()