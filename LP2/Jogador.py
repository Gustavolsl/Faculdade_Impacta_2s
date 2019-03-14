'''class Mascote: #Nome da classe
    def __init__((self, nome):
        self.nome = nome #self.nome é um atributo
        self.fome = fome # atributo
        self.saude = saude #  atributo
        self.limpeza = limpeza # atributo
        self.idade = idade'''

class Jogador: #Nome da classe
    def __init__ (self, nome, time, camisa, velocidade):
        self.nome = nome #self.nome é um atributo
        self.time = time # atributo
        self.camisa = camisa #  atributo
        self.velocidade = velocidade # atributo
    #Metodo de acesso (getters)
    def getNome(self):
         return self.nome

    def getTime(self):
         return self.time

    def getCamisa(self):
         return self.camisa

    def getVelocidade(self):
         return self.velocidade
