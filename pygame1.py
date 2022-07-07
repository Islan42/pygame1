import random

class Personagem:
    def __init__(self, nome, lvl, pv, atk, pd, pexp):
        self.nome = nome
        self.lvl = lvl
        self.pv = pv
        self.atk = atk
        self.pd = pd
        self.pexp = pexp
    def _subir_nivel(self):
        self.lvl += 1
        self.pv += 5
        self.atk += 2
        self.pd += 1
    def _ganhar_vida(self, cura):
        self.pv += cura
    def _receber_dano(self, dano):
        self.pv -= dano+self.pd
def criar_personagem(nome):
        with open('save.txt','r+') as f:
                f.write(nome+'\n')
                f.write('1\n')
                f.write('10\n')
                f.write('5\n')
                f.write('2\n')
                f.write('0\n')
        return Personagem(nome,1,10,5,2,0)
      
def batalhar():
    pass
def usar_item():
        pass
def descansar():
        pass
def salvar():
        pass
def novo_jogo(): #Precisa melhorar para limitar o número de saves
                personagem = criar_personagem(input('NOME DO PERSONAGEM: '))
                main(personagem)

def carregar():
        with open('save.txt') as f:
                aux = []
                for i in f:
                    aux.append(i[:len(i)-1])
                personagem = Personagem(*aux)
                main(personagem)
                
def main(personagem):
        def rolar_dados():
                nonlocal pocoes
                table = [0]*12 #Daqui
                for i in range(0,12):
                    table[i] = random.randint(0,1)
                table[random.randint(0,11)] = 2 #Até aqui: definir uma função pra organizar o tabuleiro
                print(table)
                resultado = random.randint(0,11)
                print(resultado)
                if table[resultado] == 1:
                    batalhar()
                elif table[resultado] == 2:
                    pocoes += 1
                    
        pers = personagem
        print('{}\n{}\n{}\n{}\n{}\n'.format(pers.nome, pers.lvl, pers.pv, pers.atk, pers.pd))
        pocoes = 0
        while True:
                print(pocoes)
                print('\n(1)ROLAR DADOS\n(2)USAR ITEM\n(3)DESCANSAR\n(4)SALVAR\n(5)SAIR\n')
                ans2 = input('O que deseja fazer? ')
                match ans2:
                        case '1':
                                rolar_dados()
                        case '2':
                                usar_item()
                        case '3':
                                descansar()
                        case '4':
                                salvar()
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
