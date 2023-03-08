ALUGADO = 0
DISPONIVEL = 1

class Veículo:
    def __init__(self, marca, modelo, ano, alu):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.alu = alu
    def __str__(self):
        return f'Veículo: {self.marca} {self.modelo}, {self.ano}'
    def __repr__(self):
        if self.alu == 1:
            return f'\nMarca: {self.marca} || Modelo: {self.modelo} || Ano: {self.ano} || Disponível\n'
        else:
            return f'\nMarca: {self.marca} || Modelo: {self.modelo} || Ano: {self.ano} || Alugado\n'

class Carro(Veículo):
    def __init__(self,marca,modelo,ano,alu,placa,quilometragem,valorDia):
        Veículo.__init__(self,marca,modelo,ano,alu)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valorDia = valorDia
    def __str__(self):
        return f'Carro {self.marca} {self.modelo}, {self.ano},\
 {self.placa}, {self.quilometragem}km, {self.valorDia}R$\n'
    def __repr__(self):
        if self.alu == 1:
            return f'\n|| Carro {self.marca} {self.modelo}, Ano: {self.ano} ||\n\
|| Placa: {self.placa}, Quilometragem {self.quilometragem}km ||\n|| Valor diario: {self.valorDia}R$, Diponível||\n'
        else:
            return f'\n|| Carro {self.marca} {self.modelo}, Ano: {self.ano} ||\n\
|| Placa: {self.placa}, Quilometragem {self.quilometragem}km ||\n|| Valor diario: {self.valorDia}R$, Alugado||\n'

listaCar = []
car1 = Carro('Chevrolet','Malibu',1973,ALUGADO,'DIE-5656',7000,560)
car2 = Carro('Cadillac','Miller Meteor',1959,ALUGADO,'BOO-2162',12873,700)
car3 = Carro('Ford','Mustang',1967,DISPONIVEL,'SPD-9999',300,325)
listaCar.extend([car1,car2,car3])

#função para printar a lista de veículos
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

def addCar(marcax,modelox,anox,alux):
    carx = Carro(marcax,modelox,anox,alux)
    listaVe.append(vx)
