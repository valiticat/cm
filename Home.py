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
         "Договір оренди"]) 
   with type_col:
      select_type = st.radio('', ['Витратний', 'Прибутковий'], horizontal=True)
   
   if select_cat == "Договір на послуги з ремонту тепловозу":
      st.write("""Існує типовий договір обраного виду""") 

      # User Inputs
      with st.expander("Зазначте необхідні дані для завершення формування типового договору"):

         in0_col, in01_col = st.columns(2)
         with in0_col:
            input0 = st.selectbox("Ініціатор договору", 
            ["Львівська залізниця", "Південна залізниця"])
         with in01_col:
            input01 = st.selectbox("Виробничий підрозділ ініціатора",
            ['Локомотивне депо Львів-Захід'])

         in02_col, empty_col = st.columns([0.2,1])
         with in02_col:
            input02 = st.selectbox("Період (рік) проведення ремонтів", [2022, 2023])

         in1_col, in2_col = st.columns(2)
         with in1_col:
            input1 = st.selectbox("Обсяг ремонту", ["ПР-1", "ПР-2"])
         with in2_col:
            input2 = st.selectbox("Обсяг ТО", ["ТО-3", "ТО-4"])

         in3_col, in4_col = st.columns(2)
         with in3_col:
            input3 = st.selectbox("Місто укладання договору", 
            ["Львів", "Київ", "Харків", "Дніпро", "Одеса", "Лиман"])
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
            input12 = st.number_input("Вартість однієї послуги з ремонту (грн), з ПДВ")
            input122 = st.number_input("Вартість одного ТО (грн)")
         
         with in13_col:
            input13 = st.number_input("Загальна вартість договору (грн), з ПДВ")

         input14 = st.text_input("Призначення платежу")

         st.caption("Приймання в ремон та видача з ремонту")
         in15_col, in16_col = st.columns(2)
         with in15_col:
            input15 = st.text_input("Форма акту приймання", "ТУ-25")
         with in16_col:
            input16 = st.text_input("Номер інструкції", "ЦТ 0057")

      # Add empty line for better readibility
      st.write("")
      st.write("")

      with st.expander("Преамбула"):

         col1, col2, col3 = st.columns(3)
         with col2:
            st.subheader("ДОГОВІР №")
         st.write(f"""на надання послуг з поточного ремонту в обсязі {input1} 
         та технічного обслуговування в обсязі {input2}""")

         col1, col2 = st.columns([1,0.2])
         with col1:
            st.caption(f"м. {input3}")
         with col2:
            st.caption(input4)

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
         st.caption(f"""2.2. Загальна вартість договору складає {input13} грн.  
         в т.ч. ПДВ 20% - {input13*0.20} грн.""")
         st.caption(f"""2.3. Вартість однієї послуги з проведення {input1} становить,
         {input12} грн, в т.ч. ПДВ 20% – {input12*0.20} грн.""")
         st.caption(f"Вартість однієї послуги з проведення {input2} становить {input122} грн.")
         st.caption("""2.4. Замовник здійснює 100% попередню оплату вартості послуги на поточний 
         рахунок Виконавця на підставі виставленого рахунку, з урахування об’ємів послуг які будуть надаватись.""")
         st.caption(f"""2.5. При здійсненні оплати в графі призначення платежу необхідно проставляти числовий номер {input14}""")
         st.caption("""2.6. Вартість послуг, які не передбачені даним договором, визначається додатково та оформляється 
         і погоджується представниками Сторін з оформленням додаткових угод до даного договору або інших договорів.""")
         st.caption("""2.7. У разі збільшення розміру заробітної плати та зміни інших ціноутворюючих факторів, фактичного 
         показника індексу цін виробника промислової продукції, вартість послуг за цим договором буде змінюватись шляхом 
         укладення додаткових угод до договору.""")
         st.caption("""2.8. Запасні частини, вузли, паливо-мастильні та інші матеріали, необхідні для надання послуг надає Замовник.""")
         st.caption(f"""2.9. Всі витрати пов’язані з доставкою тепловоза до місця надання послуг для проведення 
         {input2} або {input1} та у зворотному напрямку, в тому числі витрати по сплаті вартості залізничного тарифу несе Замовник.""")
         
      with st.expander("3. Умови та місце наданих послуг"):
         st.caption("""3.1. Місцем надання послуг є територія Виконавця:""")
         st.caption("""3.2. Подача тепловоза здійснюється в ремонтопридатному стані. 
         Тепловоз повинен бути укомплектований усіма вузлами та деталями, передбаченими конструкторською документацією.""")
         st.caption("""3.3 Термін надання однієї послуги складає не більше п’яти робочих діб з моменту постановки тепловоза на 
         стійло та здійснення попередньої оплати у відповідності до п. 2.4 даного договору.""")
         st.caption("""Термін надання послуги може бути збільшений при необхідності надання додаткових послуг 
         на термін їх надання, а також відсутність запасних частин, вузлів, паливо-мастильних та інші матеріалів, 
         необхідних для надання послуг.""")
         st.caption(f"""3.2. Додаткові послуг, які не входять в перелік планових видів робіт {input1} та/або {input2} та 
         непередбачені даним договором, надаються додатково та оформляються і погоджуються представниками Сторін. 
         Перелік додаткових послуг оформляється актом за підписом уповноважених представників Сторін на підставі 
         якого укладається додаткова угода до договору.""")
         st.caption(f"""3.3. Виконавець проводить приймання тепловоза в ремонт та видачу з ремонту при наявності 
         у Замовника акту встановленої форми {input15} оформленого згідно інструкції {input16} та оформлених перевізних документів.""")
         st.caption("""3.4. Замовник має право направляти своїх представників в процесі надання послуг для контролю якості 
         та повноти обсягів надання послуг. Такі перевірки здійснюються з ініціативи Замовника із залученням 
         відповідних фахівців за відома Виконавця.""")
         st.caption("""3.5. Замовник зобов’язується прийняти тепловоз після надання Виконавцем послуг.""")

      with st.expander("4. Порядок приймання-передачі наданих послуг"):
         st.caption("""4.1. Приймання наданих послуг здійснюється Замовником з обов’язковим складанням відповідного 
         Акту приймання-передачі наданих послуг, який підписується повноважними представниками Сторін, протягом 5 (п’яти) 
         робочих днів з дати надання послуг.""")
         st.caption("""4.2. Уповноваженими зі сторони Виконавця, які підписуватимуть Акт приймання-передачі наданих послуг є особи, 
         що діють на підставі відповідних довіреностей: начальник служби локомотивного господарства регіональної філії, 
         заступник начальника служби локомотивного господарства регіональної філії, головний інженер служби локомотивного 
         господарства регіональної філії, начальник виробничого структурного підрозділу регіональної філії (особа, що виконує 
         його обов’язки), в інтересах якого укладено Договір.""")
         st.caption("""4.3. Акт приймання-передачі наданих послуг складається у двох примірниках. Один примірник після підписання 
         Замовником повертається Виконавцю.""")
      
      with st.expander("5. Обставини непереборної сили"):
         st.caption("""5.1. Сторони звільняються від відповідальності за невиконання або неналежне виконання 
         зобов’язань за цим Договором у разі виникнення обставин непереборної сили, які не існували під час 
         укладання Договору та виникли поза волею Сторін (аварія, катастрофа, стихійне лихо, епідемія, епізоотія, війна тощо).""")
         st.caption("""5.2. Сторона, що не може виконувати зобов’язання за цим Договором унаслідок дії обставин 
         непереборної сили, повинна не пізніше ніж протягом 10 (десяти) днів з моменту їх виникнення повідомити 
         про це іншу Сторону у письмовій формі, рекомендованим листом з описом вкладення та сертифікатом Торгово-промислової 
         палати України, що підтверджує про обставини непереборної сили.""")
         st.caption("""5.3. Доказом виникнення обставин непереборної сили та строку їх дії є відповідні документи, 
         які видаються Торгово-промисловою палатою України або її уповноваженими органами.""")
         st.caption("""5.4. У разі коли строк дії обставин непереборної сили продовжується більше ніж 30 (тридцять) 
         днів, кожна із Сторін в установленому порядку має право розірвати цей Договір.""")
      
      with st.expander("6. Відповідальність сторін"):
         st.caption("""6.1. У разі порушення Замовником обов’язків, щодо здійснення попередньої оплати 
         вартості послуг, настають наслідки передбачені ч. 3 ст. 538 ЦК України.""")
         st.caption("""6.2. За невиконання, або неналежне виконання умов договору, Сторони несуть 
         відповідальність згідно з чинним законодавством України.""")
         st.caption("""6.3. За порушення строків виконання зобов’язань за цим договором 
         Виконавець сплачує Замовнику пеню у розмірі 0,01% вартості послуг, за кожен день прострочення, 
         але не більше облікової ставки НБУ, що діяла в період за який стягується пеня.""")

      with st.expander("7. Антикорупційне застереження"):
         st.caption("""7.1. Сторони визнають та підтверджують свою повну нетерпимість до діянь, 
         предметом яких є неправомірна вигода, зокрема й до корупції, та передбачають повну заборону 
         неправомірних вигод та здійснення виплат за сприяння або спрощення формальностей в зв`язку з 
         господарською діяльністю, забезпечення швидшого вирішення будь-яких питань. Сторони керуються у 
         своїй діяльності антикорупційним законодавством України і розробленими на його основі антикорупційними програми, 
         спрямованими на боротьбу з діяннями, предметом яких є неправомірна вигода, зокрема й корупцією.""")
         st.caption("""7.2. Сторони гарантують, що їм самим та їхнім працівникам заборонено пропонувати, 
         давати або обіцяти надати будь-яку неправомірну вигоду (грошові кошти, цінні подарунки тощо) 
         удь-яким особам (зокрема й службовим особам, уповноваженим особам юридичних осіб, державним службовцям), 
         а також вимагати отримання, приймати або погоджуватися прийняти від будь-якої особи, прямо чи опосередковано, 
         будь-яку неправомірну вигоду (грошові кошти, цінні подарунки тощо).""")

      with st.expander("8. Порядок вирішення спорів"):
         st.caption("""8.1. Усі непорозуміння та спори між Сторонами, пов’язані з виконанням умов цього Договору, 
         вирішуються шляхом переговорів.""")
         st.caption("""8.2. У випадку не досягнення згоди шляхом переговорів, спірні питання вирішуються в 
         претензійно-позовному порядку згідно з чинним законодавством України.""")

      with st.expander("9. Застереження про конфіденційність"):
         st.caption("""9.1. Сторони погодилися, що текст договору, будь-які матеріали, інформація та відомості, 
         які стосуються договору, є конфіденційними і не можуть передаватися третім особам без попередньої 
         письмової згоди іншої Сторони договору, крім випадків, коли таке передавання пов’язане з одержанням 
         офіційних дозволів, документів для виконання договору або оплати податків, інших обов’язкових платежів, 
         а також у випадках, передбачених чинним законодавством України, яке регулює зобов’язання Сторін договору.""")

      with st.expander("10. Інші умови договору"):
         st.caption(""""10.1. У випадках, не передбачених даним договором, Сторони керуються чинним законодавством України.""")
         st.caption("""10.2. Зміни в цей договір можуть бути внесені за взаємною згодою Сторін, 
         що оформлюються додатковою угодою до цього договору.""")
         st.caption("""10.3. Зміни та доповнення, додаткові угоди та додатки до цього договору є його невід’ємною частиною 
         і мають юридичну силу в разі, якщо вони викладені в письмовій формі та підписані уповноваженими на те представниками Сторін.""")
         st.caption("""10.4. Договір складено українською мовою у 2 (двох) примірниках, які мають однакову юридичну чинність, 
         по одному примірнику для кожної із Сторін. Усі непорозуміння та спори між Сторонами, пов’язані з виконанням умов цього Договору, 
         вирішуються шляхом переговорів.""")
         
      with st.expander("11. Термін дії Договору"):
         st.caption(f"""11.1 Даний Договір  набирає чинності з моменту підписання його Сторонами і діє до 31.12.{input02}.""")
         st.caption("""11.2 Зміни в цей Договір можуть бути внесені за взаємною згодою Сторін та оформляються додатковою угодою до цього Договору.""")

      with st.expander("12. Додатки до договору"):
         st.caption("""12.1. До цього договору додаються такі додатки:""")
         st.caption(f"""Додаток № 1 – Графік проведення поточного ремонту в обсязі {input1} та технічних обслуговувань 
         в обсязі {input2} тепловоза серії {input10} №{input11} на {input02} рік у виробничому структурному підрозділі «{input01}» 
         регіональної філії «{input0}» акціонерного товариства «Українська залізниця» для ПрАТ «Львівський локомотиворемонтний завод» 
         на 1 (одному) аркуші.""")

   else:
      st.write("Відсутній типовий договір обраного виду")
      st.write("""Ви можете ініціювати створення нового договору 
      або використати проєкт, наданий контрагентом""")

      make_col, use_col = st.columns([0.5,1])
      with make_col:
         st.write(" ")
         make_contract = st.button("Створити", key='make_contract')
      with use_col:
         use_draft = st.file_uploader("Завантажити проєкт, наданий контрагентом", key='use_draft')

      st.write(" ")
      
      if use_draft:
         st.write("Проєкт договору потребує погодження...")

      if st.session_state.make_contract:
         st.write("""Ви можете скористатись наявними шаблонами, 
         що прискорить процедуру погодження""")

         chapters = ["Обставини непереборної сили", "Відповідальність сторін",
         "Антикорупційне застереження", "Порядок вирішення спорів", 
         "Застереження про конфіденційність"]

         select_chapters = st.multiselect("Використати шаблони", options=chapters, default=chapters[:-1])