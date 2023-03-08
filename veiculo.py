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
    def __init__(self,marca,modelo,ano,placa,quilometragem,valorDia):
        Veículo.__init__(self,marca,modelo,ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valorDia = valorDia
    def __str__(self):
        return f'Carro {self.marca} {self.modelo}, {self.ano},\
 {self.placa}, {self.quilometragem}km, {self.valorDia}R$'

listaVe = []
v1 = Veículo('Chevrolet','Malibu',1973,0)
v2 = Veículo('Cadillac','Miller Meteor',1959,0)
v3 = Veículo('Ford','Mustang',1967,1)
listaVe.extend([v1,v2,v3])

#função para printar a lista de veículos
def printVe(opcc):
    if opcc == 1:
        listaVe.sort(key=lambda x: x.marca)
        print(listaVe,'\n')
    elif opcc == 2:
        listaVe.sort(key=lambda x: x.modelo)
        print(listaVe,'\n')
    elif opcc == 3:
        listaVe.sort(key=lambda x: x.ano, reverse=True)
        print(listaVe,'\n')
    elif opcc == 4:
        for num in listaVe:
            if(num.alu==1):
                print(num)

def addVe(marcax,modelox,anox,alux):
    vx = Veículo(marcax,modelox,anox,alux)
    listaVe.append(vx)
