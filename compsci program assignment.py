#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging
import random
from psychopy.hardware import keyboard

defaultKeyboard = keyboard.Keyboard()
event.globalKeys.add(key='q', func=core.quit)

subgui = gui.Dlg()

subgui.addField("SubjectNumber:")
subgui.addField("Age:")
subgui.addField("Gender:")
subgui.addField("Handedness:")

subgui.show()

subID = subgui.data[0]
subAge = subgui.data[1]
subGender = subgui.data[2]
subHand = subgui.data[3]

if subgui.OK == False:
    core.quit()  # user pressed cancel
    
outputFileName = 'subID' + '.csv'
outVars = ['trial', 'cond', 'target_side', 'RT', 'MT', 'landing_position', 'accuracy']

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='grey', unit='height') 

# set up mouse
mouse = event.Mouse(visible=False)

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()

#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things

# Setting up instructions
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Welcome to the experiment.\n\nIn this experiment, you will be using the arrow keys to detect a target as quickly and accurately as \npossible.\n\nPress space to continue.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

Instructions = visual.TextStim(win=win, name='Instructions',
    text='On every trial, a central fixation cross will appear.\nKeeping your eyes on the central fixation cross, press space, and the trial will begin. Then, the target will appear.\n\nPress space to continue.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

instructions_part2 = visual.TextStim(win=win, name='instructions_part2',
    text='Your task is to indicate with a left key press or right key press what side \nthe target appeared on, keeping your eyes at central fixation.\n\nPress space to begin practice.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    

# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']

# make your loop
# for t in 
    
    # include your trial code in your loop but replace anything that should 
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!
    
# Loop through the instructions

welcome_sequence = [welcome_text, Instructions, instructions_part2]
for item in welcome_sequence:
    event.clearEvents()
    item.draw()
    win.flip()
    keys = event.waitKeys(keyList='space')

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

#out = pd.DataFrame(columns=outVars)

core.wait(2)
win.close()