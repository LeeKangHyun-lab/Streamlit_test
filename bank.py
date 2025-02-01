import streamlit as st

customers = {'kim':[12345, '홍길동', 300000], 'Lee':[34567, '파이썬', 7890]}

class Bank_account:
    # 속성
    def __init__(self, number, name, balance):
        self.account_number = number
        self.name = name = name
        self.balance = balance = balance

    #기능, 메서드
    def deposit(self, amount):
        #입금
        self.balance += amount

        return self.balance

    def withdraw(self, amount):
        #출금
        if self.balance >= amount:
            self.balance -= amount
        else:
            # print('잔고가 부족해서 인출 불가합니다.')
            st.write('잔고가 부족해서 인출 불가합니다.')

        return self.balance
    
    def print_bal(self):
        # print(f'잔고 : {self.balance}')
        st.write(f'잔고 : {self.balance}')

def customerIn():
    # id = input('아이디 입력>>')
    # num = input('고객 번호 입력>>')
    # name = input('고객 이름 입력>>')
    # money = int(input('잔고 입력>>'))
    # customers[id] = [num, name, money]
    id = st.text_input('아이디 입력>>')
    num = st.text_input('고객 번호 입력>>')
    name = st.text_input('고객 이름 입력>>')
    money = st.number_input('잔고 입력>>')
    customers[id] = [num, name, money]

def customerManage():
    for key, data in customers.items():
        # print(key, data)
        # print('----')
        key = Bank_account(data[0], data[1], data[2])
        # print('고객번호',key.account_number)
        # print('이름',key.name)
        # print('잔금',key.balance)
        st.write('고객번호',key.account_number)
        st.write('이름',key.name)
        st.write('잔금',key.balance)
        key.deposit(45000)
        key.print_bal()
        key.withdraw(30000)
        key.print_bal()


#main()
#객체 생성
if __name__ == '__main__':
    customerIn()
    customerManage()