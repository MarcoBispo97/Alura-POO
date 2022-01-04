class Conta:
    #palavra reservada para definir uma "receita"
    #Os atributos da nossas classe são numero, tiular, saldo e limite
    #Os objetos são inseridos nos terminais, eles ficam inseridos na MEMÓRIA INTERNA do python

    def __init__(self, numero, titular, saldo, limite):
        # para fazer com que a função seja vbariável eu coloca as variável na função construtora self
        #Uma função construtora pra construir o objeto
        print("Construindo objeto......{}".format(self))
        #self é a referência que sabe encontrar qual obj está sendo construido
        #acesso meu objeto com "sefl.numero" numero é o atributo
        #para falar vai ou busca em python geralemnte é um "."
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        #para fazer com que a função seja vbariável eu
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

        self.__saldo -= valor

    #def transfere(self, valor, origem, destino): # conta2.transfere(10, conta2, conta)
    #    origem.saca(valor)
    #    destino.deposita(valor)

    def transfere(self, valor, destino): # conta2.transfere(10, conta)
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @statistics #Sempre vai ser "001" idependentemente de ter obj ou ñ
    def codigo_banco(self):
        return "001"
    #conta = Conta(123, "Nico", 55, 1000)
    #Construindo objeto......<conta.Conta object at 0x000001DE7BAF5880>
    #conta2 = Conta(321, "Marco", 100, 1000)
    #Construindo objeto......<conta.Conta object at 0x000001DE7BAF5280>
    #conta2.transfere(10, conta)

    #Python 3.9.6(tags / v3.9.6: db3ff76, Jun282021, 15: 26:21) [MSC v.1929 64 bit(AMD64)]
    #on win32
    #from conta import Conta
    #conta = Conta(123, "Nico", 55, 1000)
    #Construindo
    #objeto...... < conta.Conta object at 0x000001B306771070 >
    #conta.extrato()
    #Saldo 55 do titular Nico
    #conta.deposita(15.0)
    #conta.extrato()
    #Saldo 70.0
    #do titular Nico
    #conta.saca(10)
    #conta.extrato()
    #Saldo 60.0 do titular Nico
    #pass'''
    # conta._Conta__limite ATRIBUTO PARA SER USADO DENTRO DA CLASSE !