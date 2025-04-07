import harcer_python
import harcer_mathem
import harcer_patm
import harcer_fizika
import harcer_grak
import harcer_sport
import harcer_hayoc_lezu
import harcer_angl
#python
def zangvac():
    print("Զանգվածների հետ կապված հարցերն են՝ \n1.Ի՞նչ է զանգվածը \n2.Ի՞նչ է list \n3.Ի՞նչ է set \n4.Ի՞նչ է tuple \n5.Ի՞նչ է dict")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "զանգված" in harc:
        harcer_python.zangvac1()
    elif "list" in harc or "լիստ" in harc:
        harcer_python.list1()
    elif "set" in harc or "սեթ" in harc:
        harcer_python.set1()
    elif "tuple" in harc or "թապլ" in harc:
        harcer_python.tuple1()
    elif "dict" in harc or "dictionary" in harc or "դիքտ" in harc or "դիքշնռի" in harc:
        harcer_python.dect1()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        zangvac()
def pajman():
    print("Պայմանների հետ կապված հարցերն են՝ \n1.Ի՞նչ է պայմանը \n2.Որո՞նք են պայմանի օպերատորները \n3.Ի՞նչ են if,elif և else")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "պայման" in harc:
        harcer_python.payman1()
    elif "օպերատոր" in harc:
        harcer_python.payman_operator()
    elif "if" in harc or "elif" in harc or "else" in harc:
        harcer_python.if_elif_else()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        pajman()

def cikl():
    print("Ցիկլերի հետ կապված հարցերն են՝ \n1.Ի՞նչ է ցիկլը \n2.Ի՞նչ է for \n3.Ի՞նչ է while \n4.Ի՞նչ է foreach")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "ցիկլ" in harc:
        harcer_python.cikl1()
    elif ("for" in harc or "ֆոռ" in harc) and "each" not in harc:
        harcer_python.for1()
    elif "while" in harc or "վայլ" in harc:
        harcer_python.while1()
    elif "foreach" in harc or "ֆոռիչ" in harc:
        harcer_python.foreach1()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        cikl()

def mathm():
    print("math մոդուլի հետ կապված հարցերն են՝ \n1.Ի՞նչ է math մոդուլը \n2.Որո՞նք են math մոդուլի ֆունկցիաները")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if ("math" in harc or "մաթ" in harc) and "ֆ" not in harc:
        harcer_python.math1()
    elif ("math" in harc or "մաթ" in harc) and "ֆ" in harc:
        harcer_python.math_funk()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        mathm()

def strg():
    print("Տողերի հետ կապված հարցերն են՝ \n1.Ի՞նչ է տողը \n2.Որո՞նք են տողերի ֆունկցիաները և մեթոդները")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "տող" in harc and "ֆ" not in harc:
        harcer_python.tox1()
    elif "տող" in harc and "ֆ" in harc:
        harcer_python.metod_funk()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        strg()

