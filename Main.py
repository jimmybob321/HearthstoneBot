import time,pyautogui
width, height = pyautogui.size()

def playCard(cardx,cardy):
    #850,925 is center of hand
    pyautogui.moveTo(cardx, cardy, duration=0.25)
    pyautogui.dragRel(0,-450,duration=1.5)

def passTurn(turn):
    #passes turn
    pyautogui.moveTo(2725,975,duration=0.25)
    pyautogui.click()
    turn = False
    return turn
def goFace():
    pass

def hitTaunt():
    pass

def startGame():
    pyautogui.moveTo(2450, 1675, duration=0.25)
    pyautogui.click()

def think():
    time.sleep(2)

def checkTurn(turn,state):
    if state.getpixel(positionx, positiony) == (111, 111, 111) or state.getpixel(positionx, positiony) == (111, 111, 111):
        turn = True
    return turn

def detectTarget():
    pass

def checkCards(img,numCards):
    #return number of cards in hand and the position of the card to play
    positions  =["850-925","850-925 850-925","850-925 850-925","850-925 850-925","850-925 850-925","850-925 850-925","850-925 850-925","850-925 850-925","850-925 850-925","850-925 850-925","850-925 850-925"]
    positions2 = positions[x].split(" ")
    count = 0
    for x in range(0,numCards):
        a = positions2.split("-")
        positionX = a[0]
        positionY = a[1]
        if state.getpixel(positionx, positiony) ==(111,111,111):
            if count == 0:
                cardx = positionx
                cardy = positiony
            count +=1

    return count,cardx,cardy

def checkMinions():
    pass

def emote():
    #emotes so it looks like a real peron
    pyautogui.moveTo(850, 800, duration=0.25)
    pyautogui.click()
    pyautogui.moveTo(725, 800, duration=0.25)
    pyautogui.click()

cards = 3
turn = False
while True:
    time.sleep(2)
    state = pyautogui.screenshot()
    turn = checkturn(turn,state)
    think()
    state = pyautogui.screenshot()
    if turn:
        count,cardx,cardy = checkCards(state,cards)
        while count!= 0:
            playCard(cardx,cardy)
            cards -=1

            count,cardx,cardy = checkCards(state)
            think()

        turn = passTurn(turn)

    break


