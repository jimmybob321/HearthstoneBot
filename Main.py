import time,pyautogui
width, height = pyautogui.size()

def playCard():
    pyautogui.moveTo(850, 925, duration=0.25)
    pyautogui.dragRel(0,-450,duration=1).5
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
def think():
    time.sleep(2)
def detectTarget():
    pass
def checkCards():
    pass
def checkMinions():
    pass

while True:
    break
time.sleep(5)
playCard()
