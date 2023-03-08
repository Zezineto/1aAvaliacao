from veiculo import listaCar, carro_por_placa, ALUGADO, DISPONIVEL

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
    
listaCli = [] #criada a lista de clientes
c1 = Cliente('Albert Whesker',223)
c2 = Cliente('Sarah Lang',135)
c3 = Cliente('Isaac Clarke',745)
c4 = Cliente('Nicole Clarke',746)#clientes criados para serem adicionados na lista
listaCli.extend([c1,c2,c3,c4]) #função(???) para adicionar clientes na lista
listaCli.sort(key=lambda x: x.nome) #usado para ordenar a lista em ordem alfabetica

lista_alugueis = []

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

def consulta_preço(placa):
    for carro in listaCar:
        if(carro.placa==placa):
            return carro.valorDia

def consulta_cliente(ident):
    for cli in listaCli:
        if(cli.iden==ident):
            return cli
        
def alugar(placa_para_aluguel,idAlu,dataini,dataf):
    placa = placa_para_aluguel
    cliente = idAlu
    valor = consulta_preço(placa)
    aluguel = Aluguel(placa,cliente,dataini,dataf,valor)
    carro = carro_por_placa(placa)
    carro.alu = ALUGADO
    return aluguel
