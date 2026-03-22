from random import randint, choice
from tkinter import *


jogo = input("Digite 1 para começar o jogo: ")

janela = Tk()
janela.title("Truco Diferenciado")
TextoInicial = Label(janela, text="PLACAR")
TextoInicial.grid(column=3, row=3)
label_placar = Label(janela, text="Você: 0 | IA: 0")
label_placar.grid(column=4, row=4)

def mostrar_placar():
    label_placar.config(text=f"Você: {PontosJOGOEU} | IA: {PontosJogoIA}")


numeroIA = []
jogoembaralhando = False
jogorodada = False
cartas = ["A", "2", "3", "4", "5", "6", "7", "J", "Q", "K"]

PontosRodadaEu = 0
PontosRodadaIA = 0

PontosJOGOEU = 0
PontosJogoIA = 0

valores = {
    "4": 1,
    "5": 2,
    "6": 3,
    "7": 4,
    "Q": 5,
    "J": 6,
    "K": 7,
    "A": 8,
    "2": 9,
    "3": 10
}

def conferirResultados(PontosEU,PontosIA) :
    if PontosEU >= 12  or PontosIA >= 12: 
        jogo = "0"
        if PontosEU > PontosIA:
            print("Você ganhou! Digite um para jogar novamente 1: ")
            jogo = input("Digite 1 para começar o jogo: ")
            PontosRodadaEu = 0
            PontosRodadaIA = 0
            PontosJOGOEU = 0
            PontosJogoIA = 0
            jogoembaralhando = False
            jogorodada = False
        else: 
            print("IA ganhou! Digite um para jogar novamente 1: ")
            jogo = input("Digite 1 para começar o jogo: ")
            PontosRodadaEu = 0
            PontosRodadaIA = 0
            PontosJOGOEU = 0
            PontosJogoIA = 0
            jogoembaralhando = False
            jogorodada = False
    else :
        return 
    

def verificarResultados(cartaEU,jogoIA) :
         if valores[cartaEU] > valores [jogoIA]:
            print ("Você ganhou essa rodada! ")
            global PontosRodadaEu
            PontosRodadaEu += 1  
         elif valores[cartaEU] < valores[jogoIA]:
            print ("IA ganhou essa rodada! ")
            global PontosRodadaIA 
            PontosRodadaIA +=1
         else: 
            print ("Empate")
            PontosRodadaIA +=1
            PontosRodadaEu += 1


while jogo == "1":
    conferirResultados(PontosJOGOEU,PontosJogoIA)
    PontosRodadaEu = 0
    PontosRodadaIA = 0
    jogoembaralhando = True
    print("Embaralhando...........")
    if jogoembaralhando: 
        numeroIA1 = choice(cartas)
        numeroIA2 = choice(cartas)
        numeroIA3 = choice(cartas)
        numeroEU1 = choice(cartas)
        numeroEU2 = choice(cartas)
        numeroEU3 = choice(cartas)
        print ("Sua mão: ", numeroEU1,numeroEU2, numeroEU3)
        jogoembaralhando = False
        jogorodada = True
        jogo = "0"

    
    
    if jogorodada: 
        maoEu = [numeroEU1,numeroEU2,numeroEU3]
        jogoIA = choice([numeroIA1,numeroIA2,numeroIA3])
        print("Carta IA ", jogoIA)
        jogoEU = int(input("Escolha sua carta: 0 - 2 " ))
        cartaEU = maoEu[jogoEU]
        maoEu.pop(jogoEU)
        print("Sua Carta ", cartaEU)
        verificarResultados(cartaEU,jogoIA)
        print("Pontos IA: ", PontosRodadaIA)
        print("Seus pontos: ", PontosRodadaEu)
        print("-------------")
        print("Sua mão:", maoEu)
        jogoEU = int(input("Escolha sua carta: 0 - 1 " ))
        cartaEU = maoEu[jogoEU]
        maoEu.pop(jogoEU)
        print("Sua Carta ", cartaEU)
        jogoIA = choice([numeroIA1,numeroIA2,numeroIA3])
        print("Carta IA ", jogoIA)
        verificarResultados(cartaEU,jogoIA)
        print("Pontos IA: ", PontosRodadaIA)
        print("Seus pontos: ", PontosRodadaEu)
        print("-------------")
        if PontosRodadaEu >= 2 or PontosRodadaIA >= 2 :
            if (PontosRodadaEu > PontosRodadaIA):
                print("Você ganhou a Rodada! ")
                PontosJOGOEU += 1
                mostrar_placar()
                jogorodada = False
                jogoembaralhando = True
                jogo = "1"
            else : 
                print("IA ganhou a rodada!")
                PontosJogoIA += 1
                mostrar_placar()
                jogorodada = False
                jogoembaralhando = True
                jogo = "1"
        else : 
            jogoIA = choice([numeroIA1,numeroIA2,numeroIA3])
            print("Carta IA ", jogoIA)
            print("Sua mão:", maoEu)
            jogoEU = int(input("Escolha sua carta: 0 " ))
            cartaEU = maoEu[jogoEU]
            maoEu.pop(jogoEU)
            print("Sua Carta ", cartaEU)
            verificarResultados(cartaEU,jogoIA)
            mostrar_placar()
            jogoembaralhando = True
            jogorodada = False
            jogo = "1"


janela.mainloop()




        





