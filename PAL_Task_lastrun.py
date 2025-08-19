#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on August 18, 2025, at 18:07
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware, iohub
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from Stimulation_Calib_Code
import os
import sys
import ctypes

# --- Step 1: Set paths ---
ds8r_dir = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
dll_path = os.path.join(ds8r_dir, "D128RProxy.dll")

# --- Step 2: Load the DLL manually ---
try:
    ctypes.WinDLL(dll_path)
    print("✅ DLL loaded manually.")
except Exception as e:
    print(f"❌ DLL load failed: {e}")

# --- Step 3: Update working directory and sys.path ---
os.chdir(ds8r_dir)
sys.path.append(ds8r_dir)

# --- Step 4: Import DS8R module ---
from ds8r import DS8R
print("✅ DS8R module imported successfully.")

import threading

# Run 'Before Experiment' code from Stimulation_Calib_Code_2
import os
import sys
import ctypes

# --- Step 1: Set paths ---
ds8r_dir = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
dll_path = os.path.join(ds8r_dir, "D128RProxy.dll")

# --- Step 2: Load the DLL manually ---
try:
    ctypes.WinDLL(dll_path)
    print("✅ DLL loaded manually.")
except Exception as e:
    print(f"❌ DLL load failed: {e}")

# --- Step 3: Update working directory and sys.path ---
os.chdir(ds8r_dir)
sys.path.append(ds8r_dir)

# --- Step 4: Import DS8R module ---
from ds8r import DS8R
print("✅ DS8R module imported successfully.")

import threading

# Run 'Before Experiment' code from Stimulation_Calib_Code_3
import os
import sys
import ctypes

# --- Step 1: Set paths ---
ds8r_dir = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
dll_path = os.path.join(ds8r_dir, "D128RProxy.dll")

# --- Step 2: Load the DLL manually ---
try:
    ctypes.WinDLL(dll_path)
    print("✅ DLL loaded manually.")
except Exception as e:
    print(f"❌ DLL load failed: {e}")

# --- Step 3: Update working directory and sys.path ---
os.chdir(ds8r_dir)
sys.path.append(ds8r_dir)

# --- Step 4: Import DS8R module ---
from ds8r import DS8R
print("✅ DS8R module imported successfully.")

import threading

# Run 'Before Experiment' code from Shock_Code
import os
import sys
import ctypes

# --- Step 1: Set paths ---
ds8r_dir = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
dll_path = os.path.join(ds8r_dir, "D128RProxy.dll")

# --- Step 2: Load the DLL manually ---
try:
    ctypes.WinDLL(dll_path)
    print("✅ DLL loaded manually.")
except Exception as e:
    print(f"❌ DLL load failed: {e}")

# --- Step 3: Update working directory and sys.path ---
os.chdir(ds8r_dir)
sys.path.append(ds8r_dir)

# --- Step 4: Import DS8R module ---
from ds8r import DS8R
print("✅ DS8R module imported successfully.")

import threading


# Run 'Before Experiment' code from Stimulation_Calib_Code_4
import os
import sys
import ctypes

# --- Step 1: Set paths ---
ds8r_dir = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
dll_path = os.path.join(ds8r_dir, "D128RProxy.dll")

# --- Step 2: Load the DLL manually ---
try:
    ctypes.WinDLL(dll_path)
    print("✅ DLL loaded manually.")
except Exception as e:
    print(f"❌ DLL load failed: {e}")

# --- Step 3: Update working directory and sys.path ---
os.chdir(ds8r_dir)
sys.path.append(ds8r_dir)

# --- Step 4: Import DS8R module ---
from ds8r import DS8R
print("✅ DS8R module imported successfully.")

import threading

# Run 'Before Experiment' code from Stimulation_Calib_Code_5
import os
import sys
import ctypes

# --- Step 1: Set paths ---
ds8r_dir = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
dll_path = os.path.join(ds8r_dir, "D128RProxy.dll")

# --- Step 2: Load the DLL manually ---
try:
    ctypes.WinDLL(dll_path)
    print("✅ DLL loaded manually.")
except Exception as e:
    print(f"❌ DLL load failed: {e}")

# --- Step 3: Update working directory and sys.path ---
os.chdir(ds8r_dir)
sys.path.append(ds8r_dir)

# --- Step 4: Import DS8R module ---
from ds8r import DS8R
print("✅ DS8R module imported successfully.")

import threading
# Run 'Before Experiment' code from Stimulation_Calib_Code_6
import os
import sys
import ctypes

# --- Step 1: Set paths ---
ds8r_dir = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
dll_path = os.path.join(ds8r_dir, "D128RProxy.dll")

# --- Step 2: Load the DLL manually ---
try:
    ctypes.WinDLL(dll_path)
    print("✅ DLL loaded manually.")
except Exception as e:
    print(f"❌ DLL load failed: {e}")

# --- Step 3: Update working directory and sys.path ---
os.chdir(ds8r_dir)
sys.path.append(ds8r_dir)

# --- Step 4: Import DS8R module ---
from ds8r import DS8R
print("✅ DS8R module imported successfully.")

import threading

# Run 'Before Experiment' code from Shock_Code_2
import os
import sys
import ctypes

# --- Step 1: Set paths ---
ds8r_dir = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
dll_path = os.path.join(ds8r_dir, "D128RProxy.dll")

# --- Step 2: Load the DLL manually ---
try:
    ctypes.WinDLL(dll_path)
    print("✅ DLL loaded manually.")
except Exception as e:
    print(f"❌ DLL load failed: {e}")

# --- Step 3: Update working directory and sys.path ---
os.chdir(ds8r_dir)
sys.path.append(ds8r_dir)

# --- Step 4: Import DS8R module ---
from ds8r import DS8R
print("✅ DS8R module imported successfully.")

import threading



# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'PAL_Task'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'Participant.ID': 'P00X',
    'Visit': 'Pre / Post',
    'Task Version (required)': '1–3',
    'fMRI_enabled': 'No',
    'Stim_Cal_enabled': 'Yes',
    'Electrode_Loc': 'LN or UN or Cross',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1680, 1050]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['Participant.ID'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\PERLadmin\\Desktop\\No_EyeTr\\PAL\\PAL_Task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='Eyetracker_Monitor', color=[-0.3000, -0.3000, -0.3000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-0.3000, -0.3000, -0.3000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('Instr_Key1') is None:
        # initialise Instr_Key1
        Instr_Key1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Instr_Key1',
        )
    if deviceManager.getDevice('Instr_Key2') is None:
        # initialise Instr_Key2
        Instr_Key2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Instr_Key2',
        )
    if deviceManager.getDevice('Instr_Key3') is None:
        # initialise Instr_Key3
        Instr_Key3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Instr_Key3',
        )
    if deviceManager.getDevice('Instr_Key4') is None:
        # initialise Instr_Key4
        Instr_Key4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Instr_Key4',
        )
    if deviceManager.getDevice('Cali_Instr_Keyboard') is None:
        # initialise Cali_Instr_Keyboard
        Cali_Instr_Keyboard = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Cali_Instr_Keyboard',
        )
    if deviceManager.getDevice('Cali_Instr_Keyboard_2') is None:
        # initialise Cali_Instr_Keyboard_2
        Cali_Instr_Keyboard_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Cali_Instr_Keyboard_2',
        )
    if deviceManager.getDevice('slider_keys') is None:
        # initialise slider_keys
        slider_keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='slider_keys',
        )
    if deviceManager.getDevice('slider_keys2') is None:
        # initialise slider_keys2
        slider_keys2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='slider_keys2',
        )
    if deviceManager.getDevice('slider_keys3') is None:
        # initialise slider_keys3
        slider_keys3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='slider_keys3',
        )
    if deviceManager.getDevice('Instr_Key5') is None:
        # initialise Instr_Key5
        Instr_Key5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Instr_Key5',
        )
    if deviceManager.getDevice('Scanner_control') is None:
        # initialise Scanner_control
        Scanner_control = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Scanner_control',
        )
    if deviceManager.getDevice('Estimation_Select') is None:
        # initialise Estimation_Select
        Estimation_Select = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Estimation_Select',
        )
    if deviceManager.getDevice('Post_break_keys') is None:
        # initialise Post_break_keys
        Post_break_keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Post_break_keys',
        )
    if deviceManager.getDevice('Recal_Procced_Keys') is None:
        # initialise Recal_Procced_Keys
        Recal_Procced_Keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Recal_Procced_Keys',
        )
    if deviceManager.getDevice('slider_keys_2') is None:
        # initialise slider_keys_2
        slider_keys_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='slider_keys_2',
        )
    if deviceManager.getDevice('slider_keys2_2') is None:
        # initialise slider_keys2_2
        slider_keys2_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='slider_keys2_2',
        )
    if deviceManager.getDevice('slider_keys3_2') is None:
        # initialise slider_keys3_2
        slider_keys3_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='slider_keys3_2',
        )
    if deviceManager.getDevice('Instr_Key5_2') is None:
        # initialise Instr_Key5_2
        Instr_Key5_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Instr_Key5_2',
        )
    if deviceManager.getDevice('Estimation_Select_2') is None:
        # initialise Estimation_Select_2
        Estimation_Select_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Estimation_Select_2',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Initialisation" ---
    # Run 'Begin Experiment' code from Background_Box
    from psychopy import visual
    
    grayBox = visual.rect.Rect(win, width=0.8, height=0.8, units='', lineWidth=0, lineColor=None, lineColorSpace=None, fillColor=[0.004, 0.004, 0.004], fillColorSpace='none', pos=(0, 0))
    # Run 'Begin Experiment' code from Task_Version_Select
    from psychopy import core, visual, event
    
    # get and clean your version string
    TaskVersion = expInfo['Task Version (required)'].strip()
    
    # pick your files based on version
    if TaskVersion == '1':
        basePath = 'Conditions/Version_1/'
    elif TaskVersion == '2':
        basePath = 'Conditions/Version_2/'
    elif TaskVersion == '3':
        basePath = 'Conditions/Version_3/'
    else:
        # show error message on screen
        errMsg = visual.TextStim(
            win=win,
            text="Warning: Must enter a valid task version number\n(i.e., 1, 2 or 3). \n\n Press any key to quit.",
            color='black',
            height=0.025
        )
        errMsg.draw()
        win.flip()
        # wait for any key before quitting
        event.waitKeys()
        core.quit()
    
    # if we get here, version was valid
    VersionSelection_H1 = basePath + f'PAL_Deterministic Schedule_V{TaskVersion}_H1.xlsx'
    VersionSelection_H2 = basePath + f'PAL_Deterministic Schedule_V{TaskVersion}_H2.xlsx'
    
    # Run 'Begin Experiment' code from Initialise_Selection_Outcome_and_StimDefault
    selectedColor = 'grey'
    last_demand = 30
    last_pulse_width = 300
    # Run 'Begin Experiment' code from Initialise_Stim_Cali_Skip
    StimCalEnabled = expInfo.get('Stim_Cal_enabled', 'no')
    
    
    # --- Initialize components for Routine "Instructions" ---
    # Run 'Begin Experiment' code from Text_Code
    from psychopy import visual, core, event
    
    # One text stim per color segment
    text_black = visual.TextStim(
        win,
        text="Welcome to the PAL task",
        color='black',
        pos=(-0.55, 0.25),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_blue = visual.TextStim(
        win,
        text=f"ver. {TaskVersion}",
        color='lightblue',
        pos=(-0.3285, 0.25),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    
    text_further = visual.TextStim(
        win,
        text=f"During this task, you must work out if \n a given image will result in stimulation or not.",
        color='black',
        pos=(-0.5, 0.05),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    
    text_further2 = visual.TextStim(
        win,
        text=f"The probability of stimulation can change at any point.\n You must learn this probability throughout the task.",
        color='black',    
        pos=(-0.5, -0.05),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    
    text_further3 = visual.TextStim(
        win,
        text=f"Press ← or → to continue.",
        color='black',
        pos=(-0.5, -0.25),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    
    
    Instr_Key1 = keyboard.Keyboard(deviceName='Instr_Key1')
    
    # --- Initialize components for Routine "Instructions_2" ---
    # Run 'Begin Experiment' code from Text_code_2
    from psychopy import visual, core, event
    
    # One text stim per color segment
    text_black3 = visual.TextStim(
        win,
        text="You must indicate what the image will \n result in by pressing ← or →.",
        color='black',
        pos=(-0.5, 0.25),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_black4 = visual.TextStim(
        win,
        text="→ means stimulation will occur. It will display: ",
        color='black',
        pos=(-0.55, 0.1),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_black5 = visual.TextStim(
        win,
        text="← means nothing will occur. It will display:  ",
        color='black',
        pos=(-0.525, 0.0),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_further3 = visual.TextStim(
        win,
        text=f"Press ← or → to continue.",
        color='black',
        pos=(-0.5, -0.25),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    
    example_image1 = visual.ImageStim(
        win=win,
        image='Extra_img/Square_shock.png',
        pos=(0.28, 0.095),      # adjust to your desired screen location
        size=(0.035, 0.035)       # scale image as needed (in norm units or pixels)
    )
    
    example_image2 = visual.ImageStim(
        win=win,
        image='Extra_img/Square_noshock.png',
        pos=(0.28, -0.0025),      # adjust to your desired screen location
        size=(0.035, 0.035)       # scale image as needed (in norm units or pixels)
    )
    Instr_Key2 = keyboard.Keyboard(deviceName='Instr_Key2')
    
    # --- Initialize components for Routine "Instructions_3" ---
    # Run 'Begin Experiment' code from Text_code_3
    from psychopy import visual, core, event
    
    # One text stim per color segment
    text_ISI_instr1 = visual.TextStim(
        win,
        text="When you make a choice, this cross wil appear: ",
        color='black',
        pos=(-0.5, 0.25),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_ISI_instr2 = visual.TextStim(
        win,
        text="Please focus on the cross while it appears.",
        color='black',
        pos=(-0.5, 0.125),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_ISI_instr3 = visual.TextStim(
        win,
        text="When an event has occured (i.e. stimulation or not), \n the cross will change colour:",
        color='black',
        pos=(-0.5, 0.0),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_ISI_instr4 = visual.TextStim(
        win,
        text=f"Press ← or → to continue.",
        color='black',
        pos=(-0.5, -0.25),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    
    example_image3 = visual.ImageStim(
        win=win,
        image='Extra_img/inter_ISI.png',
        pos=(0.34, 0.248),      # adjust to your desired screen location
        size=(0.05, 0.055)       # scale image as needed (in norm units or pixels)
    )
    
    example_image4 = visual.ImageStim(
        win=win,
        image='Extra_img/Event_Fixation.png',
        pos=(0.22, -0.0185),      # adjust to your desired screen location
        size=(0.05, 0.05)       # scale image as needed (in norm units or pixels)
    )
    Instr_Key3 = keyboard.Keyboard(deviceName='Instr_Key3')
    
    # --- Initialize components for Routine "Instructions_4" ---
    # Run 'Begin Experiment' code from Text_code
    from psychopy import visual, core, event
    
    # One text stim per color segment
    text_ISI_instr5 = visual.TextStim(
        win,
        text="There will be a break halfway (~14 mins).",
        color='black',
        pos=(-0.5, 0.15),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_ISI_instr6 = visual.TextStim(
        win,
        text="You will now begin calibration (if appropriate).",
        color='black',
        pos=(-0.5, 0.0),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_ISI_instr7 = visual.TextStim(
        win,
        text=f"Press ← or → to continue.",
        color='black',
        pos=(-0.5, -0.25),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    
    
    Instr_Key4 = keyboard.Keyboard(deviceName='Instr_Key4')
    
    # --- Initialize components for Routine "Shock_Calib_Instr" ---
    # Run 'Begin Experiment' code from Shock_Cali_Instr_Text
    from psychopy import visual, core, event
    
    # One text stim per color segment
    text_shockcal_instr1 = visual.TextStim(
        win,
        text="We will now determine your stimulation threshold.",
        color='black',
        pos=(-0.5, 0.15),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_shockcal_instr2 = visual.TextStim(
        win,
        text="Starting low, we will gradually increase the stimulation.",
        color='black',
        pos=(-0.5, 0.05),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_shockcal_instr3 = visual.TextStim(
        win,
        text="We wish to understand your 80% stimulation threshold.",
        color='black',
        pos=(-0.5, -0.05),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_shockcal_instr4 = visual.TextStim(
        win,
        text=f"Press ← or → to continue.",
        color='black',
        pos=(-0.5, -0.25),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    Cali_Instr_Keyboard = keyboard.Keyboard(deviceName='Cali_Instr_Keyboard')
    
    # --- Initialize components for Routine "Shock_Calib_Instr2" ---
    # Run 'Begin Experiment' code from Shock_Cali_Instr_Text_2
    from psychopy import visual, core, event
    
    # One text stim per color segment
    text_shockcal_instr5 = visual.TextStim(
        win,
        text="On the next screen you will receive the first stimulation.",
        color='black',
        pos=(-0.5, 0.15),  # adjust as needed
        height=0.0275,
        anchorHoriz='left'
    )
    
    text_shockcal_instr6 = visual.TextStim(
        win,
        text="Please rate this from 0 - 100% using the slider provided. \n Press spacebar to confirm your rating.",
        color='black',
        pos=(-0.5, 0.05),  # adjust as needed
        height=0.0275,
        anchorHoriz='left'
    )
    
    text_shockcal_instr7 = visual.TextStim(
        win,
        text="We cannot proceed until certain about your 80% threshold.",
        color='black',
        pos=(-0.5, -0.05),  # adjust as needed
        height=0.0275,
        anchorHoriz='left'
    )
    
    text_shockcal_instr8 = visual.TextStim(
        win,
        text=f"Press ← or → to continue.",
        color='black',
        pos=(-0.5, -0.25),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    Cali_Instr_Keyboard_2 = keyboard.Keyboard(deviceName='Cali_Instr_Keyboard_2')
    
    # --- Initialize components for Routine "Pre_Shock_ISI_Calib" ---
    Pre_Cali_ISI = visual.TextStim(win=win, name='Pre_Cali_ISI',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Shock_ISI_Calib" ---
    Calib_Shock_Cross = visual.TextStim(win=win, name='Calib_Shock_Cross',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -0.6706, -0.3490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from Stimulation_Calib_Code
    last_demand = None
    last_pulse_width = None
    
    ctl = DS8R(
        demand=10,  # adjust as needed
        pulse_width=100,   # adjust as needed
        enabled=0,
        dwell=10,
        mode=1,
        polarity=1,
        source=1,
    )
    
    def safe_run():
        try:
            ctl.run()
        except Exception as e:
            print(f"DS8R trigger error: {e}")
    
    # --- Initialize components for Routine "Shock_Calib_Looper" ---
    slider_keys = keyboard.Keyboard(deviceName='slider_keys')
    pain_slider = visual.Slider(win=win, name='pain_slider',
        startValue=0, size=(0.65, 0.02), pos=(0, -0.2), units=win.units,
        labels=["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor=[-0.5, -0.5, -0.5], lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "Loop_Checkpoint" ---
    
    # --- Initialize components for Routine "Pre_Shock_ISI_Cali_Check_1" ---
    Pre_Cali_ISI_2 = visual.TextStim(win=win, name='Pre_Cali_ISI_2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Shock_ISI_Post_Check_1" ---
    Calib_Shock_Cross_2 = visual.TextStim(win=win, name='Calib_Shock_Cross_2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -0.6706, -0.3490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from Stimulation_Calib_Code_2
    ctl = DS8R(
        demand=10,  # adjust as needed
        pulse_width=100,   # adjust as needed
        enabled=0,
        dwell=10,
        mode=1,
        polarity=1,
        source=1,
    )
    
    def safe_run():
        try:
            ctl.run()
        except Exception as e:
            print(f"DS8R trigger error: {e}")
    
    
    # --- Initialize components for Routine "Shock_Calib_Looper_2" ---
    slider_keys2 = keyboard.Keyboard(deviceName='slider_keys2')
    pain_slider2 = visual.Slider(win=win, name='pain_slider2',
        startValue=0, size=(0.65, 0.02), pos=(0, -0.2), units=win.units,
        labels=["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor=[-0.5, -0.5, -0.5], lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "Pre_Shock_ISI_Cali_Check_2" ---
    Pre_Cali_ISI_3 = visual.TextStim(win=win, name='Pre_Cali_ISI_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Shock_ISI_Post_Check_2" ---
    Calib_Shock_Cross_3 = visual.TextStim(win=win, name='Calib_Shock_Cross_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -0.6706, -0.3490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from Stimulation_Calib_Code_3
    ctl = DS8R(
        demand=10,  # adjust as needed
        pulse_width=100,   # adjust as needed
        enabled=0,
        dwell=10,
        mode=1,
        polarity=1,
        source=1,
    )
    
    def safe_run():
        try:
            ctl.run()
        except Exception as e:
            print(f"DS8R trigger error: {e}")
    
    # --- Initialize components for Routine "Shock_Calib_Looper_3" ---
    slider_keys3 = keyboard.Keyboard(deviceName='slider_keys3')
    pain_slider3 = visual.Slider(win=win, name='pain_slider3',
        startValue=0, size=(0.65, 0.02), pos=(0, -0.2), units=win.units,
        labels=["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor=[-0.5, -0.5, -0.5], lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "Instructions_Final" ---
    # Run 'Begin Experiment' code from Text_code_4
    from psychopy import visual, core, event
    
    # One text stim per color segment
    
    text_ISI_instr8 = visual.TextStim(
        win,
        text="You will now begin the task.",
        color='black',
        pos=(-0.5, 0.25),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    
    text_ISI_instr10 = visual.TextStim(
        win,
        text="Remember, left (←) means you think a shock will *not* occur. \n Right (→) means it will occur.",
        color='black',
        pos=(-0.5, 0.0),  # adjust as needed
        height=0.025,
        anchorHoriz='left'
    )
    
    text_ISI_instr9 = visual.TextStim(
        win,
        text=f"Press ← or → to continue.",
        color='black',
        pos=(-0.5, -0.25),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    
    
    Instr_Key5 = keyboard.Keyboard(deviceName='Instr_Key5')
    
    # --- Initialize components for Routine "ScannerPrompt" ---
    Scanner_wait_text = visual.TextStim(win=win, name='Scanner_wait_text',
        text='Waiting for the scanner...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.0375, wrapWidth=None, ori=0.0, 
        color='Black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Scanner_control = keyboard.Keyboard(deviceName='Scanner_control')
    # Run 'Begin Experiment' code from Scanner_timer
    fMRI_enabled = expInfo.get('fMRI_enabled', 'No')
    
    # Run 'Begin Experiment' code from Routine_Skip
    fMRI_enabled = expInfo.get('fMRI_enabled', 'no')
    
    
    # --- Initialize components for Routine "Pre_Block_ISI" ---
    ISI_Pre = visual.TextStim(win=win, name='ISI_Pre',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Blank" ---
    Blank_Text = visual.TextStim(win=win, name='Blank_Text',
        text=' ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Main_Routine_Stimulus_Selection_H1" ---
    Cued_Image = visual.ImageStim(
        win=win,
        name='Cued_Image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    Estimation_Select = keyboard.Keyboard(deviceName='Estimation_Select')
    # Run 'Begin Experiment' code from Store_Selection
    lastKey = None
    selectedColor = 'grey'
    
    # --- Initialize components for Routine "Main_Routine_Stimulus_Post_Selection_H1" ---
    Selection_Result = visual.Rect(
        win=win, name='Selection_Result',
        width=(0.225, 0.225)[0], height=(0.225, 0.225)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    Cued_image_post = visual.ImageStim(
        win=win,
        name='Cued_image_post', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "Blank" ---
    Blank_Text = visual.TextStim(win=win, name='Blank_Text',
        text=' ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Main_Task_PostISI_H1" ---
    Main_Task_H1_Post_ISI = visual.TextStim(win=win, name='Main_Task_H1_Post_ISI',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Main_Task_Post_Outcome_H1" ---
    # Run 'Begin Experiment' code from Shock_Code
    ctl = DS8R(
        demand=10,          # adjust as needed
        pulse_width=100,    # adjust as needed
        enabled=0,
        dwell=10,
        mode=1,
        polarity=1,
        source=1,
    )
    
    # Define a function to run in a separate thread
    def safe_run():
        try:
            ctl.run()
        except Exception as e:
            print(f"❌ DS8R trigger error: {e}")
    
    Cross_Outcomed = visual.TextStim(win=win, name='Cross_Outcomed',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -0.6706, -0.3490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "Main_Routine_ISI_H1" ---
    Main_Task_H1_ISI = visual.TextStim(win=win, name='Main_Task_H1_ISI',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Break" ---
    Break_Period = visual.TextStim(win=win, name='Break_Period',
        text='This is a three minute rest period.\n\nYou may exit the eyetracker.\n\nWhen the rest has ended, the experiment will resume.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Post_Break" ---
    Post_break_text = visual.TextStim(win=win, name='Post_break_text',
        text='The break period has elapsed. Please call a researcher.\n\nRecalibration will commence on the next screen.\n\n\nPress ← or → to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Post_break_keys = keyboard.Keyboard(deviceName='Post_break_keys')
    # Run 'Begin Experiment' code from Skipper3
    fMRI_enabled = expInfo.get('fMRI_enabled', 'no')
    
    # --- Initialize components for Routine "Recal_Instr" ---
    Recal_Instr_Text = visual.TextStim(win=win, name='Recal_Instr_Text',
        text='You will now recalibrate your stimulation threshold.\n\nAs before, please rate from 0 - 100%.\n\nWe will proceed once we understand your 80% threshold.\n\n\nPress ← or → to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Recal_Procced_Keys = keyboard.Keyboard(deviceName='Recal_Procced_Keys')
    
    # --- Initialize components for Routine "Pre_Shock_ISI_Calib_2" ---
    Pre_Cali_ISI_5 = visual.TextStim(win=win, name='Pre_Cali_ISI_5',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Shock_ISI_Calib_2" ---
    Calib_Shock_Cross_4 = visual.TextStim(win=win, name='Calib_Shock_Cross_4',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -0.6706, -0.3490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from Stimulation_Calib_Code_4
    last_demand = None
    last_pulse_width = None
    
    ctl = DS8R(
        demand=10,  # adjust as needed
        pulse_width=100,   # adjust as needed
        enabled=0,
        dwell=10,
        mode=1,
        polarity=1,
        source=1,
    )
    
    def safe_run():
        try:
            ctl.run()
        except Exception as e:
            print(f"DS8R trigger error: {e}")
    
    # --- Initialize components for Routine "Shock_Calib_Looper_5" ---
    slider_keys_2 = keyboard.Keyboard(deviceName='slider_keys_2')
    pain_slider_2 = visual.Slider(win=win, name='pain_slider_2',
        startValue=0, size=(0.65, 0.02), pos=(0, -0.2), units=win.units,
        labels=["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor=[-0.5, -0.5, -0.5], lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "Loop_Checkpoint_2" ---
    
    # --- Initialize components for Routine "Pre_Shock_ISI_Cali_Check_1_2" ---
    Pre_Cali_ISI_6 = visual.TextStim(win=win, name='Pre_Cali_ISI_6',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Shock_ISI_Post_Check_1_2" ---
    Calib_Shock_Cross_5 = visual.TextStim(win=win, name='Calib_Shock_Cross_5',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -0.6706, -0.3490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from Stimulation_Calib_Code_5
    ctl = DS8R(
        demand=10,  # adjust as needed
        pulse_width=100,   # adjust as needed
        enabled=0,
        dwell=10,
        mode=1,
        polarity=1,
        source=1,
    )
    
    def safe_run():
        try:
            ctl.run()
        except Exception as e:
            print(f"DS8R trigger error: {e}")
    
    # --- Initialize components for Routine "Shock_Calib_Looper_6" ---
    slider_keys2_2 = keyboard.Keyboard(deviceName='slider_keys2_2')
    pain_slider2_2 = visual.Slider(win=win, name='pain_slider2_2',
        startValue=0, size=(0.65, 0.02), pos=(0, -0.2), units=win.units,
        labels=["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor=[-0.5, -0.5, -0.5], lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "Pre_Shock_ISI_Check_2_2" ---
    Pre_Cali_ISI_7 = visual.TextStim(win=win, name='Pre_Cali_ISI_7',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Shock_ISI_Post_Check_2_2" ---
    Calib_Shock_Cross_6 = visual.TextStim(win=win, name='Calib_Shock_Cross_6',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -0.6706, -0.3490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from Stimulation_Calib_Code_6
    ctl = DS8R(
        demand=10,  # adjust as needed
        pulse_width=100,   # adjust as needed
        enabled=0,
        dwell=10,
        mode=1,
        polarity=1,
        source=1,
    )
    
    def safe_run():
        try:
            ctl.run()
        except Exception as e:
            print(f"DS8R trigger error: {e}")
    
    # --- Initialize components for Routine "Shock_Calib_Looper_7" ---
    slider_keys3_2 = keyboard.Keyboard(deviceName='slider_keys3_2')
    pain_slider3_2 = visual.Slider(win=win, name='pain_slider3_2',
        startValue=0, size=(0.65, 0.02), pos=(0, -0.2), units=win.units,
        labels=["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor=[-0.5, -0.5, -0.5], lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "Instructions_Final_2" ---
    # Run 'Begin Experiment' code from Text_code_5
    from psychopy import visual, core, event
    
    # One text stim per color segment
    
    text_ISI_instr50 = visual.TextStim(
        win,
        text="You will now return to the task.",
        color='black',
        pos=(-0.5, 0.1),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_ISI_instr51 = visual.TextStim(
        win,
        text="This is the final half.",
        color='black',
        pos=(-0.5, 0.0),  # adjust as needed
        height=0.03,
        anchorHoriz='left'
    )
    
    text_ISI_instr9 = visual.TextStim(
        win,
        text=f"Press ← or → to continue.",
        color='black',
        pos=(-0.5, -0.25),  # shift right to align after green text
        height=0.03,
        anchorHoriz='left'
    )
    
    
    Instr_Key5_2 = keyboard.Keyboard(deviceName='Instr_Key5_2')
    
    # --- Initialize components for Routine "Pre_Block_ISI" ---
    ISI_Pre = visual.TextStim(win=win, name='ISI_Pre',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Blank" ---
    Blank_Text = visual.TextStim(win=win, name='Blank_Text',
        text=' ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Main_Routine_Stimulus_Selection_H2" ---
    Cued_Image_2 = visual.ImageStim(
        win=win,
        name='Cued_Image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    Estimation_Select_2 = keyboard.Keyboard(deviceName='Estimation_Select_2')
    # Run 'Begin Experiment' code from Store_Selection_2
    lastKey = None
    selectedColor = 'grey'
    
    # --- Initialize components for Routine "Main_Routine_Stimulus_Post_Selection_H2" ---
    Selection_Result_2 = visual.Rect(
        win=win, name='Selection_Result_2',
        width=(0.225, 0.225)[0], height=(0.225, 0.225)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    Cued_image_post_2 = visual.ImageStim(
        win=win,
        name='Cued_image_post_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "Blank" ---
    Blank_Text = visual.TextStim(win=win, name='Blank_Text',
        text=' ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Main_Task_PostISI_H2" ---
    Main_Task_H1_Post_ISI_2 = visual.TextStim(win=win, name='Main_Task_H1_Post_ISI_2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Main_Task_Post_Outcome_H2" ---
    Cross_Outcomed_2 = visual.TextStim(win=win, name='Cross_Outcomed_2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -0.6706, -0.3490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from Shock_Code_2
    ctl = DS8R(
        demand=10,          # adjust as needed
        pulse_width=100,    # adjust as needed
        enabled=0,
        dwell=10,
        mode=1,
        polarity=1,
        source=1,
    )
    
    # Define a function to run in a separate thread
    def safe_run():
        try:
            ctl.run()
        except Exception as e:
            print(f"❌ DS8R trigger error: {e}")
    
    # --- Initialize components for Routine "Main_Routine_ISI_H2_2" ---
    Main_Task_H1_ISI_2 = visual.TextStim(win=win, name='Main_Task_H1_ISI_2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "End_Recording_2" ---
    
    # --- Initialize components for Routine "Task_End" ---
    End_Text = visual.TextStim(win=win, name='End_Text',
        text="End of test.\n\nThank you for participating. \n\nPlease inform the researcher of your completion.\n\nPress 'escape' to close.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Initialisation" ---
    # create an object to store info about Routine Initialisation
    Initialisation = data.Routine(
        name='Initialisation',
        components=[],
    )
    Initialisation.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Initialisation
    Initialisation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Initialisation.tStart = globalClock.getTime(format='float')
    Initialisation.status = STARTED
    thisExp.addData('Initialisation.started', Initialisation.tStart)
    Initialisation.maxDuration = None
    # keep track of which components have finished
    InitialisationComponents = Initialisation.components
    for thisComponent in Initialisation.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Initialisation" ---
    Initialisation.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Initialisation.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Initialisation.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Initialisation" ---
    for thisComponent in Initialisation.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Initialisation
    Initialisation.tStop = globalClock.getTime(format='float')
    Initialisation.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Initialisation.stopped', Initialisation.tStop)
    thisExp.nextEntry()
    # the Routine "Initialisation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions" ---
    # create an object to store info about Routine Instructions
    Instructions = data.Routine(
        name='Instructions',
        components=[Instr_Key1],
    )
    Instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Instr_Key1
    Instr_Key1.keys = []
    Instr_Key1.rt = []
    _Instr_Key1_allKeys = []
    # store start times for Instructions
    Instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions.tStart = globalClock.getTime(format='float')
    Instructions.status = STARTED
    thisExp.addData('Instructions.started', Instructions.tStart)
    Instructions.maxDuration = None
    # keep track of which components have finished
    InstructionsComponents = Instructions.components
    for thisComponent in Instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    Instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box16
        grayBox.draw()
        # Run 'Each Frame' code from Text_Code
        text_black.draw()
        text_blue.draw()
        text_further.draw()
        text_further2.draw()
        text_further3.draw()
        
        # *Instr_Key1* updates
        waitOnFlip = False
        
        # if Instr_Key1 is starting this frame...
        if Instr_Key1.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Instr_Key1.frameNStart = frameN  # exact frame index
            Instr_Key1.tStart = t  # local t and not account for scr refresh
            Instr_Key1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Key1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instr_Key1.started')
            # update status
            Instr_Key1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instr_Key1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instr_Key1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instr_Key1.status == STARTED and not waitOnFlip:
            theseKeys = Instr_Key1.getKeys(keyList=['left','right','1','2'], ignoreKeys=["escape"], waitRelease=False)
            _Instr_Key1_allKeys.extend(theseKeys)
            if len(_Instr_Key1_allKeys):
                Instr_Key1.keys = _Instr_Key1_allKeys[-1].name  # just the last key pressed
                Instr_Key1.rt = _Instr_Key1_allKeys[-1].rt
                Instr_Key1.duration = _Instr_Key1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in Instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions
    Instructions.tStop = globalClock.getTime(format='float')
    Instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions.stopped', Instructions.tStop)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_2" ---
    # create an object to store info about Routine Instructions_2
    Instructions_2 = data.Routine(
        name='Instructions_2',
        components=[Instr_Key2],
    )
    Instructions_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Instr_Key2
    Instr_Key2.keys = []
    Instr_Key2.rt = []
    _Instr_Key2_allKeys = []
    # store start times for Instructions_2
    Instructions_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_2.tStart = globalClock.getTime(format='float')
    Instructions_2.status = STARTED
    thisExp.addData('Instructions_2.started', Instructions_2.tStart)
    Instructions_2.maxDuration = None
    # keep track of which components have finished
    Instructions_2Components = Instructions_2.components
    for thisComponent in Instructions_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_2" ---
    Instructions_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box17
        grayBox.draw()
        # Run 'Each Frame' code from Text_code_2
        text_black3.draw()
        text_black4.draw()
        text_black5.draw()
        text_further3.draw()
        example_image1.draw()
        example_image2.draw()
        
        # *Instr_Key2* updates
        waitOnFlip = False
        
        # if Instr_Key2 is starting this frame...
        if Instr_Key2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Instr_Key2.frameNStart = frameN  # exact frame index
            Instr_Key2.tStart = t  # local t and not account for scr refresh
            Instr_Key2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Key2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instr_Key2.started')
            # update status
            Instr_Key2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instr_Key2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instr_Key2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instr_Key2.status == STARTED and not waitOnFlip:
            theseKeys = Instr_Key2.getKeys(keyList=['left','right','1','2'], ignoreKeys=["escape"], waitRelease=False)
            _Instr_Key2_allKeys.extend(theseKeys)
            if len(_Instr_Key2_allKeys):
                Instr_Key2.keys = _Instr_Key2_allKeys[-1].name  # just the last key pressed
                Instr_Key2.rt = _Instr_Key2_allKeys[-1].rt
                Instr_Key2.duration = _Instr_Key2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_2" ---
    for thisComponent in Instructions_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_2
    Instructions_2.tStop = globalClock.getTime(format='float')
    Instructions_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_2.stopped', Instructions_2.tStop)
    thisExp.nextEntry()
    # the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_3" ---
    # create an object to store info about Routine Instructions_3
    Instructions_3 = data.Routine(
        name='Instructions_3',
        components=[Instr_Key3],
    )
    Instructions_3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Instr_Key3
    Instr_Key3.keys = []
    Instr_Key3.rt = []
    _Instr_Key3_allKeys = []
    # store start times for Instructions_3
    Instructions_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_3.tStart = globalClock.getTime(format='float')
    Instructions_3.status = STARTED
    thisExp.addData('Instructions_3.started', Instructions_3.tStart)
    Instructions_3.maxDuration = None
    # keep track of which components have finished
    Instructions_3Components = Instructions_3.components
    for thisComponent in Instructions_3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_3" ---
    Instructions_3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box18
        grayBox.draw()
        # Run 'Each Frame' code from Text_code_3
        text_ISI_instr1.draw()
        text_ISI_instr2.draw()
        text_ISI_instr3.draw()
        text_ISI_instr4.draw()
        example_image3.draw()
        example_image4.draw()
        
        # *Instr_Key3* updates
        waitOnFlip = False
        
        # if Instr_Key3 is starting this frame...
        if Instr_Key3.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Instr_Key3.frameNStart = frameN  # exact frame index
            Instr_Key3.tStart = t  # local t and not account for scr refresh
            Instr_Key3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Key3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instr_Key3.started')
            # update status
            Instr_Key3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instr_Key3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instr_Key3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instr_Key3.status == STARTED and not waitOnFlip:
            theseKeys = Instr_Key3.getKeys(keyList=['left','right','1','2'], ignoreKeys=["escape"], waitRelease=False)
            _Instr_Key3_allKeys.extend(theseKeys)
            if len(_Instr_Key3_allKeys):
                Instr_Key3.keys = _Instr_Key3_allKeys[-1].name  # just the last key pressed
                Instr_Key3.rt = _Instr_Key3_allKeys[-1].rt
                Instr_Key3.duration = _Instr_Key3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_3" ---
    for thisComponent in Instructions_3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_3
    Instructions_3.tStop = globalClock.getTime(format='float')
    Instructions_3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_3.stopped', Instructions_3.tStop)
    thisExp.nextEntry()
    # the Routine "Instructions_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_4" ---
    # create an object to store info about Routine Instructions_4
    Instructions_4 = data.Routine(
        name='Instructions_4',
        components=[Instr_Key4],
    )
    Instructions_4.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Instr_Key4
    Instr_Key4.keys = []
    Instr_Key4.rt = []
    _Instr_Key4_allKeys = []
    # store start times for Instructions_4
    Instructions_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_4.tStart = globalClock.getTime(format='float')
    Instructions_4.status = STARTED
    thisExp.addData('Instructions_4.started', Instructions_4.tStart)
    Instructions_4.maxDuration = None
    # keep track of which components have finished
    Instructions_4Components = Instructions_4.components
    for thisComponent in Instructions_4.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_4" ---
    Instructions_4.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box18_2
        grayBox.draw()
        # Run 'Each Frame' code from Text_code
        text_ISI_instr5.draw()
        text_ISI_instr6.draw()
        text_ISI_instr7.draw()
        
        
        # *Instr_Key4* updates
        waitOnFlip = False
        
        # if Instr_Key4 is starting this frame...
        if Instr_Key4.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Instr_Key4.frameNStart = frameN  # exact frame index
            Instr_Key4.tStart = t  # local t and not account for scr refresh
            Instr_Key4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Key4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instr_Key4.started')
            # update status
            Instr_Key4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instr_Key4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instr_Key4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instr_Key4.status == STARTED and not waitOnFlip:
            theseKeys = Instr_Key4.getKeys(keyList=['left','right','1','2'], ignoreKeys=["escape"], waitRelease=False)
            _Instr_Key4_allKeys.extend(theseKeys)
            if len(_Instr_Key4_allKeys):
                Instr_Key4.keys = _Instr_Key4_allKeys[-1].name  # just the last key pressed
                Instr_Key4.rt = _Instr_Key4_allKeys[-1].rt
                Instr_Key4.duration = _Instr_Key4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_4.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_4.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_4" ---
    for thisComponent in Instructions_4.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_4
    Instructions_4.tStop = globalClock.getTime(format='float')
    Instructions_4.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_4.stopped', Instructions_4.tStop)
    thisExp.nextEntry()
    # the Routine "Instructions_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Shock_Calib_Instr" ---
    # create an object to store info about Routine Shock_Calib_Instr
    Shock_Calib_Instr = data.Routine(
        name='Shock_Calib_Instr',
        components=[Cali_Instr_Keyboard],
    )
    Shock_Calib_Instr.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Cali_Instr_Keyboard
    Cali_Instr_Keyboard.keys = []
    Cali_Instr_Keyboard.rt = []
    _Cali_Instr_Keyboard_allKeys = []
    # store start times for Shock_Calib_Instr
    Shock_Calib_Instr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Shock_Calib_Instr.tStart = globalClock.getTime(format='float')
    Shock_Calib_Instr.status = STARTED
    thisExp.addData('Shock_Calib_Instr.started', Shock_Calib_Instr.tStart)
    Shock_Calib_Instr.maxDuration = None
    # keep track of which components have finished
    Shock_Calib_InstrComponents = Shock_Calib_Instr.components
    for thisComponent in Shock_Calib_Instr.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Shock_Calib_Instr" ---
    Shock_Calib_Instr.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box_Shock_Cali_1
        grayBox.draw()
        # Run 'Each Frame' code from Shock_Cali_Instr_Text
        text_shockcal_instr1.draw()
        text_shockcal_instr2.draw()
        text_shockcal_instr3.draw()
        text_shockcal_instr4.draw()
        
        # *Cali_Instr_Keyboard* updates
        waitOnFlip = False
        
        # if Cali_Instr_Keyboard is starting this frame...
        if Cali_Instr_Keyboard.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Cali_Instr_Keyboard.frameNStart = frameN  # exact frame index
            Cali_Instr_Keyboard.tStart = t  # local t and not account for scr refresh
            Cali_Instr_Keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cali_Instr_Keyboard, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Cali_Instr_Keyboard.started')
            # update status
            Cali_Instr_Keyboard.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Cali_Instr_Keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Cali_Instr_Keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Cali_Instr_Keyboard.status == STARTED and not waitOnFlip:
            theseKeys = Cali_Instr_Keyboard.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
            _Cali_Instr_Keyboard_allKeys.extend(theseKeys)
            if len(_Cali_Instr_Keyboard_allKeys):
                Cali_Instr_Keyboard.keys = _Cali_Instr_Keyboard_allKeys[-1].name  # just the last key pressed
                Cali_Instr_Keyboard.rt = _Cali_Instr_Keyboard_allKeys[-1].rt
                Cali_Instr_Keyboard.duration = _Cali_Instr_Keyboard_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Shock_Calib_Instr.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Shock_Calib_Instr.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Shock_Calib_Instr" ---
    for thisComponent in Shock_Calib_Instr.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Shock_Calib_Instr
    Shock_Calib_Instr.tStop = globalClock.getTime(format='float')
    Shock_Calib_Instr.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Shock_Calib_Instr.stopped', Shock_Calib_Instr.tStop)
    thisExp.nextEntry()
    # the Routine "Shock_Calib_Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Shock_Calib_Instr2" ---
    # create an object to store info about Routine Shock_Calib_Instr2
    Shock_Calib_Instr2 = data.Routine(
        name='Shock_Calib_Instr2',
        components=[Cali_Instr_Keyboard_2],
    )
    Shock_Calib_Instr2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Cali_Instr_Keyboard_2
    Cali_Instr_Keyboard_2.keys = []
    Cali_Instr_Keyboard_2.rt = []
    _Cali_Instr_Keyboard_2_allKeys = []
    # store start times for Shock_Calib_Instr2
    Shock_Calib_Instr2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Shock_Calib_Instr2.tStart = globalClock.getTime(format='float')
    Shock_Calib_Instr2.status = STARTED
    thisExp.addData('Shock_Calib_Instr2.started', Shock_Calib_Instr2.tStart)
    Shock_Calib_Instr2.maxDuration = None
    # keep track of which components have finished
    Shock_Calib_Instr2Components = Shock_Calib_Instr2.components
    for thisComponent in Shock_Calib_Instr2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Shock_Calib_Instr2" ---
    Shock_Calib_Instr2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box_Shock_Cali
        grayBox.draw()
        # Run 'Each Frame' code from Shock_Cali_Instr_Text_2
        text_shockcal_instr5.draw()
        text_shockcal_instr6.draw()
        text_shockcal_instr7.draw()
        text_shockcal_instr8.draw()
        
        # *Cali_Instr_Keyboard_2* updates
        waitOnFlip = False
        
        # if Cali_Instr_Keyboard_2 is starting this frame...
        if Cali_Instr_Keyboard_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Cali_Instr_Keyboard_2.frameNStart = frameN  # exact frame index
            Cali_Instr_Keyboard_2.tStart = t  # local t and not account for scr refresh
            Cali_Instr_Keyboard_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cali_Instr_Keyboard_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Cali_Instr_Keyboard_2.started')
            # update status
            Cali_Instr_Keyboard_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Cali_Instr_Keyboard_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Cali_Instr_Keyboard_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Cali_Instr_Keyboard_2.status == STARTED and not waitOnFlip:
            theseKeys = Cali_Instr_Keyboard_2.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _Cali_Instr_Keyboard_2_allKeys.extend(theseKeys)
            if len(_Cali_Instr_Keyboard_2_allKeys):
                Cali_Instr_Keyboard_2.keys = _Cali_Instr_Keyboard_2_allKeys[-1].name  # just the last key pressed
                Cali_Instr_Keyboard_2.rt = _Cali_Instr_Keyboard_2_allKeys[-1].rt
                Cali_Instr_Keyboard_2.duration = _Cali_Instr_Keyboard_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Shock_Calib_Instr2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Shock_Calib_Instr2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Shock_Calib_Instr2" ---
    for thisComponent in Shock_Calib_Instr2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Shock_Calib_Instr2
    Shock_Calib_Instr2.tStop = globalClock.getTime(format='float')
    Shock_Calib_Instr2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Shock_Calib_Instr2.stopped', Shock_Calib_Instr2.tStop)
    thisExp.nextEntry()
    # the Routine "Shock_Calib_Instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    SecondLoopPass = data.TrialHandler2(
        name='SecondLoopPass',
        nReps=99.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(SecondLoopPass)  # add the loop to the experiment
    thisSecondLoopPas = SecondLoopPass.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSecondLoopPas.rgb)
    if thisSecondLoopPas != None:
        for paramName in thisSecondLoopPas:
            globals()[paramName] = thisSecondLoopPas[paramName]
    
    for thisSecondLoopPas in SecondLoopPass:
        currentLoop = SecondLoopPass
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisSecondLoopPas.rgb)
        if thisSecondLoopPas != None:
            for paramName in thisSecondLoopPas:
                globals()[paramName] = thisSecondLoopPas[paramName]
        
        # set up handler to look after randomisation of conditions etc
        FirstLoopPass = data.TrialHandler2(
            name='FirstLoopPass',
            nReps=99.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(FirstLoopPass)  # add the loop to the experiment
        thisFirstLoopPas = FirstLoopPass.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFirstLoopPas.rgb)
        if thisFirstLoopPas != None:
            for paramName in thisFirstLoopPas:
                globals()[paramName] = thisFirstLoopPas[paramName]
        
        for thisFirstLoopPas in FirstLoopPass:
            currentLoop = FirstLoopPass
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisFirstLoopPas.rgb)
            if thisFirstLoopPas != None:
                for paramName in thisFirstLoopPas:
                    globals()[paramName] = thisFirstLoopPas[paramName]
            
            # set up handler to look after randomisation of conditions etc
            Checkpoint = data.TrialHandler2(
                name='Checkpoint',
                nReps=99.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(Checkpoint)  # add the loop to the experiment
            thisCheckpoint = Checkpoint.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisCheckpoint.rgb)
            if thisCheckpoint != None:
                for paramName in thisCheckpoint:
                    globals()[paramName] = thisCheckpoint[paramName]
            
            for thisCheckpoint in Checkpoint:
                currentLoop = Checkpoint
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # abbreviate parameter names if possible (e.g. rgb = thisCheckpoint.rgb)
                if thisCheckpoint != None:
                    for paramName in thisCheckpoint:
                        globals()[paramName] = thisCheckpoint[paramName]
                
                # set up handler to look after randomisation of conditions etc
                Cali_Loop = data.TrialHandler2(
                    name='Cali_Loop',
                    nReps=1.0, 
                    method='sequential', 
                    extraInfo=expInfo, 
                    originPath=-1, 
                    trialList=data.importConditions('Conditions/Shock_Calibration_Sched.xlsx'), 
                    seed=None, 
                )
                thisExp.addLoop(Cali_Loop)  # add the loop to the experiment
                thisCali_Loop = Cali_Loop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisCali_Loop.rgb)
                if thisCali_Loop != None:
                    for paramName in thisCali_Loop:
                        globals()[paramName] = thisCali_Loop[paramName]
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                
                for thisCali_Loop in Cali_Loop:
                    currentLoop = Cali_Loop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                    # abbreviate parameter names if possible (e.g. rgb = thisCali_Loop.rgb)
                    if thisCali_Loop != None:
                        for paramName in thisCali_Loop:
                            globals()[paramName] = thisCali_Loop[paramName]
                    
                    # --- Prepare to start Routine "Pre_Shock_ISI_Calib" ---
                    # create an object to store info about Routine Pre_Shock_ISI_Calib
                    Pre_Shock_ISI_Calib = data.Routine(
                        name='Pre_Shock_ISI_Calib',
                        components=[Pre_Cali_ISI],
                    )
                    Pre_Shock_ISI_Calib.status = NOT_STARTED
                    continueRoutine = True
                    # update component parameters for each repeat
                    # store start times for Pre_Shock_ISI_Calib
                    Pre_Shock_ISI_Calib.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                    Pre_Shock_ISI_Calib.tStart = globalClock.getTime(format='float')
                    Pre_Shock_ISI_Calib.status = STARTED
                    thisExp.addData('Pre_Shock_ISI_Calib.started', Pre_Shock_ISI_Calib.tStart)
                    Pre_Shock_ISI_Calib.maxDuration = None
                    # keep track of which components have finished
                    Pre_Shock_ISI_CalibComponents = Pre_Shock_ISI_Calib.components
                    for thisComponent in Pre_Shock_ISI_Calib.components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "Pre_Shock_ISI_Calib" ---
                    # if trial has changed, end Routine now
                    if isinstance(Cali_Loop, data.TrialHandler2) and thisCali_Loop.thisN != Cali_Loop.thisTrial.thisN:
                        continueRoutine = False
                    Pre_Shock_ISI_Calib.forceEnded = routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *Pre_Cali_ISI* updates
                        
                        # if Pre_Cali_ISI is starting this frame...
                        if Pre_Cali_ISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            Pre_Cali_ISI.frameNStart = frameN  # exact frame index
                            Pre_Cali_ISI.tStart = t  # local t and not account for scr refresh
                            Pre_Cali_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(Pre_Cali_ISI, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Pre_Cali_ISI.started')
                            # update status
                            Pre_Cali_ISI.status = STARTED
                            Pre_Cali_ISI.setAutoDraw(True)
                        
                        # if Pre_Cali_ISI is active this frame...
                        if Pre_Cali_ISI.status == STARTED:
                            # update params
                            pass
                        
                        # if Pre_Cali_ISI is stopping this frame...
                        if Pre_Cali_ISI.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > Pre_Cali_ISI.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                Pre_Cali_ISI.tStop = t  # not accounting for scr refresh
                                Pre_Cali_ISI.tStopRefresh = tThisFlipGlobal  # on global time
                                Pre_Cali_ISI.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'Pre_Cali_ISI.stopped')
                                # update status
                                Pre_Cali_ISI.status = FINISHED
                                Pre_Cali_ISI.setAutoDraw(False)
                        # Run 'Each Frame' code from Box_Cali_Pre
                        grayBox.draw()
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                            )
                            # skip the frame we paused on
                            continue
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            Pre_Shock_ISI_Calib.forceEnded = routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in Pre_Shock_ISI_Calib.components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "Pre_Shock_ISI_Calib" ---
                    for thisComponent in Pre_Shock_ISI_Calib.components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store stop times for Pre_Shock_ISI_Calib
                    Pre_Shock_ISI_Calib.tStop = globalClock.getTime(format='float')
                    Pre_Shock_ISI_Calib.tStopRefresh = tThisFlipGlobal
                    thisExp.addData('Pre_Shock_ISI_Calib.stopped', Pre_Shock_ISI_Calib.tStop)
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if Pre_Shock_ISI_Calib.maxDurationReached:
                        routineTimer.addTime(-Pre_Shock_ISI_Calib.maxDuration)
                    elif Pre_Shock_ISI_Calib.forceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    
                    # --- Prepare to start Routine "Shock_ISI_Calib" ---
                    # create an object to store info about Routine Shock_ISI_Calib
                    Shock_ISI_Calib = data.Routine(
                        name='Shock_ISI_Calib',
                        components=[Calib_Shock_Cross],
                    )
                    Shock_ISI_Calib.status = NOT_STARTED
                    continueRoutine = True
                    # update component parameters for each repeat
                    # Run 'Begin Routine' code from Stimulation_Calib_Code
                    ctl.demand = int(Set_Demand)
                    ctl.pulse_width = int(Set_Width)
                    ctl.enabled = 1  # Re-arm device
                    
                    trigger_thread = threading.Thread(target=safe_run)
                    trigger_thread.start()
                    trigger_thread.join(timeout=2.0)  # 2-second timeout
                    
                    if trigger_thread.is_alive():
                        print("⚠️ DS8R trigger timed out!")
                        # Optionally kill the thread or reset ctl here
                    
                    last_demand = Set_Demand
                    last_pulse_width = Set_Width
                    # store start times for Shock_ISI_Calib
                    Shock_ISI_Calib.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                    Shock_ISI_Calib.tStart = globalClock.getTime(format='float')
                    Shock_ISI_Calib.status = STARTED
                    thisExp.addData('Shock_ISI_Calib.started', Shock_ISI_Calib.tStart)
                    Shock_ISI_Calib.maxDuration = None
                    # keep track of which components have finished
                    Shock_ISI_CalibComponents = Shock_ISI_Calib.components
                    for thisComponent in Shock_ISI_Calib.components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "Shock_ISI_Calib" ---
                    # if trial has changed, end Routine now
                    if isinstance(Cali_Loop, data.TrialHandler2) and thisCali_Loop.thisN != Cali_Loop.thisTrial.thisN:
                        continueRoutine = False
                    Shock_ISI_Calib.forceEnded = routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 2.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *Calib_Shock_Cross* updates
                        
                        # if Calib_Shock_Cross is starting this frame...
                        if Calib_Shock_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            Calib_Shock_Cross.frameNStart = frameN  # exact frame index
                            Calib_Shock_Cross.tStart = t  # local t and not account for scr refresh
                            Calib_Shock_Cross.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(Calib_Shock_Cross, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Calib_Shock_Cross.started')
                            # update status
                            Calib_Shock_Cross.status = STARTED
                            Calib_Shock_Cross.setAutoDraw(True)
                        
                        # if Calib_Shock_Cross is active this frame...
                        if Calib_Shock_Cross.status == STARTED:
                            # update params
                            pass
                        
                        # if Calib_Shock_Cross is stopping this frame...
                        if Calib_Shock_Cross.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > Calib_Shock_Cross.tStartRefresh + 2.0-frameTolerance:
                                # keep track of stop time/frame for later
                                Calib_Shock_Cross.tStop = t  # not accounting for scr refresh
                                Calib_Shock_Cross.tStopRefresh = tThisFlipGlobal  # on global time
                                Calib_Shock_Cross.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'Calib_Shock_Cross.stopped')
                                # update status
                                Calib_Shock_Cross.status = FINISHED
                                Calib_Shock_Cross.setAutoDraw(False)
                        # Run 'Each Frame' code from Box_Cali_Shock
                        grayBox.draw()
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                            )
                            # skip the frame we paused on
                            continue
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            Shock_ISI_Calib.forceEnded = routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in Shock_ISI_Calib.components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "Shock_ISI_Calib" ---
                    for thisComponent in Shock_ISI_Calib.components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store stop times for Shock_ISI_Calib
                    Shock_ISI_Calib.tStop = globalClock.getTime(format='float')
                    Shock_ISI_Calib.tStopRefresh = tThisFlipGlobal
                    thisExp.addData('Shock_ISI_Calib.stopped', Shock_ISI_Calib.tStop)
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if Shock_ISI_Calib.maxDurationReached:
                        routineTimer.addTime(-Shock_ISI_Calib.maxDuration)
                    elif Shock_ISI_Calib.forceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-2.000000)
                    
                    # --- Prepare to start Routine "Shock_Calib_Looper" ---
                    # create an object to store info about Routine Shock_Calib_Looper
                    Shock_Calib_Looper = data.Routine(
                        name='Shock_Calib_Looper',
                        components=[slider_keys, pain_slider],
                    )
                    Shock_Calib_Looper.status = NOT_STARTED
                    continueRoutine = True
                    # update component parameters for each repeat
                    # create starting attributes for slider_keys
                    slider_keys.keys = []
                    slider_keys.rt = []
                    _slider_keys_allKeys = []
                    pain_slider.reset()
                    # Run 'Begin Routine' code from Slider_Code
                    slider_keys.clearEvents()
                    # Run 'Begin Routine' code from Slider_Text
                    from psychopy import visual, core, event
                    
                    # One text stim per color segment
                    text_sliderconf_1 = visual.TextStim(
                        win,
                        text="How strong was the stimulation?",
                        color='black',
                        pos=(-0.5, 0.15),  # adjust as needed
                        height=0.0275,
                        anchorHoriz='left'
                    )
                    
                    # One text stim per color segment
                    text_sliderconf_2 = visual.TextStim(
                        win,
                        text="Press ← or → to change rating. Press spacebar to confirm.",
                        color='black',
                        pos=(-0.5, 0.05),  # adjust as needed
                        height=0.0275,
                        anchorHoriz='left'
                    )
                    
                    # store start times for Shock_Calib_Looper
                    Shock_Calib_Looper.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                    Shock_Calib_Looper.tStart = globalClock.getTime(format='float')
                    Shock_Calib_Looper.status = STARTED
                    thisExp.addData('Shock_Calib_Looper.started', Shock_Calib_Looper.tStart)
                    Shock_Calib_Looper.maxDuration = None
                    # keep track of which components have finished
                    Shock_Calib_LooperComponents = Shock_Calib_Looper.components
                    for thisComponent in Shock_Calib_Looper.components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "Shock_Calib_Looper" ---
                    # if trial has changed, end Routine now
                    if isinstance(Cali_Loop, data.TrialHandler2) and thisCali_Loop.thisN != Cali_Loop.thisTrial.thisN:
                        continueRoutine = False
                    Shock_Calib_Looper.forceEnded = routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *slider_keys* updates
                        waitOnFlip = False
                        
                        # if slider_keys is starting this frame...
                        if slider_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            slider_keys.frameNStart = frameN  # exact frame index
                            slider_keys.tStart = t  # local t and not account for scr refresh
                            slider_keys.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(slider_keys, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            slider_keys.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(slider_keys.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(slider_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        
                        # if slider_keys is stopping this frame...
                        if slider_keys.status == STARTED:
                            if bool('space' in slider_keys.keys):
                                # keep track of stop time/frame for later
                                slider_keys.tStop = t  # not accounting for scr refresh
                                slider_keys.tStopRefresh = tThisFlipGlobal  # on global time
                                slider_keys.frameNStop = frameN  # exact frame index
                                # update status
                                slider_keys.status = FINISHED
                                slider_keys.status = FINISHED
                        if slider_keys.status == STARTED and not waitOnFlip:
                            theseKeys = slider_keys.getKeys(keyList=['left','right', 'space', '1', '2'], ignoreKeys=["escape"], waitRelease=False)
                            _slider_keys_allKeys.extend(theseKeys)
                            if len(_slider_keys_allKeys):
                                slider_keys.keys = _slider_keys_allKeys[-1].name  # just the last key pressed
                                slider_keys.rt = _slider_keys_allKeys[-1].rt
                                slider_keys.duration = _slider_keys_allKeys[-1].duration
                        
                        # *pain_slider* updates
                        
                        # if pain_slider is starting this frame...
                        if pain_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            pain_slider.frameNStart = frameN  # exact frame index
                            pain_slider.tStart = t  # local t and not account for scr refresh
                            pain_slider.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(pain_slider, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            pain_slider.status = STARTED
                            pain_slider.setAutoDraw(True)
                        
                        # if pain_slider is active this frame...
                        if pain_slider.status == STARTED:
                            # update params
                            pass
                        
                        # if pain_slider is stopping this frame...
                        if pain_slider.status == STARTED:
                            if bool('space' in slider_keys.keys):
                                # keep track of stop time/frame for later
                                pain_slider.tStop = t  # not accounting for scr refresh
                                pain_slider.tStopRefresh = tThisFlipGlobal  # on global time
                                pain_slider.frameNStop = frameN  # exact frame index
                                # update status
                                pain_slider.status = FINISHED
                                pain_slider.setAutoDraw(False)
                        # Run 'Each Frame' code from Box_Shock_Cali_3
                        grayBox.draw()
                        # Run 'Each Frame' code from Slider_Code
                        # Read keypresses from the Builder's Keyboard component
                        keys = slider_keys.getKeys()
                        
                        for key in keys:
                            if key.name in ['left', '1']:
                                if pain_slider.markerPos is not None:
                                    pain_slider.markerPos = max(pain_slider.markerPos - 1, 0)
                                else:
                                    pain_slider.markerPos = 0
                        
                            elif key.name in ['right', '2']:
                                if pain_slider.markerPos is not None:
                                    pain_slider.markerPos = min(pain_slider.markerPos + 1, 10)
                                else:
                                    pain_slider.markerPos = 1
                        
                            elif key.name in ['space', 'return']:
                                rating = pain_slider.getRating()
                                if rating is not None:
                                    print(f"✅ Rating confirmed: {rating}")
                                    thisExp.addData("pain_rating", rating)
                                    continueRoutine = False  # End the routine
                        
                        # Run 'Each Frame' code from Slider_Text
                        text_sliderconf_1.draw()
                        text_sliderconf_2.draw()
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                            )
                            # skip the frame we paused on
                            continue
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            Shock_Calib_Looper.forceEnded = routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in Shock_Calib_Looper.components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "Shock_Calib_Looper" ---
                    for thisComponent in Shock_Calib_Looper.components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store stop times for Shock_Calib_Looper
                    Shock_Calib_Looper.tStop = globalClock.getTime(format='float')
                    Shock_Calib_Looper.tStopRefresh = tThisFlipGlobal
                    thisExp.addData('Shock_Calib_Looper.stopped', Shock_Calib_Looper.tStop)
                    Cali_Loop.addData('pain_slider.response', pain_slider.getRating())
                    Cali_Loop.addData('pain_slider.rt', pain_slider.getRT())
                    # Run 'End Routine' code from Slider_Code
                    # Ensure the slider rating is set from markerPos when using keyboard control
                    if pain_slider.rating is None and pain_slider.markerPos is not None:
                        pain_slider.rating = pain_slider.markerPos
                    
                    thisExp.addData('pain_rating', pain_slider.rating)
                    
                    last_rating = pain_slider.rating
                    # Run 'End Routine' code from End_Loop
                    # Ensure rating is stored
                    if pain_slider.rating is None and pain_slider.markerPos is not None:
                        pain_slider.rating = pain_slider.markerPos
                    
                    thisExp.addData('pain_rating', pain_slider.rating)
                    
                    Last_rating = pain_slider.rating
                    
                    # Ensure rating is stored
                    if pain_slider.rating is None and pain_slider.markerPos is not None:
                        pain_slider.rating = pain_slider.markerPos
                    
                    thisExp.addData('pain_rating', pain_slider.rating)
                    
                    # Check stopping/looping conditions
                    if pain_slider.rating >= 8:
                        Cali_Loop.finished = True  # End loop as target achieved
                    # the Routine "Shock_Calib_Looper" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 1.0 repeats of 'Cali_Loop'
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                
                # --- Prepare to start Routine "Loop_Checkpoint" ---
                # create an object to store info about Routine Loop_Checkpoint
                Loop_Checkpoint = data.Routine(
                    name='Loop_Checkpoint',
                    components=[],
                )
                Loop_Checkpoint.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # store start times for Loop_Checkpoint
                Loop_Checkpoint.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                Loop_Checkpoint.tStart = globalClock.getTime(format='float')
                Loop_Checkpoint.status = STARTED
                thisExp.addData('Loop_Checkpoint.started', Loop_Checkpoint.tStart)
                Loop_Checkpoint.maxDuration = None
                # keep track of which components have finished
                Loop_CheckpointComponents = Loop_Checkpoint.components
                for thisComponent in Loop_Checkpoint.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Loop_Checkpoint" ---
                # if trial has changed, end Routine now
                if isinstance(Checkpoint, data.TrialHandler2) and thisCheckpoint.thisN != Checkpoint.thisTrial.thisN:
                    continueRoutine = False
                Loop_Checkpoint.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        Loop_Checkpoint.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Loop_Checkpoint.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Loop_Checkpoint" ---
                for thisComponent in Loop_Checkpoint.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for Loop_Checkpoint
                Loop_Checkpoint.tStop = globalClock.getTime(format='float')
                Loop_Checkpoint.tStopRefresh = tThisFlipGlobal
                thisExp.addData('Loop_Checkpoint.stopped', Loop_Checkpoint.tStop)
                # Run 'End Routine' code from Checkpoint_code
                # Check stopping/looping conditions
                if pain_slider.rating == 8:
                    Checkpoint.finished = True  # End loop as target achieved
                # the Routine "Loop_Checkpoint" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed 99.0 repeats of 'Checkpoint'
            
            
            # --- Prepare to start Routine "Pre_Shock_ISI_Cali_Check_1" ---
            # create an object to store info about Routine Pre_Shock_ISI_Cali_Check_1
            Pre_Shock_ISI_Cali_Check_1 = data.Routine(
                name='Pre_Shock_ISI_Cali_Check_1',
                components=[Pre_Cali_ISI_2],
            )
            Pre_Shock_ISI_Cali_Check_1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for Pre_Shock_ISI_Cali_Check_1
            Pre_Shock_ISI_Cali_Check_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Pre_Shock_ISI_Cali_Check_1.tStart = globalClock.getTime(format='float')
            Pre_Shock_ISI_Cali_Check_1.status = STARTED
            thisExp.addData('Pre_Shock_ISI_Cali_Check_1.started', Pre_Shock_ISI_Cali_Check_1.tStart)
            Pre_Shock_ISI_Cali_Check_1.maxDuration = None
            # keep track of which components have finished
            Pre_Shock_ISI_Cali_Check_1Components = Pre_Shock_ISI_Cali_Check_1.components
            for thisComponent in Pre_Shock_ISI_Cali_Check_1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Pre_Shock_ISI_Cali_Check_1" ---
            # if trial has changed, end Routine now
            if isinstance(FirstLoopPass, data.TrialHandler2) and thisFirstLoopPas.thisN != FirstLoopPass.thisTrial.thisN:
                continueRoutine = False
            Pre_Shock_ISI_Cali_Check_1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Pre_Cali_ISI_2* updates
                
                # if Pre_Cali_ISI_2 is starting this frame...
                if Pre_Cali_ISI_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Pre_Cali_ISI_2.frameNStart = frameN  # exact frame index
                    Pre_Cali_ISI_2.tStart = t  # local t and not account for scr refresh
                    Pre_Cali_ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Pre_Cali_ISI_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_2.started')
                    # update status
                    Pre_Cali_ISI_2.status = STARTED
                    Pre_Cali_ISI_2.setAutoDraw(True)
                
                # if Pre_Cali_ISI_2 is active this frame...
                if Pre_Cali_ISI_2.status == STARTED:
                    # update params
                    pass
                
                # if Pre_Cali_ISI_2 is stopping this frame...
                if Pre_Cali_ISI_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Pre_Cali_ISI_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Pre_Cali_ISI_2.tStop = t  # not accounting for scr refresh
                        Pre_Cali_ISI_2.tStopRefresh = tThisFlipGlobal  # on global time
                        Pre_Cali_ISI_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_2.stopped')
                        # update status
                        Pre_Cali_ISI_2.status = FINISHED
                        Pre_Cali_ISI_2.setAutoDraw(False)
                # Run 'Each Frame' code from Box_Cali_Pre_2
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Pre_Shock_ISI_Cali_Check_1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Pre_Shock_ISI_Cali_Check_1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Pre_Shock_ISI_Cali_Check_1" ---
            for thisComponent in Pre_Shock_ISI_Cali_Check_1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Pre_Shock_ISI_Cali_Check_1
            Pre_Shock_ISI_Cali_Check_1.tStop = globalClock.getTime(format='float')
            Pre_Shock_ISI_Cali_Check_1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Pre_Shock_ISI_Cali_Check_1.stopped', Pre_Shock_ISI_Cali_Check_1.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Pre_Shock_ISI_Cali_Check_1.maxDurationReached:
                routineTimer.addTime(-Pre_Shock_ISI_Cali_Check_1.maxDuration)
            elif Pre_Shock_ISI_Cali_Check_1.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "Shock_ISI_Post_Check_1" ---
            # create an object to store info about Routine Shock_ISI_Post_Check_1
            Shock_ISI_Post_Check_1 = data.Routine(
                name='Shock_ISI_Post_Check_1',
                components=[Calib_Shock_Cross_2],
            )
            Shock_ISI_Post_Check_1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Stimulation_Calib_Code_2
            ctl.demand = last_demand
            ctl.pulse_width = last_pulse_width
            ctl.enabled = 1  # Re-arm device
            
            trigger_thread = threading.Thread(target=safe_run)
            trigger_thread.start()
            trigger_thread.join(timeout=2.0)  # 2-second timeout
            
            if trigger_thread.is_alive():
                print("⚠️ DS8R trigger timed out!")
                # Optionally kill the thread or reset ctl here
            # store start times for Shock_ISI_Post_Check_1
            Shock_ISI_Post_Check_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Shock_ISI_Post_Check_1.tStart = globalClock.getTime(format='float')
            Shock_ISI_Post_Check_1.status = STARTED
            thisExp.addData('Shock_ISI_Post_Check_1.started', Shock_ISI_Post_Check_1.tStart)
            Shock_ISI_Post_Check_1.maxDuration = None
            # keep track of which components have finished
            Shock_ISI_Post_Check_1Components = Shock_ISI_Post_Check_1.components
            for thisComponent in Shock_ISI_Post_Check_1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Shock_ISI_Post_Check_1" ---
            # if trial has changed, end Routine now
            if isinstance(FirstLoopPass, data.TrialHandler2) and thisFirstLoopPas.thisN != FirstLoopPass.thisTrial.thisN:
                continueRoutine = False
            Shock_ISI_Post_Check_1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Calib_Shock_Cross_2* updates
                
                # if Calib_Shock_Cross_2 is starting this frame...
                if Calib_Shock_Cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Calib_Shock_Cross_2.frameNStart = frameN  # exact frame index
                    Calib_Shock_Cross_2.tStart = t  # local t and not account for scr refresh
                    Calib_Shock_Cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Calib_Shock_Cross_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_2.started')
                    # update status
                    Calib_Shock_Cross_2.status = STARTED
                    Calib_Shock_Cross_2.setAutoDraw(True)
                
                # if Calib_Shock_Cross_2 is active this frame...
                if Calib_Shock_Cross_2.status == STARTED:
                    # update params
                    pass
                
                # if Calib_Shock_Cross_2 is stopping this frame...
                if Calib_Shock_Cross_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Calib_Shock_Cross_2.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Calib_Shock_Cross_2.tStop = t  # not accounting for scr refresh
                        Calib_Shock_Cross_2.tStopRefresh = tThisFlipGlobal  # on global time
                        Calib_Shock_Cross_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_2.stopped')
                        # update status
                        Calib_Shock_Cross_2.status = FINISHED
                        Calib_Shock_Cross_2.setAutoDraw(False)
                # Run 'Each Frame' code from Box_Cali_Shock_2
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Shock_ISI_Post_Check_1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Shock_ISI_Post_Check_1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Shock_ISI_Post_Check_1" ---
            for thisComponent in Shock_ISI_Post_Check_1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Shock_ISI_Post_Check_1
            Shock_ISI_Post_Check_1.tStop = globalClock.getTime(format='float')
            Shock_ISI_Post_Check_1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Shock_ISI_Post_Check_1.stopped', Shock_ISI_Post_Check_1.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Shock_ISI_Post_Check_1.maxDurationReached:
                routineTimer.addTime(-Shock_ISI_Post_Check_1.maxDuration)
            elif Shock_ISI_Post_Check_1.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            
            # --- Prepare to start Routine "Shock_Calib_Looper_2" ---
            # create an object to store info about Routine Shock_Calib_Looper_2
            Shock_Calib_Looper_2 = data.Routine(
                name='Shock_Calib_Looper_2',
                components=[slider_keys2, pain_slider2],
            )
            Shock_Calib_Looper_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for slider_keys2
            slider_keys2.keys = []
            slider_keys2.rt = []
            _slider_keys2_allKeys = []
            pain_slider2.reset()
            # Run 'Begin Routine' code from Slider_Code_2
            slider_keys2.clearEvents()
            
            # Run 'Begin Routine' code from Slider_Text_2
            from psychopy import visual, core, event
            
            # One text stim per color segment
            text_sliderconf_1 = visual.TextStim(
                win,
                text="How strong was the stimulation?",
                color='black',
                pos=(-0.5, 0.15),  # adjust as needed
                height=0.0275,
                anchorHoriz='left'
            )
            
            # One text stim per color segment
            text_sliderconf_2 = visual.TextStim(
                win,
                text="Press ← or → to change rating. Press spacebar to confirm.",
                color='black',
                pos=(-0.5, 0.05),  # adjust as needed
                height=0.0275,
                anchorHoriz='left'
            )
            
            # Run 'Begin Routine' code from End_Loop_2
            
            
            # store start times for Shock_Calib_Looper_2
            Shock_Calib_Looper_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Shock_Calib_Looper_2.tStart = globalClock.getTime(format='float')
            Shock_Calib_Looper_2.status = STARTED
            thisExp.addData('Shock_Calib_Looper_2.started', Shock_Calib_Looper_2.tStart)
            Shock_Calib_Looper_2.maxDuration = None
            # keep track of which components have finished
            Shock_Calib_Looper_2Components = Shock_Calib_Looper_2.components
            for thisComponent in Shock_Calib_Looper_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Shock_Calib_Looper_2" ---
            # if trial has changed, end Routine now
            if isinstance(FirstLoopPass, data.TrialHandler2) and thisFirstLoopPas.thisN != FirstLoopPass.thisTrial.thisN:
                continueRoutine = False
            Shock_Calib_Looper_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *slider_keys2* updates
                waitOnFlip = False
                
                # if slider_keys2 is starting this frame...
                if slider_keys2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider_keys2.frameNStart = frameN  # exact frame index
                    slider_keys2.tStart = t  # local t and not account for scr refresh
                    slider_keys2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider_keys2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    slider_keys2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(slider_keys2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(slider_keys2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if slider_keys2 is stopping this frame...
                if slider_keys2.status == STARTED:
                    if bool('space' in slider_keys2.keys):
                        # keep track of stop time/frame for later
                        slider_keys2.tStop = t  # not accounting for scr refresh
                        slider_keys2.tStopRefresh = tThisFlipGlobal  # on global time
                        slider_keys2.frameNStop = frameN  # exact frame index
                        # update status
                        slider_keys2.status = FINISHED
                        slider_keys2.status = FINISHED
                if slider_keys2.status == STARTED and not waitOnFlip:
                    theseKeys = slider_keys2.getKeys(keyList=['left','right', 'space', '1', '2'], ignoreKeys=["escape"], waitRelease=False)
                    _slider_keys2_allKeys.extend(theseKeys)
                    if len(_slider_keys2_allKeys):
                        slider_keys2.keys = _slider_keys2_allKeys[-1].name  # just the last key pressed
                        slider_keys2.rt = _slider_keys2_allKeys[-1].rt
                        slider_keys2.duration = _slider_keys2_allKeys[-1].duration
                
                # *pain_slider2* updates
                
                # if pain_slider2 is starting this frame...
                if pain_slider2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pain_slider2.frameNStart = frameN  # exact frame index
                    pain_slider2.tStart = t  # local t and not account for scr refresh
                    pain_slider2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pain_slider2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    pain_slider2.status = STARTED
                    pain_slider2.setAutoDraw(True)
                
                # if pain_slider2 is active this frame...
                if pain_slider2.status == STARTED:
                    # update params
                    pass
                
                # if pain_slider2 is stopping this frame...
                if pain_slider2.status == STARTED:
                    if bool('space' in slider_keys2.keys):
                        # keep track of stop time/frame for later
                        pain_slider2.tStop = t  # not accounting for scr refresh
                        pain_slider2.tStopRefresh = tThisFlipGlobal  # on global time
                        pain_slider2.frameNStop = frameN  # exact frame index
                        # update status
                        pain_slider2.status = FINISHED
                        pain_slider2.setAutoDraw(False)
                # Run 'Each Frame' code from Box_Shock_Cali_4
                grayBox.draw()
                # Run 'Each Frame' code from Slider_Code_2
                # Read keypresses from the Builder's Keyboard component
                keys = slider_keys2.getKeys()
                
                for key in keys:
                    if key.name in ['left', '1']:
                        if pain_slider2.markerPos is not None:
                            pain_slider2.markerPos = max(pain_slider2.markerPos - 1, 0)
                        else:
                            pain_slider2.markerPos = 0
                
                    elif key.name in ['right', '2']:
                        if pain_slider2.markerPos is not None:
                            pain_slider2.markerPos = min(pain_slider2.markerPos + 1, 10)
                        else:
                            pain_slider2.markerPos = 1
                
                    elif key.name in ['space', 'return']:
                        rating = pain_slider2.getRating()
                        if rating is not None:
                            print(f"✅ Rating confirmed: {rating}")
                            thisExp.addData("pain_rating2", rating)
                            continueRoutine = False  # End the routine
                
                # Run 'Each Frame' code from Slider_Text_2
                text_sliderconf_1.draw()
                text_sliderconf_2.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Shock_Calib_Looper_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Shock_Calib_Looper_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Shock_Calib_Looper_2" ---
            for thisComponent in Shock_Calib_Looper_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Shock_Calib_Looper_2
            Shock_Calib_Looper_2.tStop = globalClock.getTime(format='float')
            Shock_Calib_Looper_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Shock_Calib_Looper_2.stopped', Shock_Calib_Looper_2.tStop)
            FirstLoopPass.addData('pain_slider2.response', pain_slider2.getRating())
            FirstLoopPass.addData('pain_slider2.rt', pain_slider2.getRT())
            # Run 'End Routine' code from End_Loop_2
            # Ensure rating is stored
            if pain_slider2.rating is None and pain_slider2.markerPos is not None:
                pain_slider2.rating = pain_slider2.markerPos
            
            thisExp.addData('pain_rating', pain_slider2.rating)
            
            if pain_slider2.rating == 8:
                FirstLoopPass.finished = True
            # the Routine "Shock_Calib_Looper_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 99.0 repeats of 'FirstLoopPass'
        
        
        # --- Prepare to start Routine "Pre_Shock_ISI_Cali_Check_2" ---
        # create an object to store info about Routine Pre_Shock_ISI_Cali_Check_2
        Pre_Shock_ISI_Cali_Check_2 = data.Routine(
            name='Pre_Shock_ISI_Cali_Check_2',
            components=[Pre_Cali_ISI_3],
        )
        Pre_Shock_ISI_Cali_Check_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from RoutSkip8
        if StimCalEnabled.lower() not in ['yes', 'y']:
            SecondLoopPass.finished = True  # End loop as target achieved
            continueRoutine = False
        # store start times for Pre_Shock_ISI_Cali_Check_2
        Pre_Shock_ISI_Cali_Check_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Pre_Shock_ISI_Cali_Check_2.tStart = globalClock.getTime(format='float')
        Pre_Shock_ISI_Cali_Check_2.status = STARTED
        thisExp.addData('Pre_Shock_ISI_Cali_Check_2.started', Pre_Shock_ISI_Cali_Check_2.tStart)
        Pre_Shock_ISI_Cali_Check_2.maxDuration = None
        # keep track of which components have finished
        Pre_Shock_ISI_Cali_Check_2Components = Pre_Shock_ISI_Cali_Check_2.components
        for thisComponent in Pre_Shock_ISI_Cali_Check_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Pre_Shock_ISI_Cali_Check_2" ---
        # if trial has changed, end Routine now
        if isinstance(SecondLoopPass, data.TrialHandler2) and thisSecondLoopPas.thisN != SecondLoopPass.thisTrial.thisN:
            continueRoutine = False
        Pre_Shock_ISI_Cali_Check_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Pre_Cali_ISI_3* updates
            
            # if Pre_Cali_ISI_3 is starting this frame...
            if Pre_Cali_ISI_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pre_Cali_ISI_3.frameNStart = frameN  # exact frame index
                Pre_Cali_ISI_3.tStart = t  # local t and not account for scr refresh
                Pre_Cali_ISI_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pre_Cali_ISI_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_3.started')
                # update status
                Pre_Cali_ISI_3.status = STARTED
                Pre_Cali_ISI_3.setAutoDraw(True)
            
            # if Pre_Cali_ISI_3 is active this frame...
            if Pre_Cali_ISI_3.status == STARTED:
                # update params
                pass
            
            # if Pre_Cali_ISI_3 is stopping this frame...
            if Pre_Cali_ISI_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pre_Cali_ISI_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Pre_Cali_ISI_3.tStop = t  # not accounting for scr refresh
                    Pre_Cali_ISI_3.tStopRefresh = tThisFlipGlobal  # on global time
                    Pre_Cali_ISI_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_3.stopped')
                    # update status
                    Pre_Cali_ISI_3.status = FINISHED
                    Pre_Cali_ISI_3.setAutoDraw(False)
            # Run 'Each Frame' code from Box_Cali_Pre_3
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Pre_Shock_ISI_Cali_Check_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pre_Shock_ISI_Cali_Check_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pre_Shock_ISI_Cali_Check_2" ---
        for thisComponent in Pre_Shock_ISI_Cali_Check_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Pre_Shock_ISI_Cali_Check_2
        Pre_Shock_ISI_Cali_Check_2.tStop = globalClock.getTime(format='float')
        Pre_Shock_ISI_Cali_Check_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Pre_Shock_ISI_Cali_Check_2.stopped', Pre_Shock_ISI_Cali_Check_2.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Pre_Shock_ISI_Cali_Check_2.maxDurationReached:
            routineTimer.addTime(-Pre_Shock_ISI_Cali_Check_2.maxDuration)
        elif Pre_Shock_ISI_Cali_Check_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Shock_ISI_Post_Check_2" ---
        # create an object to store info about Routine Shock_ISI_Post_Check_2
        Shock_ISI_Post_Check_2 = data.Routine(
            name='Shock_ISI_Post_Check_2',
            components=[Calib_Shock_Cross_3],
        )
        Shock_ISI_Post_Check_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Stimulation_Calib_Code_3
        ctl.demand = last_demand
        ctl.pulse_width = last_pulse_width
        ctl.enabled = 1  # Re-arm device
        
        trigger_thread = threading.Thread(target=safe_run)
        trigger_thread.start()
        trigger_thread.join(timeout=2.0)  # 2-second timeout
        
        if trigger_thread.is_alive():
            print("⚠️ DS8R trigger timed out!")
        # Run 'Begin Routine' code from RoutSkip9
        if StimCalEnabled.lower() not in ['yes', 'y']:
            continueRoutine = False
        # store start times for Shock_ISI_Post_Check_2
        Shock_ISI_Post_Check_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Shock_ISI_Post_Check_2.tStart = globalClock.getTime(format='float')
        Shock_ISI_Post_Check_2.status = STARTED
        thisExp.addData('Shock_ISI_Post_Check_2.started', Shock_ISI_Post_Check_2.tStart)
        Shock_ISI_Post_Check_2.maxDuration = None
        # keep track of which components have finished
        Shock_ISI_Post_Check_2Components = Shock_ISI_Post_Check_2.components
        for thisComponent in Shock_ISI_Post_Check_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Shock_ISI_Post_Check_2" ---
        # if trial has changed, end Routine now
        if isinstance(SecondLoopPass, data.TrialHandler2) and thisSecondLoopPas.thisN != SecondLoopPass.thisTrial.thisN:
            continueRoutine = False
        Shock_ISI_Post_Check_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Calib_Shock_Cross_3* updates
            
            # if Calib_Shock_Cross_3 is starting this frame...
            if Calib_Shock_Cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Calib_Shock_Cross_3.frameNStart = frameN  # exact frame index
                Calib_Shock_Cross_3.tStart = t  # local t and not account for scr refresh
                Calib_Shock_Cross_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Calib_Shock_Cross_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_3.started')
                # update status
                Calib_Shock_Cross_3.status = STARTED
                Calib_Shock_Cross_3.setAutoDraw(True)
            
            # if Calib_Shock_Cross_3 is active this frame...
            if Calib_Shock_Cross_3.status == STARTED:
                # update params
                pass
            
            # if Calib_Shock_Cross_3 is stopping this frame...
            if Calib_Shock_Cross_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Calib_Shock_Cross_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Calib_Shock_Cross_3.tStop = t  # not accounting for scr refresh
                    Calib_Shock_Cross_3.tStopRefresh = tThisFlipGlobal  # on global time
                    Calib_Shock_Cross_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_3.stopped')
                    # update status
                    Calib_Shock_Cross_3.status = FINISHED
                    Calib_Shock_Cross_3.setAutoDraw(False)
            # Run 'Each Frame' code from Box_Cali_Shock_3
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Shock_ISI_Post_Check_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Shock_ISI_Post_Check_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Shock_ISI_Post_Check_2" ---
        for thisComponent in Shock_ISI_Post_Check_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Shock_ISI_Post_Check_2
        Shock_ISI_Post_Check_2.tStop = globalClock.getTime(format='float')
        Shock_ISI_Post_Check_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Shock_ISI_Post_Check_2.stopped', Shock_ISI_Post_Check_2.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Shock_ISI_Post_Check_2.maxDurationReached:
            routineTimer.addTime(-Shock_ISI_Post_Check_2.maxDuration)
        elif Shock_ISI_Post_Check_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Shock_Calib_Looper_3" ---
        # create an object to store info about Routine Shock_Calib_Looper_3
        Shock_Calib_Looper_3 = data.Routine(
            name='Shock_Calib_Looper_3',
            components=[slider_keys3, pain_slider3],
        )
        Shock_Calib_Looper_3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for slider_keys3
        slider_keys3.keys = []
        slider_keys3.rt = []
        _slider_keys3_allKeys = []
        pain_slider3.reset()
        # Run 'Begin Routine' code from Slider_Code_3
        slider_keys2.clearEvents()
        
        # Run 'Begin Routine' code from Slider_Text_3
        from psychopy import visual, core, event
        
        # One text stim per color segment
        text_sliderconf_1 = visual.TextStim(
            win,
            text="How strong was the stimulation?",
            color='black',
            pos=(-0.5, 0.15),  # adjust as needed
            height=0.0275,
            anchorHoriz='left'
        )
        
        # One text stim per color segment
        text_sliderconf_2 = visual.TextStim(
            win,
            text="Press ← or → to change rating. Press spacebar to confirm.",
            color='black',
            pos=(-0.5, 0.05),  # adjust as needed
            height=0.0275,
            anchorHoriz='left'
        )
        
        # Run 'Begin Routine' code from End_Loop_3
        
        
        # Run 'Begin Routine' code from RoutSkip10
        if StimCalEnabled.lower() not in ['yes', 'y']:
            continueRoutine = False
        # store start times for Shock_Calib_Looper_3
        Shock_Calib_Looper_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Shock_Calib_Looper_3.tStart = globalClock.getTime(format='float')
        Shock_Calib_Looper_3.status = STARTED
        thisExp.addData('Shock_Calib_Looper_3.started', Shock_Calib_Looper_3.tStart)
        Shock_Calib_Looper_3.maxDuration = None
        # keep track of which components have finished
        Shock_Calib_Looper_3Components = Shock_Calib_Looper_3.components
        for thisComponent in Shock_Calib_Looper_3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Shock_Calib_Looper_3" ---
        # if trial has changed, end Routine now
        if isinstance(SecondLoopPass, data.TrialHandler2) and thisSecondLoopPas.thisN != SecondLoopPass.thisTrial.thisN:
            continueRoutine = False
        Shock_Calib_Looper_3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *slider_keys3* updates
            waitOnFlip = False
            
            # if slider_keys3 is starting this frame...
            if slider_keys3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_keys3.frameNStart = frameN  # exact frame index
                slider_keys3.tStart = t  # local t and not account for scr refresh
                slider_keys3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_keys3, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_keys3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(slider_keys3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(slider_keys3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if slider_keys3 is stopping this frame...
            if slider_keys3.status == STARTED:
                if bool('space' in slider_keys3.keys):
                    # keep track of stop time/frame for later
                    slider_keys3.tStop = t  # not accounting for scr refresh
                    slider_keys3.tStopRefresh = tThisFlipGlobal  # on global time
                    slider_keys3.frameNStop = frameN  # exact frame index
                    # update status
                    slider_keys3.status = FINISHED
                    slider_keys3.status = FINISHED
            if slider_keys3.status == STARTED and not waitOnFlip:
                theseKeys = slider_keys3.getKeys(keyList=['left','right', 'space', '1', '2'], ignoreKeys=["escape"], waitRelease=False)
                _slider_keys3_allKeys.extend(theseKeys)
                if len(_slider_keys3_allKeys):
                    slider_keys3.keys = _slider_keys3_allKeys[-1].name  # just the last key pressed
                    slider_keys3.rt = _slider_keys3_allKeys[-1].rt
                    slider_keys3.duration = _slider_keys3_allKeys[-1].duration
            
            # *pain_slider3* updates
            
            # if pain_slider3 is starting this frame...
            if pain_slider3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pain_slider3.frameNStart = frameN  # exact frame index
                pain_slider3.tStart = t  # local t and not account for scr refresh
                pain_slider3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pain_slider3, 'tStartRefresh')  # time at next scr refresh
                # update status
                pain_slider3.status = STARTED
                pain_slider3.setAutoDraw(True)
            
            # if pain_slider3 is active this frame...
            if pain_slider3.status == STARTED:
                # update params
                pass
            
            # if pain_slider3 is stopping this frame...
            if pain_slider3.status == STARTED:
                if bool('space' in slider_keys3.keys):
                    # keep track of stop time/frame for later
                    pain_slider3.tStop = t  # not accounting for scr refresh
                    pain_slider3.tStopRefresh = tThisFlipGlobal  # on global time
                    pain_slider3.frameNStop = frameN  # exact frame index
                    # update status
                    pain_slider3.status = FINISHED
                    pain_slider3.setAutoDraw(False)
            # Run 'Each Frame' code from Box_Shock_Cali_5
            grayBox.draw()
            # Run 'Each Frame' code from Slider_Code_3
            # Read keypresses from the Builder's Keyboard component
            keys = slider_keys3.getKeys()
            
            for key in keys:
                if key.name in ['left', '1']:
                    if pain_slider3.markerPos is not None:
                        pain_slider3.markerPos = max(pain_slider3.markerPos - 1, 0)
                    else:
                        pain_slider3.markerPos = 0
            
                elif key.name in ['right', '2']:
                    if pain_slider3.markerPos is not None:
                        pain_slider3.markerPos = min(pain_slider3.markerPos + 1, 10)
                    else:
                        pain_slider3.markerPos = 1
            
                elif key.name in ['space', 'return']:
                    rating = pain_slider3.getRating()
                    if rating is not None:
                        print(f"✅ Rating confirmed: {rating}")
                        thisExp.addData("pain_rating3", rating)
                        continueRoutine = False  # End the routine
            
            # Run 'Each Frame' code from Slider_Text_3
            text_sliderconf_1.draw()
            text_sliderconf_2.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Shock_Calib_Looper_3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Shock_Calib_Looper_3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Shock_Calib_Looper_3" ---
        for thisComponent in Shock_Calib_Looper_3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Shock_Calib_Looper_3
        Shock_Calib_Looper_3.tStop = globalClock.getTime(format='float')
        Shock_Calib_Looper_3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Shock_Calib_Looper_3.stopped', Shock_Calib_Looper_3.tStop)
        SecondLoopPass.addData('pain_slider3.response', pain_slider3.getRating())
        SecondLoopPass.addData('pain_slider3.rt', pain_slider3.getRT())
        # Run 'End Routine' code from End_Loop_3
        # Ensure rating is stored
        if pain_slider3.rating is None and pain_slider3.markerPos is not None:
            pain_slider3.rating = pain_slider3.markerPos
        
        thisExp.addData('pain_rating3', pain_slider3.rating)
        
        if pain_slider3.rating == 8:
            SecondLoopPass.finished = True
            
        thisExp.addData('first_cali_final_demand', last_demand)
        # the Routine "Shock_Calib_Looper_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 99.0 repeats of 'SecondLoopPass'
    
    
    # --- Prepare to start Routine "Instructions_Final" ---
    # create an object to store info about Routine Instructions_Final
    Instructions_Final = data.Routine(
        name='Instructions_Final',
        components=[Instr_Key5],
    )
    Instructions_Final.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Instr_Key5
    Instr_Key5.keys = []
    Instr_Key5.rt = []
    _Instr_Key5_allKeys = []
    # store start times for Instructions_Final
    Instructions_Final.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_Final.tStart = globalClock.getTime(format='float')
    Instructions_Final.status = STARTED
    thisExp.addData('Instructions_Final.started', Instructions_Final.tStart)
    Instructions_Final.maxDuration = None
    # keep track of which components have finished
    Instructions_FinalComponents = Instructions_Final.components
    for thisComponent in Instructions_Final.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_Final" ---
    Instructions_Final.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box18_3
        grayBox.draw()
        # Run 'Each Frame' code from Text_code_4
        text_ISI_instr8.draw()
        text_ISI_instr10.draw()
        text_ISI_instr9.draw()
        
        # *Instr_Key5* updates
        waitOnFlip = False
        
        # if Instr_Key5 is starting this frame...
        if Instr_Key5.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Instr_Key5.frameNStart = frameN  # exact frame index
            Instr_Key5.tStart = t  # local t and not account for scr refresh
            Instr_Key5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Key5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instr_Key5.started')
            # update status
            Instr_Key5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instr_Key5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instr_Key5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instr_Key5.status == STARTED and not waitOnFlip:
            theseKeys = Instr_Key5.getKeys(keyList=['left','right','1','2'], ignoreKeys=["escape"], waitRelease=False)
            _Instr_Key5_allKeys.extend(theseKeys)
            if len(_Instr_Key5_allKeys):
                Instr_Key5.keys = _Instr_Key5_allKeys[-1].name  # just the last key pressed
                Instr_Key5.rt = _Instr_Key5_allKeys[-1].rt
                Instr_Key5.duration = _Instr_Key5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_Final.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_Final.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_Final" ---
    for thisComponent in Instructions_Final.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_Final
    Instructions_Final.tStop = globalClock.getTime(format='float')
    Instructions_Final.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_Final.stopped', Instructions_Final.tStop)
    # Run 'End Routine' code from Timer_0
    time_trialEnd = globalClock.getTime()
    
    thisExp.addData('Experiment_Begin_Time', time_trialEnd)
    thisExp.nextEntry()
    # the Routine "Instructions_Final" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Prompt_Looper = data.TrialHandler2(
        name='Prompt_Looper',
        nReps=5.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(Prompt_Looper)  # add the loop to the experiment
    thisPrompt_Looper = Prompt_Looper.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrompt_Looper.rgb)
    if thisPrompt_Looper != None:
        for paramName in thisPrompt_Looper:
            globals()[paramName] = thisPrompt_Looper[paramName]
    
    for thisPrompt_Looper in Prompt_Looper:
        currentLoop = Prompt_Looper
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisPrompt_Looper.rgb)
        if thisPrompt_Looper != None:
            for paramName in thisPrompt_Looper:
                globals()[paramName] = thisPrompt_Looper[paramName]
        
        # --- Prepare to start Routine "ScannerPrompt" ---
        # create an object to store info about Routine ScannerPrompt
        ScannerPrompt = data.Routine(
            name='ScannerPrompt',
            components=[Scanner_wait_text, Scanner_control],
        )
        ScannerPrompt.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for Scanner_control
        Scanner_control.keys = []
        Scanner_control.rt = []
        _Scanner_control_allKeys = []
        # Run 'Begin Routine' code from Scanner_timer
        time_ScannerPromptBegin = globalClock.getTime()
        # Run 'Begin Routine' code from Routine_Skip
        if fMRI_enabled.lower() not in ['yes', 'y']:
            continueRoutine = False
        # store start times for ScannerPrompt
        ScannerPrompt.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ScannerPrompt.tStart = globalClock.getTime(format='float')
        ScannerPrompt.status = STARTED
        thisExp.addData('ScannerPrompt.started', ScannerPrompt.tStart)
        ScannerPrompt.maxDuration = None
        # keep track of which components have finished
        ScannerPromptComponents = ScannerPrompt.components
        for thisComponent in ScannerPrompt.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ScannerPrompt" ---
        # if trial has changed, end Routine now
        if isinstance(Prompt_Looper, data.TrialHandler2) and thisPrompt_Looper.thisN != Prompt_Looper.thisTrial.thisN:
            continueRoutine = False
        ScannerPrompt.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Scanner_wait_text* updates
            
            # if Scanner_wait_text is starting this frame...
            if Scanner_wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Scanner_wait_text.frameNStart = frameN  # exact frame index
                Scanner_wait_text.tStart = t  # local t and not account for scr refresh
                Scanner_wait_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Scanner_wait_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Scanner_wait_text.started')
                # update status
                Scanner_wait_text.status = STARTED
                Scanner_wait_text.setAutoDraw(True)
            
            # if Scanner_wait_text is active this frame...
            if Scanner_wait_text.status == STARTED:
                # update params
                pass
            
            # *Scanner_control* updates
            waitOnFlip = False
            
            # if Scanner_control is starting this frame...
            if Scanner_control.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Scanner_control.frameNStart = frameN  # exact frame index
                Scanner_control.tStart = t  # local t and not account for scr refresh
                Scanner_control.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Scanner_control, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Scanner_control.started')
                # update status
                Scanner_control.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Scanner_control.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Scanner_control.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Scanner_control.status == STARTED and not waitOnFlip:
                theseKeys = Scanner_control.getKeys(keyList=['5'], ignoreKeys=["escape"], waitRelease=False)
                _Scanner_control_allKeys.extend(theseKeys)
                if len(_Scanner_control_allKeys):
                    Scanner_control.keys = _Scanner_control_allKeys[-1].name  # just the last key pressed
                    Scanner_control.rt = _Scanner_control_allKeys[-1].rt
                    Scanner_control.duration = _Scanner_control_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from BoxScanPrompt
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ScannerPrompt.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ScannerPrompt.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ScannerPrompt" ---
        for thisComponent in ScannerPrompt.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ScannerPrompt
        ScannerPrompt.tStop = globalClock.getTime(format='float')
        ScannerPrompt.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ScannerPrompt.stopped', ScannerPrompt.tStop)
        # Run 'End Routine' code from Scanner_timer
        time_ScannerPromptEnd = globalClock.getTime()
        
        thisExp.addData('time_ScannerPromptBegin', time_ScannerPromptBegin)
        thisExp.addData('time_ScannerPromptEnd', time_ScannerPromptEnd)
        # the Routine "ScannerPrompt" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 5.0 repeats of 'Prompt_Looper'
    
    
    # --- Prepare to start Routine "Pre_Block_ISI" ---
    # create an object to store info about Routine Pre_Block_ISI
    Pre_Block_ISI = data.Routine(
        name='Pre_Block_ISI',
        components=[ISI_Pre],
    )
    Pre_Block_ISI.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Pre_Timer
    time_trialBegin = globalClock.getTime()
    
    # store start times for Pre_Block_ISI
    Pre_Block_ISI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Pre_Block_ISI.tStart = globalClock.getTime(format='float')
    Pre_Block_ISI.status = STARTED
    thisExp.addData('Pre_Block_ISI.started', Pre_Block_ISI.tStart)
    Pre_Block_ISI.maxDuration = None
    # keep track of which components have finished
    Pre_Block_ISIComponents = Pre_Block_ISI.components
    for thisComponent in Pre_Block_ISI.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Pre_Block_ISI" ---
    Pre_Block_ISI.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI_Pre* updates
        
        # if ISI_Pre is starting this frame...
        if ISI_Pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_Pre.frameNStart = frameN  # exact frame index
            ISI_Pre.tStart = t  # local t and not account for scr refresh
            ISI_Pre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_Pre, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI_Pre.started')
            # update status
            ISI_Pre.status = STARTED
            ISI_Pre.setAutoDraw(True)
        
        # if ISI_Pre is active this frame...
        if ISI_Pre.status == STARTED:
            # update params
            pass
        
        # if ISI_Pre is stopping this frame...
        if ISI_Pre.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI_Pre.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                ISI_Pre.tStop = t  # not accounting for scr refresh
                ISI_Pre.tStopRefresh = tThisFlipGlobal  # on global time
                ISI_Pre.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI_Pre.stopped')
                # update status
                ISI_Pre.status = FINISHED
                ISI_Pre.setAutoDraw(False)
        # Run 'Each Frame' code from Pre_Box
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Pre_Block_ISI.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pre_Block_ISI.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Pre_Block_ISI" ---
    for thisComponent in Pre_Block_ISI.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Pre_Block_ISI
    Pre_Block_ISI.tStop = globalClock.getTime(format='float')
    Pre_Block_ISI.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Pre_Block_ISI.stopped', Pre_Block_ISI.tStop)
    # Run 'End Routine' code from Pre_Timer
    time_trialEnd = globalClock.getTime()
    
    thisExp.addData('Pre_ISI_Begin', time_trialBegin)
    thisExp.addData('Pre_ISI_End', time_trialEnd)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Pre_Block_ISI.maxDurationReached:
        routineTimer.addTime(-Pre_Block_ISI.maxDuration)
    elif Pre_Block_ISI.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    InnerLoop = data.TrialHandler2(
        name='InnerLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(VersionSelection_H1), 
        seed=None, 
    )
    thisExp.addLoop(InnerLoop)  # add the loop to the experiment
    thisInnerLoop = InnerLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop.rgb)
    if thisInnerLoop != None:
        for paramName in thisInnerLoop:
            globals()[paramName] = thisInnerLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisInnerLoop in InnerLoop:
        currentLoop = InnerLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop.rgb)
        if thisInnerLoop != None:
            for paramName in thisInnerLoop:
                globals()[paramName] = thisInnerLoop[paramName]
        
        # --- Prepare to start Routine "Blank" ---
        # create an object to store info about Routine Blank
        Blank = data.Routine(
            name='Blank',
            components=[Blank_Text],
        )
        Blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Timer_PostISI
        time_trialBegin = globalClock.getTime()
        # store start times for Blank
        Blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Blank.tStart = globalClock.getTime(format='float')
        Blank.status = STARTED
        thisExp.addData('Blank.started', Blank.tStart)
        Blank.maxDuration = None
        # keep track of which components have finished
        BlankComponents = Blank.components
        for thisComponent in Blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Blank" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
            continueRoutine = False
        Blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.05:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Blank_Text* updates
            
            # if Blank_Text is starting this frame...
            if Blank_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Blank_Text.frameNStart = frameN  # exact frame index
                Blank_Text.tStart = t  # local t and not account for scr refresh
                Blank_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Blank_Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Blank_Text.started')
                # update status
                Blank_Text.status = STARTED
                Blank_Text.setAutoDraw(True)
            
            # if Blank_Text is active this frame...
            if Blank_Text.status == STARTED:
                # update params
                pass
            
            # if Blank_Text is stopping this frame...
            if Blank_Text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Blank_Text.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    Blank_Text.tStop = t  # not accounting for scr refresh
                    Blank_Text.tStopRefresh = tThisFlipGlobal  # on global time
                    Blank_Text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Blank_Text.stopped')
                    # update status
                    Blank_Text.status = FINISHED
                    Blank_Text.setAutoDraw(False)
            # Run 'Each Frame' code from Box21
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Blank" ---
        for thisComponent in Blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Blank
        Blank.tStop = globalClock.getTime(format='float')
        Blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Blank.stopped', Blank.tStop)
        # Run 'End Routine' code from Timer_PostISI
        thisExp.addData('PostISI_Start_Time', time_trialBegin)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Blank.maxDurationReached:
            routineTimer.addTime(-Blank.maxDuration)
        elif Blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.050000)
        
        # --- Prepare to start Routine "Main_Routine_Stimulus_Selection_H1" ---
        # create an object to store info about Routine Main_Routine_Stimulus_Selection_H1
        Main_Routine_Stimulus_Selection_H1 = data.Routine(
            name='Main_Routine_Stimulus_Selection_H1',
            components=[Cued_Image, Estimation_Select],
        )
        Main_Routine_Stimulus_Selection_H1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Cued_Image.setImage(Fractal_img)
        # create starting attributes for Estimation_Select
        Estimation_Select.keys = []
        Estimation_Select.rt = []
        _Estimation_Select_allKeys = []
        # Run 'Begin Routine' code from Timer_2
        time_trialBegin = globalClock.getTime()
        
        
        # store start times for Main_Routine_Stimulus_Selection_H1
        Main_Routine_Stimulus_Selection_H1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Routine_Stimulus_Selection_H1.tStart = globalClock.getTime(format='float')
        Main_Routine_Stimulus_Selection_H1.status = STARTED
        thisExp.addData('Main_Routine_Stimulus_Selection_H1.started', Main_Routine_Stimulus_Selection_H1.tStart)
        Main_Routine_Stimulus_Selection_H1.maxDuration = None
        # keep track of which components have finished
        Main_Routine_Stimulus_Selection_H1Components = Main_Routine_Stimulus_Selection_H1.components
        for thisComponent in Main_Routine_Stimulus_Selection_H1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Routine_Stimulus_Selection_H1" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
            continueRoutine = False
        Main_Routine_Stimulus_Selection_H1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Cued_Image* updates
            
            # if Cued_Image is starting this frame...
            if Cued_Image.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                Cued_Image.frameNStart = frameN  # exact frame index
                Cued_Image.tStart = t  # local t and not account for scr refresh
                Cued_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cued_Image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cued_Image.started')
                # update status
                Cued_Image.status = STARTED
                Cued_Image.setAutoDraw(True)
            
            # if Cued_Image is active this frame...
            if Cued_Image.status == STARTED:
                # update params
                pass
            
            # *Estimation_Select* updates
            waitOnFlip = False
            
            # if Estimation_Select is starting this frame...
            if Estimation_Select.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                Estimation_Select.frameNStart = frameN  # exact frame index
                Estimation_Select.tStart = t  # local t and not account for scr refresh
                Estimation_Select.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Estimation_Select, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Estimation_Select.started')
                # update status
                Estimation_Select.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Estimation_Select.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Estimation_Select.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Estimation_Select.status == STARTED and not waitOnFlip:
                theseKeys = Estimation_Select.getKeys(keyList=['left','right','1','2'], ignoreKeys=["escape"], waitRelease=False)
                _Estimation_Select_allKeys.extend(theseKeys)
                if len(_Estimation_Select_allKeys):
                    Estimation_Select.keys = _Estimation_Select_allKeys[-1].name  # just the last key pressed
                    Estimation_Select.rt = _Estimation_Select_allKeys[-1].rt
                    Estimation_Select.duration = _Estimation_Select_allKeys[-1].duration
                    # was this correct?
                    if (Estimation_Select.keys == str(High_Prob_Choice_Corr)) or (Estimation_Select.keys == High_Prob_Choice_Corr):
                        Estimation_Select.corr = 1
                    else:
                        Estimation_Select.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from Box2
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Routine_Stimulus_Selection_H1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Routine_Stimulus_Selection_H1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Routine_Stimulus_Selection_H1" ---
        for thisComponent in Main_Routine_Stimulus_Selection_H1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Routine_Stimulus_Selection_H1
        Main_Routine_Stimulus_Selection_H1.tStop = globalClock.getTime(format='float')
        Main_Routine_Stimulus_Selection_H1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Routine_Stimulus_Selection_H1.stopped', Main_Routine_Stimulus_Selection_H1.tStop)
        # check responses
        if Estimation_Select.keys in ['', [], None]:  # No response was made
            Estimation_Select.keys = None
            # was no response the correct answer?!
            if str(High_Prob_Choice_Corr).lower() == 'none':
               Estimation_Select.corr = 1;  # correct non-response
            else:
               Estimation_Select.corr = 0;  # failed to respond (incorrectly)
        # store data for InnerLoop (TrialHandler)
        InnerLoop.addData('Estimation_Select.keys',Estimation_Select.keys)
        InnerLoop.addData('Estimation_Select.corr', Estimation_Select.corr)
        if Estimation_Select.keys != None:  # we had a response
            InnerLoop.addData('Estimation_Select.rt', Estimation_Select.rt)
            InnerLoop.addData('Estimation_Select.duration', Estimation_Select.duration)
        # Run 'End Routine' code from Store_Selection
        if Estimation_Select.keys:
            lastKey = Estimation_Select.keys
            if lastKey in ['left', '1']:
                selectedColor = [0.0000, 0.3, 0.05]
            elif lastKey in ['right', '2']:
                selectedColor = [0.52, 0.4, -0.02]
            else:
                selectedColor = 'grey'
        else:
            lastKey = None
            selectedColor = 'grey'
        # Run 'End Routine' code from Timer_2
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('Choice_Begin_Time', time_trialBegin)
        thisExp.addData('Choice_End_Time', time_trialEnd)
        # the Routine "Main_Routine_Stimulus_Selection_H1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Main_Routine_Stimulus_Post_Selection_H1" ---
        # create an object to store info about Routine Main_Routine_Stimulus_Post_Selection_H1
        Main_Routine_Stimulus_Post_Selection_H1 = data.Routine(
            name='Main_Routine_Stimulus_Post_Selection_H1',
            components=[Selection_Result, Cued_image_post],
        )
        Main_Routine_Stimulus_Post_Selection_H1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Selection_Result.setFillColor(selectedColor)
        Selection_Result.setLineColor('grey')
        Cued_image_post.setImage(Fractal_img)
        # Run 'Begin Routine' code from Timer_3
        time_trialBegin = globalClock.getTime()
        # store start times for Main_Routine_Stimulus_Post_Selection_H1
        Main_Routine_Stimulus_Post_Selection_H1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Routine_Stimulus_Post_Selection_H1.tStart = globalClock.getTime(format='float')
        Main_Routine_Stimulus_Post_Selection_H1.status = STARTED
        thisExp.addData('Main_Routine_Stimulus_Post_Selection_H1.started', Main_Routine_Stimulus_Post_Selection_H1.tStart)
        Main_Routine_Stimulus_Post_Selection_H1.maxDuration = None
        # keep track of which components have finished
        Main_Routine_Stimulus_Post_Selection_H1Components = Main_Routine_Stimulus_Post_Selection_H1.components
        for thisComponent in Main_Routine_Stimulus_Post_Selection_H1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Routine_Stimulus_Post_Selection_H1" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
            continueRoutine = False
        Main_Routine_Stimulus_Post_Selection_H1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Selection_Result* updates
            
            # if Selection_Result is starting this frame...
            if Selection_Result.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Selection_Result.frameNStart = frameN  # exact frame index
                Selection_Result.tStart = t  # local t and not account for scr refresh
                Selection_Result.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Selection_Result, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Selection_Result.started')
                # update status
                Selection_Result.status = STARTED
                Selection_Result.setAutoDraw(True)
            
            # if Selection_Result is active this frame...
            if Selection_Result.status == STARTED:
                # update params
                pass
            
            # if Selection_Result is stopping this frame...
            if Selection_Result.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Selection_Result.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Selection_Result.tStop = t  # not accounting for scr refresh
                    Selection_Result.tStopRefresh = tThisFlipGlobal  # on global time
                    Selection_Result.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Selection_Result.stopped')
                    # update status
                    Selection_Result.status = FINISHED
                    Selection_Result.setAutoDraw(False)
            
            # *Cued_image_post* updates
            
            # if Cued_image_post is starting this frame...
            if Cued_image_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Cued_image_post.frameNStart = frameN  # exact frame index
                Cued_image_post.tStart = t  # local t and not account for scr refresh
                Cued_image_post.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cued_image_post, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cued_image_post.started')
                # update status
                Cued_image_post.status = STARTED
                Cued_image_post.setAutoDraw(True)
            
            # if Cued_image_post is active this frame...
            if Cued_image_post.status == STARTED:
                # update params
                pass
            
            # if Cued_image_post is stopping this frame...
            if Cued_image_post.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Cued_image_post.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Cued_image_post.tStop = t  # not accounting for scr refresh
                    Cued_image_post.tStopRefresh = tThisFlipGlobal  # on global time
                    Cued_image_post.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cued_image_post.stopped')
                    # update status
                    Cued_image_post.status = FINISHED
                    Cued_image_post.setAutoDraw(False)
            # Run 'Each Frame' code from Box3
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Routine_Stimulus_Post_Selection_H1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Routine_Stimulus_Post_Selection_H1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Routine_Stimulus_Post_Selection_H1" ---
        for thisComponent in Main_Routine_Stimulus_Post_Selection_H1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Routine_Stimulus_Post_Selection_H1
        Main_Routine_Stimulus_Post_Selection_H1.tStop = globalClock.getTime(format='float')
        Main_Routine_Stimulus_Post_Selection_H1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Routine_Stimulus_Post_Selection_H1.stopped', Main_Routine_Stimulus_Post_Selection_H1.tStop)
        # Run 'End Routine' code from Timer_3
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('Post_choice_Begin_Time', time_trialBegin)
        thisExp.addData('Post_choice_End_Time', time_trialEnd)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Main_Routine_Stimulus_Post_Selection_H1.maxDurationReached:
            routineTimer.addTime(-Main_Routine_Stimulus_Post_Selection_H1.maxDuration)
        elif Main_Routine_Stimulus_Post_Selection_H1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "Blank" ---
        # create an object to store info about Routine Blank
        Blank = data.Routine(
            name='Blank',
            components=[Blank_Text],
        )
        Blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Timer_PostISI
        time_trialBegin = globalClock.getTime()
        # store start times for Blank
        Blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Blank.tStart = globalClock.getTime(format='float')
        Blank.status = STARTED
        thisExp.addData('Blank.started', Blank.tStart)
        Blank.maxDuration = None
        # keep track of which components have finished
        BlankComponents = Blank.components
        for thisComponent in Blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Blank" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
            continueRoutine = False
        Blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.05:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Blank_Text* updates
            
            # if Blank_Text is starting this frame...
            if Blank_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Blank_Text.frameNStart = frameN  # exact frame index
                Blank_Text.tStart = t  # local t and not account for scr refresh
                Blank_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Blank_Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Blank_Text.started')
                # update status
                Blank_Text.status = STARTED
                Blank_Text.setAutoDraw(True)
            
            # if Blank_Text is active this frame...
            if Blank_Text.status == STARTED:
                # update params
                pass
            
            # if Blank_Text is stopping this frame...
            if Blank_Text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Blank_Text.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    Blank_Text.tStop = t  # not accounting for scr refresh
                    Blank_Text.tStopRefresh = tThisFlipGlobal  # on global time
                    Blank_Text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Blank_Text.stopped')
                    # update status
                    Blank_Text.status = FINISHED
                    Blank_Text.setAutoDraw(False)
            # Run 'Each Frame' code from Box21
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Blank" ---
        for thisComponent in Blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Blank
        Blank.tStop = globalClock.getTime(format='float')
        Blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Blank.stopped', Blank.tStop)
        # Run 'End Routine' code from Timer_PostISI
        thisExp.addData('PostISI_Start_Time', time_trialBegin)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Blank.maxDurationReached:
            routineTimer.addTime(-Blank.maxDuration)
        elif Blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.050000)
        
        # --- Prepare to start Routine "Main_Task_PostISI_H1" ---
        # create an object to store info about Routine Main_Task_PostISI_H1
        Main_Task_PostISI_H1 = data.Routine(
            name='Main_Task_PostISI_H1',
            components=[Main_Task_H1_Post_ISI],
        )
        Main_Task_PostISI_H1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Main_Task_PostISI_H1
        Main_Task_PostISI_H1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Task_PostISI_H1.tStart = globalClock.getTime(format='float')
        Main_Task_PostISI_H1.status = STARTED
        thisExp.addData('Main_Task_PostISI_H1.started', Main_Task_PostISI_H1.tStart)
        Main_Task_PostISI_H1.maxDuration = None
        # keep track of which components have finished
        Main_Task_PostISI_H1Components = Main_Task_PostISI_H1.components
        for thisComponent in Main_Task_PostISI_H1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Task_PostISI_H1" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
            continueRoutine = False
        Main_Task_PostISI_H1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Main_Task_H1_Post_ISI* updates
            
            # if Main_Task_H1_Post_ISI is starting this frame...
            if Main_Task_H1_Post_ISI.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                Main_Task_H1_Post_ISI.frameNStart = frameN  # exact frame index
                Main_Task_H1_Post_ISI.tStart = t  # local t and not account for scr refresh
                Main_Task_H1_Post_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Main_Task_H1_Post_ISI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Main_Task_H1_Post_ISI.started')
                # update status
                Main_Task_H1_Post_ISI.status = STARTED
                Main_Task_H1_Post_ISI.setAutoDraw(True)
            
            # if Main_Task_H1_Post_ISI is active this frame...
            if Main_Task_H1_Post_ISI.status == STARTED:
                # update params
                pass
            
            # if Main_Task_H1_Post_ISI is stopping this frame...
            if Main_Task_H1_Post_ISI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Main_Task_H1_Post_ISI.tStartRefresh + Int_ISI-frameTolerance:
                    # keep track of stop time/frame for later
                    Main_Task_H1_Post_ISI.tStop = t  # not accounting for scr refresh
                    Main_Task_H1_Post_ISI.tStopRefresh = tThisFlipGlobal  # on global time
                    Main_Task_H1_Post_ISI.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Main_Task_H1_Post_ISI.stopped')
                    # update status
                    Main_Task_H1_Post_ISI.status = FINISHED
                    Main_Task_H1_Post_ISI.setAutoDraw(False)
            # Run 'Each Frame' code from Box4
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Task_PostISI_H1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Task_PostISI_H1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Task_PostISI_H1" ---
        for thisComponent in Main_Task_PostISI_H1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Task_PostISI_H1
        Main_Task_PostISI_H1.tStop = globalClock.getTime(format='float')
        Main_Task_PostISI_H1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Task_PostISI_H1.stopped', Main_Task_PostISI_H1.tStop)
        # Run 'End Routine' code from Timer_4
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('PostISI_End_Time', time_trialEnd)
        # the Routine "Main_Task_PostISI_H1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Main_Task_Post_Outcome_H1" ---
        # create an object to store info about Routine Main_Task_Post_Outcome_H1
        Main_Task_Post_Outcome_H1 = data.Routine(
            name='Main_Task_Post_Outcome_H1',
            components=[Cross_Outcomed],
        )
        Main_Task_Post_Outcome_H1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Shock_Code
        ctl.demand = last_demand
        ctl.pulse_width = last_pulse_width
        ctl.enabled = 1  # Re-arm device
        
        if Outcome == 1:
            print("⚡ About to trigger DS8R...")
        
            # Create and start the thread
            trigger_thread = threading.Thread(target=safe_run)
            trigger_thread.start()
        
            # Wait for the thread to finish, with a timeout
            trigger_thread.join(timeout=2.0)  # adjust timeout as needed
        
            if trigger_thread.is_alive():
                print("⚠️ DS8R trigger timed out — skipping trigger this trial.")
                # Optionally, try to reset ctl or log more info
            else:
                print("✅ DS8R trigger completed.")
        else:
            print("⏭ No trigger this trial (Outcome != 1).")
        # Run 'Begin Routine' code from Timer_5
        time_trialBegin = globalClock.getTime()
        # store start times for Main_Task_Post_Outcome_H1
        Main_Task_Post_Outcome_H1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Task_Post_Outcome_H1.tStart = globalClock.getTime(format='float')
        Main_Task_Post_Outcome_H1.status = STARTED
        thisExp.addData('Main_Task_Post_Outcome_H1.started', Main_Task_Post_Outcome_H1.tStart)
        Main_Task_Post_Outcome_H1.maxDuration = None
        # keep track of which components have finished
        Main_Task_Post_Outcome_H1Components = Main_Task_Post_Outcome_H1.components
        for thisComponent in Main_Task_Post_Outcome_H1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Task_Post_Outcome_H1" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
            continueRoutine = False
        Main_Task_Post_Outcome_H1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from Box5
            grayBox.draw()
            
            # *Cross_Outcomed* updates
            
            # if Cross_Outcomed is starting this frame...
            if Cross_Outcomed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Cross_Outcomed.frameNStart = frameN  # exact frame index
                Cross_Outcomed.tStart = t  # local t and not account for scr refresh
                Cross_Outcomed.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cross_Outcomed, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cross_Outcomed.started')
                # update status
                Cross_Outcomed.status = STARTED
                Cross_Outcomed.setAutoDraw(True)
            
            # if Cross_Outcomed is active this frame...
            if Cross_Outcomed.status == STARTED:
                # update params
                pass
            
            # if Cross_Outcomed is stopping this frame...
            if Cross_Outcomed.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Cross_Outcomed.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Cross_Outcomed.tStop = t  # not accounting for scr refresh
                    Cross_Outcomed.tStopRefresh = tThisFlipGlobal  # on global time
                    Cross_Outcomed.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cross_Outcomed.stopped')
                    # update status
                    Cross_Outcomed.status = FINISHED
                    Cross_Outcomed.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Task_Post_Outcome_H1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Task_Post_Outcome_H1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Task_Post_Outcome_H1" ---
        for thisComponent in Main_Task_Post_Outcome_H1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Task_Post_Outcome_H1
        Main_Task_Post_Outcome_H1.tStop = globalClock.getTime(format='float')
        Main_Task_Post_Outcome_H1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Task_Post_Outcome_H1.stopped', Main_Task_Post_Outcome_H1.tStop)
        # Run 'End Routine' code from Timer_5
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('Outcome_Delivered_Time', time_trialBegin)
        thisExp.addData('Outcome_Delivered_Routine_End', time_trialEnd)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Main_Task_Post_Outcome_H1.maxDurationReached:
            routineTimer.addTime(-Main_Task_Post_Outcome_H1.maxDuration)
        elif Main_Task_Post_Outcome_H1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Main_Routine_ISI_H1" ---
        # create an object to store info about Routine Main_Routine_ISI_H1
        Main_Routine_ISI_H1 = data.Routine(
            name='Main_Routine_ISI_H1',
            components=[Main_Task_H1_ISI],
        )
        Main_Routine_ISI_H1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Main_Task_H1_ISI.setColor([-0.7500, -0.7500, -0.7500], colorSpace='rgb')
        Main_Task_H1_ISI.setText('+')
        # Run 'Begin Routine' code from Timer_1
        time_trialBegin = globalClock.getTime()
        # store start times for Main_Routine_ISI_H1
        Main_Routine_ISI_H1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Routine_ISI_H1.tStart = globalClock.getTime(format='float')
        Main_Routine_ISI_H1.status = STARTED
        thisExp.addData('Main_Routine_ISI_H1.started', Main_Routine_ISI_H1.tStart)
        Main_Routine_ISI_H1.maxDuration = None
        # keep track of which components have finished
        Main_Routine_ISI_H1Components = Main_Routine_ISI_H1.components
        for thisComponent in Main_Routine_ISI_H1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Routine_ISI_H1" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
            continueRoutine = False
        Main_Routine_ISI_H1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Main_Task_H1_ISI* updates
            
            # if Main_Task_H1_ISI is starting this frame...
            if Main_Task_H1_ISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Main_Task_H1_ISI.frameNStart = frameN  # exact frame index
                Main_Task_H1_ISI.tStart = t  # local t and not account for scr refresh
                Main_Task_H1_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Main_Task_H1_ISI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Main_Task_H1_ISI.started')
                # update status
                Main_Task_H1_ISI.status = STARTED
                Main_Task_H1_ISI.setAutoDraw(True)
            
            # if Main_Task_H1_ISI is active this frame...
            if Main_Task_H1_ISI.status == STARTED:
                # update params
                pass
            
            # if Main_Task_H1_ISI is stopping this frame...
            if Main_Task_H1_ISI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Main_Task_H1_ISI.tStartRefresh + Pre_ISI-frameTolerance:
                    # keep track of stop time/frame for later
                    Main_Task_H1_ISI.tStop = t  # not accounting for scr refresh
                    Main_Task_H1_ISI.tStopRefresh = tThisFlipGlobal  # on global time
                    Main_Task_H1_ISI.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Main_Task_H1_ISI.stopped')
                    # update status
                    Main_Task_H1_ISI.status = FINISHED
                    Main_Task_H1_ISI.setAutoDraw(False)
            # Run 'Each Frame' code from Box1
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Routine_ISI_H1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Routine_ISI_H1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Routine_ISI_H1" ---
        for thisComponent in Main_Routine_ISI_H1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Routine_ISI_H1
        Main_Routine_ISI_H1.tStop = globalClock.getTime(format='float')
        Main_Routine_ISI_H1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Routine_ISI_H1.stopped', Main_Routine_ISI_H1.tStop)
        # Run 'End Routine' code from Timer_1
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('Post2_ISI_Begin', time_trialBegin)
        thisExp.addData('Post2_ISI_End', time_trialEnd)
        # the Routine "Main_Routine_ISI_H1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InnerLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Break" ---
    # create an object to store info about Routine Break
    Break = data.Routine(
        name='Break',
        components=[Break_Period],
    )
    Break.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Break
    Break.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Break.tStart = globalClock.getTime(format='float')
    Break.status = STARTED
    thisExp.addData('Break.started', Break.tStart)
    Break.maxDuration = None
    # keep track of which components have finished
    BreakComponents = Break.components
    for thisComponent in Break.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Break" ---
    Break.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 180.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_Period* updates
        
        # if Break_Period is starting this frame...
        if Break_Period.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_Period.frameNStart = frameN  # exact frame index
            Break_Period.tStart = t  # local t and not account for scr refresh
            Break_Period.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_Period, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Break_Period.started')
            # update status
            Break_Period.status = STARTED
            Break_Period.setAutoDraw(True)
        
        # if Break_Period is active this frame...
        if Break_Period.status == STARTED:
            # update params
            pass
        
        # if Break_Period is stopping this frame...
        if Break_Period.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Break_Period.tStartRefresh + 180-frameTolerance:
                # keep track of stop time/frame for later
                Break_Period.tStop = t  # not accounting for scr refresh
                Break_Period.tStopRefresh = tThisFlipGlobal  # on global time
                Break_Period.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Break_Period.stopped')
                # update status
                Break_Period.status = FINISHED
                Break_Period.setAutoDraw(False)
        # Run 'Each Frame' code from Break_Box
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Break.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Break.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Break" ---
    for thisComponent in Break.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Break
    Break.tStop = globalClock.getTime(format='float')
    Break.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Break.stopped', Break.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Break.maxDurationReached:
        routineTimer.addTime(-Break.maxDuration)
    elif Break.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-180.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Post_Break" ---
    # create an object to store info about Routine Post_Break
    Post_Break = data.Routine(
        name='Post_Break',
        components=[Post_break_text, Post_break_keys],
    )
    Post_Break.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Post_break_keys
    Post_break_keys.keys = []
    Post_break_keys.rt = []
    _Post_break_keys_allKeys = []
    # Run 'Begin Routine' code from Skipper3
    if fMRI_enabled.lower() in ['yes', 'y']:
        continueRoutine = False
    # store start times for Post_Break
    Post_Break.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Post_Break.tStart = globalClock.getTime(format='float')
    Post_Break.status = STARTED
    thisExp.addData('Post_Break.started', Post_Break.tStart)
    Post_Break.maxDuration = None
    # keep track of which components have finished
    Post_BreakComponents = Post_Break.components
    for thisComponent in Post_Break.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Post_Break" ---
    Post_Break.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Post_break_text* updates
        
        # if Post_break_text is starting this frame...
        if Post_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Post_break_text.frameNStart = frameN  # exact frame index
            Post_break_text.tStart = t  # local t and not account for scr refresh
            Post_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Post_break_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Post_break_text.started')
            # update status
            Post_break_text.status = STARTED
            Post_break_text.setAutoDraw(True)
        
        # if Post_break_text is active this frame...
        if Post_break_text.status == STARTED:
            # update params
            pass
        
        # *Post_break_keys* updates
        waitOnFlip = False
        
        # if Post_break_keys is starting this frame...
        if Post_break_keys.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Post_break_keys.frameNStart = frameN  # exact frame index
            Post_break_keys.tStart = t  # local t and not account for scr refresh
            Post_break_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Post_break_keys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Post_break_keys.started')
            # update status
            Post_break_keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Post_break_keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Post_break_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Post_break_keys.status == STARTED and not waitOnFlip:
            theseKeys = Post_break_keys.getKeys(keyList=['left','right','1','2'], ignoreKeys=["escape"], waitRelease=False)
            _Post_break_keys_allKeys.extend(theseKeys)
            if len(_Post_break_keys_allKeys):
                Post_break_keys.keys = _Post_break_keys_allKeys[-1].name  # just the last key pressed
                Post_break_keys.rt = _Post_break_keys_allKeys[-1].rt
                Post_break_keys.duration = _Post_break_keys_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box13
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Post_Break.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Post_Break.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Post_Break" ---
    for thisComponent in Post_Break.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Post_Break
    Post_Break.tStop = globalClock.getTime(format='float')
    Post_Break.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Post_Break.stopped', Post_Break.tStop)
    thisExp.nextEntry()
    # the Routine "Post_Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Recal_Instr" ---
    # create an object to store info about Routine Recal_Instr
    Recal_Instr = data.Routine(
        name='Recal_Instr',
        components=[Recal_Instr_Text, Recal_Procced_Keys],
    )
    Recal_Instr.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Recal_Procced_Keys
    Recal_Procced_Keys.keys = []
    Recal_Procced_Keys.rt = []
    _Recal_Procced_Keys_allKeys = []
    # store start times for Recal_Instr
    Recal_Instr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Recal_Instr.tStart = globalClock.getTime(format='float')
    Recal_Instr.status = STARTED
    thisExp.addData('Recal_Instr.started', Recal_Instr.tStart)
    Recal_Instr.maxDuration = None
    # keep track of which components have finished
    Recal_InstrComponents = Recal_Instr.components
    for thisComponent in Recal_Instr.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Recal_Instr" ---
    Recal_Instr.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box_Recal_Instr
        grayBox.draw()
        
        # *Recal_Instr_Text* updates
        
        # if Recal_Instr_Text is starting this frame...
        if Recal_Instr_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Recal_Instr_Text.frameNStart = frameN  # exact frame index
            Recal_Instr_Text.tStart = t  # local t and not account for scr refresh
            Recal_Instr_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Recal_Instr_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Recal_Instr_Text.started')
            # update status
            Recal_Instr_Text.status = STARTED
            Recal_Instr_Text.setAutoDraw(True)
        
        # if Recal_Instr_Text is active this frame...
        if Recal_Instr_Text.status == STARTED:
            # update params
            pass
        
        # *Recal_Procced_Keys* updates
        waitOnFlip = False
        
        # if Recal_Procced_Keys is starting this frame...
        if Recal_Procced_Keys.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Recal_Procced_Keys.frameNStart = frameN  # exact frame index
            Recal_Procced_Keys.tStart = t  # local t and not account for scr refresh
            Recal_Procced_Keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Recal_Procced_Keys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Recal_Procced_Keys.started')
            # update status
            Recal_Procced_Keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Recal_Procced_Keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Recal_Procced_Keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Recal_Procced_Keys.status == STARTED and not waitOnFlip:
            theseKeys = Recal_Procced_Keys.getKeys(keyList=['left','right','1', '2'], ignoreKeys=["escape"], waitRelease=False)
            _Recal_Procced_Keys_allKeys.extend(theseKeys)
            if len(_Recal_Procced_Keys_allKeys):
                Recal_Procced_Keys.keys = _Recal_Procced_Keys_allKeys[-1].name  # just the last key pressed
                Recal_Procced_Keys.rt = _Recal_Procced_Keys_allKeys[-1].rt
                Recal_Procced_Keys.duration = _Recal_Procced_Keys_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Recal_Instr.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Recal_Instr.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Recal_Instr" ---
    for thisComponent in Recal_Instr.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Recal_Instr
    Recal_Instr.tStop = globalClock.getTime(format='float')
    Recal_Instr.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Recal_Instr.stopped', Recal_Instr.tStop)
    thisExp.nextEntry()
    # the Routine "Recal_Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    SecondLoopPass2 = data.TrialHandler2(
        name='SecondLoopPass2',
        nReps=99.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(SecondLoopPass2)  # add the loop to the experiment
    thisSecondLoopPass2 = SecondLoopPass2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSecondLoopPass2.rgb)
    if thisSecondLoopPass2 != None:
        for paramName in thisSecondLoopPass2:
            globals()[paramName] = thisSecondLoopPass2[paramName]
    
    for thisSecondLoopPass2 in SecondLoopPass2:
        currentLoop = SecondLoopPass2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisSecondLoopPass2.rgb)
        if thisSecondLoopPass2 != None:
            for paramName in thisSecondLoopPass2:
                globals()[paramName] = thisSecondLoopPass2[paramName]
        
        # set up handler to look after randomisation of conditions etc
        FirstLoopPass2 = data.TrialHandler2(
            name='FirstLoopPass2',
            nReps=99.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(FirstLoopPass2)  # add the loop to the experiment
        thisFirstLoopPass2 = FirstLoopPass2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFirstLoopPass2.rgb)
        if thisFirstLoopPass2 != None:
            for paramName in thisFirstLoopPass2:
                globals()[paramName] = thisFirstLoopPass2[paramName]
        
        for thisFirstLoopPass2 in FirstLoopPass2:
            currentLoop = FirstLoopPass2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisFirstLoopPass2.rgb)
            if thisFirstLoopPass2 != None:
                for paramName in thisFirstLoopPass2:
                    globals()[paramName] = thisFirstLoopPass2[paramName]
            
            # set up handler to look after randomisation of conditions etc
            Checkpoint2 = data.TrialHandler2(
                name='Checkpoint2',
                nReps=99.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(Checkpoint2)  # add the loop to the experiment
            thisCheckpoint2 = Checkpoint2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisCheckpoint2.rgb)
            if thisCheckpoint2 != None:
                for paramName in thisCheckpoint2:
                    globals()[paramName] = thisCheckpoint2[paramName]
            
            for thisCheckpoint2 in Checkpoint2:
                currentLoop = Checkpoint2
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # abbreviate parameter names if possible (e.g. rgb = thisCheckpoint2.rgb)
                if thisCheckpoint2 != None:
                    for paramName in thisCheckpoint2:
                        globals()[paramName] = thisCheckpoint2[paramName]
                
                # set up handler to look after randomisation of conditions etc
                CaliLoop2 = data.TrialHandler2(
                    name='CaliLoop2',
                    nReps=1.0, 
                    method='sequential', 
                    extraInfo=expInfo, 
                    originPath=-1, 
                    trialList=data.importConditions('Conditions/Shock_Calibration_Sched.xlsx'), 
                    seed=None, 
                )
                thisExp.addLoop(CaliLoop2)  # add the loop to the experiment
                thisCaliLoop2 = CaliLoop2.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisCaliLoop2.rgb)
                if thisCaliLoop2 != None:
                    for paramName in thisCaliLoop2:
                        globals()[paramName] = thisCaliLoop2[paramName]
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                
                for thisCaliLoop2 in CaliLoop2:
                    currentLoop = CaliLoop2
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                    # abbreviate parameter names if possible (e.g. rgb = thisCaliLoop2.rgb)
                    if thisCaliLoop2 != None:
                        for paramName in thisCaliLoop2:
                            globals()[paramName] = thisCaliLoop2[paramName]
                    
                    # --- Prepare to start Routine "Pre_Shock_ISI_Calib_2" ---
                    # create an object to store info about Routine Pre_Shock_ISI_Calib_2
                    Pre_Shock_ISI_Calib_2 = data.Routine(
                        name='Pre_Shock_ISI_Calib_2',
                        components=[Pre_Cali_ISI_5],
                    )
                    Pre_Shock_ISI_Calib_2.status = NOT_STARTED
                    continueRoutine = True
                    # update component parameters for each repeat
                    # store start times for Pre_Shock_ISI_Calib_2
                    Pre_Shock_ISI_Calib_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                    Pre_Shock_ISI_Calib_2.tStart = globalClock.getTime(format='float')
                    Pre_Shock_ISI_Calib_2.status = STARTED
                    thisExp.addData('Pre_Shock_ISI_Calib_2.started', Pre_Shock_ISI_Calib_2.tStart)
                    Pre_Shock_ISI_Calib_2.maxDuration = None
                    # keep track of which components have finished
                    Pre_Shock_ISI_Calib_2Components = Pre_Shock_ISI_Calib_2.components
                    for thisComponent in Pre_Shock_ISI_Calib_2.components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "Pre_Shock_ISI_Calib_2" ---
                    # if trial has changed, end Routine now
                    if isinstance(CaliLoop2, data.TrialHandler2) and thisCaliLoop2.thisN != CaliLoop2.thisTrial.thisN:
                        continueRoutine = False
                    Pre_Shock_ISI_Calib_2.forceEnded = routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 1.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *Pre_Cali_ISI_5* updates
                        
                        # if Pre_Cali_ISI_5 is starting this frame...
                        if Pre_Cali_ISI_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            Pre_Cali_ISI_5.frameNStart = frameN  # exact frame index
                            Pre_Cali_ISI_5.tStart = t  # local t and not account for scr refresh
                            Pre_Cali_ISI_5.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(Pre_Cali_ISI_5, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_5.started')
                            # update status
                            Pre_Cali_ISI_5.status = STARTED
                            Pre_Cali_ISI_5.setAutoDraw(True)
                        
                        # if Pre_Cali_ISI_5 is active this frame...
                        if Pre_Cali_ISI_5.status == STARTED:
                            # update params
                            pass
                        
                        # if Pre_Cali_ISI_5 is stopping this frame...
                        if Pre_Cali_ISI_5.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > Pre_Cali_ISI_5.tStartRefresh + 1.0-frameTolerance:
                                # keep track of stop time/frame for later
                                Pre_Cali_ISI_5.tStop = t  # not accounting for scr refresh
                                Pre_Cali_ISI_5.tStopRefresh = tThisFlipGlobal  # on global time
                                Pre_Cali_ISI_5.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_5.stopped')
                                # update status
                                Pre_Cali_ISI_5.status = FINISHED
                                Pre_Cali_ISI_5.setAutoDraw(False)
                        # Run 'Each Frame' code from Box_Cali_Pre_5
                        grayBox.draw()
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                            )
                            # skip the frame we paused on
                            continue
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            Pre_Shock_ISI_Calib_2.forceEnded = routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in Pre_Shock_ISI_Calib_2.components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "Pre_Shock_ISI_Calib_2" ---
                    for thisComponent in Pre_Shock_ISI_Calib_2.components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store stop times for Pre_Shock_ISI_Calib_2
                    Pre_Shock_ISI_Calib_2.tStop = globalClock.getTime(format='float')
                    Pre_Shock_ISI_Calib_2.tStopRefresh = tThisFlipGlobal
                    thisExp.addData('Pre_Shock_ISI_Calib_2.stopped', Pre_Shock_ISI_Calib_2.tStop)
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if Pre_Shock_ISI_Calib_2.maxDurationReached:
                        routineTimer.addTime(-Pre_Shock_ISI_Calib_2.maxDuration)
                    elif Pre_Shock_ISI_Calib_2.forceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-1.000000)
                    
                    # --- Prepare to start Routine "Shock_ISI_Calib_2" ---
                    # create an object to store info about Routine Shock_ISI_Calib_2
                    Shock_ISI_Calib_2 = data.Routine(
                        name='Shock_ISI_Calib_2',
                        components=[Calib_Shock_Cross_4],
                    )
                    Shock_ISI_Calib_2.status = NOT_STARTED
                    continueRoutine = True
                    # update component parameters for each repeat
                    # Run 'Begin Routine' code from Stimulation_Calib_Code_4
                    ctl.demand = int(Set_Demand)
                    ctl.pulse_width = int(Set_Width)
                    ctl.enabled = 1  # Re-arm device
                    
                    trigger_thread = threading.Thread(target=safe_run)
                    trigger_thread.start()
                    trigger_thread.join(timeout=2.0)  # 2-second timeout
                    
                    if trigger_thread.is_alive():
                        print("⚠️ DS8R trigger timed out!")
                        # Optionally kill the thread or reset ctl here
                    
                    last_demand = Set_Demand
                    last_pulse_width = Set_Width
                    # store start times for Shock_ISI_Calib_2
                    Shock_ISI_Calib_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                    Shock_ISI_Calib_2.tStart = globalClock.getTime(format='float')
                    Shock_ISI_Calib_2.status = STARTED
                    thisExp.addData('Shock_ISI_Calib_2.started', Shock_ISI_Calib_2.tStart)
                    Shock_ISI_Calib_2.maxDuration = None
                    # keep track of which components have finished
                    Shock_ISI_Calib_2Components = Shock_ISI_Calib_2.components
                    for thisComponent in Shock_ISI_Calib_2.components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "Shock_ISI_Calib_2" ---
                    # if trial has changed, end Routine now
                    if isinstance(CaliLoop2, data.TrialHandler2) and thisCaliLoop2.thisN != CaliLoop2.thisTrial.thisN:
                        continueRoutine = False
                    Shock_ISI_Calib_2.forceEnded = routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 2.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *Calib_Shock_Cross_4* updates
                        
                        # if Calib_Shock_Cross_4 is starting this frame...
                        if Calib_Shock_Cross_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            Calib_Shock_Cross_4.frameNStart = frameN  # exact frame index
                            Calib_Shock_Cross_4.tStart = t  # local t and not account for scr refresh
                            Calib_Shock_Cross_4.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(Calib_Shock_Cross_4, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_4.started')
                            # update status
                            Calib_Shock_Cross_4.status = STARTED
                            Calib_Shock_Cross_4.setAutoDraw(True)
                        
                        # if Calib_Shock_Cross_4 is active this frame...
                        if Calib_Shock_Cross_4.status == STARTED:
                            # update params
                            pass
                        
                        # if Calib_Shock_Cross_4 is stopping this frame...
                        if Calib_Shock_Cross_4.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > Calib_Shock_Cross_4.tStartRefresh + 2.0-frameTolerance:
                                # keep track of stop time/frame for later
                                Calib_Shock_Cross_4.tStop = t  # not accounting for scr refresh
                                Calib_Shock_Cross_4.tStopRefresh = tThisFlipGlobal  # on global time
                                Calib_Shock_Cross_4.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_4.stopped')
                                # update status
                                Calib_Shock_Cross_4.status = FINISHED
                                Calib_Shock_Cross_4.setAutoDraw(False)
                        # Run 'Each Frame' code from Box_Cali_Shock_4
                        grayBox.draw()
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                            )
                            # skip the frame we paused on
                            continue
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            Shock_ISI_Calib_2.forceEnded = routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in Shock_ISI_Calib_2.components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "Shock_ISI_Calib_2" ---
                    for thisComponent in Shock_ISI_Calib_2.components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store stop times for Shock_ISI_Calib_2
                    Shock_ISI_Calib_2.tStop = globalClock.getTime(format='float')
                    Shock_ISI_Calib_2.tStopRefresh = tThisFlipGlobal
                    thisExp.addData('Shock_ISI_Calib_2.stopped', Shock_ISI_Calib_2.tStop)
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if Shock_ISI_Calib_2.maxDurationReached:
                        routineTimer.addTime(-Shock_ISI_Calib_2.maxDuration)
                    elif Shock_ISI_Calib_2.forceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-2.000000)
                    
                    # --- Prepare to start Routine "Shock_Calib_Looper_5" ---
                    # create an object to store info about Routine Shock_Calib_Looper_5
                    Shock_Calib_Looper_5 = data.Routine(
                        name='Shock_Calib_Looper_5',
                        components=[slider_keys_2, pain_slider_2],
                    )
                    Shock_Calib_Looper_5.status = NOT_STARTED
                    continueRoutine = True
                    # update component parameters for each repeat
                    # create starting attributes for slider_keys_2
                    slider_keys_2.keys = []
                    slider_keys_2.rt = []
                    _slider_keys_2_allKeys = []
                    pain_slider_2.reset()
                    # Run 'Begin Routine' code from Slider_Code_5
                    slider_keys.clearEvents()
                    # Run 'Begin Routine' code from Slider_Text_5
                    from psychopy import visual, core, event
                    
                    # One text stim per color segment
                    text_sliderconf_1 = visual.TextStim(
                        win,
                        text="How strong was the stimulation?",
                        color='black',
                        pos=(-0.5, 0.15),  # adjust as needed
                        height=0.0275,
                        anchorHoriz='left'
                    )
                    
                    # One text stim per color segment
                    text_sliderconf_2 = visual.TextStim(
                        win,
                        text="Press ← or → to change rating. Press spacebar to confirm.",
                        color='black',
                        pos=(-0.5, 0.05),  # adjust as needed
                        height=0.0275,
                        anchorHoriz='left'
                    )
                    
                    # store start times for Shock_Calib_Looper_5
                    Shock_Calib_Looper_5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                    Shock_Calib_Looper_5.tStart = globalClock.getTime(format='float')
                    Shock_Calib_Looper_5.status = STARTED
                    thisExp.addData('Shock_Calib_Looper_5.started', Shock_Calib_Looper_5.tStart)
                    Shock_Calib_Looper_5.maxDuration = None
                    # keep track of which components have finished
                    Shock_Calib_Looper_5Components = Shock_Calib_Looper_5.components
                    for thisComponent in Shock_Calib_Looper_5.components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "Shock_Calib_Looper_5" ---
                    # if trial has changed, end Routine now
                    if isinstance(CaliLoop2, data.TrialHandler2) and thisCaliLoop2.thisN != CaliLoop2.thisTrial.thisN:
                        continueRoutine = False
                    Shock_Calib_Looper_5.forceEnded = routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *slider_keys_2* updates
                        waitOnFlip = False
                        
                        # if slider_keys_2 is starting this frame...
                        if slider_keys_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            slider_keys_2.frameNStart = frameN  # exact frame index
                            slider_keys_2.tStart = t  # local t and not account for scr refresh
                            slider_keys_2.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(slider_keys_2, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            slider_keys_2.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(slider_keys_2.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(slider_keys_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        
                        # if slider_keys_2 is stopping this frame...
                        if slider_keys_2.status == STARTED:
                            if bool('space' in slider_keys_2.keys):
                                # keep track of stop time/frame for later
                                slider_keys_2.tStop = t  # not accounting for scr refresh
                                slider_keys_2.tStopRefresh = tThisFlipGlobal  # on global time
                                slider_keys_2.frameNStop = frameN  # exact frame index
                                # update status
                                slider_keys_2.status = FINISHED
                                slider_keys_2.status = FINISHED
                        if slider_keys_2.status == STARTED and not waitOnFlip:
                            theseKeys = slider_keys_2.getKeys(keyList=['left','right', 'space', '1', '2'], ignoreKeys=["escape"], waitRelease=False)
                            _slider_keys_2_allKeys.extend(theseKeys)
                            if len(_slider_keys_2_allKeys):
                                slider_keys_2.keys = _slider_keys_2_allKeys[-1].name  # just the last key pressed
                                slider_keys_2.rt = _slider_keys_2_allKeys[-1].rt
                                slider_keys_2.duration = _slider_keys_2_allKeys[-1].duration
                        
                        # *pain_slider_2* updates
                        
                        # if pain_slider_2 is starting this frame...
                        if pain_slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            pain_slider_2.frameNStart = frameN  # exact frame index
                            pain_slider_2.tStart = t  # local t and not account for scr refresh
                            pain_slider_2.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(pain_slider_2, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            pain_slider_2.status = STARTED
                            pain_slider_2.setAutoDraw(True)
                        
                        # if pain_slider_2 is active this frame...
                        if pain_slider_2.status == STARTED:
                            # update params
                            pass
                        
                        # if pain_slider_2 is stopping this frame...
                        if pain_slider_2.status == STARTED:
                            if bool('space' in slider_keys_2.keys):
                                # keep track of stop time/frame for later
                                pain_slider_2.tStop = t  # not accounting for scr refresh
                                pain_slider_2.tStopRefresh = tThisFlipGlobal  # on global time
                                pain_slider_2.frameNStop = frameN  # exact frame index
                                # update status
                                pain_slider_2.status = FINISHED
                                pain_slider_2.setAutoDraw(False)
                        # Run 'Each Frame' code from Box_Shock_Cali_7
                        grayBox.draw()
                        # Run 'Each Frame' code from Slider_Code_5
                        # Read keypresses from the Builder's Keyboard component
                        keys = slider_keys_2.getKeys()
                        
                        for key in keys:
                            if key.name in ['left', '1']:
                                if pain_slider_2.markerPos is not None:
                                    pain_slider_2.markerPos = max(pain_slider_2.markerPos - 1, 0)
                                else:
                                    pain_slider_2.markerPos = 0
                        
                            elif key.name in ['right', '2']:
                                if pain_slider_2.markerPos is not None:
                                    pain_slider_2.markerPos = min(pain_slider_2.markerPos + 1, 10)
                                else:
                                    pain_slider_2.markerPos = 1
                        
                            elif key.name in ['space', 'return']:
                                rating = pain_slider_2.getRating()
                                if rating is not None:
                                    print(f"✅ Rating confirmed: {rating}")
                                    thisExp.addData("pain_rating", rating)
                                    continueRoutine = False  # End the routine
                        
                        # Run 'Each Frame' code from Slider_Text_5
                        text_sliderconf_1.draw()
                        text_sliderconf_2.draw()
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                            )
                            # skip the frame we paused on
                            continue
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            Shock_Calib_Looper_5.forceEnded = routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in Shock_Calib_Looper_5.components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "Shock_Calib_Looper_5" ---
                    for thisComponent in Shock_Calib_Looper_5.components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store stop times for Shock_Calib_Looper_5
                    Shock_Calib_Looper_5.tStop = globalClock.getTime(format='float')
                    Shock_Calib_Looper_5.tStopRefresh = tThisFlipGlobal
                    thisExp.addData('Shock_Calib_Looper_5.stopped', Shock_Calib_Looper_5.tStop)
                    CaliLoop2.addData('pain_slider_2.response', pain_slider_2.getRating())
                    CaliLoop2.addData('pain_slider_2.rt', pain_slider_2.getRT())
                    # Run 'End Routine' code from Slider_Code_5
                    # Ensure the slider rating is set from markerPos when using keyboard control
                    if pain_slider_2.rating is None and pain_slider_2.markerPos is not None:
                        pain_slider_2.rating = pain_slider_2.markerPos
                    
                    thisExp.addData('pain_rating', pain_slider_2.rating)
                    
                    last_rating = pain_slider_2.rating
                    # Run 'End Routine' code from End_Loop_5
                    # Ensure rating is stored
                    if pain_slider_2.rating is None and pain_slider_2.markerPos is not None:
                        pain_slider_2.rating = pain_slider_2.markerPos
                    
                    thisExp.addData('pain_rating', pain_slider_2.rating)
                    
                    Last_rating = pain_slider.rating
                    
                    # Ensure rating is stored
                    if pain_slider_2.rating is None and pain_slider.markerPos is not None:
                        pain_slider_2.rating = pain_slider_2.markerPos
                    
                    thisExp.addData('pain_rating', pain_slider_2.rating)
                    
                    # Check stopping/looping conditions
                    if pain_slider_2.rating >= 8:
                        CaliLoop2.finished = True  # End loop as target achieved
                    # the Routine "Shock_Calib_Looper_5" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 1.0 repeats of 'CaliLoop2'
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                
                # --- Prepare to start Routine "Loop_Checkpoint_2" ---
                # create an object to store info about Routine Loop_Checkpoint_2
                Loop_Checkpoint_2 = data.Routine(
                    name='Loop_Checkpoint_2',
                    components=[],
                )
                Loop_Checkpoint_2.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from RoutSkip4_2
                if StimCalEnabled.lower() not in ['yes', 'y']:
                    Checkpoint2.finished = True  # End loop as target achieved
                    continueRoutine = False
                # store start times for Loop_Checkpoint_2
                Loop_Checkpoint_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                Loop_Checkpoint_2.tStart = globalClock.getTime(format='float')
                Loop_Checkpoint_2.status = STARTED
                thisExp.addData('Loop_Checkpoint_2.started', Loop_Checkpoint_2.tStart)
                Loop_Checkpoint_2.maxDuration = None
                # keep track of which components have finished
                Loop_Checkpoint_2Components = Loop_Checkpoint_2.components
                for thisComponent in Loop_Checkpoint_2.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Loop_Checkpoint_2" ---
                # if trial has changed, end Routine now
                if isinstance(Checkpoint2, data.TrialHandler2) and thisCheckpoint2.thisN != Checkpoint2.thisTrial.thisN:
                    continueRoutine = False
                Loop_Checkpoint_2.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        Loop_Checkpoint_2.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Loop_Checkpoint_2.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Loop_Checkpoint_2" ---
                for thisComponent in Loop_Checkpoint_2.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for Loop_Checkpoint_2
                Loop_Checkpoint_2.tStop = globalClock.getTime(format='float')
                Loop_Checkpoint_2.tStopRefresh = tThisFlipGlobal
                thisExp.addData('Loop_Checkpoint_2.stopped', Loop_Checkpoint_2.tStop)
                # Run 'End Routine' code from Checkpoint_code_2
                # Check stopping/looping conditions
                if pain_slider.rating == 8:
                    Checkpoint2.finished = True  # End loop as target achieved
                # the Routine "Loop_Checkpoint_2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed 99.0 repeats of 'Checkpoint2'
            
            
            # --- Prepare to start Routine "Pre_Shock_ISI_Cali_Check_1_2" ---
            # create an object to store info about Routine Pre_Shock_ISI_Cali_Check_1_2
            Pre_Shock_ISI_Cali_Check_1_2 = data.Routine(
                name='Pre_Shock_ISI_Cali_Check_1_2',
                components=[Pre_Cali_ISI_6],
            )
            Pre_Shock_ISI_Cali_Check_1_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for Pre_Shock_ISI_Cali_Check_1_2
            Pre_Shock_ISI_Cali_Check_1_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Pre_Shock_ISI_Cali_Check_1_2.tStart = globalClock.getTime(format='float')
            Pre_Shock_ISI_Cali_Check_1_2.status = STARTED
            thisExp.addData('Pre_Shock_ISI_Cali_Check_1_2.started', Pre_Shock_ISI_Cali_Check_1_2.tStart)
            Pre_Shock_ISI_Cali_Check_1_2.maxDuration = None
            # keep track of which components have finished
            Pre_Shock_ISI_Cali_Check_1_2Components = Pre_Shock_ISI_Cali_Check_1_2.components
            for thisComponent in Pre_Shock_ISI_Cali_Check_1_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Pre_Shock_ISI_Cali_Check_1_2" ---
            # if trial has changed, end Routine now
            if isinstance(FirstLoopPass2, data.TrialHandler2) and thisFirstLoopPass2.thisN != FirstLoopPass2.thisTrial.thisN:
                continueRoutine = False
            Pre_Shock_ISI_Cali_Check_1_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Pre_Cali_ISI_6* updates
                
                # if Pre_Cali_ISI_6 is starting this frame...
                if Pre_Cali_ISI_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Pre_Cali_ISI_6.frameNStart = frameN  # exact frame index
                    Pre_Cali_ISI_6.tStart = t  # local t and not account for scr refresh
                    Pre_Cali_ISI_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Pre_Cali_ISI_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_6.started')
                    # update status
                    Pre_Cali_ISI_6.status = STARTED
                    Pre_Cali_ISI_6.setAutoDraw(True)
                
                # if Pre_Cali_ISI_6 is active this frame...
                if Pre_Cali_ISI_6.status == STARTED:
                    # update params
                    pass
                
                # if Pre_Cali_ISI_6 is stopping this frame...
                if Pre_Cali_ISI_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Pre_Cali_ISI_6.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Pre_Cali_ISI_6.tStop = t  # not accounting for scr refresh
                        Pre_Cali_ISI_6.tStopRefresh = tThisFlipGlobal  # on global time
                        Pre_Cali_ISI_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_6.stopped')
                        # update status
                        Pre_Cali_ISI_6.status = FINISHED
                        Pre_Cali_ISI_6.setAutoDraw(False)
                # Run 'Each Frame' code from Box_Cali_Pre_6
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Pre_Shock_ISI_Cali_Check_1_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Pre_Shock_ISI_Cali_Check_1_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Pre_Shock_ISI_Cali_Check_1_2" ---
            for thisComponent in Pre_Shock_ISI_Cali_Check_1_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Pre_Shock_ISI_Cali_Check_1_2
            Pre_Shock_ISI_Cali_Check_1_2.tStop = globalClock.getTime(format='float')
            Pre_Shock_ISI_Cali_Check_1_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Pre_Shock_ISI_Cali_Check_1_2.stopped', Pre_Shock_ISI_Cali_Check_1_2.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Pre_Shock_ISI_Cali_Check_1_2.maxDurationReached:
                routineTimer.addTime(-Pre_Shock_ISI_Cali_Check_1_2.maxDuration)
            elif Pre_Shock_ISI_Cali_Check_1_2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "Shock_ISI_Post_Check_1_2" ---
            # create an object to store info about Routine Shock_ISI_Post_Check_1_2
            Shock_ISI_Post_Check_1_2 = data.Routine(
                name='Shock_ISI_Post_Check_1_2',
                components=[Calib_Shock_Cross_5],
            )
            Shock_ISI_Post_Check_1_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Stimulation_Calib_Code_5
            ctl.demand = last_demand
            ctl.pulse_width = last_pulse_width
            ctl.enabled = 1  # re-arm the device
            
            trigger_thread = threading.Thread(target=safe_run)
            trigger_thread.start()
            trigger_thread.join(timeout=2.0)  # 2-second timeout
            
            if trigger_thread.is_alive():
                print("⚠️ DS8R trigger timed out!")
                # Optionally kill the thread or reset ctl here
            # store start times for Shock_ISI_Post_Check_1_2
            Shock_ISI_Post_Check_1_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Shock_ISI_Post_Check_1_2.tStart = globalClock.getTime(format='float')
            Shock_ISI_Post_Check_1_2.status = STARTED
            thisExp.addData('Shock_ISI_Post_Check_1_2.started', Shock_ISI_Post_Check_1_2.tStart)
            Shock_ISI_Post_Check_1_2.maxDuration = None
            # keep track of which components have finished
            Shock_ISI_Post_Check_1_2Components = Shock_ISI_Post_Check_1_2.components
            for thisComponent in Shock_ISI_Post_Check_1_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Shock_ISI_Post_Check_1_2" ---
            # if trial has changed, end Routine now
            if isinstance(FirstLoopPass2, data.TrialHandler2) and thisFirstLoopPass2.thisN != FirstLoopPass2.thisTrial.thisN:
                continueRoutine = False
            Shock_ISI_Post_Check_1_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Calib_Shock_Cross_5* updates
                
                # if Calib_Shock_Cross_5 is starting this frame...
                if Calib_Shock_Cross_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Calib_Shock_Cross_5.frameNStart = frameN  # exact frame index
                    Calib_Shock_Cross_5.tStart = t  # local t and not account for scr refresh
                    Calib_Shock_Cross_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Calib_Shock_Cross_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_5.started')
                    # update status
                    Calib_Shock_Cross_5.status = STARTED
                    Calib_Shock_Cross_5.setAutoDraw(True)
                
                # if Calib_Shock_Cross_5 is active this frame...
                if Calib_Shock_Cross_5.status == STARTED:
                    # update params
                    pass
                
                # if Calib_Shock_Cross_5 is stopping this frame...
                if Calib_Shock_Cross_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Calib_Shock_Cross_5.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Calib_Shock_Cross_5.tStop = t  # not accounting for scr refresh
                        Calib_Shock_Cross_5.tStopRefresh = tThisFlipGlobal  # on global time
                        Calib_Shock_Cross_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_5.stopped')
                        # update status
                        Calib_Shock_Cross_5.status = FINISHED
                        Calib_Shock_Cross_5.setAutoDraw(False)
                # Run 'Each Frame' code from Box_Cali_Shock_5
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Shock_ISI_Post_Check_1_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Shock_ISI_Post_Check_1_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Shock_ISI_Post_Check_1_2" ---
            for thisComponent in Shock_ISI_Post_Check_1_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Shock_ISI_Post_Check_1_2
            Shock_ISI_Post_Check_1_2.tStop = globalClock.getTime(format='float')
            Shock_ISI_Post_Check_1_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Shock_ISI_Post_Check_1_2.stopped', Shock_ISI_Post_Check_1_2.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Shock_ISI_Post_Check_1_2.maxDurationReached:
                routineTimer.addTime(-Shock_ISI_Post_Check_1_2.maxDuration)
            elif Shock_ISI_Post_Check_1_2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            
            # --- Prepare to start Routine "Shock_Calib_Looper_6" ---
            # create an object to store info about Routine Shock_Calib_Looper_6
            Shock_Calib_Looper_6 = data.Routine(
                name='Shock_Calib_Looper_6',
                components=[slider_keys2_2, pain_slider2_2],
            )
            Shock_Calib_Looper_6.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for slider_keys2_2
            slider_keys2_2.keys = []
            slider_keys2_2.rt = []
            _slider_keys2_2_allKeys = []
            pain_slider2_2.reset()
            # Run 'Begin Routine' code from Slider_Code_6
            slider_keys2.clearEvents()
            
            # Run 'Begin Routine' code from Slider_Text_6
            from psychopy import visual, core, event
            
            # One text stim per color segment
            text_sliderconf_1 = visual.TextStim(
                win,
                text="How strong was the stimulation?",
                color='black',
                pos=(-0.5, 0.15),  # adjust as needed
                height=0.0275,
                anchorHoriz='left'
            )
            
            # One text stim per color segment
            text_sliderconf_2 = visual.TextStim(
                win,
                text="Press ← or → to change rating. Press spacebar to confirm.",
                color='black',
                pos=(-0.5, 0.05),  # adjust as needed
                height=0.0275,
                anchorHoriz='left'
            )
            
            # Run 'Begin Routine' code from End_Loop_6
            
            
            # store start times for Shock_Calib_Looper_6
            Shock_Calib_Looper_6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Shock_Calib_Looper_6.tStart = globalClock.getTime(format='float')
            Shock_Calib_Looper_6.status = STARTED
            thisExp.addData('Shock_Calib_Looper_6.started', Shock_Calib_Looper_6.tStart)
            Shock_Calib_Looper_6.maxDuration = None
            # keep track of which components have finished
            Shock_Calib_Looper_6Components = Shock_Calib_Looper_6.components
            for thisComponent in Shock_Calib_Looper_6.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Shock_Calib_Looper_6" ---
            # if trial has changed, end Routine now
            if isinstance(FirstLoopPass2, data.TrialHandler2) and thisFirstLoopPass2.thisN != FirstLoopPass2.thisTrial.thisN:
                continueRoutine = False
            Shock_Calib_Looper_6.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *slider_keys2_2* updates
                waitOnFlip = False
                
                # if slider_keys2_2 is starting this frame...
                if slider_keys2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider_keys2_2.frameNStart = frameN  # exact frame index
                    slider_keys2_2.tStart = t  # local t and not account for scr refresh
                    slider_keys2_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider_keys2_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    slider_keys2_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(slider_keys2_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(slider_keys2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if slider_keys2_2 is stopping this frame...
                if slider_keys2_2.status == STARTED:
                    if bool('space' in slider_keys2_2.keys):
                        # keep track of stop time/frame for later
                        slider_keys2_2.tStop = t  # not accounting for scr refresh
                        slider_keys2_2.tStopRefresh = tThisFlipGlobal  # on global time
                        slider_keys2_2.frameNStop = frameN  # exact frame index
                        # update status
                        slider_keys2_2.status = FINISHED
                        slider_keys2_2.status = FINISHED
                if slider_keys2_2.status == STARTED and not waitOnFlip:
                    theseKeys = slider_keys2_2.getKeys(keyList=['left','right', 'space', '1', '2'], ignoreKeys=["escape"], waitRelease=False)
                    _slider_keys2_2_allKeys.extend(theseKeys)
                    if len(_slider_keys2_2_allKeys):
                        slider_keys2_2.keys = _slider_keys2_2_allKeys[-1].name  # just the last key pressed
                        slider_keys2_2.rt = _slider_keys2_2_allKeys[-1].rt
                        slider_keys2_2.duration = _slider_keys2_2_allKeys[-1].duration
                
                # *pain_slider2_2* updates
                
                # if pain_slider2_2 is starting this frame...
                if pain_slider2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pain_slider2_2.frameNStart = frameN  # exact frame index
                    pain_slider2_2.tStart = t  # local t and not account for scr refresh
                    pain_slider2_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pain_slider2_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    pain_slider2_2.status = STARTED
                    pain_slider2_2.setAutoDraw(True)
                
                # if pain_slider2_2 is active this frame...
                if pain_slider2_2.status == STARTED:
                    # update params
                    pass
                
                # if pain_slider2_2 is stopping this frame...
                if pain_slider2_2.status == STARTED:
                    if bool('space' in slider_keys2_2.keys):
                        # keep track of stop time/frame for later
                        pain_slider2_2.tStop = t  # not accounting for scr refresh
                        pain_slider2_2.tStopRefresh = tThisFlipGlobal  # on global time
                        pain_slider2_2.frameNStop = frameN  # exact frame index
                        # update status
                        pain_slider2_2.status = FINISHED
                        pain_slider2_2.setAutoDraw(False)
                # Run 'Each Frame' code from Box_Shock_Cali_8
                grayBox.draw()
                # Run 'Each Frame' code from Slider_Code_6
                # Read keypresses from the Builder's Keyboard component
                keys = slider_keys2_2.getKeys()
                
                for key in keys:
                    if key.name in ['left', '1']:
                        if pain_slider2_2.markerPos is not None:
                            pain_slider2_2.markerPos = max(pain_slider2_2.markerPos - 1, 0)
                        else:
                            slider_keys2_2.markerPos = 0
                
                    elif key.name in ['right', '2']:
                        if pain_slider2_2.markerPos is not None:
                            pain_slider2_2.markerPos = min(pain_slider2_2.markerPos + 1, 10)
                        else:
                            slider_keys2_2.markerPos = 1
                
                    elif key.name in ['space', 'return']:
                        rating = pain_slider2_2.getRating()
                        if rating is not None:
                            print(f"✅ Rating confirmed: {rating}")
                            thisExp.addData("pain_rating2", rating)
                            continueRoutine = False  # End the routine
                
                # Run 'Each Frame' code from Slider_Text_6
                text_sliderconf_1.draw()
                text_sliderconf_2.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Shock_Calib_Looper_6.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Shock_Calib_Looper_6.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Shock_Calib_Looper_6" ---
            for thisComponent in Shock_Calib_Looper_6.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Shock_Calib_Looper_6
            Shock_Calib_Looper_6.tStop = globalClock.getTime(format='float')
            Shock_Calib_Looper_6.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Shock_Calib_Looper_6.stopped', Shock_Calib_Looper_6.tStop)
            FirstLoopPass2.addData('pain_slider2_2.response', pain_slider2_2.getRating())
            FirstLoopPass2.addData('pain_slider2_2.rt', pain_slider2_2.getRT())
            # Run 'End Routine' code from End_Loop_6
            # Ensure rating is stored
            if pain_slider2_2.rating is None and pain_slider2_2.markerPos is not None:
                pain_slider2_2.rating = pain_slider2_2.markerPos
            
            thisExp.addData('pain_rating', pain_slider2_2.rating)
            
            if pain_slider2_2.rating == 8:
                FirstLoopPass2.finished = True
            # the Routine "Shock_Calib_Looper_6" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 99.0 repeats of 'FirstLoopPass2'
        
        
        # --- Prepare to start Routine "Pre_Shock_ISI_Check_2_2" ---
        # create an object to store info about Routine Pre_Shock_ISI_Check_2_2
        Pre_Shock_ISI_Check_2_2 = data.Routine(
            name='Pre_Shock_ISI_Check_2_2',
            components=[Pre_Cali_ISI_7],
        )
        Pre_Shock_ISI_Check_2_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Pre_Shock_ISI_Check_2_2
        Pre_Shock_ISI_Check_2_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Pre_Shock_ISI_Check_2_2.tStart = globalClock.getTime(format='float')
        Pre_Shock_ISI_Check_2_2.status = STARTED
        thisExp.addData('Pre_Shock_ISI_Check_2_2.started', Pre_Shock_ISI_Check_2_2.tStart)
        Pre_Shock_ISI_Check_2_2.maxDuration = None
        # keep track of which components have finished
        Pre_Shock_ISI_Check_2_2Components = Pre_Shock_ISI_Check_2_2.components
        for thisComponent in Pre_Shock_ISI_Check_2_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Pre_Shock_ISI_Check_2_2" ---
        # if trial has changed, end Routine now
        if isinstance(SecondLoopPass2, data.TrialHandler2) and thisSecondLoopPass2.thisN != SecondLoopPass2.thisTrial.thisN:
            continueRoutine = False
        Pre_Shock_ISI_Check_2_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Pre_Cali_ISI_7* updates
            
            # if Pre_Cali_ISI_7 is starting this frame...
            if Pre_Cali_ISI_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pre_Cali_ISI_7.frameNStart = frameN  # exact frame index
                Pre_Cali_ISI_7.tStart = t  # local t and not account for scr refresh
                Pre_Cali_ISI_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pre_Cali_ISI_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_7.started')
                # update status
                Pre_Cali_ISI_7.status = STARTED
                Pre_Cali_ISI_7.setAutoDraw(True)
            
            # if Pre_Cali_ISI_7 is active this frame...
            if Pre_Cali_ISI_7.status == STARTED:
                # update params
                pass
            
            # if Pre_Cali_ISI_7 is stopping this frame...
            if Pre_Cali_ISI_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pre_Cali_ISI_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Pre_Cali_ISI_7.tStop = t  # not accounting for scr refresh
                    Pre_Cali_ISI_7.tStopRefresh = tThisFlipGlobal  # on global time
                    Pre_Cali_ISI_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Pre_Cali_ISI_7.stopped')
                    # update status
                    Pre_Cali_ISI_7.status = FINISHED
                    Pre_Cali_ISI_7.setAutoDraw(False)
            # Run 'Each Frame' code from Box_Cali_Pre_7
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Pre_Shock_ISI_Check_2_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pre_Shock_ISI_Check_2_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pre_Shock_ISI_Check_2_2" ---
        for thisComponent in Pre_Shock_ISI_Check_2_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Pre_Shock_ISI_Check_2_2
        Pre_Shock_ISI_Check_2_2.tStop = globalClock.getTime(format='float')
        Pre_Shock_ISI_Check_2_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Pre_Shock_ISI_Check_2_2.stopped', Pre_Shock_ISI_Check_2_2.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Pre_Shock_ISI_Check_2_2.maxDurationReached:
            routineTimer.addTime(-Pre_Shock_ISI_Check_2_2.maxDuration)
        elif Pre_Shock_ISI_Check_2_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Shock_ISI_Post_Check_2_2" ---
        # create an object to store info about Routine Shock_ISI_Post_Check_2_2
        Shock_ISI_Post_Check_2_2 = data.Routine(
            name='Shock_ISI_Post_Check_2_2',
            components=[Calib_Shock_Cross_6],
        )
        Shock_ISI_Post_Check_2_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Stimulation_Calib_Code_6
        ctl.demand = last_demand
        ctl.pulse_width = last_pulse_width
        ctl.enabled = 1  # Re-arm device
        
        trigger_thread = threading.Thread(target=safe_run)
        trigger_thread.start()
        trigger_thread.join(timeout=2.0)  # 2-second timeout
        
        if trigger_thread.is_alive():
            print("⚠️ DS8R trigger timed out!")
            # Optionally kill the thread or reset ctl here
        # store start times for Shock_ISI_Post_Check_2_2
        Shock_ISI_Post_Check_2_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Shock_ISI_Post_Check_2_2.tStart = globalClock.getTime(format='float')
        Shock_ISI_Post_Check_2_2.status = STARTED
        thisExp.addData('Shock_ISI_Post_Check_2_2.started', Shock_ISI_Post_Check_2_2.tStart)
        Shock_ISI_Post_Check_2_2.maxDuration = None
        # keep track of which components have finished
        Shock_ISI_Post_Check_2_2Components = Shock_ISI_Post_Check_2_2.components
        for thisComponent in Shock_ISI_Post_Check_2_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Shock_ISI_Post_Check_2_2" ---
        # if trial has changed, end Routine now
        if isinstance(SecondLoopPass2, data.TrialHandler2) and thisSecondLoopPass2.thisN != SecondLoopPass2.thisTrial.thisN:
            continueRoutine = False
        Shock_ISI_Post_Check_2_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Calib_Shock_Cross_6* updates
            
            # if Calib_Shock_Cross_6 is starting this frame...
            if Calib_Shock_Cross_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Calib_Shock_Cross_6.frameNStart = frameN  # exact frame index
                Calib_Shock_Cross_6.tStart = t  # local t and not account for scr refresh
                Calib_Shock_Cross_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Calib_Shock_Cross_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_6.started')
                # update status
                Calib_Shock_Cross_6.status = STARTED
                Calib_Shock_Cross_6.setAutoDraw(True)
            
            # if Calib_Shock_Cross_6 is active this frame...
            if Calib_Shock_Cross_6.status == STARTED:
                # update params
                pass
            
            # if Calib_Shock_Cross_6 is stopping this frame...
            if Calib_Shock_Cross_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Calib_Shock_Cross_6.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Calib_Shock_Cross_6.tStop = t  # not accounting for scr refresh
                    Calib_Shock_Cross_6.tStopRefresh = tThisFlipGlobal  # on global time
                    Calib_Shock_Cross_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Calib_Shock_Cross_6.stopped')
                    # update status
                    Calib_Shock_Cross_6.status = FINISHED
                    Calib_Shock_Cross_6.setAutoDraw(False)
            # Run 'Each Frame' code from Box_Cali_Shock_6
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Shock_ISI_Post_Check_2_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Shock_ISI_Post_Check_2_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Shock_ISI_Post_Check_2_2" ---
        for thisComponent in Shock_ISI_Post_Check_2_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Shock_ISI_Post_Check_2_2
        Shock_ISI_Post_Check_2_2.tStop = globalClock.getTime(format='float')
        Shock_ISI_Post_Check_2_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Shock_ISI_Post_Check_2_2.stopped', Shock_ISI_Post_Check_2_2.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Shock_ISI_Post_Check_2_2.maxDurationReached:
            routineTimer.addTime(-Shock_ISI_Post_Check_2_2.maxDuration)
        elif Shock_ISI_Post_Check_2_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Shock_Calib_Looper_7" ---
        # create an object to store info about Routine Shock_Calib_Looper_7
        Shock_Calib_Looper_7 = data.Routine(
            name='Shock_Calib_Looper_7',
            components=[slider_keys3_2, pain_slider3_2],
        )
        Shock_Calib_Looper_7.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for slider_keys3_2
        slider_keys3_2.keys = []
        slider_keys3_2.rt = []
        _slider_keys3_2_allKeys = []
        pain_slider3_2.reset()
        # Run 'Begin Routine' code from Slider_Code_7
        slider_keys2.clearEvents()
        
        # Run 'Begin Routine' code from Slider_Text_7
        from psychopy import visual, core, event
        
        # One text stim per color segment
        text_sliderconf_1 = visual.TextStim(
            win,
            text="How strong was the stimulation?",
            color='black',
            pos=(-0.5, 0.15),  # adjust as needed
            height=0.0275,
            anchorHoriz='left'
        )
        
        # One text stim per color segment
        text_sliderconf_2 = visual.TextStim(
            win,
            text="Press ← or → to change rating. Press spacebar to confirm.",
            color='black',
            pos=(-0.5, 0.05),  # adjust as needed
            height=0.0275,
            anchorHoriz='left'
        )
        
        # Run 'Begin Routine' code from End_Loop_7
        
        
        # store start times for Shock_Calib_Looper_7
        Shock_Calib_Looper_7.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Shock_Calib_Looper_7.tStart = globalClock.getTime(format='float')
        Shock_Calib_Looper_7.status = STARTED
        thisExp.addData('Shock_Calib_Looper_7.started', Shock_Calib_Looper_7.tStart)
        Shock_Calib_Looper_7.maxDuration = None
        # keep track of which components have finished
        Shock_Calib_Looper_7Components = Shock_Calib_Looper_7.components
        for thisComponent in Shock_Calib_Looper_7.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Shock_Calib_Looper_7" ---
        # if trial has changed, end Routine now
        if isinstance(SecondLoopPass2, data.TrialHandler2) and thisSecondLoopPass2.thisN != SecondLoopPass2.thisTrial.thisN:
            continueRoutine = False
        Shock_Calib_Looper_7.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *slider_keys3_2* updates
            waitOnFlip = False
            
            # if slider_keys3_2 is starting this frame...
            if slider_keys3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_keys3_2.frameNStart = frameN  # exact frame index
                slider_keys3_2.tStart = t  # local t and not account for scr refresh
                slider_keys3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_keys3_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_keys3_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(slider_keys3_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(slider_keys3_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if slider_keys3_2 is stopping this frame...
            if slider_keys3_2.status == STARTED:
                if bool('space' in slider_keys3_2.keys):
                    # keep track of stop time/frame for later
                    slider_keys3_2.tStop = t  # not accounting for scr refresh
                    slider_keys3_2.tStopRefresh = tThisFlipGlobal  # on global time
                    slider_keys3_2.frameNStop = frameN  # exact frame index
                    # update status
                    slider_keys3_2.status = FINISHED
                    slider_keys3_2.status = FINISHED
            if slider_keys3_2.status == STARTED and not waitOnFlip:
                theseKeys = slider_keys3_2.getKeys(keyList=['left','right', 'space', '1', '2'], ignoreKeys=["escape"], waitRelease=False)
                _slider_keys3_2_allKeys.extend(theseKeys)
                if len(_slider_keys3_2_allKeys):
                    slider_keys3_2.keys = _slider_keys3_2_allKeys[-1].name  # just the last key pressed
                    slider_keys3_2.rt = _slider_keys3_2_allKeys[-1].rt
                    slider_keys3_2.duration = _slider_keys3_2_allKeys[-1].duration
            
            # *pain_slider3_2* updates
            
            # if pain_slider3_2 is starting this frame...
            if pain_slider3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pain_slider3_2.frameNStart = frameN  # exact frame index
                pain_slider3_2.tStart = t  # local t and not account for scr refresh
                pain_slider3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pain_slider3_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                pain_slider3_2.status = STARTED
                pain_slider3_2.setAutoDraw(True)
            
            # if pain_slider3_2 is active this frame...
            if pain_slider3_2.status == STARTED:
                # update params
                pass
            
            # if pain_slider3_2 is stopping this frame...
            if pain_slider3_2.status == STARTED:
                if bool('space' in slider_keys3_2.keys):
                    # keep track of stop time/frame for later
                    pain_slider3_2.tStop = t  # not accounting for scr refresh
                    pain_slider3_2.tStopRefresh = tThisFlipGlobal  # on global time
                    pain_slider3_2.frameNStop = frameN  # exact frame index
                    # update status
                    pain_slider3_2.status = FINISHED
                    pain_slider3_2.setAutoDraw(False)
            # Run 'Each Frame' code from Box_Shock_Cali_9
            grayBox.draw()
            # Run 'Each Frame' code from Slider_Code_7
            # Read keypresses from the Builder's Keyboard component
            keys = slider_keys3_2.getKeys()
            
            for key in keys:
                if key.name in ['left', '1']:
                    if pain_slider3_2.markerPos is not None:
                        pain_slider3_2.markerPos = max(pain_slider3_2.markerPos - 1, 0)
                    else:
                        pain_slider3_2.markerPos = 0
            
                elif key.name in ['right', '2']:
                    if pain_slider3_2.markerPos is not None:
                        pain_slider3_2.markerPos = min(pain_slider3_2.markerPos + 1, 10)
                    else:
                        pain_slider3_2.markerPos = 1
            
                elif key.name in ['space', 'return']:
                    rating = pain_slider3_2.getRating()
                    if rating is not None:
                        print(f"✅ Rating confirmed: {rating}")
                        thisExp.addData("pain_rating3", rating)
                        continueRoutine = False  # End the routine
            
            # Run 'Each Frame' code from Slider_Text_7
            text_sliderconf_1.draw()
            text_sliderconf_2.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Shock_Calib_Looper_7.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Shock_Calib_Looper_7.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Shock_Calib_Looper_7" ---
        for thisComponent in Shock_Calib_Looper_7.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Shock_Calib_Looper_7
        Shock_Calib_Looper_7.tStop = globalClock.getTime(format='float')
        Shock_Calib_Looper_7.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Shock_Calib_Looper_7.stopped', Shock_Calib_Looper_7.tStop)
        SecondLoopPass2.addData('pain_slider3_2.response', pain_slider3_2.getRating())
        SecondLoopPass2.addData('pain_slider3_2.rt', pain_slider3_2.getRT())
        # Run 'End Routine' code from End_Loop_7
        # Ensure rating is stored
        if pain_slider3_2.rating is None and pain_slider3_2.markerPos is not None:
            pain_slider3_2.rating = pain_slider3_2.markerPos
        
        thisExp.addData('pain_rating3', pain_slider3_2.rating)
        
        if pain_slider3_2.rating == 8:
            SecondLoopPass2.finished = True
            
        thisExp.addData('second_cali_final_demand', last_demand)
        # the Routine "Shock_Calib_Looper_7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 99.0 repeats of 'SecondLoopPass2'
    
    
    # --- Prepare to start Routine "Instructions_Final_2" ---
    # create an object to store info about Routine Instructions_Final_2
    Instructions_Final_2 = data.Routine(
        name='Instructions_Final_2',
        components=[Instr_Key5_2],
    )
    Instructions_Final_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Instr_Key5_2
    Instr_Key5_2.keys = []
    Instr_Key5_2.rt = []
    _Instr_Key5_2_allKeys = []
    # store start times for Instructions_Final_2
    Instructions_Final_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_Final_2.tStart = globalClock.getTime(format='float')
    Instructions_Final_2.status = STARTED
    thisExp.addData('Instructions_Final_2.started', Instructions_Final_2.tStart)
    Instructions_Final_2.maxDuration = None
    # keep track of which components have finished
    Instructions_Final_2Components = Instructions_Final_2.components
    for thisComponent in Instructions_Final_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_Final_2" ---
    Instructions_Final_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box18_4
        grayBox.draw()
        # Run 'Each Frame' code from Text_code_5
        text_ISI_instr50.draw()
        text_ISI_instr51.draw()
        text_ISI_instr9.draw()
        
        # *Instr_Key5_2* updates
        waitOnFlip = False
        
        # if Instr_Key5_2 is starting this frame...
        if Instr_Key5_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Instr_Key5_2.frameNStart = frameN  # exact frame index
            Instr_Key5_2.tStart = t  # local t and not account for scr refresh
            Instr_Key5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Key5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instr_Key5_2.started')
            # update status
            Instr_Key5_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instr_Key5_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instr_Key5_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instr_Key5_2.status == STARTED and not waitOnFlip:
            theseKeys = Instr_Key5_2.getKeys(keyList=['left','right','1','2'], ignoreKeys=["escape"], waitRelease=False)
            _Instr_Key5_2_allKeys.extend(theseKeys)
            if len(_Instr_Key5_2_allKeys):
                Instr_Key5_2.keys = _Instr_Key5_2_allKeys[-1].name  # just the last key pressed
                Instr_Key5_2.rt = _Instr_Key5_2_allKeys[-1].rt
                Instr_Key5_2.duration = _Instr_Key5_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_Final_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_Final_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_Final_2" ---
    for thisComponent in Instructions_Final_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_Final_2
    Instructions_Final_2.tStop = globalClock.getTime(format='float')
    Instructions_Final_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_Final_2.stopped', Instructions_Final_2.tStop)
    # Run 'End Routine' code from Timer
    time_trialEnd = globalClock.getTime()
    
    thisExp.addData('Experiment_Begin_Time', time_trialEnd)
    thisExp.nextEntry()
    # the Routine "Instructions_Final_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Pre_Block_ISI" ---
    # create an object to store info about Routine Pre_Block_ISI
    Pre_Block_ISI = data.Routine(
        name='Pre_Block_ISI',
        components=[ISI_Pre],
    )
    Pre_Block_ISI.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Pre_Timer
    time_trialBegin = globalClock.getTime()
    
    # store start times for Pre_Block_ISI
    Pre_Block_ISI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Pre_Block_ISI.tStart = globalClock.getTime(format='float')
    Pre_Block_ISI.status = STARTED
    thisExp.addData('Pre_Block_ISI.started', Pre_Block_ISI.tStart)
    Pre_Block_ISI.maxDuration = None
    # keep track of which components have finished
    Pre_Block_ISIComponents = Pre_Block_ISI.components
    for thisComponent in Pre_Block_ISI.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Pre_Block_ISI" ---
    Pre_Block_ISI.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI_Pre* updates
        
        # if ISI_Pre is starting this frame...
        if ISI_Pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_Pre.frameNStart = frameN  # exact frame index
            ISI_Pre.tStart = t  # local t and not account for scr refresh
            ISI_Pre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_Pre, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI_Pre.started')
            # update status
            ISI_Pre.status = STARTED
            ISI_Pre.setAutoDraw(True)
        
        # if ISI_Pre is active this frame...
        if ISI_Pre.status == STARTED:
            # update params
            pass
        
        # if ISI_Pre is stopping this frame...
        if ISI_Pre.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI_Pre.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                ISI_Pre.tStop = t  # not accounting for scr refresh
                ISI_Pre.tStopRefresh = tThisFlipGlobal  # on global time
                ISI_Pre.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI_Pre.stopped')
                # update status
                ISI_Pre.status = FINISHED
                ISI_Pre.setAutoDraw(False)
        # Run 'Each Frame' code from Pre_Box
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Pre_Block_ISI.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pre_Block_ISI.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Pre_Block_ISI" ---
    for thisComponent in Pre_Block_ISI.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Pre_Block_ISI
    Pre_Block_ISI.tStop = globalClock.getTime(format='float')
    Pre_Block_ISI.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Pre_Block_ISI.stopped', Pre_Block_ISI.tStop)
    # Run 'End Routine' code from Pre_Timer
    time_trialEnd = globalClock.getTime()
    
    thisExp.addData('Pre_ISI_Begin', time_trialBegin)
    thisExp.addData('Pre_ISI_End', time_trialEnd)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Pre_Block_ISI.maxDurationReached:
        routineTimer.addTime(-Pre_Block_ISI.maxDuration)
    elif Pre_Block_ISI.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    InnerLoop2 = data.TrialHandler2(
        name='InnerLoop2',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(VersionSelection_H2), 
        seed=None, 
    )
    thisExp.addLoop(InnerLoop2)  # add the loop to the experiment
    thisInnerLoop2 = InnerLoop2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop2.rgb)
    if thisInnerLoop2 != None:
        for paramName in thisInnerLoop2:
            globals()[paramName] = thisInnerLoop2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisInnerLoop2 in InnerLoop2:
        currentLoop = InnerLoop2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop2.rgb)
        if thisInnerLoop2 != None:
            for paramName in thisInnerLoop2:
                globals()[paramName] = thisInnerLoop2[paramName]
        
        # --- Prepare to start Routine "Blank" ---
        # create an object to store info about Routine Blank
        Blank = data.Routine(
            name='Blank',
            components=[Blank_Text],
        )
        Blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Timer_PostISI
        time_trialBegin = globalClock.getTime()
        # store start times for Blank
        Blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Blank.tStart = globalClock.getTime(format='float')
        Blank.status = STARTED
        thisExp.addData('Blank.started', Blank.tStart)
        Blank.maxDuration = None
        # keep track of which components have finished
        BlankComponents = Blank.components
        for thisComponent in Blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Blank" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop2, data.TrialHandler2) and thisInnerLoop2.thisN != InnerLoop2.thisTrial.thisN:
            continueRoutine = False
        Blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.05:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Blank_Text* updates
            
            # if Blank_Text is starting this frame...
            if Blank_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Blank_Text.frameNStart = frameN  # exact frame index
                Blank_Text.tStart = t  # local t and not account for scr refresh
                Blank_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Blank_Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Blank_Text.started')
                # update status
                Blank_Text.status = STARTED
                Blank_Text.setAutoDraw(True)
            
            # if Blank_Text is active this frame...
            if Blank_Text.status == STARTED:
                # update params
                pass
            
            # if Blank_Text is stopping this frame...
            if Blank_Text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Blank_Text.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    Blank_Text.tStop = t  # not accounting for scr refresh
                    Blank_Text.tStopRefresh = tThisFlipGlobal  # on global time
                    Blank_Text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Blank_Text.stopped')
                    # update status
                    Blank_Text.status = FINISHED
                    Blank_Text.setAutoDraw(False)
            # Run 'Each Frame' code from Box21
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Blank" ---
        for thisComponent in Blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Blank
        Blank.tStop = globalClock.getTime(format='float')
        Blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Blank.stopped', Blank.tStop)
        # Run 'End Routine' code from Timer_PostISI
        thisExp.addData('PostISI_Start_Time', time_trialBegin)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Blank.maxDurationReached:
            routineTimer.addTime(-Blank.maxDuration)
        elif Blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.050000)
        
        # --- Prepare to start Routine "Main_Routine_Stimulus_Selection_H2" ---
        # create an object to store info about Routine Main_Routine_Stimulus_Selection_H2
        Main_Routine_Stimulus_Selection_H2 = data.Routine(
            name='Main_Routine_Stimulus_Selection_H2',
            components=[Cued_Image_2, Estimation_Select_2],
        )
        Main_Routine_Stimulus_Selection_H2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Cued_Image_2.setImage(Fractal_img)
        # create starting attributes for Estimation_Select_2
        Estimation_Select_2.keys = []
        Estimation_Select_2.rt = []
        _Estimation_Select_2_allKeys = []
        # Run 'Begin Routine' code from Timer_8
        time_trialBegin = globalClock.getTime()
        
        # store start times for Main_Routine_Stimulus_Selection_H2
        Main_Routine_Stimulus_Selection_H2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Routine_Stimulus_Selection_H2.tStart = globalClock.getTime(format='float')
        Main_Routine_Stimulus_Selection_H2.status = STARTED
        thisExp.addData('Main_Routine_Stimulus_Selection_H2.started', Main_Routine_Stimulus_Selection_H2.tStart)
        Main_Routine_Stimulus_Selection_H2.maxDuration = None
        # keep track of which components have finished
        Main_Routine_Stimulus_Selection_H2Components = Main_Routine_Stimulus_Selection_H2.components
        for thisComponent in Main_Routine_Stimulus_Selection_H2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Routine_Stimulus_Selection_H2" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop2, data.TrialHandler2) and thisInnerLoop2.thisN != InnerLoop2.thisTrial.thisN:
            continueRoutine = False
        Main_Routine_Stimulus_Selection_H2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Cued_Image_2* updates
            
            # if Cued_Image_2 is starting this frame...
            if Cued_Image_2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                Cued_Image_2.frameNStart = frameN  # exact frame index
                Cued_Image_2.tStart = t  # local t and not account for scr refresh
                Cued_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cued_Image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cued_Image_2.started')
                # update status
                Cued_Image_2.status = STARTED
                Cued_Image_2.setAutoDraw(True)
            
            # if Cued_Image_2 is active this frame...
            if Cued_Image_2.status == STARTED:
                # update params
                pass
            
            # *Estimation_Select_2* updates
            waitOnFlip = False
            
            # if Estimation_Select_2 is starting this frame...
            if Estimation_Select_2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                Estimation_Select_2.frameNStart = frameN  # exact frame index
                Estimation_Select_2.tStart = t  # local t and not account for scr refresh
                Estimation_Select_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Estimation_Select_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Estimation_Select_2.started')
                # update status
                Estimation_Select_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Estimation_Select_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Estimation_Select_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Estimation_Select_2.status == STARTED and not waitOnFlip:
                theseKeys = Estimation_Select_2.getKeys(keyList=['left','right','1','2'], ignoreKeys=["escape"], waitRelease=False)
                _Estimation_Select_2_allKeys.extend(theseKeys)
                if len(_Estimation_Select_2_allKeys):
                    Estimation_Select_2.keys = _Estimation_Select_2_allKeys[-1].name  # just the last key pressed
                    Estimation_Select_2.rt = _Estimation_Select_2_allKeys[-1].rt
                    Estimation_Select_2.duration = _Estimation_Select_2_allKeys[-1].duration
                    # was this correct?
                    if (Estimation_Select_2.keys == str(High_Prob_Choice_Corr)) or (Estimation_Select_2.keys == High_Prob_Choice_Corr):
                        Estimation_Select_2.corr = 1
                    else:
                        Estimation_Select_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from Box7
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Routine_Stimulus_Selection_H2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Routine_Stimulus_Selection_H2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Routine_Stimulus_Selection_H2" ---
        for thisComponent in Main_Routine_Stimulus_Selection_H2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Routine_Stimulus_Selection_H2
        Main_Routine_Stimulus_Selection_H2.tStop = globalClock.getTime(format='float')
        Main_Routine_Stimulus_Selection_H2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Routine_Stimulus_Selection_H2.stopped', Main_Routine_Stimulus_Selection_H2.tStop)
        # check responses
        if Estimation_Select_2.keys in ['', [], None]:  # No response was made
            Estimation_Select_2.keys = None
            # was no response the correct answer?!
            if str(High_Prob_Choice_Corr).lower() == 'none':
               Estimation_Select_2.corr = 1;  # correct non-response
            else:
               Estimation_Select_2.corr = 0;  # failed to respond (incorrectly)
        # store data for InnerLoop2 (TrialHandler)
        InnerLoop2.addData('Estimation_Select_2.keys',Estimation_Select_2.keys)
        InnerLoop2.addData('Estimation_Select_2.corr', Estimation_Select_2.corr)
        if Estimation_Select_2.keys != None:  # we had a response
            InnerLoop2.addData('Estimation_Select_2.rt', Estimation_Select_2.rt)
            InnerLoop2.addData('Estimation_Select_2.duration', Estimation_Select_2.duration)
        # Run 'End Routine' code from Store_Selection_2
        if Estimation_Select_2.keys:
            lastKey = Estimation_Select_2.keys
            if lastKey in ['left', '1']:
                selectedColor = [0.0000, 0.3, 0.05]
            elif lastKey in ['right', '2']:
                selectedColor = [0.52, 0.4, -0.02]
            else:
                selectedColor = 'grey'
        else:
            lastKey = None
            selectedColor = 'grey'
        # Run 'End Routine' code from Timer_8
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('Choice_Begin_Time', time_trialBegin)
        thisExp.addData('Choice_End_Time', time_trialEnd)
        # the Routine "Main_Routine_Stimulus_Selection_H2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Main_Routine_Stimulus_Post_Selection_H2" ---
        # create an object to store info about Routine Main_Routine_Stimulus_Post_Selection_H2
        Main_Routine_Stimulus_Post_Selection_H2 = data.Routine(
            name='Main_Routine_Stimulus_Post_Selection_H2',
            components=[Selection_Result_2, Cued_image_post_2],
        )
        Main_Routine_Stimulus_Post_Selection_H2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Selection_Result_2.setFillColor(selectedColor)
        Selection_Result_2.setLineColor('grey')
        Cued_image_post_2.setImage(Fractal_img)
        # Run 'Begin Routine' code from Timer_9
        time_trialBegin = globalClock.getTime()
        # store start times for Main_Routine_Stimulus_Post_Selection_H2
        Main_Routine_Stimulus_Post_Selection_H2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Routine_Stimulus_Post_Selection_H2.tStart = globalClock.getTime(format='float')
        Main_Routine_Stimulus_Post_Selection_H2.status = STARTED
        thisExp.addData('Main_Routine_Stimulus_Post_Selection_H2.started', Main_Routine_Stimulus_Post_Selection_H2.tStart)
        Main_Routine_Stimulus_Post_Selection_H2.maxDuration = None
        # keep track of which components have finished
        Main_Routine_Stimulus_Post_Selection_H2Components = Main_Routine_Stimulus_Post_Selection_H2.components
        for thisComponent in Main_Routine_Stimulus_Post_Selection_H2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Routine_Stimulus_Post_Selection_H2" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop2, data.TrialHandler2) and thisInnerLoop2.thisN != InnerLoop2.thisTrial.thisN:
            continueRoutine = False
        Main_Routine_Stimulus_Post_Selection_H2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Selection_Result_2* updates
            
            # if Selection_Result_2 is starting this frame...
            if Selection_Result_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Selection_Result_2.frameNStart = frameN  # exact frame index
                Selection_Result_2.tStart = t  # local t and not account for scr refresh
                Selection_Result_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Selection_Result_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Selection_Result_2.started')
                # update status
                Selection_Result_2.status = STARTED
                Selection_Result_2.setAutoDraw(True)
            
            # if Selection_Result_2 is active this frame...
            if Selection_Result_2.status == STARTED:
                # update params
                pass
            
            # if Selection_Result_2 is stopping this frame...
            if Selection_Result_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Selection_Result_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Selection_Result_2.tStop = t  # not accounting for scr refresh
                    Selection_Result_2.tStopRefresh = tThisFlipGlobal  # on global time
                    Selection_Result_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Selection_Result_2.stopped')
                    # update status
                    Selection_Result_2.status = FINISHED
                    Selection_Result_2.setAutoDraw(False)
            
            # *Cued_image_post_2* updates
            
            # if Cued_image_post_2 is starting this frame...
            if Cued_image_post_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Cued_image_post_2.frameNStart = frameN  # exact frame index
                Cued_image_post_2.tStart = t  # local t and not account for scr refresh
                Cued_image_post_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cued_image_post_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cued_image_post_2.started')
                # update status
                Cued_image_post_2.status = STARTED
                Cued_image_post_2.setAutoDraw(True)
            
            # if Cued_image_post_2 is active this frame...
            if Cued_image_post_2.status == STARTED:
                # update params
                pass
            
            # if Cued_image_post_2 is stopping this frame...
            if Cued_image_post_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Cued_image_post_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Cued_image_post_2.tStop = t  # not accounting for scr refresh
                    Cued_image_post_2.tStopRefresh = tThisFlipGlobal  # on global time
                    Cued_image_post_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cued_image_post_2.stopped')
                    # update status
                    Cued_image_post_2.status = FINISHED
                    Cued_image_post_2.setAutoDraw(False)
            # Run 'Each Frame' code from Box8
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Routine_Stimulus_Post_Selection_H2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Routine_Stimulus_Post_Selection_H2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Routine_Stimulus_Post_Selection_H2" ---
        for thisComponent in Main_Routine_Stimulus_Post_Selection_H2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Routine_Stimulus_Post_Selection_H2
        Main_Routine_Stimulus_Post_Selection_H2.tStop = globalClock.getTime(format='float')
        Main_Routine_Stimulus_Post_Selection_H2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Routine_Stimulus_Post_Selection_H2.stopped', Main_Routine_Stimulus_Post_Selection_H2.tStop)
        # Run 'End Routine' code from Timer_9
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('Post_choice_Begin_Time', time_trialBegin)
        thisExp.addData('Post_choice_End_Time', time_trialEnd)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Main_Routine_Stimulus_Post_Selection_H2.maxDurationReached:
            routineTimer.addTime(-Main_Routine_Stimulus_Post_Selection_H2.maxDuration)
        elif Main_Routine_Stimulus_Post_Selection_H2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "Blank" ---
        # create an object to store info about Routine Blank
        Blank = data.Routine(
            name='Blank',
            components=[Blank_Text],
        )
        Blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Timer_PostISI
        time_trialBegin = globalClock.getTime()
        # store start times for Blank
        Blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Blank.tStart = globalClock.getTime(format='float')
        Blank.status = STARTED
        thisExp.addData('Blank.started', Blank.tStart)
        Blank.maxDuration = None
        # keep track of which components have finished
        BlankComponents = Blank.components
        for thisComponent in Blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Blank" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop2, data.TrialHandler2) and thisInnerLoop2.thisN != InnerLoop2.thisTrial.thisN:
            continueRoutine = False
        Blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.05:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Blank_Text* updates
            
            # if Blank_Text is starting this frame...
            if Blank_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Blank_Text.frameNStart = frameN  # exact frame index
                Blank_Text.tStart = t  # local t and not account for scr refresh
                Blank_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Blank_Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Blank_Text.started')
                # update status
                Blank_Text.status = STARTED
                Blank_Text.setAutoDraw(True)
            
            # if Blank_Text is active this frame...
            if Blank_Text.status == STARTED:
                # update params
                pass
            
            # if Blank_Text is stopping this frame...
            if Blank_Text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Blank_Text.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    Blank_Text.tStop = t  # not accounting for scr refresh
                    Blank_Text.tStopRefresh = tThisFlipGlobal  # on global time
                    Blank_Text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Blank_Text.stopped')
                    # update status
                    Blank_Text.status = FINISHED
                    Blank_Text.setAutoDraw(False)
            # Run 'Each Frame' code from Box21
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Blank" ---
        for thisComponent in Blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Blank
        Blank.tStop = globalClock.getTime(format='float')
        Blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Blank.stopped', Blank.tStop)
        # Run 'End Routine' code from Timer_PostISI
        thisExp.addData('PostISI_Start_Time', time_trialBegin)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Blank.maxDurationReached:
            routineTimer.addTime(-Blank.maxDuration)
        elif Blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.050000)
        
        # --- Prepare to start Routine "Main_Task_PostISI_H2" ---
        # create an object to store info about Routine Main_Task_PostISI_H2
        Main_Task_PostISI_H2 = data.Routine(
            name='Main_Task_PostISI_H2',
            components=[Main_Task_H1_Post_ISI_2],
        )
        Main_Task_PostISI_H2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Main_Task_PostISI_H2
        Main_Task_PostISI_H2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Task_PostISI_H2.tStart = globalClock.getTime(format='float')
        Main_Task_PostISI_H2.status = STARTED
        thisExp.addData('Main_Task_PostISI_H2.started', Main_Task_PostISI_H2.tStart)
        Main_Task_PostISI_H2.maxDuration = None
        # keep track of which components have finished
        Main_Task_PostISI_H2Components = Main_Task_PostISI_H2.components
        for thisComponent in Main_Task_PostISI_H2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Task_PostISI_H2" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop2, data.TrialHandler2) and thisInnerLoop2.thisN != InnerLoop2.thisTrial.thisN:
            continueRoutine = False
        Main_Task_PostISI_H2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Main_Task_H1_Post_ISI_2* updates
            
            # if Main_Task_H1_Post_ISI_2 is starting this frame...
            if Main_Task_H1_Post_ISI_2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                Main_Task_H1_Post_ISI_2.frameNStart = frameN  # exact frame index
                Main_Task_H1_Post_ISI_2.tStart = t  # local t and not account for scr refresh
                Main_Task_H1_Post_ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Main_Task_H1_Post_ISI_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Main_Task_H1_Post_ISI_2.started')
                # update status
                Main_Task_H1_Post_ISI_2.status = STARTED
                Main_Task_H1_Post_ISI_2.setAutoDraw(True)
            
            # if Main_Task_H1_Post_ISI_2 is active this frame...
            if Main_Task_H1_Post_ISI_2.status == STARTED:
                # update params
                pass
            
            # if Main_Task_H1_Post_ISI_2 is stopping this frame...
            if Main_Task_H1_Post_ISI_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Main_Task_H1_Post_ISI_2.tStartRefresh + Int_ISI-frameTolerance:
                    # keep track of stop time/frame for later
                    Main_Task_H1_Post_ISI_2.tStop = t  # not accounting for scr refresh
                    Main_Task_H1_Post_ISI_2.tStopRefresh = tThisFlipGlobal  # on global time
                    Main_Task_H1_Post_ISI_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Main_Task_H1_Post_ISI_2.stopped')
                    # update status
                    Main_Task_H1_Post_ISI_2.status = FINISHED
                    Main_Task_H1_Post_ISI_2.setAutoDraw(False)
            # Run 'Each Frame' code from Box9
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Task_PostISI_H2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Task_PostISI_H2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Task_PostISI_H2" ---
        for thisComponent in Main_Task_PostISI_H2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Task_PostISI_H2
        Main_Task_PostISI_H2.tStop = globalClock.getTime(format='float')
        Main_Task_PostISI_H2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Task_PostISI_H2.stopped', Main_Task_PostISI_H2.tStop)
        # Run 'End Routine' code from Timer_10
        time_trialEnd = globalClock.getTime()
        # the Routine "Main_Task_PostISI_H2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Main_Task_Post_Outcome_H2" ---
        # create an object to store info about Routine Main_Task_Post_Outcome_H2
        Main_Task_Post_Outcome_H2 = data.Routine(
            name='Main_Task_Post_Outcome_H2',
            components=[Cross_Outcomed_2],
        )
        Main_Task_Post_Outcome_H2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Timer_11
        time_trialBegin = globalClock.getTime()
        # Run 'Begin Routine' code from Shock_Code_2
        ctl.demand = last_demand
        ctl.pulse_width = last_pulse_width
        ctl.enabled = 1  # Re-arm device
        
        if Outcome == 1:
            print("⚡ About to trigger DS8R...")
        
            # Create and start the thread
            trigger_thread = threading.Thread(target=safe_run)
            trigger_thread.start()
        
            # Wait for the thread to finish, with a timeout
            trigger_thread.join(timeout=2.0)  # adjust timeout as needed
        
            if trigger_thread.is_alive():
                print("⚠️ DS8R trigger timed out — skipping trigger this trial.")
                # Optionally, try to reset ctl or log more info
            else:
                print("✅ DS8R trigger completed.")
        else:
            print("⏭ No trigger this trial (Outcome != 1).")
        # store start times for Main_Task_Post_Outcome_H2
        Main_Task_Post_Outcome_H2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Task_Post_Outcome_H2.tStart = globalClock.getTime(format='float')
        Main_Task_Post_Outcome_H2.status = STARTED
        thisExp.addData('Main_Task_Post_Outcome_H2.started', Main_Task_Post_Outcome_H2.tStart)
        Main_Task_Post_Outcome_H2.maxDuration = None
        # keep track of which components have finished
        Main_Task_Post_Outcome_H2Components = Main_Task_Post_Outcome_H2.components
        for thisComponent in Main_Task_Post_Outcome_H2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Task_Post_Outcome_H2" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop2, data.TrialHandler2) and thisInnerLoop2.thisN != InnerLoop2.thisTrial.thisN:
            continueRoutine = False
        Main_Task_Post_Outcome_H2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Cross_Outcomed_2* updates
            
            # if Cross_Outcomed_2 is starting this frame...
            if Cross_Outcomed_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Cross_Outcomed_2.frameNStart = frameN  # exact frame index
                Cross_Outcomed_2.tStart = t  # local t and not account for scr refresh
                Cross_Outcomed_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cross_Outcomed_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cross_Outcomed_2.started')
                # update status
                Cross_Outcomed_2.status = STARTED
                Cross_Outcomed_2.setAutoDraw(True)
            
            # if Cross_Outcomed_2 is active this frame...
            if Cross_Outcomed_2.status == STARTED:
                # update params
                pass
            
            # if Cross_Outcomed_2 is stopping this frame...
            if Cross_Outcomed_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Cross_Outcomed_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Cross_Outcomed_2.tStop = t  # not accounting for scr refresh
                    Cross_Outcomed_2.tStopRefresh = tThisFlipGlobal  # on global time
                    Cross_Outcomed_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cross_Outcomed_2.stopped')
                    # update status
                    Cross_Outcomed_2.status = FINISHED
                    Cross_Outcomed_2.setAutoDraw(False)
            # Run 'Each Frame' code from Box10
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Task_Post_Outcome_H2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Task_Post_Outcome_H2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Task_Post_Outcome_H2" ---
        for thisComponent in Main_Task_Post_Outcome_H2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Task_Post_Outcome_H2
        Main_Task_Post_Outcome_H2.tStop = globalClock.getTime(format='float')
        Main_Task_Post_Outcome_H2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Task_Post_Outcome_H2.stopped', Main_Task_Post_Outcome_H2.tStop)
        # Run 'End Routine' code from Timer_11
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('Outcome_Delivered_Time', time_trialBegin)
        thisExp.addData('Outcome_Delivered_Routine_End', time_trialEnd)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Main_Task_Post_Outcome_H2.maxDurationReached:
            routineTimer.addTime(-Main_Task_Post_Outcome_H2.maxDuration)
        elif Main_Task_Post_Outcome_H2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Main_Routine_ISI_H2_2" ---
        # create an object to store info about Routine Main_Routine_ISI_H2_2
        Main_Routine_ISI_H2_2 = data.Routine(
            name='Main_Routine_ISI_H2_2',
            components=[Main_Task_H1_ISI_2],
        )
        Main_Routine_ISI_H2_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Main_Task_H1_ISI_2.setColor([-0.7500, -0.7500, -0.7500], colorSpace='rgb')
        Main_Task_H1_ISI_2.setText('+')
        # Run 'Begin Routine' code from Timer_13
        time_trialBegin = globalClock.getTime()
        # store start times for Main_Routine_ISI_H2_2
        Main_Routine_ISI_H2_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Routine_ISI_H2_2.tStart = globalClock.getTime(format='float')
        Main_Routine_ISI_H2_2.status = STARTED
        thisExp.addData('Main_Routine_ISI_H2_2.started', Main_Routine_ISI_H2_2.tStart)
        Main_Routine_ISI_H2_2.maxDuration = None
        # keep track of which components have finished
        Main_Routine_ISI_H2_2Components = Main_Routine_ISI_H2_2.components
        for thisComponent in Main_Routine_ISI_H2_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Main_Routine_ISI_H2_2" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop2, data.TrialHandler2) and thisInnerLoop2.thisN != InnerLoop2.thisTrial.thisN:
            continueRoutine = False
        Main_Routine_ISI_H2_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Main_Task_H1_ISI_2* updates
            
            # if Main_Task_H1_ISI_2 is starting this frame...
            if Main_Task_H1_ISI_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Main_Task_H1_ISI_2.frameNStart = frameN  # exact frame index
                Main_Task_H1_ISI_2.tStart = t  # local t and not account for scr refresh
                Main_Task_H1_ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Main_Task_H1_ISI_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Main_Task_H1_ISI_2.started')
                # update status
                Main_Task_H1_ISI_2.status = STARTED
                Main_Task_H1_ISI_2.setAutoDraw(True)
            
            # if Main_Task_H1_ISI_2 is active this frame...
            if Main_Task_H1_ISI_2.status == STARTED:
                # update params
                pass
            
            # if Main_Task_H1_ISI_2 is stopping this frame...
            if Main_Task_H1_ISI_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Main_Task_H1_ISI_2.tStartRefresh + Pre_ISI-frameTolerance:
                    # keep track of stop time/frame for later
                    Main_Task_H1_ISI_2.tStop = t  # not accounting for scr refresh
                    Main_Task_H1_ISI_2.tStopRefresh = tThisFlipGlobal  # on global time
                    Main_Task_H1_ISI_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Main_Task_H1_ISI_2.stopped')
                    # update status
                    Main_Task_H1_ISI_2.status = FINISHED
                    Main_Task_H1_ISI_2.setAutoDraw(False)
            # Run 'Each Frame' code from Box1_2
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Routine_ISI_H2_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Routine_ISI_H2_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Routine_ISI_H2_2" ---
        for thisComponent in Main_Routine_ISI_H2_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Routine_ISI_H2_2
        Main_Routine_ISI_H2_2.tStop = globalClock.getTime(format='float')
        Main_Routine_ISI_H2_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Routine_ISI_H2_2.stopped', Main_Routine_ISI_H2_2.tStop)
        # Run 'End Routine' code from Timer_13
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('Post2_ISI_Begin', time_trialBegin)
        thisExp.addData('Post2_ISI_End', time_trialEnd)
        # the Routine "Main_Routine_ISI_H2_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InnerLoop2'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "End_Recording_2" ---
    # create an object to store info about Routine End_Recording_2
    End_Recording_2 = data.Routine(
        name='End_Recording_2',
        components=[],
    )
    End_Recording_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for End_Recording_2
    End_Recording_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End_Recording_2.tStart = globalClock.getTime(format='float')
    End_Recording_2.status = STARTED
    thisExp.addData('End_Recording_2.started', End_Recording_2.tStart)
    End_Recording_2.maxDuration = None
    # keep track of which components have finished
    End_Recording_2Components = End_Recording_2.components
    for thisComponent in End_Recording_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End_Recording_2" ---
    End_Recording_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End_Recording_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_Recording_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End_Recording_2" ---
    for thisComponent in End_Recording_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End_Recording_2
    End_Recording_2.tStop = globalClock.getTime(format='float')
    End_Recording_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End_Recording_2.stopped', End_Recording_2.tStop)
    thisExp.nextEntry()
    # the Routine "End_Recording_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Task_End" ---
    # create an object to store info about Routine Task_End
    Task_End = data.Routine(
        name='Task_End',
        components=[End_Text],
    )
    Task_End.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Task_End
    Task_End.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Task_End.tStart = globalClock.getTime(format='float')
    Task_End.status = STARTED
    thisExp.addData('Task_End.started', Task_End.tStart)
    Task_End.maxDuration = None
    # keep track of which components have finished
    Task_EndComponents = Task_End.components
    for thisComponent in Task_End.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Task_End" ---
    Task_End.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box11
        grayBox.draw()
        
        # *End_Text* updates
        
        # if End_Text is starting this frame...
        if End_Text.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            End_Text.frameNStart = frameN  # exact frame index
            End_Text.tStart = t  # local t and not account for scr refresh
            End_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(End_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'End_Text.started')
            # update status
            End_Text.status = STARTED
            End_Text.setAutoDraw(True)
        
        # if End_Text is active this frame...
        if End_Text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Task_End.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Task_End.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Task_End" ---
    for thisComponent in Task_End.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Task_End
    Task_End.tStop = globalClock.getTime(format='float')
    Task_End.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Task_End.stopped', Task_End.tStop)
    # Run 'End Routine' code from Timer_Final
    time_trialEnd = globalClock.getTime()
    
    thisExp.addData('Experiment_End_Time', time_trialEnd)
    thisExp.nextEntry()
    # the Routine "Task_End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
