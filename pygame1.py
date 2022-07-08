import random
import math

class Personagem:
    def __init__(self, nome, lvl, pv, atk, pd, pexp, pocoes):
        self.nome = nome
        self.lvl = int(lvl)
        self.pv = int(pv)
        self.atk = int(atk)
        self.pd = int(pd)
        self.pexp = int(pexp)
        self.pocoes = int(pocoes)
    def subir_nivel(self):
        self.lvl += 1
        self.pv += 5
        self.atk += 2
        self.pd += 1
        self.pexp = 0
    def ganhar_vida(self, cura):
        self.pv += cura
    def receber_dano(self, dano):
        recebido = int(math.fabs(dano-self.pd))
        self.pv -= recebido
        print('Você recebeu {} de dano.\n'.format(recebido))
    def ganhar_experiencia(self, valor):
        self.pexp += valor

class Enemy:
    def __init__(self, personagem):
        self.lvl = personagem.lvl
        self.pv = self.lvl*4+random.randint(0,3*self.lvl)
        self.atk = self.lvl*2+random.randint(0,self.lvl)
        self.pd = self.lvl
    def receber_dano(self, dano):
        recebido = int(math.fabs(dano-self.pd))
        self.pv -= recebido
        print('O inimigo recebeu {} de dano.\n'.format(recebido))
        
def criar_personagem(nome):
        with open('save.txt','r+') as f:
                f.write(nome+'\n')
                f.write('1\n')
                f.write('10\n')
                f.write('5\n')
                f.write('2\n')
                f.write('0\n')
                f.write('1\n')
        return Personagem(nome,1,10,5,2,0,1)
      
def rolar_dados(personagem):
                table = [0]*12 #Daqui
                for i in range(0,12):
                    table[i] = random.randint(0,1)
                table[random.randint(0,11)] = 2 #Até aqui: definir uma função pra organizar o tabuleiro
                table[random.randint(0,11)] = 2 #Até aqui: definir uma função pra organizar o tabuleiro
                table[random.randint(0,11)] = 2 #Até aqui: definir uma função pra organizar o tabuleiro
                print(table)
                resultado = random.randint(0,11)
                print(resultado)
                if table[resultado] == 1:
                    enemy = Enemy(personagem)
                    batalhar(personagem, enemy)
                elif table[resultado] == 2:
                    personagem.pocoes += 1
                    print('\nVocê encontrou uma poção')
			
def batalhar(personagem, enemy):
    print('\nVocê encontrou um inimigo de nível {} com {}PV. O que vai fazer? '.format(enemy.lvl, enemy.pv))
    while True:
        print('\nSEUS PV: {}\n(1) - ATACAR!\n'.format(personagem.pv))
        ans = input('Qual sua ação nesse turno? ')
        while ans != '1':
            ans = input('Digite uma opção válida: ')
        match ans:
            case '1':
                dado1 = random.randint(1,6)
                print('\nVocê tirou {} no dado'.format(dado1))
                dado2 = random.randint(1,6)
                enemy.receber_dano(dado1)
                if enemy.pv >0:
                    personagem.receber_dano(dado2)
        if enemy.pv <= 0:
            expg = enemy.lvl*3
            print('Seu inimigo foi derrotado. Você ganhou {} pontos de experiencia'.format(expg))
            personagem.ganhar_experiencia(expg)
            break
        if personagem.pv <= 0:
            break
            
def usar_item(personagem):
        if personagem.pocoes > 0:
            personagem.ganhar_vida(5)
            personagem.pocoes -=1
        else:
            print('\nVocê não tem mais poções')
            
def descansar(personagem):
        personagem.ganhar_vida(2)
	
def salvar(personagem):
        with open('save.txt', 'w', encoding = 'utf-8') as f:
		f.write(personagem.nome + '\n')
		f.write(str(personagem.lvl) + '\n')
		f.write(str(personagem.pv) + '\n')
		f.write(str(personagem.atk) + '\n')
		f.write(str(personagem.pd) + '\n')
		f.write(str(personagem.pexp) + '\n')
		f.write(str(personagem.pocoes) + '\n')
	print('\nPERSONAGEM SALVO (y)')

def novo_jogo(): #Precisa melhorar para limitar o número de saves
                personagem = criar_personagem(input('NOME DO PERSONAGEM: '))
                main(personagem)

def carregar():
        with open('save.txt', encoding = 'utf-8') as f:
                aux = []
                for i in f:
                    aux.append(i[:len(i)-1])
                main(Personagem(*aux))
                
def main(personagem):        
        pers = personagem
        print('NOME: {}\nNÍVEL: {}\nPV: {}\nP.ATK: {}\nP.DF: {}\nEXP: {}\nPOCOES: {}\n'.format(pers.nome, pers.lvl, pers.pv, pers.atk, pers.pd, pers.pexp, pers.pocoes))
        while True:
                if pers.pv <= 0:
                    print('FIM DE JOGO')
                    break
                if pers.pexp >= 10:
                    print('\nPARABÉNS! VOCÊ SUBIU DE NÍVEL')
                    print('NOVOS ATRIBUTOS:')
                    aux = [pers.lvl, pers.pv, pers.atk, pers.pd]
                    pers.subir_nivel()
                    aux2 = [pers.lvl, pers.pv, pers.atk, pers.pd]
                    for i in range(0,4):
                        print('{}=>{}'.format(aux[i],aux2[i]))
                    pers.ganhar_vida(6)
                print('\nPV: {}   EXP: {}   POCOES: {}'.format(pers.pv, pers.pexp, pers.pocoes))
                print('\n(1)ROLAR DADOS\n(2)USAR ITEM\n(3)DESCANSAR\n(4)SALVAR\n(5)SAIR\n')
                ans2 = input('O que deseja fazer? ')
                match ans2:
                        case '1':
                                rolar_dados(personagem)
                        case '2':
                                usar_item(personagem)
                        case '3':
                                descansar(personagem)
                        case '4':
                                salvar(personagem)
                        case '5':
                                break
                        case _:
                                print('Opção inválida')
                                
print("(1) - INICIAR NOVO JOGO\n(2) - CONTINUAR\n(3) - SAIR\n")
ans = input('Escolha a opção: ')
while ans != '1' and ans != '2' and ans != '3':
	ans = input('Você deve escolher um dos números: ')
match ans:
        case '1':
                novo_jogo()
        case '2':
                carregar()
        case '3':
                pass
