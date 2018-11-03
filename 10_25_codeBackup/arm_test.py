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

##Pulse length to degrees
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

#pwm channel number on PWM Driver
pwm_channel_0 = 0
pwm_channel_1 = 1
pwm_channel_2 = 2
pwm_channel_3 = 3
pwm_channel_4 = 4
pwm_channel_5 = 5
pwm_channel_6 = 6
pwm_channel_7 = 7
pwm_channel_8 = 8
pwm_channel_9 = 9
pwm_channel_10 = 10
pwm_channel_11 = 11
pwm_channel_12 = 12
pwm_channel_13 = 13
pwm_channel_14 = 14
pwm_channel_15 = 15

#Class Face contains methods for the Facial expressions
class Face:
    
    def __init__ (self):
        print ("init")

    def Right_Eyebrow(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def Left_Eyebrow(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def Eye_Center(self,channel,degree):
        #110
        pwm.set_pwm(channel,0,degree)
    
    def Mouth(self,channel,degree):
        #60 open | 0 close
        pwm.set_pwm(channel,0,degree)
    
    def Left_Eye_Lid(self,channel,degree):
        #150 open | 90 close
        pwm.set_pwm(channel,0,degree)
    
    def Right_Eye_Lid(self,channel,degree):
        #60 open | 120 close
        pwm.set_pwm(channel,0,degree)

    def Eye_Vertical(self,channel,degree):
        #60 up | 100 down
        pwm.set_pwm(channel,0,degree)
    
    def Eye_Horizontal(self,channel,degree):
        #160 left | 80 Right
        pwm.set_pwm(channel,0,degree)

    def Face_Reset(self):
        #self.Eye_Center(pwm_channel_5,degree_110)
        self.Right_Eyebrow(pwm_channel_4,degree_120)
        self.Left_Eyebrow(pwm_channel_4,degree_120)
        self.Mouth(pwm_channel_8,degree_0)
        self.Left_Eye_Lid(pwm_channel_1,degree_150)
        self.Right_Eye_Lid(pwm_channel_2,degree_60)
        self.Eye_Vertical(pwm_channel_6,degree_80)
        self.Eye_Horizontal(pwm_channel_5,degree_120)
        print("Reset is done")

    def Excited(self):
        Robo_face.Mouth(pwm_channel_8,degree_45)
        Robo_face.Left_Eyebrow(pwm_channel_4,degree_150)
        Robo_face.Left_Eye_Lid(pwm_channel_1,degree_90)
        Robo_face.Right_Eye_Lid(pwm_channel_2,degree_120)
        time.sleep(0.5)
        Robo_face.Right_Eyebrow(pwm_channel_4,degree_120)
        Robo_face.Mouth(pwm_channel_8,degree_60)
        Robo_face.Left_Eye_Lid(pwm_channel_1,degree_100)
        Robo_face.Right_Eye_Lid(pwm_channel_2,degree_110)
        time.sleep(0.15)


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


#if __name__ == "main":

# Set frequency to 50hz, good for servos.
pwm.set_pwm_freq(50)
print('Moving servo on channel 0, press Ctrl-C to quit...')

k = 0

while True:
    i = 0
    j = 0
    
    pwm.set_pwm(pwm_channel_14,0,degree_150)
    time.sleep(1.5)

    while i < 30:
        pwm.set_pwm(pwm_channel_13,0,degree_100)
        time.sleep(0.3)
        pwm.set_pwm(pwm_channel_13,0,degree_80)
        time.sleep(0.3)
        i = i + 1
        print(i)
        
        

    pwm.set_pwm(pwm_channel_13,0,degree_120)
    time.sleep(1)
    pwm.set_pwm(pwm_channel_14,0,degree_100)
    time.sleep(1.5)
    
    while (j < 30):
        pwm.set_pwm(pwm_channel_13,0,degree_100)
        time.sleep(0.3)
        pwm.set_pwm(pwm_channel_13,0,degree_80)
        time.sleep(0.3)
        j = j + 1
    
    pwm.set_pwm(pwm_channel_14,0,degree_150)
    time.sleep(1.5)
    
  
