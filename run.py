#!/usr/bin/env python -W ignore::DeprecationWarning
# -*- coding: utf-8 -*-

import app_online_flt as app
import path_load
import os
from  helpers import *
import pandas as pd
#==============================================================================#
# Define global variables.
#==============================================================================#

# Port adress of OpenBCI Cyton board

# BCI_PORT = '/dev/tty.usbserial-DM00CVLC'
#BCI_PORT = path_load.PortDiscover().port

#==============================================================================#
# Run application
#==============================================================================#
# connect { if connect on start? }
# electrodes { number of connected electrodes to process}
# time_run { time of trial in seconds }
# mode { one of two modes }
# // mode 1
# Harmonic reference
# // mode 2
# Subharmonic reference

# Initialize app

#==============================================================================#
# CONFIGURATION
#==============================================================================#

test = app.CcaLive(
port='/dev/tty.usbserial-DM00CVLC',
sampling_rate=250,
connect=True,
electrodes=2,
time_run=30,
save=False,
ip_slave='192.168.0.17'
)
#==============================================================================#
#==============================================================================#


#==============================================================================#
# Initialize // DO NOT CHANGE ANYTHING //
#==============================================================================#

print("Number of acquired electrodes: {}".format(test.electrodes))
print("Time of trial: {}".format(test.time_run))
print("Sampling rate: {}".format(test.sampling_rate))
print("Connected on serial port: {}".format(test.bci_port))
print("Number of trial/subject: ", make_next())
print("".join(["=" for x in range(32)]))

#==============================================================================#
# CONFIGURATION
#==============================================================================#
# Add references signal /
# Stimulus for experiment. Max amount = 4.
# ========================== #
test.add_stimuli(11)
test.add_stimuli(12)
test.add_stimuli(14)
# ========================== #


SUBJ = int(input("Subject: "))


#==============================================================================#


#==============================================================================#
# LEAVE BELOW THIS PART // DO NOT CHANGE ANYTHING //
#==============================================================================#





print("".join(["=" for x in range(32)]))

print("Starting application...")
test.decission()

try:
    test.get_correlation()
except AttributeError as e:
    pass

# Make sure it's dead.
if test.prcs.is_alive():
    print("Terminating process...")
    test.prcs.terminate()
    print("Done!")

create_subject_from_file(SUBJ)



import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("outputs/SUBJ"+str(SUBJ)+"-results.csv", delimiter=',', engine='python')

bodziec_1 = []
bodziec_2 = []
bodziec_3 = []


for i,j in enumerate(dane.iloc[2:,2]):
    if i % 3 == 0:
        bodziec_1.append(j)
    elif i % 3 == 1:
        bodziec_2.append(j)
    elif i % 3 == 2:
        bodziec_3.append(j)



len(bodziec_3)

plt.plot(bodziec_1, label=str(test.reference_signals[0].hz))
plt.plot(bodziec_2, label=str(test.reference_signals[1].hz))
plt.plot(bodziec_3, label=str(test.reference_signals[2].hz))
plt.legend()
#plt.title(str(input("Title: ")))
plt.show()
#plt.savefig(str(input("Save as ")) + '.png')
