from cliente import Aluguel
import cliente
from veiculo import ALUGADO, DISPONIVEL
import veiculo
from datetime import date
import datetime

#Class App sera usado para definir todas as funções do código que envolvam listas
#(que basicamente são todas elas :p)
class App:
    def printCar(opcc):
        if opcc == 1:
            listaCar.sort(key=lambda x: x.marca)
            print(listaCar,'\n')
        elif opcc == 2:
            listaCar.sort(key=lambda x: x.modelo)
            print(listaCar,'\n')
        elif opcc == 3:
            listaCar.sort(key=lambda x: x.ano, reverse=True)
            print(listaCar,'\n')
        elif opcc == 4:
            for num in listaCar:
                if(num.alu==1):
                    print(num)
        
    def print_carros_disponiveis():
        for num in listaCar:
            if(num.alu==1):
                print(f'Placa: {num.placa}, Carro: {num.marca} {num.modelo} {num.ano},\nPreço: {num.valorDia}R$\
, Quilometragem: {num.quilometragem}km\n')
        #print('Nenhum.') Como q printa isso sem printar 3 vezes?

    def carro_por_placa(placa):
        for carro in listaCar:
            if(carro.placa==placa):
                return carro

    def addCar(marcax,modelox,anox,alux,placax,quilox,valorx):
        carx = veiculo.Carro(marcax,modelox,anox,alux,placax,quilox,valorx)
        listaCar.append(carx)

        #função para printar a lista de clientes
    def printCli():
        print(listaCli,'\n')

    #função para adicionar clientes a lista
    def addCli(nomex,idenx):
        cx = cliente.Cliente(nomex,idenx)
        listaCli.append(cx)

    def percorrer():
        for num in listaCli:
            if(num.iden == 746):
                print(num.nome,'\n')

    #funções de consulta
    def consulta_preço(placa):
        for carro in listaCar:
            if(carro.placa==placa):
                return carro.valorDia

    def consulta_cliente(ident):
        for cli in listaCli:
            if(cli.iden==ident):
                return cli.iden

    def consulta_alugueis(ident):
        for alu in lista_alugueis:
            if(alu.cliente==ident):
                return alu

    def consulta_placa(ident):
        for alu in lista_alugueis:
            if(alu.cliente==ident):
                return alu.placa

    #fução de alugar o carro para um cliente
    def alugar(placa_para_aluguel,idAlu,dataini,dataf):
        cliente = idAlu
        placa = placa_para_aluguel
        valor = App.consulta_preço(placa)
        aluguel_x = Aluguel(cliente,placa,dataini,dataf,valor)
        carro = App.carro_por_placa(placa)
        carro.alu = ALUGADO
        return aluguel_x

    #função que calcula o valor que o cliente deve pagar ao carro ser devolvido
    def devolver(aluguel):
        print('Digite a data a qual o carro foi devolvido: ')
    
        def data_devolução(diaz, mesz, anoz):
            data3 = datetime.date(day = diaz, month = mesz, year = anoz)
            return data3

        diaz = int(input('dia: '))
        mesz = int(input('mes: '))
        anoz = int(input('ano: '))
        data_dev = data_devolução(diaz, mesz, anoz)
    
        if(data_dev>aluguel.dataf):
            dias_extras = (data_dev - aluguel.dataf).days
            valor_adicional = aluguel.preçoc * 0.20
            preço_adicional = dias_extras * valor_adicional
            preço_total = (aluguel.preçoc * (data_dev).day) + preço_adicional
        else:
            dias_aluguel = (data_dev - aluguel.dataf).days
            if(dias_aluguel==0):
                dias_aluguel+=1
            preço_total = dias_aluguel * aluguel.preçoc
        print('O valor total que deve ser pago é: ',preço_total)
        for carro in listaCar:
            if(carro.placa == aluguel.placa):
                carro.alu = DISPONIVEL
        for cli in lista_alugueis:
            if(cli.cliente==aluguel.cliente):
                lista_alugueis.remove(cli)
        print('Devolução concluida.\n')
