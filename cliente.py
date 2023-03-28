import veiculo
import datetime

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

    def data_inicial(diax, mesx, anox):
        data1 = datetime.date(day = diax, month = mesx, year = anox)
        return data1
    def data_final(diay, mesy, anoy):
        data2 = datetime.date(day = diay, month = mesy, year = anoy)
        return data2
        
    def __str__(self):
        return f''
    def __repr__(self):
        return f'\nID do cliente: {self.cliente}, Placa do carro: {self.placa}, Data de entrega: {self.dataf}\n'
