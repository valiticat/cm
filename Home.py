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

         st.caption("Інформація щодо контрагента")
         in5_col, in6_col = st.columns(2)
         with in5_col:
            input5 = st.text_input("Код ЄДРПОУ Контрагента*", '38560924')
            st.caption("*спробуй 38560924 або 40297125")
         with in6_col:
            edr = {'38560924' : { 
               'title' : 'Товариство з обмеженою відповідальністю "Полтавський тепловозоремонтний завод"',
               'rep' : "Василенко Василина Василівна" 
            },
            '40297125' : {
               'title' : 'Товариство з обмеженою відповідальністю "Запорізькій тепловозоремонтний завод"',
               'rep' : 'Петренко Петро Петрович'
            }}
            st.write("")
            input6 = edr.get(input5).get('title')
            input7 = edr.get(input5).get('rep')
            st.caption(input6)
         
         in8_col, in9_col = st.columns(2)
         with in8_col:
            input8 = st.text_input("Номер довіреності")
         with in9_col:
            input9 = st.date_input("Дата видачі довіреності")

         st.caption("Інформація щодо предмету договору")
         in10_col, in11_col = st.columns(2)
         with in10_col:
            input10 = st.text_input("Серія", "ЧМЕЗ")
         with in11_col:
            input11 = st.text_input("Номер", "302")

         in12_col, in13_col = st.columns(2)
         with in12_col:
            input12 = st.number_input("Вартість договору (грн), з ПДВ")
         with in13_col:
            input13 = st.text_input("Номер", "302")


         
         
         


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
      st.subheader("ДОГОВІР №")
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
      st.caption(f"""{input6}, далі – Замовник, в особі {input7}, яка(ий) діє на підставі 
      довіреності № {input8} від {input9} р., з іншої сторони, при  спільному 
      згадуванні – Сторони, уклали цей Договір про наступне.""")

   with st.expander("1. Предмет договору"):
      st.caption(f"""1.1. Виконавець зобов’язується надати послуги з поточного ремонту 
      в обсязі {input1} та технічного обслуговування в обсязі {input2} тепловоза серії {input10} № {input11} 
      власності Замовника з використанням матеріалів та запасних частин Замовника 
      (далі {input1}, {input2} або послуги), а Замовник провести оплату вартості послуг 
      згідно з умовами цього договору.""")
      st.caption(f"""1.2. За даним договором Виконавець протягом його дії проводить 
      {input1} та {input2} один раз згідно графіка (Додаток 1).""")

   with st.expander("2. Вартість послуг і умови розрахунку"):
      st.caption(f"""2.1. Вартість послуг за договором визначена у Протоколі погодження вартості 
      послуг (Додаток № 2), який є невід’ємною частиною даного Договору.""")
      st.caption(f"""2.2. Загальна вартість договору складає {input12} грн.  
      в т.ч. ПДВ 20% - {input12*0.20} грн.""")







   
   for chapter in chapters[3:]:
      with st.expander(chapter):
         st.write("Some text")