#fim da classe
        
#Listas para armazenar carros,clientes e alugueis e seus objetos pre-existentes
listaCar = [] #craida lista de carros
car1 = veiculo.Carro('Chevrolet','Malibu',1973,ALUGADO,'DIE-5656',7000,560)
car2 = veiculo.Carro('Cadillac','Miller Meteor',1959,ALUGADO,'BOO-2162',12873,700)
car3 = veiculo.Carro('Ford','Mustang',1967,DISPONIVEL,'SPD-9999',300,325)
listaCar.extend([car1,car2,car3])

listaCli = [] #criada a lista de clientes
c1 = cliente.Cliente('Albert Whesker',223)
c2 = cliente.Cliente('Sarah Lang',135)
c3 = cliente.Cliente('Isaac Clarke',745)
c4 = cliente.Cliente('Nicole Clarke',746)#clientes criados para serem adicionados na lista
listaCli.extend([c1,c2,c3,c4]) #função(???) para adicionar clientes na lista
listaCli.sort(key=lambda x: x.nome) #usado para ordenar a lista em ordem alfabetica

lista_alugueis = [] #criada a lista de alugueis
aluguel_1 = cliente.Aluguel(223,'DIE-5656',datetime.date(2022,10,5),datetime.date(2022,10,10),560)
aluguel_2 = cliente.Aluguel(135,'BOO-2162',datetime.date(2022,8,1),datetime.date(2022,8,15),700)
lista_alugueis.extend([aluguel_1,aluguel_2])
#Fim das listas

#Inicio do menu
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
        App.print_carros_disponiveis()
        placa_para_aluguel = input('Digite a placa que deseja alugar: ')
        id_cliente = int(input('Digite o id do cliente que deseja alugar:'))
        cliente = App.consulta_cliente(id_cliente)
        print('Digite a data inicial:')
        diax = int(input('dia: '))
        mesx = int(input('mes: '))
        anox = int(input('ano: '))
        print('Digite a data final')
        dataini = Aluguel.data_inicial(diax, mesx, anox)
        diay = int(input('dia: '))
        mesy = int(input('mes: '))
        anoy = int(input('ano: '))
        dataf = Aluguel.data_final(diay, mesy, anoy)
        aluguel_x = App.alugar(placa_para_aluguel,cliente,dataini,dataf)
        lista_alugueis.append(aluguel_x)
    elif opc == 2:
        print(lista_alugueis,'\n')
        id_cliente = int(input('Digite o id do cliente que deseja devolver o carro: '))
        aluguel = App.consulta_alugueis(id_cliente)
        App.devolver(aluguel)
    elif opc == 3:
        nomex = input('Digite o nome do cliente: ')
        idenx+=1
        print('id do novo cliente: ',idenx,'\n')
        App.addCli(nomex,idenx)
    elif opc == 4:
        marcax = input('Digite a marca do veículo: ')
        modelox = input('Digite o modelo do veículo: ')
        anox = int(input('Digite o ano do modelo: '))
        alux = 1
        placax = input('Digite a placa do carro: ')
        quilox = int(input('Digite a quilometragem do carro: '))
        valorx = float(input('Digite o valor da diaria do carro: '))
        App.addCar(marcax,modelox,anox,alux,placax,quilox,valorx)
    elif opc == 5:
        print('Lista de Clientes:\n')
        App.printCli()
    elif opc == 6:
        print('Como deseja ver a lista de veículos?')
        print('1-Ordenada por marca\n2-Ordernada por modelo\n3-Ordenada por ano\n4-Mostrar veículos disponíveis')
        opcc = int(input('Digite a opção desejada: '))
        print('\nVeículos:\n')
        App.printCar(opcc)
    else:
        print('Opção invalida.')
        break

    menu()
    opc = int(input('Digite a opção: '))
    
print('Programa fechado.')
exit()
#fim do menu
