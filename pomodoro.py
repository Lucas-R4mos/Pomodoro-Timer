from controller import set_timer
from controller import countdown
from controller import alert

class Turn:
    def __init__(self, duration):
        self.duration = duration


while True:
    workingDuration = input('Insert Working turn time: ')
    if workingDuration.isnumeric() == True:
        break
    else:
        print("Insert time in minutes.")

while True:
    restingDuration = input('Insert Resting turn time: ')
    if restingDuration.isnumeric() == True:
        break
    else:
        print("Insert time in minutes.")

working = Turn(workingDuration)
resting = Turn(restingDuration)

turns = [working, resting]

print('\n', end='\r')

while True:
    for turn in turns:
        import time
        finish = set_timer(turn.duration)
        while time.time() < finish:
            remaining = countdown(finish)
            if turn == working:
                print('   Working time! ' + remaining, end='\r')
            if turn == resting:
                print('   Resting time! ' + remaining, end='\r')
            time.sleep(1)
        alert()