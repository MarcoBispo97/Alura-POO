def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

#O texto acime é um dicionário

#Def são funções

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))

#No mundo procedural isso não é obrigatório, entretanto é usual !
#Função em arquivos e módulos diferentes.
