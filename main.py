import win32api
import win32con
import time
from os import system
from ctypes import windll, c_uint
from pyautogui import click

class Weapon:
    def __init__(self):
        self.val_x = [[0 for y in range(40)] for x in range(3)]
        self.val_y = [[0 for y in range(40)] for x in range(3)]
        self.id = -1
        self.ROF = 1000 #Rate of Fire - time between each shot in MS - lower = faster
        self.name = "Gun"


PickedGuns = [Weapon(), Weapon(), Weapon()]
AvailableGuns = list()

# globals
stance = 0
cur_eqp_gun = 0
cur_shot = 0
elapsed = 0
gun_att = [[False for i in range(5)] for j in range(2)]
scope_type = [1, 1, 1]
att_mod = [0, 0, 0]
cur_gun_id = [12, 1, 22]
custom_y_val = [0, 0, 0]
isAutoFire = [False, False, False]
isOn = False
isMapOpen = False
isInventoryOpen = False
isMenuOpen = False

def GetTotalYVal():
    global PickedGuns, cur_shot, cur_eqp_gun, att_mod, custom_y_val, stance
    #print cur_shot, cur_eqp_gun, att_mod, custom_y_val, stance

    debug = PickedGuns[cur_eqp_gun].val_y[cur_shot]
    debug2 = debug[cur_shot]

    ret = debug2
    ret = ret - (4*stance)
    ret -= att_mod[cur_eqp_gun]
    ret += custom_y_val[cur_eqp_gun]
    ret *= scope_type[cur_eqp_gun]
    return ret

def IsRunning():
    global isMapOpen, isMenuOpen, isInventoryOpen, isOn
    if isMapOpen:
        return False
    if isMenuOpen:
        return False
    if isInventoryOpen:
        return False
    return isOn
def b2s(b):
    if b:
        return "True"
    return "False"
def ListKeys():
  print "F1: Change AR\n" \
        "F2: Change SMG\n" \
        "F3: Change Sniper\n" \
        "F4: Change Pistol\n" \
        "0: Remove Attachments\n" \
        "1: Change Grip\n" \
        "2: Add\Remove Stock\n" \
        "3: Add\Remove Compensator\n" \
        "4: Change Scope\n" \
        "6: Reset All Paramters\n"
def Status():
    global isOn, isMenuOpen, isMapOpen, isInventoryOpen, cur_eqp_gun, att_mod, cur_shot, PickedGuns
    system('cls')       # clear screen
    i = cur_eqp_gun
    print "Overall:", b2s(IsRunning()), "\n" \
          "test"\
          "Status:", b2s(isOn), "\n"\
          "		Map:", b2s(isMapOpen), "\n" \
          "		Menu:", b2s(isMenuOpen), "\n" \
          "		Inventory:", b2s(isInventoryOpen), "\n\n"\
          "Weapon Stats:\n"\
          "     Slot:", (i+1), "\n"\
          "     Name:", PickedGuns[i].name, "\n"\
          "     Attachments:", "TBA", "\n"\
          "     Recoil Value: ", GetTotalYVal(), "\n"
    ListKeys()

def move_mouse(y):
    #print ("Moving mouse by: [%d]" %(y))
    windll.user32.mouse_event(c_uint(0x0001), c_uint(0), c_uint(y), c_uint(0), c_uint(0))
def IsKeyDown(key):
    return win32api.GetAsyncKeyState(key)

