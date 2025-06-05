import streamlit as st
import joblib


model=joblib.load('placement.pkl')

def main():
    st.title('welcome to predictore ')
    cgpa=st.number_input('enter your cgpa ')
    cgpa=st.slider('choose your cgpa from slider',min_value=0.0,max_value=10.0,step=0.1)
    st.write('entered cgpa',cgpa)

    if st.button('prdict'):
        result=model.predict([[cgpa]])
        st.success(f'your package would be{result} Lpa')

if __name__=='__main__':
    main()
        
