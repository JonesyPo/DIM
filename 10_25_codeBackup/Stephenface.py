# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths

degree_0 = 102
degree_30 = 171
degree_45 = 206
degree_60 = 240
degree_70 = 263
degree_80 = 286
degree_90 = 310
degree_100 = 333
degree_110 = 356
degree_120 = 379
degree_135 = 414
degree_150 = 448
degree_160 = 471
degree_180 = 505



# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)

print('Moving servo on channel 0, press Ctrl-C to quit...')
#while True:
    # Move servo on channel O between extremes.
def Eye_Center():
    pwm.set_pwm(5,0,degree_110)

def eyeLidsOpen():
    pwm.set_pwm(1,0,degree_150) #Left eye lid open
    pwm.set_pwm(2,0,degree_60) #Right eye lid open
    #time.sleep(1)

def eyeLidsClose():
    pwm.set_pwm(1,0,degree_90) #Left eye lid close
    pwm.set_pwm(2,0,degree_120) #Right eye lid close
    #time.sleep(1)

def eyeLidSquint():
    pwm.set_pwm(1,0,degree_120)
    pwm.set_pwm(2,0,degree_90)

def eyesVerUp():
    pwm.set_pwm(6,0,degree_60) #Eye Ver
    #pwm.set_pwm(7,0,240)
    #pwm.set_pwm(1,0,448)
    #pwm.set_pwm(2,0,240)
    #time.sleep(1)

def eyesVerUpMed():
    pwm.set_pwm(6,0,degree_80)

def eyesVerDown():
    pwm.set_pwm(6,0,degree_100) #Eye Ver
    #pwm.set_pwm(7,0,333)
    #pwm.set_pwm(1,0,310)
    #pwm.set_pwm(2,0,379)
    #time.sleep(1)

def Eye_Hor_Left():
    pwm.set_pwm(5,0,degree_160) #Eye Hor

def Eye_Brow_up():
    pwm.set_pwm(4,0,degree_160) #EyeBrow
    #pwm.set_pwm(1,0,448)
    #pwm.set_pwm(2,0,240)
    #time.sleep(1)

def eyeBrowLevel():
    pwm.set_pwm(4,0,degree_110);

def eyeBrowTiltUp():
    pwm.set_pwm(4,0,degree_135);

def Eye_Hor_Right():
    pwm.set_pwm(5,0,degree_80) #Eye Hor

def Eye_Brow_down():
    pwm.set_pwm(4,0,degree_80) #EyeBrow
#wm.set_pwm(1,0,310)
    #pwm.set_pwm(2,0,379)
    #time.sleep(1)

def mouthOpen():
    pwm.set_pwm(8,0,degree_0) #Mouth open
    #time.sleep(0.5)

def mouthHalfOpen():
    pwm.set_pwm(8,0,degree_45)

def mouthClose():
    pwm.set_pwm(8,0,degree_60) #Mouth Close
    #time.sleep(0.5)

while True:
    Eye_Center()
    time.sleep(1)
    eyeBrowLevel()
    
    time.sleep(1)
     #eyeLid
    eyesVerDown()
    time.sleep(1)
    mouthOpen()
    time.sleep(1)
    eyeLidsClose()
    time.sleep(1)
    eyeBrowTiltUp()
    time.sleep(1)
    
    eyeLidSquint()
    time.sleep(1)
    mouthHalfOpen() 
    time.sleep(1)
    eyesVerUpMed()
    time.sleep(5)
 #Eye_Brow_up()
    #time.sleep(1)
    #Eye_Brow_down()
    #time.sleep(1)
    #eyeBrowUpHalf()
    #time.sleep(2)
    #eyeBrowDownHalf()
       #time.sleep(2)
       #eyeLidSquint()
       #time.sleep(2)
       #mouthHalfOpen()
       
    
 
    
