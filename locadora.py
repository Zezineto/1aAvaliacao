from cliente import printCli, addCli, percorrer, Cliente, Aluguel, alugar, lista_alugueis, consulta_cliente
from veiculo import Veículo, Carro, printCar, addCar, print_carros_disponiveis

class App:
    pass

idenx = 0
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
        print('Carros disponíveis para alugar:')
        print_carros_disponiveis()
        placa_para_aluguel = input('Digite a placa que deseja alugar: ')
        id_cliente = int(input('Digite o id do cliente que deseja alugar:'))
        cliente = consulta_cliente(id_cliente)
        dataini = input('Digite a data do aluguel: ')
        dataf = input('Digite a data de devolução: ')
        aluguel = alugar(placa_para_aluguel,cliente,dataini,dataf)
        lista_alugueis.append(aluguel)
    elif opc == 2:
        print('opc 2')
    elif opc == 3:
        nomex = input('Digite o nome do cliente: ')
        idenx+=1
        print('id do novo cliente: ',idenx,'\n')
        addCli(nomex,idenx)
    elif opc == 4:
        marcax = input('Digite a marca do veículo: ')
        modelox = input('Digite o modelo do veículo: ')
        anox = int(input('Digite o ano do modelo: '))
        alux = 1
        addCar(marcax,modelox,anox,alux)
    elif opc == 5:
        print('Lista de Clientes:\n')
        printCli()
    elif opc == 6:
        print('Como deseja ver a lista de veículos?')
        print('1-Ordenada por marca\n2-Ordernada por modelo\n3-Ordenada por ano\n4-Mostrar veículos disponíveis')
        opcc = int(input('Digite a opção desejada: '))
        print('\nVeículos:\n')
        printCar(opcc)
    else:
        print('Opção invalida.')
        break

    menu()
    opc = int(input('Digite a opção: '))
    
print('Programa fechado.')
