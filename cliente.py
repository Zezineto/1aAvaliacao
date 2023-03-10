from veiculo import listaCar, carro_por_placa, ALUGADO, DISPONIVEL
import veiculo

class Cliente:
    def __init__(self, nome, iden):
        self.nome = nome
        self.iden = iden
    def __str__(self):
        return f'Nome: {self.nome} \nid: {self.iden}\n'
    def __repr__(self):
        return f'\nNome: {self.nome} || id: {self.iden}\n'

class Aluguel:
    def __init__(self, cliente, placa, dataini, dataf,preçoc):
        self.cliente = cliente
        self.placa = placa
        self.dataini = dataini
        self.dataf = dataf
        self.preçoc = preçoc
    def __str__(self):
        return f''
    def __repr__(self):
        return f'\nID do cliente: {self.cliente}, Placa do carro: {self.placa}, Data de entrega: {self.dataf}\n'
    
listaCli = [] #criada a lista de clientes
c1 = Cliente('Albert Whesker',223)
c2 = Cliente('Sarah Lang',135)
c3 = Cliente('Isaac Clarke',745)
c4 = Cliente('Nicole Clarke',746)#clientes criados para serem adicionados na lista
listaCli.extend([c1,c2,c3,c4]) #função(???) para adicionar clientes na lista
listaCli.sort(key=lambda x: x.nome) #usado para ordenar a lista em ordem alfabetica

lista_alugueis = []
aluguel_1 = Aluguel(223,'DIE-5656',1,7,560)
aluguel_2 = Aluguel(135,'BOO-2162',1,15,700)
lista_alugueis.extend([aluguel_1,aluguel_2])
#função para printar a lista de clientes
def printCli():
   print(listaCli,'\n')

#função para adicionar clientes a lista
def addCli(nomex,idenx):
    cx = Cliente(nomex,idenx)
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
            return cli

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
    placa = placa_para_aluguel
    cliente = idAlu
    valor = consulta_preço(placa)
    aluguel_x = Aluguel(placa,cliente,dataini,dataf,valor)
    carro = carro_por_placa(placa)
    carro.alu = ALUGADO
    return aluguel_x

#função que calcula o valor que o cliente deve pagar ao carro ser devolvido
def devolver(aluguel):
    data_dev = int(input('Digite a data a qual o carro foi devolvido: '))
    if(data_dev>aluguel.dataf):
        dias_extras = data_dev - aluguel.dataf
        valor_adicional = aluguel.preçoc * 0.20
        preço_adicional = dias_extras * valor_adicional
        preço_total = (aluguel.preçoc * data_dev) + preço_adicional
    else:
        preço_total = data_dev * preçoc
    print('O valor total que deve ser pago é: ',preço_total)
    for carro in listaCar:
        if(carro.placa == aluguel.placa):
            carro.alu = DISPONIVEL
    print('Devolução concluida.\n')
        
