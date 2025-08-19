#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on July 24, 2025, at 13:42
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

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from Shock_Cal_Code
import os

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
# Run 'Before Experiment' code from Shock_Cal_Code
import os

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
    'fMRI_enabled': 'Yes / No',
    'EyeL_enabled': 'Yes / No',
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
_fullScr = True
_winSize = [1707, 1067]
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
        originPath='C:\\Users\\PERLadmin\\Desktop\\DOREA_Task_Battery\\PAL\\PAL_Task.py',
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
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[-0.3000, -0.3000, -0.3000], colorSpace='rgb',
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
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
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
            backend='ioHub',
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
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
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
    
    # Run 'Begin Experiment' code from Initialise_Selection_Outcome
    selectedColor = 'grey'
    
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
        text="When an event has occured (i.e. sitmulation or not), \n the cross will change colour:",
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
    
    # --- Initialize components for Routine "Shock_Recalib" ---
    # Run 'Begin Experiment' code from Shock_Cal_Code
    import sys
    import ctypes
    from ds8r import DS8R
    
    # --- Path to DS8R and DLL ---
    ds8r_path = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
    sys.path.append(ds8r_path)
    dll_path = os.path.join(ds8r_path, "D128RProxy.dll")
    
    # --- Load DLL ---
    try:
        ctypes.WinDLL(dll_path)
        print("✅ DLL loaded manually.")
    except Exception as e:
        print(f"❌ DLL load failed: {e}")
    
    # --- Initialize DS8R stimulator ---
    ctl = DS8R(demand=20, pulse_width=2000, enabled=1)
    print("✅ DS8R object initialized.")
    
    # --- Tracking for calibration ---
    calibration_done = False
    shock_history = []
    rating_history = []
    
    # --- Initialize components for Routine "EyeL_Calib" ---
    
    # --- Initialize components for Routine "Instructions_Final" ---
    # Run 'Begin Experiment' code from Text_code_4
    from psychopy import visual, core, event
    
    # One text stim per color segment
    
    text_ISI_instr8 = visual.TextStim(
        win,
        text="You will now begin the task.",
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
    
    
    # --- Initialize components for Routine "Main_Routine_ISI_H1" ---
    Main_Task_H1_ISI = visual.TextStim(win=win, name='Main_Task_H1_ISI',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
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
        ori=0.0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
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
        width=(0.275, 0.275)[0], height=(0.275, 0.275)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    Cued_image_post = visual.ImageStim(
        win=win,
        name='Cued_image_post', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
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
    Cross_Outcomed = visual.TextStim(win=win, name='Cross_Outcomed',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -0.6706, -0.3490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "Extra_ISI_1" ---
    Extra_ISI_One = visual.TextStim(win=win, name='Extra_ISI_One',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Break" ---
    # Run 'Begin Experiment' code from TimerCode
    from psychopy import visual, core, event
    import numpy as np
    
    fMRI_enabled = expInfo.get('fMRI_enabled', 'no')
    
    # --- Initialize components for Routine "Post_Break" ---
    Post_break_text = visual.TextStim(win=win, name='Post_break_text',
        text='The break period has elapsed. Please call a researcher.\n\n\n\n\nPress ← or → to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Post_break_keys = keyboard.Keyboard(deviceName='Post_break_keys')
    # Run 'Begin Experiment' code from Skipper3
    fMRI_enabled = expInfo.get('fMRI_enabled', 'no')
    
    # --- Initialize components for Routine "Shock_Recalib" ---
    # Run 'Begin Experiment' code from Shock_Cal_Code
    import sys
    import ctypes
    from ds8r import DS8R
    
    # --- Path to DS8R and DLL ---
    ds8r_path = r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R"
    sys.path.append(ds8r_path)
    dll_path = os.path.join(ds8r_path, "D128RProxy.dll")
    
    # --- Load DLL ---
    try:
        ctypes.WinDLL(dll_path)
        print("✅ DLL loaded manually.")
    except Exception as e:
        print(f"❌ DLL load failed: {e}")
    
    # --- Initialize DS8R stimulator ---
    ctl = DS8R(demand=20, pulse_width=2000, enabled=1)
    print("✅ DS8R object initialized.")
    
    # --- Tracking for calibration ---
    calibration_done = False
    shock_history = []
    rating_history = []
    
    # --- Initialize components for Routine "EyeL_Recalib" ---
    
    # --- Initialize components for Routine "Main_Routine_ISI_H2" ---
    Main_Task_H2_ISI = visual.TextStim(win=win, name='Main_Task_H2_ISI',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
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
        ori=0.0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
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
        width=(0.275, 0.275)[0], height=(0.275, 0.275)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    Cued_image_post_2 = visual.ImageStim(
        win=win,
        name='Cued_image_post_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
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
    
    # --- Initialize components for Routine "Extra_ISI_2" ---
    Extra_ISI_Two = visual.TextStim(win=win, name='Extra_ISI_Two',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.125, wrapWidth=None, ori=0.0, 
        color=[-0.7500, -0.7500, -0.7500], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
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
    
    # --- Prepare to start Routine "Shock_Recalib" ---
    # create an object to store info about Routine Shock_Recalib
    Shock_Recalib = data.Routine(
        name='Shock_Recalib',
        components=[],
    )
    Shock_Recalib.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Shock_Cal_Code
    slider_keys = keyboard.Keyboard()
    slider_keys.clearEvents()
    
    if not calibration_done:
        print(f"⚡ Delivering shock at {ctl.demand} mA")
        ctl.enabled = 1  # Re-arm the stimulator
        ctl.run()
        thisExp.addData("shock_intensity", ctl.demand)
    else:
        print("✅ Calibration already completed. Skipping shock.")
    
    
    # store start times for Shock_Recalib
    Shock_Recalib.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Shock_Recalib.tStart = globalClock.getTime(format='float')
    Shock_Recalib.status = STARTED
    thisExp.addData('Shock_Recalib.started', Shock_Recalib.tStart)
    Shock_Recalib.maxDuration = None
    # keep track of which components have finished
    Shock_RecalibComponents = Shock_Recalib.components
    for thisComponent in Shock_Recalib.components:
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
    
    # --- Run Routine "Shock_Recalib" ---
    Shock_Recalib.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Shock_Cal_Code
        keys = slider_keys.getKeys()
        
        for key in keys:
            if key.name == 'left':
                if pain_slider.markerPos is not None:
                    pain_slider.markerPos = max(pain_slider.markerPos - 1, 0)
                else:
                    pain_slider.markerPos = 0
        
            elif key.name == 'right':
                if pain_slider.markerPos is not None:
                    pain_slider.markerPos = min(pain_slider.markerPos + 1, 10)
                else:
                    pain_slider.markerPos = 1
        
            elif key.name in ['space', 'return']:
                rating = pain_slider.getRating()
                if rating is not None:
                    print(f"✅ Rating confirmed: {rating}")
                    rating_history.append(rating)
                    shock_history.append(ctl.demand)
                    thisExp.addData("pain_rating", rating)
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
            Shock_Recalib.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Shock_Recalib.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Shock_Recalib" ---
    for thisComponent in Shock_Recalib.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Shock_Recalib
    Shock_Recalib.tStop = globalClock.getTime(format='float')
    Shock_Recalib.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Shock_Recalib.stopped', Shock_Recalib.tStop)
    # Run 'End Routine' code from Shock_Cal_Code
    if not calibration_done:
        rating = pain_slider.getRating()
        print(f"📝 Final rating for this trial: {rating}")
        if rating is not None:
            rating_history.append(rating)
            shock_history.append(ctl.demand)
            thisExp.addData("pain_rating", rating)
    
        # --- Adjust demand based on rating ---
        if rating < 8:
            ctl.demand += 2
        elif rating > 9:
            ctl.demand = max(1, ctl.demand - 1)
    
        # --- Check if we're done ---
        recent = rating_history[-5:]
        if recent.count(8) >= 3:
            calibration_done = True
            final_threshold = ctl.demand
            print(f"✅ Calibration complete at {final_threshold} mA")
            thisExp.addData("calibration_threshold", final_threshold)
            thisExp.addData("calibration_ratings", rating_history)
            thisExp.addData("calibration_shock_history", shock_history)
    else:
        print("⏭ Calibration complete. No adjustment.")
    
    # Always save updated histories
    thisExp.addData("FinalShockHistory", shock_history)
    thisExp.addData("FinalRatingHistory", rating_history)
    thisExp.nextEntry()
    # the Routine "Shock_Recalib" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EyeL_Calib" ---
    # create an object to store info about Routine EyeL_Calib
    EyeL_Calib = data.Routine(
        name='EyeL_Calib',
        components=[],
    )
    EyeL_Calib.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for EyeL_Calib
    EyeL_Calib.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EyeL_Calib.tStart = globalClock.getTime(format='float')
    EyeL_Calib.status = STARTED
    thisExp.addData('EyeL_Calib.started', EyeL_Calib.tStart)
    EyeL_Calib.maxDuration = None
    # keep track of which components have finished
    EyeL_CalibComponents = EyeL_Calib.components
    for thisComponent in EyeL_Calib.components:
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
    
    # --- Run Routine "EyeL_Calib" ---
    EyeL_Calib.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box20
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
            EyeL_Calib.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EyeL_Calib.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EyeL_Calib" ---
    for thisComponent in EyeL_Calib.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EyeL_Calib
    EyeL_Calib.tStop = globalClock.getTime(format='float')
    EyeL_Calib.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EyeL_Calib.stopped', EyeL_Calib.tStop)
    thisExp.nextEntry()
    # the Routine "EyeL_Calib" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    
    
    # set up handler to look after randomisation of conditions etc
    InnerLoop = data.TrialHandler2(
        name='InnerLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        VersionSelection_H1, 
        selection='0:9'
    )
    , 
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
        
        thisExp.addData('Pre_ISI_Begin', time_trialBegin)
        thisExp.addData('Pre_ISI_End', time_trialEnd)
        # the Routine "Main_Routine_ISI_H1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Blank" ---
        # create an object to store info about Routine Blank
        Blank = data.Routine(
            name='Blank',
            components=[Blank_Text],
        )
        Blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
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
        # Run 'Begin Routine' code from Timer_4
        time_trialBegin = globalClock.getTime()
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
        
        thisExp.addData('PostISI_Begin_Time', time_trialBegin)
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
        ctl = DS8R(
            demand=80,          # adjust as needed
            pulse_width=300,    # adjust as needed
            enabled=1,
            dwell=10,
            mode=1,
            polarity=1,
            source=1,
            recovery=50
        )
        
        ctl.enabled = 1  # re-arm the device
        
        if Outcome == 1:
            print("⚡ Triggering DS8R now...")
            ctl.run()
        else:
            print("⏭ No trigger this trial (Outcome != 1).")
        
        # Second block (no extra space!)
        if Outcome == 1:
            time_shockTriggered = globalClock.getTime()
            print(f"⚡ Shock triggered at: {time_shockTriggered:.4f} seconds")
            ctl.enabled = 1
            ctl.run()
            
        thisExp.addData('shock_time', time_shockTriggered)
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
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InnerLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Extra_ISI_1" ---
    # create an object to store info about Routine Extra_ISI_1
    Extra_ISI_1 = data.Routine(
        name='Extra_ISI_1',
        components=[Extra_ISI_One],
    )
    Extra_ISI_1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Timer_6
    time_trialBegin = globalClock.getTime()
    # store start times for Extra_ISI_1
    Extra_ISI_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Extra_ISI_1.tStart = globalClock.getTime(format='float')
    Extra_ISI_1.status = STARTED
    thisExp.addData('Extra_ISI_1.started', Extra_ISI_1.tStart)
    Extra_ISI_1.maxDuration = None
    # keep track of which components have finished
    Extra_ISI_1Components = Extra_ISI_1.components
    for thisComponent in Extra_ISI_1.components:
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
    
    # --- Run Routine "Extra_ISI_1" ---
    Extra_ISI_1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Extra_ISI_One* updates
        
        # if Extra_ISI_One is starting this frame...
        if Extra_ISI_One.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Extra_ISI_One.frameNStart = frameN  # exact frame index
            Extra_ISI_One.tStart = t  # local t and not account for scr refresh
            Extra_ISI_One.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Extra_ISI_One, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Extra_ISI_One.started')
            # update status
            Extra_ISI_One.status = STARTED
            Extra_ISI_One.setAutoDraw(True)
        
        # if Extra_ISI_One is active this frame...
        if Extra_ISI_One.status == STARTED:
            # update params
            pass
        
        # if Extra_ISI_One is stopping this frame...
        if Extra_ISI_One.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Extra_ISI_One.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                Extra_ISI_One.tStop = t  # not accounting for scr refresh
                Extra_ISI_One.tStopRefresh = tThisFlipGlobal  # on global time
                Extra_ISI_One.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Extra_ISI_One.stopped')
                # update status
                Extra_ISI_One.status = FINISHED
                Extra_ISI_One.setAutoDraw(False)
        # Run 'Each Frame' code from Box_21
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
            Extra_ISI_1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Extra_ISI_1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Extra_ISI_1" ---
    for thisComponent in Extra_ISI_1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Extra_ISI_1
    Extra_ISI_1.tStop = globalClock.getTime(format='float')
    Extra_ISI_1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Extra_ISI_1.stopped', Extra_ISI_1.tStop)
    # Run 'End Routine' code from Timer_6
    time_trialEnd = globalClock.getTime()
    
    thisExp.addData('PostHalf_ISI_Start', time_trialBegin)
    thisExp.addData('PostHalf_ISI_End.UseThisEndPoint.', time_trialEnd)
    # Run 'End Routine' code from Skipper2
    skipNextRoutine = fMRI_enabled.lower() in ['yes', 'y']
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Extra_ISI_1.maxDurationReached:
        routineTimer.addTime(-Extra_ISI_1.maxDuration)
    elif Extra_ISI_1.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.500000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Break" ---
    # create an object to store info about Routine Break
    Break = data.Routine(
        name='Break',
        components=[],
    )
    Break.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from TimerCode
    # Only skip if the flag is set
    if 'skipNextRoutine' in globals() and skipNextRoutine:
        continueRoutine = False
    
    from psychopy import visual, core, event
    import numpy as np
    
    # === SETTINGS ===
    timer_duration = 210  # in seconds
    radius = 0.075        # size of the circular timer
    pos = (0, 0)          # position of the timer on screen
    
    # === SETUP WINDOW ===
    #win = visual.Window(fullscr=True, color='grey', units='height')
    
    # === BACKGROUND BOX ===
    grayBox2 = visual.Rect(
        win,
        width=0.8,
        height=0.8,
        units='height',
        lineWidth=0,
        lineColor=None,
        fillColor=[0.004, 0.004, 0.004],
        fillColorSpace='rgb',
        pos=(0, 0)
    )
    
    # === CIRCLE BEHIND THE WEDGE ===
    circle_bg = visual.Circle(
        win,
        radius=radius,
        edges=128,
        fillColor=[0.1, 0.1, 0.1],  # dark gray
        fillColorSpace='rgb',
        lineColor=None,
        pos=pos,
        autoDraw=False
    )
    
    # === TIMER WEDGE FUNCTION ===
    def make_wedge(progress_fraction, radius=0.2, resolution=100):
        # Creates a counterclockwise wedge starting from top (90 degrees)
        angle = 360 * progress_fraction
        num_points = max(2, int(resolution * progress_fraction))
        theta = np.linspace(90, 90 + angle, num_points)
        x = np.cos(np.deg2rad(theta)) * radius
        y = np.sin(np.deg2rad(theta)) * radius
        verts = [(0, 0)] + list(zip(x, y))
        return verts
    
    # === INITIALIZE TIMER CLOCK ===
    timer_clock = core.Clock()
    
    # === INITIALIZE WEDGE SHAPE ===
    wedge = visual.ShapeStim(
        win,
        vertices=make_wedge(1.0, radius),
        fillColor=[0.28, 0.28, 0.28],
        lineColor=None,
        fillColorSpace='rgb',
        pos=pos,
        closeShape=True,
        autoDraw=False
    )
    
    # === OPTIONAL LABEL TEXT ===
    label = visual.TextStim(
        win,
        text="This is a break period. You are over 50% complete.\nYou may relax until the timer runs out.",
        pos=(0, -0.325),
        color='black',
        height=0.025
    )
    
    # === START TIMER ===
    timer_clock.reset()
    running = True
    
    while running:
        elapsed = timer_clock.getTime()
        progress = max(0, 1 - (elapsed / timer_duration))
    
        # ESC to quit
        keys = event.getKeys()
        if 'escape' in keys:
            core.quit()
    
        # Update wedge
        if elapsed < timer_duration:
            wedge.vertices = make_wedge(progress, radius)
    
        # Draw components (in order)
        grayBox2.draw()       # background box
        circle_bg.draw()      # circle background behind wedge
        if elapsed < timer_duration:
            wedge.draw()      # wedge timer
        label.draw()          # text label
    
        # Flip screen
        win.flip()
    
        # End after time limit
        if elapsed >= timer_duration:
            running = False
    
    # === CONTINUE TO NEXT ROUTINE (no exit) ===
    # Leave win open, ready for next block or routine
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from TimerCode
        if not hasattr(thisExp, 'skipFlagChecked'):
            if fMRI_enabled.lower() in ['yes', 'y']:
                continueRoutine = False
            thisExp.skipFlagChecked = True
        
        if continueRoutine:
            grayBox2.draw()
        
            elapsed = timer_clock.getTime()
            progress = max(0, 1 - (elapsed / timer_duration))
        
            wedge.vertices = make_wedge(progress)
        
            if elapsed < timer_duration:
                wedge.draw()
        
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
    thisExp.nextEntry()
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    
    # --- Prepare to start Routine "Shock_Recalib" ---
    # create an object to store info about Routine Shock_Recalib
    Shock_Recalib = data.Routine(
        name='Shock_Recalib',
        components=[],
    )
    Shock_Recalib.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Shock_Cal_Code
    slider_keys = keyboard.Keyboard()
    slider_keys.clearEvents()
    
    if not calibration_done:
        print(f"⚡ Delivering shock at {ctl.demand} mA")
        ctl.enabled = 1  # Re-arm the stimulator
        ctl.run()
        thisExp.addData("shock_intensity", ctl.demand)
    else:
        print("✅ Calibration already completed. Skipping shock.")
    
    
    # store start times for Shock_Recalib
    Shock_Recalib.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Shock_Recalib.tStart = globalClock.getTime(format='float')
    Shock_Recalib.status = STARTED
    thisExp.addData('Shock_Recalib.started', Shock_Recalib.tStart)
    Shock_Recalib.maxDuration = None
    # keep track of which components have finished
    Shock_RecalibComponents = Shock_Recalib.components
    for thisComponent in Shock_Recalib.components:
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
    
    # --- Run Routine "Shock_Recalib" ---
    Shock_Recalib.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Shock_Cal_Code
        keys = slider_keys.getKeys()
        
        for key in keys:
            if key.name == 'left':
                if pain_slider.markerPos is not None:
                    pain_slider.markerPos = max(pain_slider.markerPos - 1, 0)
                else:
                    pain_slider.markerPos = 0
        
            elif key.name == 'right':
                if pain_slider.markerPos is not None:
                    pain_slider.markerPos = min(pain_slider.markerPos + 1, 10)
                else:
                    pain_slider.markerPos = 1
        
            elif key.name in ['space', 'return']:
                rating = pain_slider.getRating()
                if rating is not None:
                    print(f"✅ Rating confirmed: {rating}")
                    rating_history.append(rating)
                    shock_history.append(ctl.demand)
                    thisExp.addData("pain_rating", rating)
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
            Shock_Recalib.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Shock_Recalib.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Shock_Recalib" ---
    for thisComponent in Shock_Recalib.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Shock_Recalib
    Shock_Recalib.tStop = globalClock.getTime(format='float')
    Shock_Recalib.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Shock_Recalib.stopped', Shock_Recalib.tStop)
    # Run 'End Routine' code from Shock_Cal_Code
    if not calibration_done:
        rating = pain_slider.getRating()
        print(f"📝 Final rating for this trial: {rating}")
        if rating is not None:
            rating_history.append(rating)
            shock_history.append(ctl.demand)
            thisExp.addData("pain_rating", rating)
    
        # --- Adjust demand based on rating ---
        if rating < 8:
            ctl.demand += 2
        elif rating > 9:
            ctl.demand = max(1, ctl.demand - 1)
    
        # --- Check if we're done ---
        recent = rating_history[-5:]
        if recent.count(8) >= 3:
            calibration_done = True
            final_threshold = ctl.demand
            print(f"✅ Calibration complete at {final_threshold} mA")
            thisExp.addData("calibration_threshold", final_threshold)
            thisExp.addData("calibration_ratings", rating_history)
            thisExp.addData("calibration_shock_history", shock_history)
    else:
        print("⏭ Calibration complete. No adjustment.")
    
    # Always save updated histories
    thisExp.addData("FinalShockHistory", shock_history)
    thisExp.addData("FinalRatingHistory", rating_history)
    thisExp.nextEntry()
    # the Routine "Shock_Recalib" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EyeL_Recalib" ---
    # create an object to store info about Routine EyeL_Recalib
    EyeL_Recalib = data.Routine(
        name='EyeL_Recalib',
        components=[],
    )
    EyeL_Recalib.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for EyeL_Recalib
    EyeL_Recalib.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EyeL_Recalib.tStart = globalClock.getTime(format='float')
    EyeL_Recalib.status = STARTED
    thisExp.addData('EyeL_Recalib.started', EyeL_Recalib.tStart)
    EyeL_Recalib.maxDuration = None
    # keep track of which components have finished
    EyeL_RecalibComponents = EyeL_Recalib.components
    for thisComponent in EyeL_Recalib.components:
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
    
    # --- Run Routine "EyeL_Recalib" ---
    EyeL_Recalib.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Box15
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
            EyeL_Recalib.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EyeL_Recalib.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EyeL_Recalib" ---
    for thisComponent in EyeL_Recalib.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EyeL_Recalib
    EyeL_Recalib.tStop = globalClock.getTime(format='float')
    EyeL_Recalib.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EyeL_Recalib.stopped', EyeL_Recalib.tStop)
    thisExp.nextEntry()
    # the Routine "EyeL_Recalib" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    InnerLoop2 = data.TrialHandler2(
        name='InnerLoop2',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        VersionSelection_H2, 
        selection='0:10'
    )
    , 
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
        
        # --- Prepare to start Routine "Main_Routine_ISI_H2" ---
        # create an object to store info about Routine Main_Routine_ISI_H2
        Main_Routine_ISI_H2 = data.Routine(
            name='Main_Routine_ISI_H2',
            components=[Main_Task_H2_ISI],
        )
        Main_Routine_ISI_H2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Main_Task_H2_ISI.setColor([-0.7500, -0.7500, -0.7500], colorSpace='rgb')
        Main_Task_H2_ISI.setText('+')
        # Run 'Begin Routine' code from Timer_7
        time_trialBegin = globalClock.getTime()
        # store start times for Main_Routine_ISI_H2
        Main_Routine_ISI_H2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Routine_ISI_H2.tStart = globalClock.getTime(format='float')
        Main_Routine_ISI_H2.status = STARTED
        thisExp.addData('Main_Routine_ISI_H2.started', Main_Routine_ISI_H2.tStart)
        Main_Routine_ISI_H2.maxDuration = None
        # keep track of which components have finished
        Main_Routine_ISI_H2Components = Main_Routine_ISI_H2.components
        for thisComponent in Main_Routine_ISI_H2.components:
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
        
        # --- Run Routine "Main_Routine_ISI_H2" ---
        # if trial has changed, end Routine now
        if isinstance(InnerLoop2, data.TrialHandler2) and thisInnerLoop2.thisN != InnerLoop2.thisTrial.thisN:
            continueRoutine = False
        Main_Routine_ISI_H2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Main_Task_H2_ISI* updates
            
            # if Main_Task_H2_ISI is starting this frame...
            if Main_Task_H2_ISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Main_Task_H2_ISI.frameNStart = frameN  # exact frame index
                Main_Task_H2_ISI.tStart = t  # local t and not account for scr refresh
                Main_Task_H2_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Main_Task_H2_ISI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Main_Task_H2_ISI.started')
                # update status
                Main_Task_H2_ISI.status = STARTED
                Main_Task_H2_ISI.setAutoDraw(True)
            
            # if Main_Task_H2_ISI is active this frame...
            if Main_Task_H2_ISI.status == STARTED:
                # update params
                pass
            
            # if Main_Task_H2_ISI is stopping this frame...
            if Main_Task_H2_ISI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Main_Task_H2_ISI.tStartRefresh + Pre_ISI-frameTolerance:
                    # keep track of stop time/frame for later
                    Main_Task_H2_ISI.tStop = t  # not accounting for scr refresh
                    Main_Task_H2_ISI.tStopRefresh = tThisFlipGlobal  # on global time
                    Main_Task_H2_ISI.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Main_Task_H2_ISI.stopped')
                    # update status
                    Main_Task_H2_ISI.status = FINISHED
                    Main_Task_H2_ISI.setAutoDraw(False)
            # Run 'Each Frame' code from Box6
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
                Main_Routine_ISI_H2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Routine_ISI_H2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Routine_ISI_H2" ---
        for thisComponent in Main_Routine_ISI_H2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Routine_ISI_H2
        Main_Routine_ISI_H2.tStop = globalClock.getTime(format='float')
        Main_Routine_ISI_H2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Routine_ISI_H2.stopped', Main_Routine_ISI_H2.tStop)
        # Run 'End Routine' code from Timer_7
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('Pre_ISI_Begin', time_trialBegin)
        thisExp.addData('Pre_ISI_End', time_trialEnd)
        # the Routine "Main_Routine_ISI_H2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Blank" ---
        # create an object to store info about Routine Blank
        Blank = data.Routine(
            name='Blank',
            components=[Blank_Text],
        )
        Blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
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
        # Run 'Begin Routine' code from Timer_10
        time_trialBegin = globalClock.getTime()
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
        
        thisExp.addData('PostISI_Begin_Time', time_trialBegin)
        thisExp.addData('PostISI_End_Time', time_trialEnd)
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
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InnerLoop2'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Extra_ISI_2" ---
    # create an object to store info about Routine Extra_ISI_2
    Extra_ISI_2 = data.Routine(
        name='Extra_ISI_2',
        components=[Extra_ISI_Two],
    )
    Extra_ISI_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Timer_12
    time_trialBegin = globalClock.getTime()
    # store start times for Extra_ISI_2
    Extra_ISI_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Extra_ISI_2.tStart = globalClock.getTime(format='float')
    Extra_ISI_2.status = STARTED
    thisExp.addData('Extra_ISI_2.started', Extra_ISI_2.tStart)
    Extra_ISI_2.maxDuration = None
    # keep track of which components have finished
    Extra_ISI_2Components = Extra_ISI_2.components
    for thisComponent in Extra_ISI_2.components:
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
    
    # --- Run Routine "Extra_ISI_2" ---
    Extra_ISI_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Extra_ISI_Two* updates
        
        # if Extra_ISI_Two is starting this frame...
        if Extra_ISI_Two.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Extra_ISI_Two.frameNStart = frameN  # exact frame index
            Extra_ISI_Two.tStart = t  # local t and not account for scr refresh
            Extra_ISI_Two.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Extra_ISI_Two, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Extra_ISI_Two.started')
            # update status
            Extra_ISI_Two.status = STARTED
            Extra_ISI_Two.setAutoDraw(True)
        
        # if Extra_ISI_Two is active this frame...
        if Extra_ISI_Two.status == STARTED:
            # update params
            pass
        
        # if Extra_ISI_Two is stopping this frame...
        if Extra_ISI_Two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Extra_ISI_Two.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                Extra_ISI_Two.tStop = t  # not accounting for scr refresh
                Extra_ISI_Two.tStopRefresh = tThisFlipGlobal  # on global time
                Extra_ISI_Two.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Extra_ISI_Two.stopped')
                # update status
                Extra_ISI_Two.status = FINISHED
                Extra_ISI_Two.setAutoDraw(False)
        # Run 'Each Frame' code from Box_22
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
            Extra_ISI_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Extra_ISI_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Extra_ISI_2" ---
    for thisComponent in Extra_ISI_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Extra_ISI_2
    Extra_ISI_2.tStop = globalClock.getTime(format='float')
    Extra_ISI_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Extra_ISI_2.stopped', Extra_ISI_2.tStop)
    # Run 'End Routine' code from Timer_12
    time_trialEnd = globalClock.getTime()
    
    thisExp.addData('PostHalf_ISI_Start', time_trialBegin)
    thisExp.addData('PostHalf_ISI_End.UseThisEndPoint.', time_trialEnd)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Extra_ISI_2.maxDurationReached:
        routineTimer.addTime(-Extra_ISI_2.maxDuration)
    elif Extra_ISI_2.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.500000)
    thisExp.nextEntry()
    
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
        if End_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
