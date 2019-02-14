



# faça uma funcao ola_fulano, que recebe um nome e um adjetivo, 
# e devolve a string "ola NOME, te acho ADJETIVO". 
# Por exemplo, ola_fulano(joao,alto) devolve 
# "ola joao, te acho alto"
# dica: você pode juntar duas strings com o operador +
# ex: "ola"+"mundo" resulta "olamundo"
def ola_fulano(nome,adj):
    return "ola"


# faça uma funcao que recebe tres numeros e retorna o maior deles
# nao use a funcao max do python
# dica: use if e o operador >
def maximo(a,b,c):
    return a

#faça uma função que recebe 3 numeros e nos diz quantos sao iguais.
# ela retorna uma string, que pode ser:
#'diferentes' se todos sao diferentes, 
# 'dois iguais' se temos dois numeros iguais,
#'todos iguais', se forem todos iguais
#dica: use if e o operador ==
def conta_iguais(a,b,c):
    return 'diferentes'

#faça uma funcao que recebe uma string e troca os 'a' por 'q'
# ou seja, se ela receber 'agua', devolve 'qguq'

# Primeiro, temos um exemplo que você não deve modificar
def exemplo():
    for c in 'exemplo':
        print(c)

#Você pode pegar os caracteres da string 1 a 1, usando for,
#como no exemplo. Rode esse exemplo no terminal do runtests.

# Depois, tente modificar a funcao abaixo
def lingua_do_q(string):
    return 'essq string nqo fqz muito sentido'


#Seu chefe decidiu que senhas boas precisam ter:
#Pelo menos 1 numero, pelo menos uma letra minuscula 
# e pelo menos uma maiuscula.
# Também tem que ter 8 ou mais caracteres
# Faça uma funçao senha_boa, que recebe uma string, 
# devolve True se é uma senha boa e False se nao é uma senha boa

# primeiro, temos um exemplo que você não deve modificar
def eh_maiuscula(c):
    if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return True
    return False


# dica: para verificar se um caractere C é uma maiuscula, voce 
# pode usar a funcao eh_maiuscula, definida acima
# (crie funcoes eh_minuscula e eh_numero similares!)


def senha_boa(senha):
    maiuscula = False
    minuscula = False
    numero = False
    tamanho = False
    return numero and maiuscula and minuscula and tamanho

#Faça uma função que recebe um número, e retorna dois:
# o número original e o seu quadrado
def dois_resultados(a):
    return (1,2)


'''
Crie uma função "divisivel por 3"
que diz se um número é divisivel por 3
sem sobrar resto.

Ou seja, ela deve retornar True para
0,3,6,9,12...
'''
def divisivel_por_3(numero):
    return True


# faça uma função relogio_segundos que:
# recebe um numero de segundos e  devolve uma string, 
# com a quantidade de horas, minutos e segundos correspondente. 
# Por exemplo, 3671 segundos corresponde a uma hora, 
# um minuto e 11 segundos.
# A sua resposta, nesse caso, deve ser a string
# '1 h, 1 min e 11 seg'
# não se preocupe com plurais (escrever mins ao invés de min)
#dica: // faz a divisão sem resto, % pega o resto
#ex: 16//5 == 3, 16%5 == 1
#dica: uma hora tem 3600 segundos, um minuto tem 60 segundos
def relogio_segundos(segundos):
    horas = 1
    minutos = 2
    segundos = 3
    #ja deixei a string armada pra você
    return str(horas)+' h, '+str(minutos)+' min e '+str(segundos)+' seg'




import unittest
class TestPartOne(unittest.TestCase):

    def test_01_ola_fulano(self):
        self.assertEqual(ola_fulano('joao','sabio'),
                         'ola joao, te acho sabio')
        self.assertEqual(ola_fulano('matheus','tolo'),
                         'ola matheus, te acho tolo')


    def test_02_maximo(self):
        self.assertEqual(maximo(1,2,3),
                         3)
        self.assertEqual(maximo(2,3,1),
                         3)
        self.assertEqual(maximo(3,2,1),
                         3)
        self.assertEqual(maximo(3,2,2),
                         3)
        self.assertEqual(maximo(1,1,4),
                         4)
    def test_03_conta_iguais(self):
        self.assertEqual(conta_iguais(1,2,3),'diferentes')
        self.assertEqual(conta_iguais(1,1,3),'dois iguais')
        self.assertEqual(conta_iguais(1,3,1),'dois iguais')
        self.assertEqual(conta_iguais(3,1,1),'dois iguais')
        self.assertEqual(conta_iguais(3,3,3),'todos iguais')
    
    def test_04_lingua_do_q(self):
        palavras='','aaa','abcdea'
        pqlqvrqs='','qqq','qbcdeq'
        for i in range(len(palavras)):
             self.assertEqual(lingua_do_q(palavras[i]),
                                   pqlqvrqs[i])
    
    
    
    
    def test_05_senha_boa(self):
        self.assertEqual(senha_boa('banana'),
                         False)
        self.assertEqual(senha_boa('banana1A'),
                         True)
        self.assertEqual(senha_boa('banana1A2A3b'),
                         True)
        self.assertEqual(senha_boa('1Aa'),
                         False)
        self.assertEqual(senha_boa('1111Aa'),
                         False)
        self.assertEqual(senha_boa('1234567890'),
                         False)
        self.assertEqual(senha_boa('123456789a'),
                         False)
        self.assertEqual(senha_boa('123456789A'),
                         False)
        self.assertEqual(senha_boa('abcdefghA'),
                         False)
        self.assertEqual(senha_boa('abcdefgh1'),
                         False)
        self.assertEqual(senha_boa('abcdefgh'),
                         False)

    def test_06_dois_resultados(self):
        self.assertEqual(dois_resultados(0),
                         (0,0))
        self.assertEqual(dois_resultados(1),
                         (1,1))
        self.assertEqual(dois_resultados(-1),
                         (-1,1))
        self.assertEqual(dois_resultados(2),
                         (2,4))
    
    def test_07_divisivel_por_3(self):
        self.assertTrue(divisivel_por_3(3))
        self.assertFalse(divisivel_por_3(4))
        self.assertTrue(divisivel_por_3(6))
        self.assertFalse(divisivel_por_3(40))
        self.assertTrue(divisivel_por_3(645))
        self.assertFalse(divisivel_por_3(110))
        self.assertTrue(divisivel_por_3(0))






    def test_08_relogio_segundos(self):
        self.assertEqual(relogio_segundos(3661),
                         '1 h, 1 min e 1 seg')
        self.assertEqual(relogio_segundos(3601),
                         '1 h, 0 min e 1 seg')
        self.assertEqual(relogio_segundos(3660),
                         '1 h, 1 min e 0 seg')
        self.assertEqual(relogio_segundos(3600),
                         '1 h, 0 min e 0 seg')
        self.assertEqual(relogio_segundos(7207),
                         '2 h, 0 min e 7 seg')
        self.assertEqual(relogio_segundos(61),
                         '0 h, 1 min e 1 seg')
        self.assertEqual(relogio_segundos(1),
                         '0 h, 0 min e 1 seg')
        self.assertEqual(relogio_segundos(60),
                         '0 h, 1 min e 0 seg')
        self.assertEqual(relogio_segundos(0),
                         '0 h, 0 min e 0 seg')
    

        


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartOne)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


