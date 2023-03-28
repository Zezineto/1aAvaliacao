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
