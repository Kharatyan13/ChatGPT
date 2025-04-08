import python
import mathematics
import history
import physics
import literature
import sports
import armenian_language
import english
#python
def array():
    print("Զանգվածների հետ կապված հարցերն են՝ \n1.Ի՞նչ է զանգվածը \n2.Ի՞նչ է list \n3.Ի՞նչ է set \n4.Ի՞նչ է tuple \n5.Ի՞նչ է dict")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        array()
def condition():
    print("Պայմանների հետ կապված հարցերն են՝ \n1.Ի՞նչ է պայմանը \n2.Որո՞նք են պայմանի օպերատորները \n3.Ի՞նչ են if,elif և else")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
    question = question.lower()
    if "պայման" in question:
        python.condition()
    elif "օպերատոր" in question:
        python.coditional_operator()
    elif "if" in question or "elif" in question or "else" in question:
        python.if_elif_else()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        condition()

def cycle():
    print("Ցիկլերի հետ կապված հարցերն են՝ \n1.Ի՞նչ է ցիկլը \n2.Ի՞նչ է for \n3.Ի՞նչ է while \n4.Ի՞նչ է foreach")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
    question = question.lower()
    if "ցիկլ" in question:
        python.cycle()
    elif ("for" in question or "ֆոռ" in question) and "each" not in question:
        python.for1()
    elif "while" in question or "վայլ" in question:
        python.while1()
    elif "foreach" in question or "ֆոռիչ" in question:
        python.foreach1()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        cycle()

def math():
    print("math մոդուլի հետ կապված հարցերն են՝ \n1.Ի՞նչ է math մոդուլը \n2.Որո՞նք են math մոդուլի ֆունկցիաները")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
    question = question.lower()
    if ("math" in question or "մաթ" in question) and "ֆ" not in question:
        python.math1()
    elif ("math" in question or "մաթ" in question) and "ֆ" in question:
        python.math_func()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        math()

def strg():
    print("Տողերի հետ կապված հարցերն են՝ \n1.Ի՞նչ է տողը \n2.Որո՞նք են տողերի ֆունկցիաները և մեթոդները")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
    question = question.lower()
    if "տող" in question and "ֆ" not in question:
        python.strg1()
    elif "տող" in question and "ֆ" in question:
        python.method_func()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        strg()

