import streamlit as st
import pandas as pd

# Configure the page
st.set_page_config(
   page_title="CM",
   page_icon="📄",
   layout="centered",
   initial_sidebar_state="collapsed",
)


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
   #  st.write("Here goes your normal Streamlit app...")
   #  st.button("Click me")


   st.subheader("Обрати вид договору")
   cat_col, type_col = st.columns([1,1])
   with cat_col:
      select_cat = st.selectbox(
         "", 
         ["Договір на послуги з ремонту тепловозу", 
         "Договір оренди", "Договір надання послуг"]) 
   with type_col:
      select_type = st.radio('', ['Витратний', 'Прибутковий'], horizontal=True)

   st.write("""Існує типовий договір обраного виду. Зазначте необхідні дані
   для формування договору.""")

   if select_cat == "Договір на послуги з ремонту тепловозу":
      col1, col2 = st.columns(2)
      with col1:
         input1 = st.selectbox("Обсяг ремонту", ["ПР-1"])
      with col2:
         input2 = st.selectbox("Обсяг ТО", ["ТО-3"])

   chapters = [
      "Преамбула", "1. Предмет договору", "2. Вартість послуг і умови розрахунку",
   "3. Умови та місце наданих послуг", "4. Порядок приймання-передачі наданих послуг", 
   "5. Обставини непереборної сили", "6. Відповідальність сторін", 
   "7. Антикорупційне застереження", "8. Порядок вирішення спорів", 
   "9. Застереження про конфіденційність", "10. Інші умови договору",
   "11. Термін дії Договору", "12. Додатки до договору", 
   "13. Юридичні адреси та банківські реквізити Сторін"]





   st.subheader("ДОГОВІР №__")
   st.write("""на надання послуг з поточного ремонту в обсязі 
   ПР-1 та технічного обслуговування в обсязі ТО-3""")

   for chapter in chapters:
      with st.expander(chapter):
         st.write("Some text")
