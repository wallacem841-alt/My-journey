import pyautogui
import time

# screen dimentions 1366 x 768

nikke_advise = 10

rookie_token = 5

special_token = 2

pyautogui.PAUSE = 2

clicktime = 1
Anitime = 3
loadscreen = 12

time.sleep(clicktime)
# clicks in the game from the outside
pyautogui.click(x=413, y=750)

def Outpoast_rewards():
    #Outpoast rewards
    time.sleep(clicktime)
    # clicks the outpoast defense
    pyautogui.click(x=403, y=632)
    time.sleep(clicktime)
    #clicks claim
    pyautogui.click(x=768, y=646)
    time.sleep(Anitime)
    # clicks to get out
    pyautogui.click(x=768, y=646)
    time.sleep(Anitime)
    # clicks to get out
    pyautogui.click(x=768, y=646)
    time.sleep(Anitime)

def wipe_out():
    #wipe out
    time.sleep(clicktime)
    # clicks the outpoast defense
    pyautogui.click(x=403, y=632)
    # clicks wipe
    time.sleep(clicktime)
    pyautogui.click(x=599, y=633)
    # confirms wipe
    time.sleep(Anitime)
    pyautogui.click(x=753, y=588)
    # clicks to get out
    time.sleep(Anitime)
    pyautogui.click(x=179, y=526)
    # clicks to get out
    time.sleep(Anitime)
    pyautogui.click(x=179, y=526)
    # clicks to get out
    time.sleep(Anitime)
    pyautogui.click(x=179, y=526)

def store_interaction1():
    #First store interaction
    # Click store
    time.sleep(clicktime)
    pyautogui.click(x=408, y=478)
    # clicks ordinary package
    time.sleep(loadscreen)
    pyautogui.click(x=103, y=164)
    # click daily
    time.sleep(Anitime)
    pyautogui.click(x=260, y=225)
    #click package
    time.sleep(Anitime)
    pyautogui.click(x=86, y=379)
    #click away
    time.sleep(Anitime)
    pyautogui.click(x=236, y=624)
    #back to menu
    time.sleep(Anitime)
    pyautogui.press('esc')
    pyautogui.press('esc')

def store_interaction2():
    #Second store interaction
    # Click store
    time.sleep(loadscreen)
    pyautogui.click(x=403, y=527)
    #click free purchess
    time.sleep(loadscreen)
    pyautogui.click(x=150, y=458)
    #confirm free purchess
    time.sleep(clicktime)
    pyautogui.click(x=757, y=661)
    # click away
    time.sleep(Anitime)
    pyautogui.click(x=365, y=676)
    #reset store
    time.sleep(Anitime)
    pyautogui.click(x=203, y=351)
    # confirm reset
    time.sleep(Anitime)
    pyautogui.click(x=786, y=481)
    # click away
    time.sleep(Anitime)
    pyautogui.click(x=365, y=676)
    #click free purchess
    time.sleep(Anitime)
    pyautogui.click(x=150, y=458)
    #confirm free purchess
    time.sleep(clicktime)
    pyautogui.click(x=757, y=661)
    # click away
    time.sleep(Anitime)
    pyautogui.click(x=365, y=676)
    #back to menu
    time.sleep(clicktime)
    pyautogui.press('esc')
    pyautogui.press('esc')

def friends_list():
    #friends list
    #click friends list
    time.sleep(loadscreen)
    pyautogui.click(x=1327, y=184)
    # click send-receive
    time.sleep(Anitime)
    pyautogui.click(x=804, y=656)
    # clicks to get out
    time.sleep(Anitime)
    pyautogui.click(x=179, y=526)
    # clicks to get out
    time.sleep(Anitime)
    pyautogui.click(x=179, y=526)
    # clicks to get out
    time.sleep(Anitime)
    pyautogui.click(x=179, y=526)

