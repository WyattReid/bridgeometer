#!/usr/bin/env python

import subprocess
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

BANDWIDTH_KBPS = 30000

def speed_to_meter(speed):
	
	fraction = speed / BANDWIDTH_KBPS
	return fraction*100

if __name__ == '__main__':

	command = ['ifstat','-i','eth0','-n','-w','-b']

	popen = subprocess.Popen(command, stdout=subprocess.PIPE)
	
        try:             
                for line in iter(popen.stdout.readline, ""):
                        line = line.strip(' '); line = line.strip('\n')
                        arr = line.split(' ')
                        
                        try:
                                d_speed = float(arr[0])
                                u_speed = float(arr[len(arr)-1])
                        except ValueError as e:
                                print 'e: {0}'.format(arr[0])
                                continue
                        
                        percent = speed_to_meter(u_speed)

                        print '{0:.0f} {1:.0f}%'.format(u_speed, percent)
                        
                        if percent <= 5:
                                GPIO.output(12, False)
                                GPIO.output(25, False)
                                GPIO.output(24, False)
                                GPIO.output(23, False)
                                GPIO.output(18, False)

                                GPIO.output(13, False)
                                GPIO.output(6,  False)
                                GPIO.output(5,  False)
                                GPIO.output(22, False)
                                GPIO.output(27, False) 
                        if percent <= 10:
                                GPIO.output(12, True)
                                GPIO.output(25, False)
                                GPIO.output(24, False)
                                GPIO.output(23, False)
                                GPIO.output(18, False)

                                GPIO.output(13, False)
                                GPIO.output(6,  False)
                                GPIO.output(5,  False)
                                GPIO.output(22, False)
                                GPIO.output(27, False)                        
                        elif percent <= 20:
                                GPIO.output(12, True)
                                GPIO.output(25, True)
                                GPIO.output(24, False)
                                GPIO.output(23, False)
                                GPIO.output(18, False)

                                GPIO.output(13, False)
                                GPIO.output(6,  False)
                                GPIO.output(5,  False)
                                GPIO.output(22, False)
                                GPIO.output(27, False)
                        elif percent <= 30:
                                GPIO.output(12, True)
                                GPIO.output(25, True)
                                GPIO.output(24, True)
                                GPIO.output(23, False)
                                GPIO.output(18, False)

                                GPIO.output(13, False)
                                GPIO.output(6,  False)
                                GPIO.output(5,  False)
                                GPIO.output(22, False)
                                GPIO.output(27, False)
                        elif percent <= 40:
                                GPIO.output(12, True)
                                GPIO.output(25, True)
                                GPIO.output(24, True)
                                GPIO.output(23, True)
                                GPIO.output(18, False)

                                GPIO.output(13, False)
                                GPIO.output(6,  False)
                                GPIO.output(5,  False)
                                GPIO.output(22, False)
                                GPIO.output(27, False)
                        elif percent <= 50:
                                GPIO.output(12, True)
                                GPIO.output(25, True)
                                GPIO.output(24, True)
                                GPIO.output(23, True)
                                GPIO.output(18, True)

                                GPIO.output(13, False)
                                GPIO.output(6,  False)
                                GPIO.output(5,  False)
                                GPIO.output(22, False)
                                GPIO.output(27, False)
                        elif percent <= 60:
                                GPIO.output(12, True)
                                GPIO.output(25, True)
                                GPIO.output(24, True)
                                GPIO.output(23, True)
                                GPIO.output(18, True)

                                GPIO.output(13, True)
                                GPIO.output(6,  False)
                                GPIO.output(5,  False)
                                GPIO.output(22, False)
                                GPIO.output(27, False)
                        elif percent <= 70:
                                GPIO.output(12, True)
                                GPIO.output(25, True)
                                GPIO.output(24, True)
                                GPIO.output(23, True)
                                GPIO.output(18, True)

                                GPIO.output(13, True)
                                GPIO.output(6,  True)
                                GPIO.output(5,  False)
                                GPIO.output(22, False)
                                GPIO.output(27, False)
                        elif percent <= 80:
                                GPIO.output(12, True)
                                GPIO.output(25, True)
                                GPIO.output(24, True)
                                GPIO.output(23, True)
                                GPIO.output(18, True)

                                GPIO.output(13, True)
                                GPIO.output(6,  True)
                                GPIO.output(5,  True)
                                GPIO.output(22, False)
                                GPIO.output(27, False)
                        elif percent <= 90:
                                GPIO.output(12, True)
                                GPIO.output(25, True)
                                GPIO.output(24, True)
                                GPIO.output(23, True)
                                GPIO.output(18, True)

                                GPIO.output(13, True)
                                GPIO.output(6,  True)
                                GPIO.output(5,  True)
                                GPIO.output(22, True)
                                GPIO.output(27, False)
                        else:
                                GPIO.output(12, True)
                                GPIO.output(25, True)
                                GPIO.output(24, True)
                                GPIO.output(23, True)
                                GPIO.output(18, True)

                                GPIO.output(13, True)
                                GPIO.output(6,  True)
                                GPIO.output(5,  True)
                                GPIO.output(22, True)
                                GPIO.output(27, True)
        except KeyboardInterrupt as e:
                GPIO.cleanup()
                                
                                

                




