# -*- coding: utf-8 -*-
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import time
import RPi.GPIO as GPIO
import smbus
import datetime
import json
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/pi/syspro-chapter8.json"

cred = credentials.Certificate('/home/pi/syspro-chapter8.json')
firebase_admin.initialize_app(cred)
i2c = smbus.SMBus(1)
address = 0x48

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, GPIO.HIGH)
time.sleep(1)
GPIO.output(14, GPIO.LOW)

db = firestore.Client()

#  ^b  ^c  ^c  ^c^p ^c^c ^b  ^v  ^u  ^b^r  ^| ^h^p ^a^y ^b^k
def on_snapshot(doc_snapshot, changes, read_time):
    for change in changes:
        print(u'New cmd: {}'.format(change.document.id))
        led = change.document.to_dict()["led"]
        print(u'LED: {}'.format(led))
        if led == "ON":
            print "ON"
            # ON ^a  ^a^y ^b^k ^g
            GPIO.output(14, GPIO.HIGH)
        elif led == "OFF":
            print "OFF"
            # OFF ^a  ^a^y ^b^k ^g  ^p^f
            GPIO.output(14, GPIO.LOW)

on_ref = db.collection('led').where(u'led', u'==', u'ON')
off_ref = db.collection('led').where(u'led', u'==', u'OFF')

#  ^{   ^v ^b^r ^v^k  ^k ^a^y ^b^k
doc_watch = on_ref.on_snapshot(on_snapshot)
doc_watch = off_ref.on_snapshot(on_snapshot)

#               ^w ^|  ^b  ^c  ^b  ^a^k ^b^i ^`  ^b^r ^o^v  ^w ^a^w ^a Firestore ^a  ^`^a    ^a^y ^b^k ^c  ^h^f
#  ^`^l''' ^`^m ^a  ^{  ^a  ^b^l ^a^= ^c  ^h^f ^a  ^b  ^c  ^c  ^c^h ^b  ^b  ^c^h ^a^u ^b^l ^a  ^a^d ^b^k ^a  ^a $
'''
while True:
    #        ^l        ^l  ^w ^|  ^a  ^`  ^b^r ^o^v  ^w ^a^y ^b^k
    #temp =
    #hum =
    #press =

    print("Temperature:%6.2f" %(temp))
    print("Humidity:%6.2f" %(hum))
    print("Pressure:%6.2f" %(press))
    data = {"temp": temp, "hum": hum, "press":press}
    db.collection('temperature').document(str(datetime.datetime.now())).set(data)
    time.sleep(1)
'''

#        ^b  ^c  ^b  ^a  ^n   ^z ^a  ^a^m ^a  ^a^d ^a^f ^a  ^a  ^a^s ^a  ^d  ^y^p ^c  ^c  ^c^w ^b^r    ^a^f
while True:
    pass

