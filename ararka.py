#Python, mathem, patmutyun, fizika, angl, sport
import volortner
def python():
    print("Պայտոն առարկայի ոլորտներն են՝ \n1.զանգվածներ \n2.պայմաններ \n3.ցիկլեր \n4.մաթեմատիկական գործողություններ \n5.տողեր")
    volort = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    volort.lower()
    if volort == "զանգվածներ":
        volortner.zangvac()
    elif volort == "պայմաններ":
        volortner.pajman()
    elif volort == "ցիկլեր":
        volortner.cikl()
    elif volort == "մաթեմատիկական գործողություններ":
        volortner.mathm()
    elif volort == "տողեր":
        volortner.strg()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        python()

def mathem():
    print("Մաթեմատիկայի ոլորտներն են՝ \n1.հարթաչափություն \n2.տարածաչափություն \n3.տրիգոնոմետրիա \n4.հանրահաշիվ \n5.թեորեմներ")
    volort = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    volort.lower()
    if volort == "հարթաչափություն":
        volortner.hart()
    elif volort == "տարածաչափություն":
        volortner.tarac()
    elif volort == "տրիգոնոմետրիա":
        volortner.trigon()
    elif volort == "հանրահաշիվ":
        volortner.hanr()
    elif volort == "թեորեմներ":
        volortner.teorem()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        mathem()

def patm():
    print("Հայոց պատմության ոլորտներն են՝ \n1.Արտաշեսյաններ \n2.Արշակունիներ \n3.Բագրատունիներ \n4.Ռուբինյաններ \n5.Առաջին Հանրապետություն \n6.Երկրորդ Հանրապետություն \n7.Երրորդ Հանրապետություն")
    volort = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    volort.lower()
    if volort == "արտաշեսյաններ":
        volortner.art()
    elif volort == "արշակունիներ":
        volortner.arsh()
    elif volort == "բագրատունիներ":
        volortner.bagr()
    elif volort == "ռուբինյաններ":
        volortner.rubin()
    elif volort == "առաջին հանրապետություն":
        volortner.arajin()
    elif volort == "երկրորդ հանրապետություն":
        volortner.erkrord()
    elif volort == "երրորդ հանրապետություն":
        volortner.errord()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        patm()

def fizika():
    print("Ֆիզիկայի ոլորտներն են՝ \n1.աստղագիտություն \n2.ֆիզիկա")
    volort = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    volort.lower()
    if volort == "աստղագիտություն":
        volortner.astgh()
    elif volort == "ֆիզիկա":
        volortner.fizi()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        fizika()

def angl():
    print("Անգլերենի ոլորտներն են՝ \n1.ներկա \n2.անցյալ \n3.ապառնի")
    volort = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    volort.lower()
    if volort == "ներկա":
        volortner.present()
    elif volort == "անցյալ":
        volortner.past()
    elif volort == "ապառնի":
        volortner.future()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        angl()

def sport():
    print("Սպորտի ոլորտներն են՝ \n1.ֆուտբոլ \n2.բասկետբոլ \n3.վոլեյբոլ \n4.ֆորմուլա 1 \n5.օլիմպիական խաղեր")
    volort = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    volort.lower()
    if volort == "ֆուտբոլ":
        volortner.foot()
    elif volort == "բասկետբոլ":
        volortner.basket()
    elif volort == "վոլեյբոլ":
        volortner.valley()
    elif volort == "ֆոլմուլա 1":
        volortner.f1()
    elif volort == "օլիմպիական խաղեր":
        volortner.olymp()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        sport()

def lezu():
    print("Հայոց լեզվի ոլորտներն են՝ \n1.ժամանակ \n2.եղանակ \n3.խոսքի մասեր \n4.հայոց լեզվի պատմություն")
    volort = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    volort.lower()
    if volort == "ժամանակ":
        volortner.jam()
    elif volort == "եղանակ":
        volortner.exanak()
    elif volort == "խոսքի մասեր":
        volortner.xosq()
    elif volort == "հայոց լեզվի պատմություն":
        volortner.lezup()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        lezu()


def grak():
    print("Հայ գրականության ոլորտներն են՝ \n1.Թումանյան \n2.Աբովյան \n3.Մաշտոց \n4.Նարեկացի \n5.Սայաթ-Նովա")
    volort = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    volort.lower()
    if volort == "թումանյան":
        volortner.tum()
    elif volort == "աբովյան":
        volortner.abov()
    elif volort == "մաշտոց":
        volortner.mash()
    elif volort == "նարեկացի":
        volortner.nar()
    elif "սայաթ" in volort:
        volortner.sn()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        grak()
