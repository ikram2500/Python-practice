# https://www.youtube.com/watch?v=YkpG5CH0ySc
from uuid import uuid4


class Account:
    def __init__(self, name: str ) -> None:
        self.name = name 
        #self.__id = f'ACCOUNT:{uuid4()}'  # Name-mangled private attribute for account ID
        self.__id = f'ACCOUNT:{uuid4()}'

    def show_account_id(self) -> None:
        #print(self.__id)
        print(self.__id)


class SavingsAccount(Account):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.id = f'SAVINGS:{uuid4()}'

    def show_savings_id(self):
        print(self.id)


def main() -> None:
    savings = SavingsAccount('John Doe')
    savings.show_account_id()  # This will show the account ID
    savings.show_savings_id()  # This will show the savings account ID
    #print(acc.__id) # This will raise an AttributeError since __id is name-mangled
    #print(acc._Account__id)  # This will work due to name mangling, but it's not recommended to access private attributes directly
if __name__ == "__main__": 
    main()