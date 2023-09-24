#!/usr/bin/env python3
import argparse
import logging
import time
from sensor import Sensor

parser = argparse.ArgumentParser(description='Read the distance in inches from the distance sensor.')
parser.add_argument('--interval', type=float, help='time interval to poll the sensor in seconds', default=0.25)
args = parser.parse_args()
read_interval = args.interval

print("Distance Read...")
print("Interval: %5.2f" % read_interval )

def init_logging(self, log_level = 'WARNING') -> None:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, log_level))
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(console_handler)

with Sensor(pin_trigger=7, pin_echo=11) as sensor:
        sensor.init_logging('INFO')
        while(True):
                print("Distance: %5.2f in" % sensor.distance_in_inches())
                time.sleep(read_interval)
