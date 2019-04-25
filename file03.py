""" 
#classePessoa

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome

ninja = 'Ana'
print = (ninja) """

""" class AnimalEstimacao():
    def __init__(self, nome, especie, dono):
        self.nome = nome """

class Calculadora:
#self repete o nome do objeto
    #função para iniciar
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a*self.b

    def divide(self):
        return self.a / self.b
teste = Calculadora(128, 2)

print('soma: ', teste.soma())
print('subtrai: ', teste.subtrai())
