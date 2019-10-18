# Linguagem de Programação II
# AC05 ADS2D - Banco
#
# Alunos: tiago.souza@aluno.faculdadeimpacta.com.br
#         julio.fernando@aluno.faculdadeimpacta.com.br

from typing import Union, List, Dict

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.

    possui os atributos: nome, telefone e email, todos privados
    caso o email não seja um email válido gera um ValueError,
    caso o telefone não seja um número gera um TypeError
    """

    def __init__(self, nome: str, telefone: int, email: str):
        self._nome = nome
        self._telefone = telefone
        self._email = email

    def get_nome(self) -> str:
        """Acessor do atributo Nome."""
        return self._nome

    def get_telefone(self) -> int:
        """Acessor do atributo Telefone."""
        self.set_telefone(self._telefone)
        return self._telefone

    def set_telefone(self, novo_telefone: int) -> None:
        """
        Mutador do atributo telefone, caso não receba um número,
        gera um TypeError
        """
        if type(novo_telefone) is not int:
            raise TypeError("O número dever ser inteiro")
        else:
            self._telefone = novo_telefone

    @property
    def email(self) -> str:
        """Acessor do atributo Email."""
        self.email(self._email)
        return self._email

    @email.setter
    def email(self, novo_email: str) -> None:
        """
        Mutador do atributo Email, caso não receba um email válido
        gera um ValueError.
        """
        if type(novo_email) is not str or " " in novo_email:
            raise ValueError("O formato de email é inválido")
        elif "@" not in novo_email or novo_email.count("@") != 1:
            raise ValueError("O formato de email é inválido")
        elif novo_email.index("@") < 2 \
                or novo_email.index("@") >= len(novo_email) - 5:
            raise ValueError("O formato de email é inválido")
        else:
            self._email = novo_email


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    * abre_contas: abre uma nova conta, atribuindo o numero da conta em ordem
    crescente.
    * lista_contas(): apresenta um resumo de todas as contas do banco
    DICA: mantenha uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    def __init__(self, nome: str):
        self._nome = nome
        self._numContas = 0
        self._listaCliente = []
        self._listaContas = []

    def get_nome(self) -> str:
        """Acessor do Atributo Nome."""
        return self._nome

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:
        """
        Método para abertura de nova conta, recebe os clientes
        e o saldo inicial.
        Caso o saldo inicial seja menor que 0 devolve um ValueError
        """
        if saldo_ini < 0:
            raise ValueError("Saldo negativo!")
        else:
            self._numContas += 1
            self._listaCliente.append(clientes)
            self._cc = Conta(
                self._listaCliente,
                self._numContas, saldo_ini)
            self._listaContas.append(self._cc)
            self.lista_contas()

    def lista_contas(self) -> List['Conta']:
        """Retorna a lista com todas as contas do banco."""
        return self._listaContas


class Conta():
    """
    Classe Conta.
    * Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito'), 200) etc.
    * Caso o saldo inicial seja menor que zero deve lançar um ValueError
    * A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)
    DICA: Crie uma variável interna privada para guardar as
    operaões feitas na conta
    """
   
    def __init__(self, clientes: List[Cliente], numero_conta: int,
                 saldo_inicial: Number):
        self._clientes = clientes
        self._numero_conta = numero_conta
        self._saldo = saldo_inicial
        self._extrato = [('saldo_inicial', saldo_inicial)]

    def get_clientes(self) -> List[Cliente]:

        '''
        Acessor para o atributo Clientes
        '''
        return self._clientes

    def get_saldo(self) -> Number:
        '''
        Acessor para o Atributo Saldo
        '''
        return self._saldo

    def get_numero(self) -> int:
        '''
        Acessor para o atributo Numero
        '''
        return self._numero_conta

    def saque(self, valor: Number) -> None:
        '''
        Método de saque da classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve retornar um ValueError, e não efetuar o saque
        '''
        if valor > self._saldo:
            raise ValueError("Valor excede o saldo disponível")
        else:
            self._saldo -= valor
            self._extrato.append(("saque", valor))

    def deposito(self, valor: Number):
        '''
        Método depósito da classe Conta, operação deve aparecer no extrato
        '''
        self._saldo += valor
        self._extrato.append(("deposito", valor))

    def extrato(self) -> List[Dict[str, Number]]:
        '''
        Retorna uma lista com as operações (Tuplas) executadas na Conta
        '''
        return self._extrato

    @classmethod
    def mensagem(cls):
        return cls.mensagem

    @classmethod
    def set_mensagem(cls, nova_mensagem):
        cls.mensagem = nova_mensagem
