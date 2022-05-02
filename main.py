from time import sleep
import numpy as np 
import cv2 as cv
import pyautogui as auto

auto.PAUSE = 2.5

def verificarImagem(imagem):
    img = auto.locateOnScreen(imagem, confidence=0.9, grayscale=True)
    if(img == None):
        return False
    else:
        return True

def moverClicar(imagem, tempo):
    i = 1
    while(i <= 5):
        if(verificarImagem(imagem)): 
            i = 6
            auto.moveTo(auto.locateOnScreen(imagem, confidence=0.9, grayscale=True), duration = tempo)
            auto.click()
        else:
            i = i+1
            print('Encontrando imagem na tela: ',imagem)
            sleep(3)

def rolarHeroes():
    auto.moveTo(250, 600, duration=1)
    auto.mouseDown()
    auto.moveTo(250, 350, duration=1.5)
    auto.mouseUp()

def carregarHerois():
    moverClicar('img/back.png',1)
    moverClicar('img/treasure_hunt.png',1)

def logarConta():
    if(verificarImagem('img/connect.png')):
        moverClicar('img/connect.png', 1)
    if(verificarImagem('img/login.png')):        
        moverClicar('img/login.png',1)

while True:
    logarConta()
    moverClicar('img/treasure_hunt.png',1)
    moverClicar('img/back.png',1)
    moverClicar('img/heroes.png',1)
    moverClicar('img/all.png',1)
    moverClicar('img/close.png',1)
    moverClicar('img/treasure_hunt.png',1)
    for i in range(5):
        sleep(600)
        logarConta()
        carregarHerois()
        