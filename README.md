# Pomodoro Timer

Requirements: 
- Linux or MacOS
- Install sox (Read How to Use section)


This timer helps you organize your routine and improve your productivity. By informing the time in minutes you want to work followed by the time in minutes you want to rest, the timer creates a routine and sounds an alarm for each time interval.

## How to Use:

To allow your OS to sound the alarm, you must install sox:
- In apt compatible systems: *sudo apt install sox*
- In Mac: *sudo port install sox*

Then,

Clone this repository and run *pomodoro.py* with Python3. Enter the desired time intervals and get to work!

**PS:** If the clock still doesn't sound the alarm, try this for linux: (adapted from StackOverflow: https://stackoverflow.com/a/16573188)
- In a terminal, type 'cd /etc/modprobe.d' then 'sudo nano blacklist.conf'
- Comment the line that says 'blacklist pcspkr', then reboot.
- If there's no blacklist.conf file, type ls to find the blacklist file that have the 'blacklist pcspkr' line.
- Check also that the terminal preferences has the 'Terminal Bell' checked.
