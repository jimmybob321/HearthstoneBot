import time,pyautogui
width, height = pyautogui.size()
pyautogui.moveTo(100,100,duration=0.25)
def playCard():
    pyautogui.dragrel(0,650,duration=0.25)
def passTurn():
    pyautogui.moveTo(2725,975,duration=0.25)
    pyautogui.click()
def goFace():
    pass
def hitTaunt():
    pass
def startGame():
    pyautogui.moveTo(2450, 1675, duration=0.25)
    pyautogui.click()


