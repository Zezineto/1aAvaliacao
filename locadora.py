from cliente import printCli, addCli, Cliente, Aluguel
from veiculo import Veículo, Carro, printVe
class App:
    pass

def menu():
   print("Bem Vindo a Locadora")
   print("1-Alugar")
   print("2-Devolver")
   print("3-Cadastrar cliente")
   print("4-Cadastrar veículos")
   print("5-Consultar clientes")
   print("6-Consultar veículos")
   print("7-Sair")

menu()
opc = int(input('Digite a opção: '))
while opc != 7:
    if opc == 1:
        print('opc 1')
    elif opc == 2:
        print('opc 2')
    elif opc == 3:
        nomex = str(input('Digite o nome do cliente: '))
        idenx = int(input('Digite o id do cliente: '))
        addCli(nomex,idenx)
    elif opc == 4:
        print('opc 4')
    elif opc == 5:
        print('Lista de Clientes:\n')
        printCli()
    elif opc == 6:
        print('Como deseja ver a lista de veículos?')
        print('1-Ordenada por marca\n2-Ordernada por modelo\n3-Ordenada por ano\n4-Mostrar veículos disponíveis')
        opcc = int(input('Digite a opção desejada: '))
        print('\nVeículos:\n')
        printVe(opcc)
    else:
        print('Opção invalida.')

    menu()
    opc = int(input('Digite a opção: '))
    
print('Programa fechado.')
#exit()