#mathem
def hart():
    print("Հարթաչափության հետ կապված հարցերն են՝ \n1.Ի՞նչ է սեղանը \n2.Ի՞նչ է եռանկյունը \n3.Ի՞նչ է զուգահեռագիծը \n4.Ի՞նչ է շեղանկյունը \n5.Ի՞նչ է ուղղանկյունը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "սեղան" in harc:
        harcer_mathem.sexan()
    elif "եռան" in harc:
        harcer_mathem.er()
    elif "զուգահեռ" in harc:
        harcer_mathem.zugaher()
    elif "շեղան" in harc:
        harcer_mathem.shex()
    elif "ուղղան" in harc:
        harcer_mathem.uxx()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        hart()

def tarac():
    print("Տարածաչափության հետ կապված հարցերն են՝ \n1.Ի՞նչ է բուրգը \n2.Ի՞նչ է գունդը \n3.Ի՞նչ է գլանը \n4.Ի՞նչ է կոնը \n5.Ի՞նչ է ուղղանկյունանիստը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "բուրգ" in harc:
        harcer_mathem.burg()
    elif "գունդ" in harc or "գնդ" in harc:
        harcer_mathem.gund()
    elif "գլան" in harc:
        harcer_mathem.glan()
    elif "կոն" in harc:
        harcer_mathem.kon()
    elif "ուղղ" in harc:
        harcer_mathem.uxx_nist()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        tarac()


def trigon():
    print("Տրիգոնոմետրիայի հետ կապված հարցերն են՝ 1.Ի՞նչ է կոսինուսը 2.Ի՞նչ է սինուսը 3.Ի՞նչ է տանգեսը 4.Ի՞նչ է կոտանգեսը 5.Ի՞նչ են արկերը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "կոս" in harc:
        harcer_mathem.cos()
    elif "սին" in harc:
        harcer_mathem.sin()
    elif "տան" in harc and "կո" not in harc:
        harcer_mathem.tg()
    elif "կոտ" in harc:
        harcer_mathem.ctg()
    elif "արկ" in harc or "առկ" in harc:
        harcer_mathem.arc()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        trigon()


def hanr():
    print("Հանրահաշվի հետ կապված հարցերն են՝ \n1.Ի՞նչ տեսակի թվեր կան \n2.Որո՞նք են թվաբանական գործողությունները \n3.Ի՞նչ է կոտորակը \n4.Որո՞նք են կրճատ բազմապատկման բանաձևերը \n5.Ի՞նչ է քառակուսային հավասարումը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "տեսակ" in harc:
        harcer_mathem.tver_tesak()
    elif "գործող" in harc:
        harcer_mathem.gorc1()
    elif "կոտոր" in harc:
        harcer_mathem.kotorak()
    elif "կրճատ" in harc:
        harcer_mathem.krcat_bazm()
    elif "քառա" in harc:
        harcer_mathem.qarakusayin()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        hanr()


def teorem():
    print("Մաթեմատիկական թեորեմների հետ կապված հարցերն են՝ \n1.Ո՞րն է Պյութագորասի թեորեմը \n2.Ո՞րն է Թալեսի թեորեմը \n3.Ո՞րն է Բեզուի թեորեմը \n4.Ո՞րն է Սինուսների թեորեմը \n5.Ո՞րն է Կոսինուսների թեորեմը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "պյու" in harc:
        harcer_mathem.pyut()
    elif "թալ" in harc:
        harcer_mathem.tales()
    elif "բեզ" in harc:
        harcer_mathem.bezu()
    elif "սին" in harc and "կո" not in harc:
        harcer_mathem.sin_teo()
    elif "կոսին" in harc:
        harcer_mathem.cos_teo()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        teorem()

#patm
def art():
    print("Արտաշեսյանների հետ կապված հարցերն են՝ \n1.Թագավորության ստեղծումը \n2.Թագավորության վերելքը \n3.Թագավորության անկումը \n4.Արտաշեսյանների դիցարանը \n5.Թագավորության սահմանները")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "ստեղ" in harc:
        harcer_patm.art_stexc()
    elif "վեր" in harc:
        harcer_patm.art_ver()
    elif "անկ" in harc:
        harcer_patm.art_ank()
    elif "դիցա" in harc:
        harcer_patm.art_dic()
    elif "սահ" in harc:
        harcer_patm.art_tar()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        art()

def arsh():
    print("Արշակունիների հետ կապված հարցերն են՝ \n1.Թագավորության ստեղծումը \n2.Թագավորության վերելքը \n3.Թագավորության անկումը \n4.«Արշակ և Շապուհ» ավանդազրույցը \n5.Քրիստոնեության ընդունումը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "ստեղ" in harc:
        harcer_patm.arsh_stexc()
    elif "վեր" in harc:
        harcer_patm.arsh_ver()
    elif "անկ" in harc:
        harcer_patm.arsh_ank()
    elif "շապուհ" in harc:
        harcer_patm.arsh_shapuh()
    elif "քրիս" in harc:
        harcer_patm.qristonia()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        arsh()

def bagr():
    print("Բագրատունիների հետ կապված հարցերն են՝ \n1.Թագավորության ստեղծումը \n2.Թագավորության վերելքը \n3.Թագավորության անկումը \n4.Սևի ճակատամարտը \n5.Մանազկերտի ճակատամարտը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "ստեղ" in harc:
        harcer_patm.bagr_stexc()
    elif "վեր" in harc:
        harcer_patm.bagr_ver()
    elif "անկ" in harc:
        harcer_patm.bagr_ank()
    elif "սևան" in harc:
        harcer_patm.sevan()
    elif "մանազ" in harc:
        harcer_patm.manazkert()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        bagr()

def rubin():
    print("Ռուբինյանների հետ կապված հարցերն են՝ \n1.Կիլիկիայի ստեղծումը \n2.Կիլիկիայի վերելքը \n3.Կիլիկիայի անկումը \n4.Թագավորության ընդունում \n5.Ակտիվ դիվանագիտությունը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "ստեղ" in harc:
        harcer_patm.rub_stexc()
    elif "վեր" in harc:
        harcer_patm.rub_ver()
    elif "անկ" in harc:
        harcer_patm.rub_ank()
    elif "թագ" in harc:
        harcer_patm.rub_tag()
    elif "դիվա" in harc:
        harcer_patm.rub_divan()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        rubin()

def arajin():
    print("Հայաստանի Առաջին Հանրապետության հետ կապված հարցերն են՝ \n1.Մայիսյան հերոսամարտերը \n2.Հանրապետության ստեղծումը \n3.Հանրապետության անկում \n4.Հանրապետության խորհրդայնացման սկիզբը \n5.Հանրապետության դիվանագիտությունը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "մայիս" in harc:
        harcer_patm.mayis()
    elif "ստեղ" in harc:
        harcer_patm.stexc1()
    elif "անկ" in harc:
        harcer_patm.ank1()
    elif "խո" in harc:
        harcer_patm.komunism()
    elif "դիվան" in harc:
        harcer_patm.divan1()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        arajin()

def erkrord():
    print("Հայաստանի Խորհրդային Սոցիալիստական Հանրապետության հետ կապված հարցերն են՝ \n1.ՀԽՍՀ-ի ստեղծումը \n2.ՀԽՍՀ-ի անկումը \n3.Հայերի մասնակցությունը Հայրենական պատերազմում \n4.ՀԽՍՀ-ի գիտական առաջընթացը \n5.Սումգայիթյան ողբերգությունը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "ստեղ" in harc:
        harcer_patm.stexc2()
    elif "անկ" in harc:
        harcer_patm.ank2()
    elif "հայրենական" in harc:
        harcer_patm.hayrenakan()
    elif "գիտա" in harc:
        harcer_patm.gitakan()
    elif "սումգա" in harc:
        harcer_patm.sumgayit()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        erkrord()

def errord():
    print("Հայաստանի Երրորդ Հանրապետության հետ կապված հարցերն են՝ \n1.ՀՀ-ի ստեղծումը \n2.Արցախյան առաջին պատերազմը \n3.Արցախյան երկրորդ պատերազմը \n4.Թավշյա հեղափոխությունը \n5.ՀՀ-ի ներկայիս դիվանագիտությունը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "ստեղ" in harc:
        harcer_patm.stexc3()
    elif "առաջին" in harc:
        harcer_patm.arcax1()
    elif "երկրորդ" in harc:
        harcer_patm.arcax2()
    elif "թավ" in harc:
        harcer_patm.tavshya()
    elif "դիվան" in harc:
        harcer_patm.divan3()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        errord()

#fizika
def astgh():
    print("Աստղագիտության հետ կապված հարցերն են՝ \n1.Արեգակնային համակարգը \n2.Ծիր Կաթին գալակտիկան \n3.Ինչո՞ւ են Ծիր Կաթինին այլ կերպ անվանում Հարդագողի Ճանապարհ \n4.Ի՞նչ է աստղը \n5.Ի՞նչ է հեռադիտակը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "արեգակ" in harc:
        harcer_fizika.arev_ham()
    elif "ծիր" in harc and "հարդագող" not in harc:
        harcer_fizika.cir_kath()
    elif "հարդագող" in harc:
        harcer_fizika.cir_kat_anv()
    elif "աստղ" in harc:
        harcer_fizika.astgh1()
    elif "հեռադիտ" in harc:
        harcer_fizika.heraditak()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        astgh()

def fizi():
    print("Ֆիզիկայի հետ կապված հարցերն են՝ \n1.Ի՞նչ է ուժը \n2.Նյուտոնի առաջին օրենք \n3.Նյուտոնի երկրորդ օրենք \n4.Նյուտոնի երրորդ օրենք \n5.Ի՞նչ է աշխատանքը")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "ուժ" in harc:
        harcer_fizika.uj()
    elif "առաջին" in harc or "1-ին" in harc or "1ին" in harc:
        harcer_fizika.nyut1()
    elif "երկրորդ" in harc or "2-րդ" in harc or "2րդ" in harc:
        harcer_fizika.nyut2()
    elif "երրորդ" in harc or "3-րդ" in harc or "3րդ" in harc:
        harcer_fizika.nyut3()
    elif "աշխատան" in harc:
        harcer_fizika.ashxatanq()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        fizi()

#angl
def present():
    print("Ներկա ժամանակի հետ կապված հարցերն են՝ \n1.Ո՞րն է Present Simple \n2.Ո՞րն է Present Continuous \n3.Ո՞րն է Present Perfect \n4.Ո՞րն է Present Perfect Continuous")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "simple" in harc:
        harcer_angl.ps()
    elif "conti" in harc and "perfect" not in harc:
        harcer_angl.pc()
    elif "perfect" in harc and "conti" not in harc:
        harcer_angl.pp()
    elif "perfect" in harc and "conti" in harc:
        harcer_angl.ppc()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        present()

def past():
    print("Անցյալ ժամանակի հետ կապված հարցերն են՝ \n1.Ո՞րն է Past Simple \n2.Ո՞րն է Past Continuous \n3.Ո՞րն է Past Perfect \n4.Ո՞րն է Past Perfect Continuous")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "simple" in harc:
        harcer_angl.pas()
    elif "conti" in harc and "perfect" not in harc:
        harcer_angl.pac()
    elif "perfect" in harc and "conti" not in harc:
        harcer_angl.pap()
    elif "perfect" in harc and "conti" in harc:
        harcer_angl.papc()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        past()

def future():
    print("Ապառնի ժամանակի հետ կապված հարցերն են՝ \n1.Ո՞րն է Future Simple \n2.Ո՞րն է Future Continuous \n3.Ո՞րն է Future Perfect \n4.Ո՞րն է Future Perfect Continuous")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "simple" in harc:
        harcer_angl.fs()
    elif "conti" in harc and "perfect" not in harc:
        harcer_angl.fc()
    elif "perfect" in harc and "conti" not in harc:
        harcer_angl.fp()
    elif "perfect" in harc and "conti" in harc:
        harcer_angl.fpc()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        future()

#sport
def foot():
    print("Ֆուտբոլի հետ կապված հարցերն են՝ \n1.Ի՞նչ է Ոսկե գնդակը \n2.Ի՞նչ է ՖԻՖԱ-ն \n3.Ի՞նչ է ՈՒԵՖԱ-ն \n4.Ի՞նչ է Ոսկե խաղակոշիկը \n5.Հայերը ֆուտբոլում")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "գնդակ" in harc:
        harcer_sport.ballondor()
    elif "ֆիֆա" in harc:
        harcer_sport.fifa()
    elif "ուեֆա" in harc:
        harcer_sport.uefa()
    elif "կոշիկ" in harc:
        harcer_sport.goldenboot()
    elif "հայ" in harc:
        harcer_sport.hayer_foot()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        foot()

def basket():
    print("Բասկետբոլի հետ կապված հարցերն են՝ \n1.Ի՞նչ է ՆԲԱ \n2.Ո՞րն է ՖԻԲԱ աշխարհի գավաթը \n3.Ի՞նչ է ԵվրոԼիգան \n4.Հայերը բասկետբոլում")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "նբա" in harc:
        harcer_sport.nba()
    elif "ֆիբա" in harc:
        harcer_sport.fiba_ashxarh()
    elif "եվրո" in harc:
        harcer_sport.euroligue()
    elif "հայ" in harc:
        harcer_sport.hayer_basket()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        basket()

def valley():
    print("Վոլեյբոլի հետ կապված հարցերն են՝ 1.Ի՞նչ է վոլեյբոլի չեմպիոնների լիգան 2.Ո՞րն է Ոսկե գնդակը 3.Ի՞նչ է աշխարհի գավաթը 4.Հայերը վոլեյբոլում")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "չեմպիոն" in harc:
        harcer_sport.champions_ligue()
    elif "ոսկե" in harc:
        harcer_sport.goldenball()
    elif "աշխարհ" in harc:
        harcer_sport.valleywc()
    elif "հայ" in harc:
        harcer_sport.hayer_valley()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        valley()


def f1():
    print("Ֆորմուլա 1-ի հետ կապված հարցերն են՝ \n1.Ի՞նչ է Կոնստրուկտորների գավաթը \n2.Ի՞նչ է բոլիդը \n3.Ի՞նչ է Գրան Պրին")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "գավաթ" in harc:
        harcer_sport.constructor()
    elif "բոլիդ" in harc:
        harcer_sport.bolid()
    elif "գրան" in harc:
        harcer_sport.grand_prix()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        f1()

def olymp():
    print("Օլիմպիական խաղերի հետ կապված հարցերն են՝ \n1.Որո՞նք են խորհրդանիշները և ի՞նչ են նշանակում \n2.Ինչպե՞ս են ծագել օլիմպիական խաղերը \n3.Հայերն օլիմպիական խաղերում \n4.Ի՞նչ սպորտաձևեր են ներառված")
    harc = input("Գրեք, թե ինչ հարց ունեք = ")
    harc.lower()
    if "խորհր" in harc:
        harcer_sport.xorhrdanish1()
    elif "ծագ" in harc:
        harcer_sport.cagum()
    elif "հայ" in harc:
        harcer_sport.hayer_olymp()
    elif "սպորտաձ" in harc:
        harcer_sport.sportadzev()
    else:
        print("Կներեք😔: \nՁեր հարցն անհասկանալի է: \nԿարո՞ղ եք այլ կերպ ձևակերպել հարցը:")
        olymp()

#hayoc lezu
def jam():

def exanak():

def xosq():

def lezup():

#grak
def tum():

def abov():

def mash():

def nar():

def sn():
