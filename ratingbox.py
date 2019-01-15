import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import json
import operator
import time
import random
import os

alpha = 0.01
q = {}
def opentable():
    with open('q.json', 'r') as f:
        qtable = json.load(f)
    return qtable


def saveqtable(q):
    global table
    table = json.dumps(q)
    f=open("q.json","w")
    f.write(table)
    f.close()

def wfr(): #wait for rating
    print("im in")
    GPIO.add_event_detect(10, GPIO.RISING)
    GPIO.add_event_detect(12, GPIO.RISING)
    GPIO.add_event_detect(16, GPIO.RISING)
    GPIO.add_event_detect(15, GPIO.RISING)
    GPIO.add_event_detect(11, GPIO.RISING)
    GPIO.add_event_detect(8,GPIO.RISING)
    global r
    r = None
    while r is None:
        if GPIO.event_detected(10):
            GPIO.remove_event_detect(10)
            GPIO.remove_event_detect(12)
            GPIO.remove_event_detect(16)
            GPIO.remove_event_detect(15)
            GPIO.remove_event_detect(11)
            GPIO.remove_event_detect(8)
            time.sleep(0.2)
            r = -1
        elif GPIO.event_detected(12):
            GPIO.remove_event_detect(10)
            GPIO.remove_event_detect(12)
            GPIO.remove_event_detect(16)
            GPIO.remove_event_detect(15)
            GPIO.remove_event_detect(11)
            GPIO.remove_event_detect(8)
            time.sleep(0.2)
            r = -0.5
            #GPIO.remove_event_detect(12)
        elif GPIO.event_detected(16):
            GPIO.remove_event_detect(10)
            GPIO.remove_event_detect(12)
            GPIO.remove_event_detect(16)
            GPIO.remove_event_detect(15)
            GPIO.remove_event_detect(11)
            GPIO.remove_event_detect(8)
            time.sleep(0.2)
            r = 0
            #GPIO.remove_event_detect(16)
        elif GPIO.event_detected(15):
            GPIO.remove_event_detect(10)
            GPIO.remove_event_detect(12)
            GPIO.remove_event_detect(16)
            GPIO.remove_event_detect(15)
            GPIO.remove_event_detect(11)
            GPIO.remove_event_detect(8)
            time.sleep(0.2)
            r = 0.5
            #GPIO.remove_event_detect(15)
        elif GPIO.event_detected(11):
            GPIO.remove_event_detect(10)
            GPIO.remove_event_detect(12)
            GPIO.remove_event_detect(16)
            GPIO.remove_event_detect(15)
            GPIO.remove_event_detect(11)
            GPIO.remove_event_detect(8)
            time.sleep(0.2)
            r = 1
            #GPIO.remove_event_detect(11)
        #elif GPIO.event_detected(8):    #3 seconden vasthouden
        #    time.sleep(2)
         #   if GPIO.event_detected(8):
         #       quit()
    print (r)

    q[max(q.items(), key=operator.itemgetter(1))[0]]=(1-alpha)*q[max(q.items(), key=operator.itemgetter(1))[0]]+ alpha * r


    print ("ik zou klaar moeten zijn")
    saveqtable(q)


q = opentable()

run = 1
while run == 1:


    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



    print("push the button!")

    channel = GPIO.wait_for_edge(8, GPIO.RISING, timeout=5000)
    if channel is None:
        print('Timeout occurred')
    else:
        print('Edge detected on channel', channel)
        print(max(q.items(), key=operator.itemgetter(1))[0],max(q.items(), key=operator.itemgetter(1))[1])
        senfilname = max(q.items(), key=operator.itemgetter(1))[0]
        print (senfilname)
        with open('%s'  %senfilname,'r') as zin:
            vragen = json.load(zin)
        secure_random = random.SystemRandom()
        vraag = secure_random.choice(vragen)
        print(vraag)
        os.system('flite -voice /home/pi/Downloads/cmu_us_rms.flitevox -t "%s"'  %vraag)
        print("how do you like this subject?")
        wfr()



