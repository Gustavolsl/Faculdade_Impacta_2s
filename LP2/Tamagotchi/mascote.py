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
        
        if self.energia + novaEnergia >= 100:
           
            self.energia = 100
        
        else:
            if self.energia + novaEnergia <= 0:
            
                self.energia = 100
                self.vidas -= 1
            
            elif self.energia + novaEnergia >= 0 and novaEnergia < 0:
              
                self.energia = self.energia + novaEnergia


            elif self.energia + novaEnergia < 100 and self.energia + novaEnergia > 0:

                self.energia = self.energia + novaEnergia

        self.printEstado()



m1 = Mascote()
m1.setEnergia(-90)

m1.setEnergia(10)
    
    







