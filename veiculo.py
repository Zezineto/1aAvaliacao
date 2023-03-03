class Veículo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veículo):
    def __init__(self,marca,modelo,ano,placa,quilometragem,valorDia):
        Veículo.__init__(self,marca,modelo,ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valorDia = valorDia
    def __str__(self):
        return f'Carro {self.marca} {self.modelo}, {self.ano},\
 {self.placa}, {self.quilometragem}km, {self.valorDia}R$'