def initARs():
    global AvailableGuns
    AvailableGuns[0].name = "AK47"
    AvailableGuns[0].ROF = 100
    AvailableGuns[0].val_y[0] = [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 28, 28, 28, 28, 29,
                                 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29,
                                 29, 29, 29, 29, 29, 29, 29, 29, 29, 29]
    AvailableGuns[1].name = "Groza"
    AvailableGuns[1].ROF = 80
    AvailableGuns[1].val_y[0] = [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 28, 28, 28, 28, 29,
                                 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29,
                                 29, 29, 29, 29, 29, 29, 29, 29, 29, 29]
    AvailableGuns[2].name = "M16"
    AvailableGuns[2].ROF = 75
    AvailableGuns[2].val_y[0] = [25, 25, 25, 29, 33, 33, 32, 33, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
                                 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
    AvailableGuns[3].name = "Scar-L"
    AvailableGuns[3].ROF = 96
    AvailableGuns[3].val_y[0] = [20, 21, 22, 21, 22, 22, 23, 22, 23, 23, 24, 24, 25, 25, 25, 25, 26, 27, 28, 29, 30, 32,
                                 34, 34, 35, 34, 35, 34, 35, 34, 35, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35,
                                 35, 35]
    AvailableGuns[4].name = "M416"
    AvailableGuns[4].ROF = 86
    AvailableGuns[4].val_y[0] = [21, 21, 21, 21, 21, 21, 21, 21, 21, 23, 23, 24, 23, 24, 25, 25, 26, 27, 27, 32, 31, 31,
                                 31, 31, 31, 31, 31, 32, 32, 32, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35]
    AvailableGuns[5].name = "AUG"
    AvailableGuns[5].ROF = 86
    AvailableGuns[5].val_y[0] = [21, 21, 21, 21, 21, 21, 21, 21, 21, 23, 23, 24, 23, 24, 25, 25, 26, 27, 27, 32, 31, 31,
                                 31, 31, 31, 31, 31, 32, 32, 32, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35]
    AvailableGuns[6].name = "MG"
    AvailableGuns[6].ROF = 75
    AvailableGuns[6].val_y[0] = [29, 21, 21, 21, 21, 21, 21, 21, 21, 23, 23, 24, 23, 24, 25, 25, 26, 27, 27, 32, 31, 31,
                                 31, 31, 31, 31, 31, 32, 32, 32, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35]
def initSMGs():
    global AvailableGuns
    AvailableGuns[7].name = "UMP"
    AvailableGuns[7].ROF = 92
    AvailableGuns[7].val_y[0] = [18, 19, 18, 19, 18, 19, 19, 21, 23, 24, 23, 24, 23, 24, 23, 24, 23, 24, 23, 24, 23, 24,
                                 24, 25, 24, 25, 24, 25, 24, 25, 24, 25, 25, 26, 25, 26, 25, 26, 25, 26]
    AvailableGuns[8].name = "Uzi"
    AvailableGuns[8].ROF = 48
    AvailableGuns[8].val_y[0] = [16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 28, 30, 32, 34, 34, 34, 34, 34, 34, 34, 34, 34,
                                 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34]
    AvailableGuns[9].name = "Vector"
    AvailableGuns[9].ROF = 55
    AvailableGuns[9].val_y[0] = [16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 28, 30, 32, 34, 34, 34, 34, 34, 34, 34, 34, 34,
                                 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34]
    AvailableGuns[10].name = "Thompson"
    AvailableGuns[10].ROF = 92
    AvailableGuns[10].val_y[0] = [16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 28, 30, 32, 34, 34, 34, 34, 34, 34, 34, 34, 34,
                                  34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34];
def initSRs():
    global AvailableGuns
    AvailableGuns[11].name = "VSS"
    AvailableGuns[11].ROF = 86
    AvailableGuns[11].val_y[0] = [18, 19, 18, 19, 18, 19, 19, 21, 23, 24, 23, 24, 23, 24, 23, 24, 23, 24, 23, 24]
    AvailableGuns[12].name = "Mini14"
    AvailableGuns[12].ROF = 100
    AvailableGuns[12].val_y[0] = [25, 25, 25, 29, 33, 33, 32, 33, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
                                  30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
    AvailableGuns[13].name = "SKS"
    AvailableGuns[13].ROF = 90
    AvailableGuns[13].val_y[0] = [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 28, 28, 28, 28,
                                  29, 29, 29, 29, 29]
    AvailableGuns[14].name = "Mk14"
    AvailableGuns[14].ROF = 90
    AvailableGuns[14].val_y[0] = [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 28, 28, 28, 28,
                                  29, 29, 29, 29, 29]
def initPistols():
    global AvailableGuns
    AvailableGuns[15].name = "Glock"
    AvailableGuns[15].ROF = 86
    AvailableGuns[15].val_y[0] = [18, 19, 18, 19, 18, 19, 19, 21, 23, 24, 23, 24, 23, 24, 23, 24, 23, 24, 23, 24, 23,
                                  24, 24, 25, 24]
    AvailableGuns[16].name = "P92"
    AvailableGuns[16].ROF = 135
    AvailableGuns[16].val_y[0] = [18, 19, 18, 19, 18, 19, 19, 21, 23, 24, 23, 24, 23, 24, 23, 24, 23, 24, 23, 24]
    AvailableGuns[17].name = "P1911"
    AvailableGuns[17].ROF = 110
    AvailableGuns[17].val_y[0] = [16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 28, 30]

def init():
    global AvailableGuns
    for x in range(0, 18):
        AvailableGuns.append(Weapon())
        AvailableGuns[x].id = x
    initARs()

def RemoveAttachments():
    global cur_eqp_gun, att_mod, scope_type, gun_att1111
    i = cur_eqp_gun
    for x in range(0, 2):
        gun_att[i][x] = False
    att_mod[i] = 0
    scope_type[i] = 1
def ResetToDefault():
    global cur_gun_id, cur_eqp_gun, isOn
    cur_gun_id = [12, 1, 22]
    cur_eqp_gun = 2
    RemoveAttachments()
    cur_eqp_gun = 1
    RemoveAttachments()
    isOn = False
def ChangeGrip():
    global cur_eqp_gun, gun_att, att_mod
    i = cur_eqp_gun
    if gun_att[i][0]:
        gun_att[i][0] = False
        gun_att[i][1] = True
        att_mod[i] -= 3
    elif gun_att[i][1]:
        gun_att[i][1] = False
        att_mod[i] -= 3
    else:
        gun_att[i][0] = True
        att_mod[i] += 6
def ChangeStock():
    global cur_eqp_gun, gun_att
    i = cur_eqp_gun
    gun_att[i][2] = not gun_att[i][2]
    if gun_att[i][2]:
        att_mod[i] += 2
    else:
        att_mod[i] -= 2
def ChangeBarrel():
    global cur_eqp_gun, gun_att
    i = cur_eqp_gun
    gun_att[i][3] = not gun_att[i][3]
    if gun_att[i][3]:
        att_mod[i] += 6
    else:
        att_mod[i] -= 6
def ChangeScope():
    global cur_eqp_gun, scope_type
    i = cur_eqp_gun
    if scope_type[i] == 1:
        scope_type[i] = 2
    elif scope_type[i] == 2:
        scope_type[i] = 4
    elif scope_type[i] == 4:
        scope_type[i] = 8
    elif scope_type[i] == 8:
        scope_type[i] = 15
    else:
        scope_type[i] = 1

def SwitchAR():
    global cur_gun_id, PickedGuns, AvailableGuns
    i = cur_eqp_gun
    if i > 1:
        return
    cur_gun_id[i] += 1
    if (cur_gun_id > 6):
        cur_gun_id = 0
    PickedGuns[i] = AvailableGuns[cur_gun_id]

def SwitchSMG():
    print("ADD ME :(")
def SwitchSR():
    print("ADD ME :(")
def SwitchPistol():
    print("ADD ME :(")

def main():
    global isOn, isMapOpen, isMenuOpen, isInventoryOpen, cur_eqp_gun, cur_shot, elapsed, stance
    init()
    PickedGuns[0] = AvailableGuns[0]
    PickedGuns[1] = AvailableGuns[1]
    PickedGuns[2] = AvailableGuns[2]
    while True:
        elapsed += 1
        CEG = cur_eqp_gun
        # Check button press
        if IsKeyDown(49):
            isOn = True
            isMapOpen = False
            isMenuOpen = False
            isInventoryOpen = False
            cur_eqp_gun = 0
            time.sleep(0.2)
        elif IsKeyDown(50):
            isOn = True
            isMapOpen = False
            isMenuOpen = False
            isInventoryOpen = False
            cur_eqp_gun = 1
            time.sleep(0.2)
        elif IsKeyDown(51):
            isOn = True
            isMapOpen = False
            isMenuOpen = False
            isInventoryOpen = False
            cur_eqp_gun = 2
            time.sleep(0.2)
        elif IsKeyDown(52):
            isOn = False
            time.sleep(0.2)
        elif IsKeyDown(53):
            isOn = False
            time.sleep(0.2)
        elif IsKeyDown(54):
            ResetToDefault()
            time.sleep(0.2)

        if IsKeyDown(107):
            custom_y_val[CEG] += 1
            time.sleep(0.2)
        elif IsKeyDown(109):
            custom_y_val[CEG] -= 1
            time.sleep(0.2)
        elif IsKeyDown(112):
            SwitchAR()
            time.sleep(0.2)
        elif IsKeyDown(113):
            SwitchSMG()
            time.sleep(0.2)
        elif IsKeyDown(114):
            SwitchSR()
            time.sleep(0.2)
        elif IsKeyDown(115):
            SwitchPistol()
            time.sleep(0.2)
        elif IsKeyDown(96):
            RemoveAttachments()
            time.sleep(0.2)
        elif IsKeyDown(97):
            ChangeGrip()
            time.sleep(0.2)
        elif IsKeyDown(98):
            ChangeStock()
            time.sleep(0.2)
        elif IsKeyDown(99):
            ChangeBarrel()
            time.sleep(0.2)
        elif IsKeyDown(100):
            ChangeScope()
            time.sleep(0.2)

        if IsKeyDown(77):
            isMapOpen = not isMapOpen
            time.sleep(0.2)
        elif IsKeyDown(9):
            isInventoryOpen = not isInventoryOpen
            time.sleep(0.2)
        elif IsKeyDown(27):
            b = True
            if isInventoryOpen:
                isInventoryOpen = False
                b = False
            if isMapOpen:
                isMapOpen = False
                b = False
            if b:
                isMenuOpen = not isMenuOpen
            time.sleep(0.2)

        if IsKeyDown(86):
            isAutoFire[CEG] = not isAutoFire[CEG]
            time.sleep(0.2)

        if IsKeyDown(32):
            stance = 0
        elif IsKeyDown(67):
            if stance == 1:
                stance = 0
            else:
                stance = 1
            time.sleep(0.2)
        elif (IsKeyDown(90)):
            if stance == 2:
                stance = 0
            else:
                stance = 2
            time.sleep(0.2)

        # While Mouse1 is pressed
        if IsKeyDown(1) and IsRunning():
            time2wait = PickedGuns[CEG].ROF / (1000*1.0)
            time.sleep(time2wait)
            if cur_shot > 39:
                cur_shot = 0
            y = GetTotalYVal()
            move_mouse(y)
            if isAutoFire[CEG]:
                click()
            cur_shot += 1  # Increase count by 1
            elapsed = 0
            Status()
            continue
        else:
            cur_shot = 0  # Resets counter
        if elapsed > 100:
            elapsed = 0
            Status()
        time.sleep(0.01)


main()
