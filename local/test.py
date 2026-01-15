import argparse
import time
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
import numpy as np

parser = argparse.ArgumentParser(description="Motor Testing Script!")
parser.add_argument('-e', '--esc', type=int, default=1, help='ESC channel (default:1)')
parser.add_argument('-s', '--servo', type=int, default=0, help='Servo channel (default:0)')
parser.add_argument('-i', '--initialize', type=int, default = "0", help='Is the motor running for the first time since being switched on? (default: 0)')
parser.add_argument('--extra_option', type=str, default="", help='Message to explain the option (default: empty string)') #Template for additional arguments
args = parser.parse_args()
ESC_CHANNEL = args.esc
SERVO_CHANNEL = args.servo
#If the motor is running for the first time since being switched on, the ESC needs to be "armed" (meaning that we need to send a neutral signal for 2 seconds)
arm_ESC = args.initialize
extra_argument = args.extra_option

# === Constants ===
FREQ = 60 # Standard ESC expects 50-60Hz signal
NETURAL = 1500
MAX = 1900
MIN = 1200

# === Setup I2C and PCA9685 ===
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = FREQ

# === Give time for ESC to initialize ===
time.sleep(2)

# === Run motor testing sequence ===
pca.channels[ESC_CHANNEL].duty_cycle = 3500
time.sleep(1)

# === Tear down PCA board data structure ===
pca.deinit()