#mathem
def flat():
    print("Հարթաչափության հետ կապված հարցերն են՝ \n1.Ի՞նչ է սեղանը \n2.Ի՞նչ է եռանկյունը \n3.Ի՞նչ է զուգահեռագիծը \n4.Ի՞նչ է շեղանկյունը \n5.Ի՞նչ է ուղղանկյունը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        flat()

def solid():
    print("Տարածաչափության հետ կապված հարցերն են՝ \n1.Ի՞նչ է բուրգը \n2.Ի՞նչ է գունդը \n3.Ի՞նչ է գլանը \n4.Ի՞նչ է կոնը \n5.Ի՞նչ է ուղղանկյունանիստը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        solid()


def trigon():
    print("Տրիգոնոմետրիայի հետ կապված հարցերն են՝ 1.Ի՞նչ է կոսինուսը 2.Ի՞նչ է սինուսը 3.Ի՞նչ է տանգեսը 4.Ի՞նչ է կոտանգեսը 5.Ի՞նչ են արկերը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        trigon()


def algebra():
    print("Հանրահաշվի հետ կապված հարցերն են՝ \n1.Ի՞նչ տեսակի թվեր կան \n2.Որո՞նք են թվաբանական գործողությունները \n3.Ի՞նչ է կոտորակը \n4.Որո՞նք են կրճատ բազմապատկման բանաձևերը \n5.Ի՞նչ է քառակուսային հավասարումը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        algebra()


def theorem():
    print("Մաթեմատիկական թեորեմների հետ կապված հարցերն են՝ \n1.Ո՞րն է Պյութագորասի թեորեմը \n2.Ո՞րն է Թալեսի թեորեմը \n3.Ո՞րն է Բեզուի թեորեմը \n4.Ո՞րն է Սինուսների թեորեմը \n5.Ո՞րն է Կոսինուսների թեորեմը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        theorem()

#patm
def artashesyan():
    print("Արտաշեսյանների հետ կապված հարցերն են՝ \n1.Թագավորության ստեղծումը \n2.Թագավորության վերելքը \n3.Թագավորության անկումը \n4.Արտաշեսյանների դիցարանը \n5.Թագավորության սահմանները")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        artashesyan()

def arshakuni():
    print("Արշակունիների հետ կապված հարցերն են՝ \n1.Թագավորության ստեղծումը \n2.Թագավորության վերելքը \n3.Թագավորության անկումը \n4.«Արշակ և Շապուհ» ավանդազրույցը \n5.Քրիստոնեության ընդունումը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        arshakuni()

def bagratuni():
    print("Բագրատունիների հետ կապված հարցերն են՝ \n1.Թագավորության ստեղծումը \n2.Թագավորության վերելքը \n3.Թագավորության անկումը \n4.Սևի ճակատամարտը \n5.Մանազկերտի ճակատամարտը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        bagratuni()

def rubinyan():
    print("Ռուբինյանների հետ կապված հարցերն են՝ \n1.Կիլիկիայի ստեղծումը \n2.Կիլիկիայի վերելքը \n3.Կիլիկիայի անկումը \n4.Թագավորության ընդունում \n5.Ակտիվ դիվանագիտությունը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        rubinyan()

def first():
    print("Հայաստանի Առաջին Հանրապետության հետ կապված հարցերն են՝ \n1.Մայիսյան հերոսամարտերը \n2.Հանրապետության ստեղծումը \n3.Հանրապետության անկում \n4.Հանրապետության խորհրդայնացման սկիզբը \n5.Հանրապետության դիվանագիտությունը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        first()

def second():
    print("Հայաստանի Խորհրդային Սոցիալիստական Հանրապետության հետ կապված հարցերն են՝ \n1.ՀԽՍՀ-ի ստեղծումը \n2.ՀԽՍՀ-ի անկումը \n3.Հայերի մասնակցությունը Հայրենական պատերազմում \n4.ՀԽՍՀ-ի գիտական առաջընթացը \n5.Սումգայիթյան ողբերգությունը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        second()

def third():
    print("Հայաստանի Երրորդ Հանրապետության հետ կապված հարցերն են՝ \n1.ՀՀ-ի ստեղծումը \n2.Արցախյան առաջին պատերազմը \n3.Արցախյան երկրորդ պատերազմը \n4.Թավշյա հեղափոխությունը \n5.ՀՀ-ի ներկայիս դիվանագիտությունը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        third()

#fizika
def astro():
    print("Աստղագիտության հետ կապված հարցերն են՝ \n1.Արեգակնային համակարգը \n2.Ծիր Կաթին գալակտիկան \n3.Ինչո՞ւ են Ծիր Կաթինին այլ կերպ անվանում Հարդագողի Ճանապարհ \n4.Ի՞նչ է աստղը \n5.Ի՞նչ է հեռադիտակը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        astro()

def physic():
    print("Ֆիզիկայի հետ կապված հարցերն են՝ \n1.Ի՞նչ է ուժը \n2.Նյուտոնի առաջին օրենք \n3.Նյուտոնի երկրորդ օրենք \n4.Նյուտոնի երրորդ օրենք \n5.Ի՞նչ է աշխատանքը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        physic()

#angl
def present():
    print("Ներկա ժամանակի հետ կապված հարցերն են՝ \n1.Ո՞րն է Present Simple \n2.Ո՞րն է Present Continuous \n3.Ո՞րն է Present Perfect \n4.Ո՞րն է Present Perfect Continuous")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        present()

def past():
    print("Անցյալ ժամանակի հետ կապված հարցերն են՝ \n1.Ո՞րն է Past Simple \n2.Ո՞րն է Past Continuous \n3.Ո՞րն է Past Perfect \n4.Ո՞րն է Past Perfect Continuous")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        past()

def future():
    print("Ապառնի ժամանակի հետ կապված հարցերն են՝ \n1.Ո՞րն է Future Simple \n2.Ո՞րն է Future Continuous \n3.Ո՞րն է Future Perfect \n4.Ո՞րն է Future Perfect Continuous")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "simple" in harc:
        english.fs()
    elif "conti" in harc and "perfect" not in harc:
        english.fc()
    elif "perfect" in harc and "conti" not in harc:
        english.fp()
    elif "perfect" in harc and "conti" in harc:
        english.fpc()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        future()

#sport
def foot():
    print("Ֆուտբոլի հետ կապված հարցերն են՝ \n1.Ի՞նչ է Ոսկե գնդակը \n2.Ի՞նչ է ՖԻՖԱ-ն \n3.Ի՞նչ է ՈՒԵՖԱ-ն \n4.Ի՞նչ է Ոսկե խաղակոշիկը \n5.Հայերը ֆուտբոլում")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        foot()

def basket():
    print("Բասկետբոլի հետ կապված հարցերն են՝ \n1.Ի՞նչ է ՆԲԱ \n2.Ո՞րն է ՖԻԲԱ աշխարհի գավաթը \n3.Ի՞նչ է ԵվրոԼիգան \n4.Հայերը բասկետբոլում")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        basket()

def valley():
    print("Վոլեյբոլի հետ կապված հարցերն են՝ 1.Ի՞նչ է վոլեյբոլի չեմպիոնների լիգան 2.Ո՞րն է Ոսկե գնդակը 3.Ի՞նչ է աշխարհի գավաթը 4.Հայերը վոլեյբոլում")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        valley()


def f1():
    print("Ֆորմուլա 1-ի հետ կապված հարցերն են՝ \n1.Ի՞նչ է Կոնստրուկտորների գավաթը \n2.Ի՞նչ է բոլիդը \n3.Ի՞նչ է Գրան Պրին")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
    question = question.lower()
    if "գավաթ" in question:
        sports.constructor()
    elif "բոլիդ" in question:
        sports.bolid()
    elif "գրան" in question:
        sports.grand_prix()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        f1()

def olymp():
    print("Օլիմպիական խաղերի հետ կապված հարցերն են՝ \n1.Որո՞նք են խորհրդանիշները և ի՞նչ են նշանակում \n2.Ինչպե՞ս են ծագել օլիմպիական խաղերը \n3.Հայերն օլիմպիական խաղերում \n4.Ի՞նչ սպորտաձևեր են ներառված")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        olymp()

#hayoc lezu
def jam():
    print("Հայոց լեզվի ժամանակաձևերի հետ կապված հարցերն են՝ \n1.Ո՞րն է անկատար ներկան \n2.Ո՞րն է անցյալ անկատարը \n3.Ո՞րն է վաղակատար ներկան \n4.Ո՞րն է անցյալ վաղակատարը \n5.Ո՞րն է անցյալ ապակատարը \n6.Ո՞րն է անցյալ կատարյալը \n7.Ո՞րն է սահմանական ապառնին")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        jam()

def exanak():
    print("Եղանակների հետ կապված հարցերն են՝ \n1.Ո՞րն է սահմանական եղանակը \n2.Ո՞րն է ըղձական եղանակը \n3.Ո՞րն է ենթադրական եղանակը \n4.Ո՞րն է հարկադրական եղանակը \n5.Ո՞րն է հրամայական եղանակը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        exanak()

def xosq():
    print("Խոսքի մասերի հետ կապված հարցերն են՝ \n1.Ո՞րն է գոյական անունը \n2.Ո՞րն է թվական անունը \n3.Ո՞րն է ածական անունը \n4.Ո՞րն է դերանունը \n5.Ո՞րն է բայը \n6.Ո՞րն է մակբայը \n7.Ո՞րն է կապը \n8.Ո՞րն է շաղկապը \n9.Ո՞րն է վերաբերականը \n10.Ո՞րն է ձայնարկությունը")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
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
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        xosq()

def lezvi_patm():
    print("Հայոց լեզվի հետ կապված հարցերն են՝ \n1.Գրաբար \n2.Միջին հայերեն \n3.Աշխարհաբար")
    question = input("Գրեք, թե ինչ հարց ունեք = ")
    question = question.lower()
    if "գրա" in question:
        armenian_language.grabar()
    elif "միջին" in question:
        armenian_language.mijin_hayeren()
    elif "աշխարհ" in question:
        armenian_language.ashxarhabar()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        lezvi_patm()

#grak
def tum():

def abov():

def mash():

def nar():

def sn():
