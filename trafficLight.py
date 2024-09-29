import time;
import RPi.GPIO as GPIO;

redLight = 36
yellowLight = 38
greenLight = 40
delay = 1

def resetBoard():

    turnOffLights()
    GPIO.cleanup()

def setOutMode(red, yellow, green):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(yellow, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)

def turnOffLights():

    GPIO.output(redLight, GPIO.LOW)
    GPIO.output(yellowLight, GPIO.LOW)
    GPIO.output(greenLight, GPIO.LOW)

def turnOnAndOffLight(light, delay):

    turnOffLights()
    GPIO.output(light, GPIO.HIGH)
    print(f"Turn on pin {light}")
    time.sleep(delay)
    GPIO.output(light, GPIO.LOW)
    print(f"Turn off pin {light}")


setOutMode(redLight, yellowLight, greenLight)
turnOnAndOffLight(redLight, delay)
turnOnAndOffLight(yellowLight, delay)
turnOnAndOffLight(greenLight, delay)
resetBoard()