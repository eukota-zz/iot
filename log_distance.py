#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import argparse
import math
import datetime

parser = argparse.ArgumentParser(description='Logs the distance in inches from the distance sensor to input file.')
parser.add_argument('--output', help='Path to file to write to. Defaults to a local file named out.txt', default='/var/log/water_distance.txt')
parser.add_argument('--append', type=bool, help='True = append to file, False = overwrite file, Defaults to True', default=True)
parser.add_argument('--verbose', type=bool, help='verbose output will also go to log file', default=False)
args = parser.parse_args()

if args.verbose:
        print("Distance Read...")
        print("Output: %s" % args.output )
        print("Append: %r" % args.append )
        print("Verbose: %r" % args.verbose )

GPIO.setmode(GPIO.BOARD)

PIN_TRIGGER = 7
PIN_ECHO = 11

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)

if args.verbose:
        print("Waiting for sensor to settle")

time.sleep(5)

if args.verbose:
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
        res = ("%s: %5.2f in" % (datetime.datetime.now(), distance_in_inches))
        return res

try:
        r = run()
        if not args.append:
                f = open(args.output, "w+")
        else:
                f = open(args.output, "a")
        f.write(r)
        f.write("\n")
        f.close()
finally:
        GPIO.cleanup()
