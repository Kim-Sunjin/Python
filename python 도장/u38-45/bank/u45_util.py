class Account:
    def __init__(self, ano, owner,balance):
        self.ano = ano
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if self.__balance + amount >= 10000000:
            print('잔액이 1000만원을 초과했습니다.')
            return
        self.__balance += amount

    def  withdraw(self, amount):
        if self.__balance - amount <0:
            print('잔액이 부족하여 출금할 수 없습니다.')
            return
        self.__balance -= amount
        print(f'남은 잔액은 {self.__balance}원입니다.')
    
    def __str__(self):
        return f'ano: {self.ano}, owner:{self.owner}, balance: {self.__balance}'

