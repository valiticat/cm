import streamlit as st
import pandas as pd
from datetime import date

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
        if st.session_state["password"] == st.secrets["passwords"]["test_user"]:
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

   st.subheader("Формування договору")
   cat_col, type_col = st.columns([1,0.5])
   with cat_col:
      select_cat = st.selectbox(
         "Обрати вид договору", 
         ["Договір на послуги з ремонту тепловозу", 
         "Договір оренди", "Договір надання послуг"]) 
   with type_col:
      select_type = st.radio('', ['Витратний', 'Прибутковий'], horizontal=True)

   st.write("""Існує типовий договір обраного виду""") 

   # User Inputs
   with st.expander("Зазначте необхідні дані для завершення формування договору"):
      if select_cat == "Договір на послуги з ремонту тепловозу":
         in1_col, in2_col = st.columns(2)
         with in1_col:
            input1 = st.selectbox("Обсяг ремонту", ["ПР-1", "ПР-2"])
         with in2_col:
            input2 = st.selectbox("Обсяг ТО", ["ТО-3", "ТО-4"])

         in3_col, in4_col = st.columns(2)
         with in3_col:
            input3 = st.selectbox("Місто укладання договору", 
            ["Київ", "Львів", "Харків", "Дніпро", "Одеса", "Лиман"])
         with in4_col:
            current_date = date.today()
            input4 = st.date_input("Дата укладання договору", min_value=current_date)

         in5_col, in6_col = st.columns(2)
         with in5_col:
            input5 = st.text_input("Код ЄДРПОУ Контрагента*", '38560924')
            st.caption("*спробуй 38560924 або 40297125")
         with in6_col:
            edr = {'38560924' : 'Товариство з обмеженою відповідальністю "Полтавський тепловозоремонтний завод"',
            '40297125' : 'Товариство з обмеженою відповідальністю "Запорізькій тепловозоремонтний завод"'}
            st.write("")
            st.write("")
            input6 = edr.get(input5)
            st.caption(input6)

         


   chapters = [
      "Преамбула", "1. Предмет договору", "2. Вартість послуг і умови розрахунку",
   "3. Умови та місце наданих послуг", "4. Порядок приймання-передачі наданих послуг", 
   "5. Обставини непереборної сили", "6. Відповідальність сторін", 
   "7. Антикорупційне застереження", "8. Порядок вирішення спорів", 
   "9. Застереження про конфіденційність", "10. Інші умови договору",
   "11. Термін дії Договору", "12. Додатки до договору", 
   "13. Юридичні адреси та банківські реквізити Сторін"]

   # Add empty line for better readibility
   st.write("")

   col1, col2, col3 = st.columns(3)
   with col2:
      st.subheader("ДОГОВІР №__")
   st.write(f"""на надання послуг з поточного ремонту в обсязі 
   {input1} та технічного обслуговування в обсязі {input2}""")

   col1, col2 = st.columns([1,0.2])
   with col1:
      st.caption(f"м. {input3}")
   with col2:
      st.caption(input4)

   with st.expander("Преамбула"):
      st.caption("""Акціонерне товариство «Українська залізниця», далі – Виконавець, 
      в особі акціонерного товариства «Українська залізниця», з однієї сторони, та""")
      st.caption(f"""{input6}, далі – Замовник, в особі 
       _____________________, який діє на підставі довіреності № ____ від _________ р., 
       з іншої сторони, при  спільному згадуванні – Сторони, уклали цей Договір про наступне.""")

   
   
   
   for chapter in chapters[1:]:
      with st.expander(chapter):
         st.write("Some text")
