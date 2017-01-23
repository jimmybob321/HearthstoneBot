import time,pyautogui
width, height = pyautogui.size()

def playCard(cardx):
    #850 is center of hand
    pyautogui.moveTo(850, 925, duration=0.25)
    pyautogui.dragRel(0,-450,duration=1.5)

def passTurn():
    #passes turn
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

def checkCards(img):
    #return cardx

    pass

def checkMinions():
    pass

def emote():
    #emotes so it looks like a real peron
    pyautogui.moveTo(850, 800, duration=0.25)
    pyautogui.click()
    pyautogui.moveTo(725, 800, duration=0.25)
    pyautogui.click()

while True:
    time.sleep(2)
    state = pyautogui.screenshot()
    cardx = checkCards(state)
    while cardx!= 0:
        playCard(cardx)
        cardx = checkCards(state)
    passTurn()

    break

playCard(850)