def outpoast():
    # outpoast
    # click outpoast
    time.sleep(Anitime)
    pyautogui.click(x=442, y=581)
    # click bulleting board
    time.sleep(loadscreen)
    time.sleep(loadscreen)
    pyautogui.click(x=713, y=727)
    # claim all
    time.sleep(Anitime)
    time.sleep(Anitime)
    pyautogui.click(x=806, y=639)
    #esc to get out
    time.sleep(clicktime)
    pyautogui.click(x=1083, y=141)
    pyautogui.press('esc')
    time.sleep(clicktime)
    # click bulleting board
    time.sleep(clicktime)
    pyautogui.click(x=713, y=727)
    #Click options
    time.sleep(clicktime)
    pyautogui.click(x=805, y=271)
    #Click select
    time.sleep(clicktime)
    pyautogui.click(x=760, y=648)
    time.sleep(clicktime)
    pyautogui.click(x=1083, y=141)
    # dispatch
    time.sleep(Anitime)
    pyautogui.click(x=676, y=643)
    # confirm dispatch
    time.sleep(Anitime)
    pyautogui.click(x=743, y=646)
    # exit to menu
    time.sleep(clicktime)
    pyautogui.press('esc')
    time.sleep(clicktime)
    pyautogui.press('esc')
    time.sleep(clicktime)
    pyautogui.press('esc')
    time.sleep(loadscreen)
    time.sleep(Anitime)
    time.sleep(loadscreen)

def advise():
    #click nikke
    time.sleep(Anitime)
    pyautogui.click(x=535, y=703)
    #click advise
    time.sleep(clicktime)
    pyautogui.click(x=1170, y=88)
    #click 1st nikke
    time.sleep(clicktime)
    pyautogui.click(x=311, y=260)
    #starts advise loop
    for _ in range(nikke_advise):
        #clicks advise
        time.sleep(clicktime)
        pyautogui.click(x=776, y=577)
        #confirms click
        time.sleep(clicktime)
        pyautogui.click(x=803, y=479)
        #ensures lv up doesn't interupts the flow
        time.sleep(Anitime)
        pyautogui.click(x=1083, y=141)
        time.sleep(clicktime)
        pyautogui.click(x=1083, y=141)
        time.sleep(clicktime)
        pyautogui.click(x=1083, y=141)
        #clicks next nikke
        time.sleep(clicktime)
        pyautogui.click(x=1343, y=336)
    #exit to menu
    #exit to main manu
    pyautogui.click(x=115, y=725)

def arena():
    #clicks the ark
    time.sleep(Anitime)
    time.sleep(Anitime)
    time.sleep(Anitime)
    pyautogui.click(x=968, y=516)
    #clicks arena
    time.sleep(Anitime)
    time.sleep(Anitime)
    pyautogui.click(x=794, y=496)
    #clicks rookie
    time.sleep(Anitime)
    time.sleep(Anitime)
    pyautogui.click(x=586, y=402)
    #starts rookie loop
    for _ in range(rookie_token):
        #clicks start
        time.sleep(Anitime)
        pyautogui.click(x=814, y=511)
        #confirms start
        time.sleep(clicktime)
        pyautogui.click(x=780, y=629)
        #comes back to rookie menu
        time.sleep(loadscreen)
        time.sleep(loadscreen)
        pyautogui.press('esc')
        time.sleep(loadscreen)
        time.sleep(loadscreen)
    #comes back to arena menu
    pyautogui.press('esc')
    #clicks special
    time.sleep(Anitime)
    pyautogui.click(x=784, y=414)
    #starts special loop
    for _ in range(special_token):
        #clicks start
        time.sleep(Anitime)
        pyautogui.click(x=835, y=586)
        #confirms start
        time.sleep(clicktime)
        pyautogui.click(x=763, y=632)
        #comes back to special menu
        time.sleep(loadscreen)
        time.sleep(loadscreen)
        pyautogui.press('esc')
        time.sleep(loadscreen)
        time.sleep(loadscreen)
    #exit to main manu
    pyautogui.click(x=115, y=725)

def simulation():
    #clicks the ark
    time.sleep(Anitime)
    pyautogui.click(x=968, y=516)
    #clicks simulation room
    time.sleep(clicktime)
    pyautogui.click(x=549, y=385)
    #clicks beguin simulation
    time.sleep(clicktime)
    pyautogui.click(x=684, y=455)
    #config and start
    time.sleep(clicktime)
    pyautogui.click(x=764, y=383)
    time.sleep(clicktime)
    pyautogui.click(x=792, y=464)
    time.sleep(clicktime)
    pyautogui.click(x=678, y=650)
    time.sleep(Anitime)
    time.sleep(Anitime)
    #starts loop
    for _ in range(7):
        pyautogui.click(x=805, y=520)
        time.sleep(Anitime)
        pyautogui.click(x=794, y=653)
        time.sleep(Anitime)
        pyautogui.click(x=620, y=629)
        time.sleep(clicktime)
        pyautogui.click(x=766, y=477)
    

#Run
Outpoast_rewards()

wipe_out()

store_interaction1()

store_interaction2()

friends_list()

outpoast()

advise()

arena()