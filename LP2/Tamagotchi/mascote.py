class Mascote:

    def __init__ (self):
        self.vidas = 7
        self.energia = 100

    def getVidas(self):
        return self.vidas

    def getEnergia(self):
        return self.energia

    def printEstado(self):
        print('\nVidas: ', self.vidas)
        print('Energia: ', self.energia)


    def setEnergia(self, novaEnergia):

        print('testtete', novaEnergia)

        print('soma', self.energia + novaEnergia)

        print('energia atual: ', self.energia)
        print('energia nova: ', novaEnergia)        
        
        if self.energia + novaEnergia >= 100:
            print('chegou aqui 1')
            self.energia = 100
        
        else:
            if self.energia + novaEnergia <= 0:
                print('chegou aqui 2')
                self.energia = 100
                self.vidas -= 1
            
            elif self.energia + novaEnergia >= 0 and novaEnergia < 0:
                print('chegou aqui 3')
                self.energia += novaEnergia

            elif self.energia + novaEnergia < 100 and self.energia + novaEnergia > 0:
                print('chegou aqui 4')
                self.energia = self.energia + novaEnergia

        self.printEstado()


        


m1 = Mascote()
m1.setEnergia(-90)

m1 = Mascote()
m1.setEnergia(10)
    
    







