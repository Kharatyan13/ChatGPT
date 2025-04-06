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
    print("Մաթեմատիկական թեորեմների հետ կապված հարցերն են՝ 1.Ո՞րն է Պյութագորասի թեորեմը 2.Ո՞րն է Թալեսի թեորեմը 3.Ո՞րն է Բեզուի թեորեմը 4.Ո՞րն է Սինուսների թեորեմը 5.Ո՞րն է Կոսինուսների թեորեմը")
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

def arsh():

def bagr():

def rubin():

def arajin():

def erkrord():

def errord():

#fizika
def astgh():

def fizi():

#angl
def present():

def past():

def future():

#sport
def foot():

def basket():

def valley():

def f1():

def olymp():

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
