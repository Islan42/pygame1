def criar_personagem(nome,lvl,pv,atk):
        with open('save.txt','r+') as f:
                f.write(nome+'\n')
                f.write(lvl+'\n')
                f.write(pv+'\n')
                f.write(atk+'\n'*2)
def main():
        while True:
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
                print(ans2)
def rolar_dados():
        pass
def usar_item():
        pass
def descansar():
        pass
def salvar():
        pass
def novo_jogo(): #Precisa melhorar para limitar o número de saves
                criar_personagem(input('NOME DO PERSONAGEM: '),'1','10','5')
                main()

def carregar():
        with open('save.txt') as f:
                print('NOME: '+ f.readline()+'NIVEL: '+ f.readline()+'PV: '+f.readline()+'ATK: '+ f.readline())
                main()
                
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
"""
print(ans)

"""
