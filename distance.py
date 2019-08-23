#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import argparse
import math

parser = argparse.ArgumentParser(description='Read the distance in inches from the distance sensor.')
parser.add_argument('--interval', type=float, help='time interval to poll the sensor in seconds', default=0.25)
args = parser.parse_args()
read_interval = args.interval

print("Distance Read...")
print("Interval: %5.2f" % read_interval )

GPIO.setmode(GPIO.BOARD)

PIN_TRIGGER = 7
PIN_ECHO = 11

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)

print("Waiting for sensor to settle")

time.sleep(2)

print("Calculating distance")

def pulse(interval = 0.00001):
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

def run():
        pulse()
        while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time
        speed_of_sound_in_cm_per_s = 34300.0
        roundtrip_distance_in_cm = speed_of_sound_in_cm_per_s * pulse_duration
        distance_in_inches = roundtrip_distance_in_cm / 2.0 / 2.54
        #round(pulse_duration * 17150, 2)/2.54
        print("Distance: %5.2f in" % distance_in_inches)
        time.sleep(read_interval)

try:
        while(True):
                run()

finally:
        GPIO.cleanup()
