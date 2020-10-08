def set_timer(duration):
    import time

    finish = (time.time() + (int(duration) * 60))

    return finish

def countdown(finish):
    import time

    minutes_countdown = str(int(round((finish - time.time()) // 60, 0)))

    seconds_countdown = str(int(round((finish - time.time()) % 60, 0)))
    
    
    if seconds_countdown == '60':
        seconds_countdown = '0'
        minutes_countdown = str(int(minutes_countdown) + 1)

    if minutes_countdown == '0':
        minutes_countdown == '00'

    if seconds_countdown == '0':
        seconds_countdown =='00'

    return str(minutes_countdown + ':' + seconds_countdown)


def alert():
    import os
    import time

    for repeat in range(4):
        duration = (1/5) # seconds
        freq = 660  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration,      freq))
        time.sleep(1/5)

    return


def checkInputs(working_value, resting_value):
    if working_value.isnumeric():
        working = working_value
    else:
        working = 30

    if resting_value.isnumeric():
        resting = resting_value
    else:
        resting = 5

    return (working, resting)