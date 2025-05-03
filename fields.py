import python
import mathematics
import history
import physics
import literature
import sports
import armenian_language
import english
import diplomacy
import geography
import time
#python
def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)

def array():
    slow_print("Զանգվածների հետ կապված հարցերն են՝ \n1.Զանգվածը \n2.list \n3.set \n4.tuple \n5.dict\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "զանգված" in question:
        python.array1()
    elif "list" in question or "լիստ" in question:
        python.list1()
    elif "set" in question or "սեթ" in question:
        python.set1()
    elif "tuple" in question or "թապլ" in question:
        python.tuple1()
    elif "dict" in question or "dictionary" in question or "դիքտ" in question or "դիքշնռի" in question:
        python.dict1()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        array()

def condition():
    slow_print("Պայմանների հետ կապված հարցերն են՝ \n1.Պայմանը \n2.Պայմանի օպերատորները \n3.if,elif և else\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "պայման" in question:
        python.condition()
    elif "օպերատոր" in question:
        python.coditional_operator()
    elif "if" in question or "elif" in question or "else" in question:
        python.if_elif_else()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        condition()

def cycle():
    slow_print("Ցիկլերի հետ կապված հարցերն են՝ \n1.Ցիկլը \n2.for \n3.while\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "ցիկլ" in question:
        python.cycle()
    elif ("for" in question or "ֆոռ" in question) and "each" not in question:
        python.for1()
    elif "while" in question or "վայլ" in question:
        python.while1()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        cycle()

def math():
    slow_print("math մոդուլի հետ կապված հարցերն են՝ \n1.math մոդուլը \n2.math մոդուլի ֆունկցիաները\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if ("math" in question or "մաթ" in question) and "ֆ" not in question:
        python.math1()
    elif ("math" in question or "մաթ" in question) and "ֆ" in question:
        python.math1()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        math()

def strg():
    slow_print("Տողերի հետ կապված հարցերն են՝ \n1.Տողը \n2.Տողերի ֆունկցիաները և մեթոդները\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "տող" in question and "ֆ" not in question:
        python.strg1()
    elif ("տող" in question and "ֆունկ" in question) or ("տող" in question and "մեթ" in question):
        python.strg1()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        strg()


#mathem
def flat():
    slow_print("Հարթաչափության հետ կապված հարցերն են՝ \n1.Սեղանը \n2.Եռանկյունը \n3.Զուգահեռագիծը \n4.Շեղանկյունը \n5.Ուղղանկյունը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "սեղան" in question:
        mathematics.trapezoid()
    elif "եռան" in question:
        mathematics.triangle()
    elif "զուգահեռ" in question:
        mathematics.parallelogram()
    elif "շեղան" in question:
        mathematics.rhombus()
    elif "ուղղան" in question:
        mathematics.rectangle()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        flat()

def solid():
    slow_print("Տարածաչափության հետ կապված հարցերն են՝ \n1.Բուրգը \n2.Գունդը \n3.Գլանը \n4.Կոնը \n5.Ուղղանկյունանիստը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "բուրգ" in question:
        mathematics.pyramid()
    elif "գունդ" in question or "գնդ" in question:
        mathematics.ball()
    elif "գլան" in question:
        mathematics.cylinder()
    elif "կոն" in question:
        mathematics.cone()
    elif "ուղղ" in question:
        mathematics.rectangular()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        solid()

def trigon():
    slow_print("Տրիգոնոմետրիայի հետ կապված հարցերն են՝ \n1.Կոսինուսը \n2.Սինուսը \n3.Տանգեսը \n4.Կոտանգեսը \n5.Արկերը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "կոս" in question:
        mathematics.cos()
    elif "սին" in question:
        mathematics.sin()
    elif "տան" in question and "կո" not in question:
        mathematics.tg()
    elif "կոտ" in question:
        mathematics.ctg()
    elif "արկ" in question or "առկ" in question:
        mathematics.arc()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        trigon()

def algebra():
    slow_print("Հանրահաշվի հետ կապված հարցերն են՝ \n1.Թվերի տեսակներ \n2.Թվաբանական գործողությունները \n3.Կոտորակը \n4.Կրճատ բազմապատկման բանաձևերը \n5.Քառակուսային հավասարումը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "տեսակ" in question:
        mathematics.types_of_numbers()
    elif "գործող" in question:
        mathematics.operations()
    elif "կոտոր" in question:
        mathematics.fraction()
    elif "կրճատ" in question:
        mathematics.multi_formulas()
    elif "քառա" in question:
        mathematics.quadratic()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        algebra()

def theorem():
    slow_print("Մաթեմատիկական թեորեմների հետ կապված հարցերն են՝ \n1.Պյութագորասի թեորեմը \n2.Թալեսի թեորեմը \n3.Բեզուի թեորեմը \n4.Սինուսների թեորեմը \n5.Կոսինուսների թեորեմը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "պյու" in question:
        mathematics.pyut()
    elif "թալ" in question:
        mathematics.tales()
    elif "բեզ" in question:
        mathematics.bezu()
    elif "սին" in question and "կո" not in question:
        mathematics.sin_teo()
    elif "կոսին" in question:
        mathematics.cos_teo()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        theorem()


#patm
def artashesyan():
    slow_print("Արտաշեսյանների հետ կապված հարցերն են՝ \n1.Թագավորության ստեղծումը \n2.Թագավորության վերելքը \n3.Թագավորության անկումը \n4.Արտաշեսյանների դիցարանը \n5.Թագավորության սահմանները\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "ստեղ" in question:
        history.art_creation()
    elif "վեր" in question:
        history.art_rise()
    elif "անկ" in question:
        history.art_collapse()
    elif "դիցա" in question:
        history.art_cathedral()
    elif "սահ" in question:
        history.art_area()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        artashesyan()

def arshakuni():
    slow_print("Արշակունիների հետ կապված հարցերն են՝ \n1.Թագավորության ստեղծումը \n2.Թագավորության վերելքը \n3.Թագավորության անկումը \n4.«Արշակ և Շապուհ» ավանդազրույցը \n5.Քրիստոնեության ընդունումը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "ստեղ" in question:
        history.arsh_creation()
    elif "վեր" in question:
        history.arsh_rise()
    elif "անկ" in question:
        history.arsh_collapse()
    elif "շապուհ" in question:
        history.arsh_shapuh()
    elif "քրիս" in question:
        history.christianity()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        arshakuni()

def bagratuni():
    slow_print("Բագրատունիների հետ կապված հարցերն են՝ \n1.Թագավորության ստեղծումը \n2.Թագավորության վերելքը \n3.Թագավորության անկումը \n4.Սևի ճակատամարտը \n5.Մանազկերտի ճակատամարտը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "ստեղ" in question:
        history.bagr_creation()
    elif "վեր" in question:
        history.bagr_rise()
    elif "անկ" in question:
        history.bagr_collapse()
    elif "սևան" in question:
        history.sevan()
    elif "մանազ" in question:
        history.manazkert()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        bagratuni()

def rubinyan():
    slow_print("Ռուբինյանների հետ կապված հարցերն են՝ \n1.Կիլիկիայի ստեղծումը \n2.Կիլիկիայի վերելքը \n3.Կիլիկիայի անկումը \n4.Թագավորության ընդունում \n5.Ակտիվ դիվանագիտությունը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "ստեղ" in question:
        history.rub_creation()
    elif "վեր" in question:
        history.rub_rise()
    elif "անկ" in question:
        history.rub_collapse()
    elif "թագ" in question:
        history.rub_kingdom()
    elif "դիվա" in question:
        history.rub_diplomacy()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        rubinyan()

def first():
    slow_print("Հայաստանի Առաջին Հանրապետության հետ կապված հարցերն են՝ \n1.Մայիսյան հերոսամարտերը \n2.Հանրապետության ստեղծումը \n3.Հանրապետության անկում \n4.Հանրապետության խորհրդայնացման սկիզբը \n5.Հանրապետության դիվանագիտությունը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "մայիս" in question:
        history.mayis()
    elif "ստեղ" in question:
        history.creation1()
    elif "անկ" in question:
        history.collapse1()
    elif "խո" in question:
        history.communism()
    elif "դիվան" in question:
        history.diplomacy1()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        first()

def second():
    slow_print("Հայաստանի Խորհրդային Սոցիալիստական Հանրապետության հետ կապված հարցերն են՝ \n1.ՀԽՍՀ-ի ստեղծումը \n2.ՀԽՍՀ-ի անկումը \n3.Հայերի մասնակցությունը Հայրենական պատերազմում \n4.ՀԽՍՀ-ի գիտական առաջընթացը \n5.Սումգայիթյան ողբերգությունը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "ստեղ" in question:
        history.creation2()
    elif "անկ" in question:
        history.collapse2()
    elif "հայրենական" in question:
        history.patriotic()
    elif "գիտա" in question:
        history.scientific()
    elif "սումգա" in question:
        history.sumgayit()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        second()

def third():
    slow_print("Հայաստանի Երրորդ Հանրապետության հետ կապված հարցերն են՝ \n1.ՀՀ-ի ստեղծումը \n2.Արցախյան առաջին պատերազմը \n3.Արցախյան երկրորդ պատերազմը \n4.Թավշյա հեղափոխությունը \n5.ՀՀ-ի ներկայիս դիվանագիտությունը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "ստեղ" in question:
        history.creation3()
    elif "առաջին" in question:
        history.arcax1()
    elif "երկրորդ" in question:
        history.arcax2()
    elif "թավ" in question:
        history.tavshya()
    elif "դիվան" in question:
        history.diplomacy3()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        third()

#fizika
def astro():
    slow_print("Աստղագիտության հետ կապված հարցերն են՝ \n1.Արեգակնային համակարգը \n2.Ծիր Կաթին գալակտիկան \n3.Ինչո՞ւ են Ծիր Կաթինին այլ կերպ անվանում Հարդագողի Ճանապարհ \n4.Աստղը \n5.Հեռադիտակը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "արեգակ" in question:
        physics.solar_system()
    elif "ծիր" in question and "հարդագող" not in question:
        physics.milky_way()
    elif "հարդագող" in question:
        physics.hardagoxi()
    elif "աստղ" in question:
        physics.star()
    elif "հեռադիտ" in question:
        physics.telescope()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        astro()

def physic():
    slow_print("Ֆիզիկայի հետ կապված հարցերն են՝ \n1.Ուժը \n2.Նյուտոնի առաջին օրենք \n3.Նյուտոնի երկրորդ օրենք \n4.Նյուտոնի երրորդ օրենք \n5.Աշխատանքը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "ուժ" in question:
        physics.force()
    elif "առաջին" in question or "1-ին" in question or "1ին" in question:
        physics.nyut1()
    elif "երկրորդ" in question or "2-րդ" in question or "2րդ" in question:
        physics.nyut2()
    elif "երրորդ" in question or "3-րդ" in question or "3րդ" in question:
        physics.nyut3()
    elif "աշխատան" in question:
        physics.work()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        physic()

#angl
def present():
    slow_print("Ներկա ժամանակի հետ կապված հարցերն են՝ \n1.Present Simple \n2.Present Continuous \n3.Present Perfect \n4.Present Perfect Continuous\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "simple" in question:
        english.ps()
    elif "conti" in question and "perfect" not in question:
        english.pc()
    elif "perfect" in question and "conti" not in question:
        english.pp()
    elif "perfect" in question and "conti" in question:
        english.ppc()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        present()

def past():
    slow_print("Անցյալ ժամանակի հետ կապված հարցերն են՝ \n1.Past Simple \n2.Past Continuous \n3.Past Perfect \n4.Past Perfect Continuous\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "simple" in question:
        english.pas()
    elif "conti" in question and "perfect" not in question:
        english.pac()
    elif "perfect" in question and "conti" not in question:
        english.pap()
    elif "perfect" in question and "conti" in question:
        english.papc()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        past()

def future():
    slow_print("Ապառնի ժամանակի հետ կապված հարցերն են՝ \n1.Future Simple \n2.Future Continuous \n3.Future Perfect \n4.Future Perfect Continuous\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "simple" in question:
        english.fs()
    elif "conti" in question and "perfect" not in question:
        english.fc()
    elif "perfect" in question and "conti" not in question:
        english.fp()
    elif "perfect" in question and "conti" in question:
        english.fpc()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        future()


#sport
def foot():
    slow_print("Ֆուտբոլի հետ կապված հարցերն են՝ \n1.Ոսկե գնդակը \n2.ՖԻՖԱ \n3.ՈՒԵՖԱ \n4.Ոսկե խաղակոշիկը \n5.Հայերը ֆուտբոլում\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "գնդակ" in question:
        sports.ballondor()
    elif "ֆիֆա" in question:
        sports.fifa()
    elif "ուեֆա" in question:
        sports.uefa()
    elif "կոշիկ" in question:
        sports.goldenboot()
    elif "հայ" in question:
        sports.armenian_foot()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        foot()

def basket():
    slow_print("Բասկետբոլի հետ կապված հարցերն են՝ \n1.ՆԲԱ \n2.ՖԻԲԱ աշխարհի գավաթ \n3.ԵվրոԼիգա \n4.Հայերը բասկետբոլում\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "նբա" in question:
        sports.nba()
    elif "ֆիբա" in question:
        sports.fiba_wc()
    elif "եվրո" in question:
        sports.euroligue()
    elif "հայ" in question:
        sports.armenian_basket()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        basket()

def valley():
    slow_print("Վոլեյբոլի հետ կապված հարցերն են՝ 1.Վոլեյբոլի չեմպիոնների լիգան 2.Ոսկե գնդակը 3.Աշխարհի գավաթը 4.Հայերը վոլեյբոլում\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "չեմպիոն" in question:
        sports.champions_ligue()
    elif "ոսկե" in question:
        sports.goldenball()
    elif "աշխարհ" in question:
        sports.valleywc()
    elif "հայ" in question:
        sports.armenians_valley()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        valley()

def f1():
    slow_print("Ֆորմուլա 1-ի հետ կապված հարցերն են՝ \n1.Կոնստրուկտորների գավաթը \n2.Բոլիդը \n3.Գրան Պրին\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "գավաթ" in question:
        sports.constructor()
    elif "բոլիդ" in question:
        sports.bolid()
    elif "գրան" in question:
        sports.grand_prix()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        f1()

def olymp():
    slow_print("Օլիմպիական խաղերի հետ կապված հարցերն են՝ \n1.Խորհրդանիշներ \n2.Ծագում \n3.Հայերն օլիմպիական խաղերում \n4.Ներառված սպորտաձևեր\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "խորհր" in question:
        sports.olympic_symbol()
    elif "ծագ" in question:
        sports.origin()
    elif "հայ" in question:
        sports.hayer_olymp()
    elif "սպորտաձ" in question:
        sports.olympic_sports()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        olymp()


#hayoc lezu
def jam():
    slow_print("Հայոց լեզվի ժամանակաձևերի հետ կապված հարցերն են՝ \n1.Անկատար ներկան \n2.Անցյալ անկատարը \n3.Վաղակատար ներկան \n4.Անցյալ վաղակատարը \n5.Անցյալ ապակատարը \n6.Անցյալ կատարյալը \n7.Սահմանական ապառնին\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "անկատ" in question and "ներկ" in question:
        armenian_language.ankatar_nerka()
    elif "անկատ" in question and "անց" in question:
        armenian_language.ankatar_ancyal()
    elif "վաղ" in question and "ներ" in question:
        armenian_language.vaxakatar_nerka()
    elif "վաղ" in question and "անց" in question:
        armenian_language.vaxakatar_ancyal()
    elif "ապա" in question and "անց" in question:
        armenian_language.apakatar_ancyal()
    elif "կատարյալ" in question and "անց" in question:
        armenian_language.kataryal_ancyal()
    elif "ապառնի" in question:
        armenian_language.sahmanakan_aparni()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        jam()

def exanak():
    slow_print("Եղանակների հետ կապված հարցերն են՝ \n1.Սահմանական եղանակը \n2.Ըղձական եղանակը \n3.Ենթադրական եղանակը \n4.Հարկադրական եղանակը \n5.Հրամայական եղանակը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "սահման" in question:
        armenian_language.sahmanakan()
    elif "ըղձա" in question:
        armenian_language.yxdzakan()
    elif "ենթա" in question:
        armenian_language.entadrakan()
    elif "հարկա" in question:
        armenian_language.harkadrakan()
    elif "հրա" in question:
        armenian_language.hramayakan()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        exanak()

def xosq():
    slow_print("Խոսքի մասերի հետ կապված հարցերն են՝ \n1.Գոյական անունը \n2.Թվական անունը \n3.Ածական անունը \n4.Դերանունը \n5.Բայը \n6.Մակբայը \n7.Կապը \n8.Շաղկապը \n9.Վերաբերականը \n10.Ձայնարկությունը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "գոյա" in question:
        armenian_language.goyakan()
    elif "թվա" in question:
        armenian_language.tvakan()
    elif "ածակ" in question:
        armenian_language.acakan()
    elif "դերան" in question:
        armenian_language.deranun()
    elif "բայ" in question and "մակ" not in question:
        armenian_language.bay()
    elif "մակբայ" in question:
        armenian_language.makbay()
    elif "կապ" in question and "շաղ" not in question:
        armenian_language.kap()
    elif "շաղկապ" in question:
        armenian_language.shaxkap()
    elif "վերաբեր" in question:
        armenian_language.veraberakan()
    elif "ձայնար" in question:
        armenian_language.dzajnarkutyun()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        xosq()

def lezvi_patm():
    slow_print("Հայոց լեզվի հետ կապված հարցերն են՝ \n1.Գրաբար \n2.Միջին հայերեն \n3.Աշխարհաբար\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "գրա" in question:
        armenian_language.grabar()
    elif "միջին" in question:
        armenian_language.mijin_hayeren()
    elif "աշխարհ" in question:
        armenian_language.ashxarhabar()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        lezvi_patm()


#grak
def tum():
    slow_print("Հովհաննես Թումանյանի հետ կապված հարցերն են՝ \n1.Կյանքը \n2.Ստեղծագործությունները \n3.«Ամենայն Հայոց Բանաստեղծ» անվան ստացումը \n4.Նրա դերը գրականության մեջ \n5.Թարգմանչական գործը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "կյան" in question:
        literature.tum_life()
    elif "ստեղծ" in question:
        literature.tum_creation()
    elif "ամենայն" in question:
        literature.amenayn_hayoc_ban()
    elif "դեր" in question:
        literature.tum_role()
    elif "թարգ" in question:
        literature.tum_translations()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        tum()

def abov():
    slow_print("Խաչատուր Աբովյանի հետ կապված հարցերն են՝ \n1.Կյանքը \n2.Ստեղծագործությունները \n3.Նրա դերը գրականության մեջ \n4.Անհետացման հետ կապված վարկածները \n5.«Վերք Հայաստանի» պատմավեպը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "կյան" in question:
        literature.abov_life()
    elif "ստեղ" in question:
        literature.abov_creation()
    elif "դեր" in question:
        literature.abov_role()
    elif "անհետ" in question:
        literature.abov_disappearance()
    elif "վերք" in question:
        literature.verq_hay()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        abov()

def mash():
    slow_print("Մեսրոպ Մաշտոցի հետ կապված հարցերն են՝ \n1.Կյանքը \n2.Հայ գրերի գյուտը \n3.Ստեղծագործությունները \n4.Այլ ազգերի գրերի գյուտը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "կյան" in question:
        literature.mash_life()
    elif "հայ" in question:
        literature.invention_of_writing()
    elif "ստեղ" in question:
        literature.mash_creation()
    elif "այլ" in question:
        literature.other_nations()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        mash()

def nar():
    slow_print("Գրիգոր Նարեկացու հետ կապված հարցերն են՝ \n1.Կյանքը \n2.Ստեղծագործությունները \n3.«Մատյան ողբերգության» կամ «Նարեկ» գիրքը \n4.Հոգևոր կյանքը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "կյա" in question and "հոգ" not in question:
        literature.nar_life()
    elif "ստեղ" in question:
        literature.nar_creation()
    elif "նարեկ" in question and "մատյան" in question:
        literature.narek()
    elif "հոգ" in question:
        literature.nar_spiritual_life()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        nar()

def sn():
    slow_print("Սայաթ Նովայի հետ կապված հարցերն են՝ \n1.Կյանքը \n2.Ստեղծագործությունները \n3.Նրա հետ կապված վեճերը \n4.Խաղերը\n")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "կյան" in question:
        literature.sn_life()
    elif "ստեղ" in question:
        literature.sn_creation()
    elif "վեճ" in question:
        literature.sn_debate()
    elif "խաղ" in question:
        literature.sn_xaxer()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        sn()


#divanagitutyun
def first_world():
    slow_print("""Առաջին աշխարհի հետ կապված հարցերն են՝
    1.Դիվանագիտություն
    2.Երկրներ
    3.Ալիանսներ և միություններ
    4.Առաջացում\n""")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "դիվան" in question:
        diplomacy.diplomacy1()
    elif "երկ" in question:
        diplomacy.countries1()
    elif "միու" in question:
        diplomacy.union1()
    elif "առաջ" in question or "ստեղ" in question:
        diplomacy.creation1()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        first_world()

def second_world():
    slow_print("""Երկրորդ աշխարհի հետ կապված հարցերն են՝
    1.Դիվանագիտություն
    2.Երկրներ
    3.Ալիանսներ և միություններ
    4.Առաջացում\n""")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "դիվան" in question:
        diplomacy.diplomacy2()
    elif "երկ" in question:
        diplomacy.countries2()
    elif "միու" in question:
        diplomacy.union2()
    elif "առաջ" in question or "ստեղ" in question:
        diplomacy.creation2()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        second_world()

def third_world():
    slow_print("""Երրորդ աշխարհի հետ կապված հարցերն են՝
    1.Դիվանագիտություն
    2.Երկրներ
    3.Ալիանսներ և միություններ
    4.Առաջացում\n""")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "դիվան" in question:
        diplomacy.diplomacy3()
    elif "երկ" in question:
        diplomacy.countries3()
    elif "միու" in question:
        diplomacy.union3()
    elif "առաջ" in question or "ստեղ" in question:
        diplomacy.creation3()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        third_world()

#ashxarh
def leading_countries():
    slow_print("""Առաջատար երկրների հետ կապված հարցերն են՝
    1.Տնտեսություն
    2.Արտադրություն
    3.Բնակչություն
    4.Հանքահանում
    5.Ռազմական ուժ\n""")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "տնտես" in question:
        geography.economy()
    elif "արտադ" in question:
        geography.manufacture()
    elif "բնակ" in question:
        geography.population()
    elif "հանքա" in question:
        geography.mining()
    elif "ուժ" in question:
        geography.military()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        leading_countries()

def continents():
    slow_print("""Աշխարհամասերի հետ կապված հարցերն են՝
    1.Եվրոպա
    2.Ասիա
    3.Աֆրիկա
    4.Օվկիանիա
    5.Ամերիկա
    6.Անտարկտիդա\n""")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "եվրոպա" in question:
        geography.europe()
    elif "ասիա" in question:
        geography.asia()
    elif "աֆրիկա" in question:
        geography.africa()
    elif "օվկիանիա" in question:
        geography.oceania()
    elif "ամերիկա" in question:
        geography.america()
    elif "անտարկտիդա" in question:
        geography.antarctida()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        continents()

def race():
    slow_print("""Մարդկային ռասաների հետ կապված հարցերն են՝
    1.Նեգրոիդ
    2.Եվրոպոիդ
    3.Մոնղոլոիդ
    4.Ավստրալոիդ\n""")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "նեգր" in question:
        geography.negroid()
    elif "եվրո" in question:
        geography.europoid()
    elif "մոնղ" in question:
        geography.mongoloid()
    elif "ավստ" in question:
        geography.ausraloid()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        race()

def water():
    slow_print("""Ջրային աշխարհի հետ կապված հարցերն են՝
    1.Լճեր
    2.Ծովեր
    3.Օվկիանոսներ
    4.Գետեր
    5.Ջրվեժներ
    6.Ծոցեր
    7.Ջրանցքներ\n""")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "ճ" in question:
        geography.lake()
    elif "ծով" in question:
        geography.sea()
    elif "օվկ" in question:
        geography.ocean()
    elif "գետ" in question:
        geography.river()
    elif "ջրվեժ" in question:
        geography.waterfall()
    elif "ծոց" in question:
        geography.bay()
    elif "ջրանցք" in question:
        geography.canal()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        water()

def religion():
    slow_print("""Կրոնների հետ կապված հարցերն են՝
    1.Քրիստոնեություն
    2.Իսլամ կամ Մահմեդականություն
    3.Հինդուիզմ
    4.Բուդդիզմ
    5.Հուդայականություն\n""")
    question = input("Գրեք, թե ինչ հարց ունեք՝ ")
    question = question.lower()
    if "քրիստ" in question:
        geography.christ()
    elif "իսլամ" in question or "մահմե" in question:
        geography.islam()
    elif "հինդու" in question:
        geography.huda()
    elif "բուդ" in question:
        geography.budda()
    elif "հուդա" in question:
        geography.israel()
    else:
        slow_print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:\n")
        religion()
