import hajiIsyakSelect as hs
import pyautogui as pag
import sys

def mondayToSundayExceptFriday():
    hs.hajiSubuh()
    hs.hajiIsyak()
    hs.hajiMaghrib()
    hs.hajiAsar()
    hs.hajiZohor()
    stopRec()


def friday():
    hs.hajiSubuh()
    hs.hajiIsyak()
    hs.hajiMaghrib()
    hs.hajiAsar()
    stopRec()

def stopRec():
    pag.moveTo(869, 13, 0.1)
    pag.click()
    sys.exit()
