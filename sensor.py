'''
Sensor reading class for interacting with the sensor
Inits sensor and allows for reading distance
'''
import RPi.GPIO as GPIO
import time
import logging

SPEED_OF_SOUND_IN_CM_PER_S = 34300.0

class Sensor:
    def __init__(self, pin_trigger, pin_echo) -> None:
        self.init_logging()
        GPIO.setmode(GPIO.BOARD)
        self.PIN_TRIGGER = pin_trigger
        self.PIN_ECHO = pin_echo
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
        logging.info("Waiting for sensor to settle")
        time.sleep(5)
        logging.info("Calculating distance")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        GPIO.cleanup()

    def init_logging(self, log_level = 'WARNING') -> None:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, log_level))
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(console_handler)

    def pulse(self, interval = 0.00001) -> None:
        GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

    def distance_in_inches(self) -> float:
        self.pulse()
        while GPIO.input(self.PIN_ECHO)==0:
                pulse_start_time = time.time()
        while GPIO.input(self.PIN_ECHO)==1:
                pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time
        roundtrip_distance_in_cm = SPEED_OF_SOUND_IN_CM_PER_S * pulse_duration
        distance_in_inches = roundtrip_distance_in_cm / 2.0 / 2.54
        return distance_in_inches
