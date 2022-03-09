class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'Código: {self.codigo} - Saldo: {self.saldo}'


conta_do_gui = ContaCorrente(15)
conta_do_gui.depositar(500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.depositar(500)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]
print(contas[0])


def deposita_para_todas_as_contas(contas_a_receber, valor):
    for conta_a_receber in contas_a_receber:
        conta_a_receber.depositar(valor)


# contas.insert(0, 70)
deposita_para_todas_as_contas(contas, 100)
print(conta_do_gui)

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 35, 1980)

usuarios = (guilherme, daniela, ('João', 30, 1975))
