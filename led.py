import RPi.GPIO as GPIO
#importing time for sleep calls
import time

#variables to set throughout the program
cond = 1
global rled
global gled
global yled

#assigning colors to pins
rled = 12
yled = 16
gled = 18


#method to blink choosen light color
#probably could've wrote another
#method but i'll do that later just copy and pasted to make blink for now
def turnOnLed(led):
        GPIO.setmode(GPIO.BOARD)
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, 1)

	time.sleep(.75)

	GPIO.output(led, 0)
	GPIO.cleanup()
	time.sleep(.75)
	GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, 1)
        time.sleep(.75)
	
        GPIO.output(led, 0)
        GPIO.cleanup()
	time.sleep(.75)
	GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, 1)
        time.sleep(.75)

        GPIO.output(led, 0)
        GPIO.cleanup()

	GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, 1)
        time.sleep(.75)

        GPIO.output(led, 0)
        GPIO.cleanup()

	return

while cond == 1:
	answer = raw_input('Turn on 1. green , 2.red or 3.yellow, press x to quit: ')
	if answer == '1':
		turnOnLed(gled)
                cond = 1
        elif answer == '2':
                turnOnLed(rled)
                cond = 1
        elif answer == '3':
                turnOnLed(yled)
                cond = 1
        elif answer == 'x':
                print 'exiting....'
                cond =2
