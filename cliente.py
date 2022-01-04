class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property #Esse método representa uma propriedade !
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title() #Primeira letra maíuscula

    @nome.setter
    def nome(self, nome):
        print("chamando @setter nome()")
        self.__nome = nome #Primeira letra maíuscula

    #from cliente import Cliente
    #cliente = Cliente("Marco")
    #chamando @property nome()
    #cliente.nome = "Nico"
    #chmando @setter nome()
    #cliente.nome
    #chamando @property nome()
    #'Nico'