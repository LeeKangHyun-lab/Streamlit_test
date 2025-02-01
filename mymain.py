import streamlit as st
import bank
import rock

#사이드바 화면
st.sidebar.header('로그인')
user_id = st.sidebar.text_input('아이디 입력')
user_pw = st.sidebar.text_input('패스워드 입력',type = 'password')

if user_pw == '1234':
    st.sidebar.header('=== KangHyun\'s Portfolio ====')
    selectbox_options = ['은행클래스', '가위바위보 게임']
    menu = st.sidebar.selectbox('메뉴선택',selectbox_options, index = None)

    if menu == '은행클래스':
        bank.customerIn()
        bank.customerManage()
    elif menu == '가위바위보 게임':
        rock.run_rock()
    