from abc import ABC, abstractmethod

class Conta:
    
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
        
        
    @property
    def saldo(self):
        return self._saldo
     
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):  
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if(valor<self.saldo):
            return False
        self._saldo -= valor
        return True
    
    def depositar(self, valor):
        if(valor<0):
            return False
        self._saldo += valor
        return True
    
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.limite = 1000
        self. limite_saques = 3
    

class Historico:
    def __init__(self):
        self._transacoes = []
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)
    
    
class Transacao(ABC):
    
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
        
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, conta):
        if conta.depositar(self._valor):
            return f"Depósito de R$ {self._valor:.2f}"
        return None
    
class Saque(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, conta):
        if conta.sacar(self._valor):
            return f"Saque de R$ {self._valor:.2f}"
        return None

    
    
class Cliente:
    
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        if(transacao.registrar(conta)):
            conta.historico.adicionar_transacao(transacao)
        
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento