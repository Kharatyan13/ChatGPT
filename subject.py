#Python, mathem, patmutyun, fizika, angl, sport
import fields
def python():
    print("Պայտոն առարկայի ոլորտներն են՝ \n1.զանգվածներ \n2.պայմաններ \n3.ցիկլեր \n4.մաթեմատիկական գործողություններ \n5.տողեր")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    field = field.lower()
    if field == "զանգվածներ":
        fields.array()
    elif field == "պայմաններ":
        fields.condition()
    elif field == "ցիկլեր":
        fields.cycle()
    elif field == "մաթեմատիկական գործողություններ":
        fields.math()
    elif field == "տողեր":
        fields.strg()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        python()

def mathematics():
    print("Մաթեմատիկայի ոլորտներն են՝ \n1.հարթաչափություն \n2.տարածաչափություն \n3.տրիգոնոմետրիա \n4.հանրահաշիվ \n5.թեորեմներ")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    field = field.lower()
    if field == "հարթաչափություն":
        fields.flat()
    elif field == "տարածաչափություն":
        fields.solid()
    elif field == "տրիգոնոմետրիա":
        fields.trigon()
    elif field == "հանրահաշիվ":
        fields.algebra()
    elif field == "թեորեմներ":
        fields.theorem()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        mathematics()

def history():
    print("Հայոց պատմության ոլորտներն են՝ \n1.Արտաշեսյաններ \n2.Արշակունիներ \n3.Բագրատունիներ \n4.Ռուբինյաններ \n5.Առաջին Հանրապետություն \n6.Երկրորդ Հանրապետություն \n7.Երրորդ Հանրապետություն")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    field = field.lower()
    if field == "արտաշեսյաններ":
        fields.artashesyan()
    elif field == "արշակունիներ":
        fields.arshakuni()
    elif field == "բագրատունիներ":
        fields.bagratuni()
    elif field == "ռուբինյաններ":
        fields.rubinyan()
    elif field == "առաջին հանրապետություն":
        fields.first()
    elif field == "երկրորդ հանրապետություն":
        fields.second()
    elif field == "երրորդ հանրապետություն":
        fields.third()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        history()

def physics():
    print("Ֆիզիկայի ոլորտներն են՝ \n1.աստղագիտություն \n2.ֆիզիկա")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    field = field.lower()
    if field == "աստղագիտություն":
        fields.astro()
    elif field == "ֆիզիկա":
        fields.physic()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        physics()

def english():
    print("Անգլերենի ոլորտներն են՝ \n1.ներկա \n2.անցյալ \n3.ապառնի")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    field = field.lower()
    if field == "ներկա":
        fields.present()
    elif field == "անցյալ":
        fields.past()
    elif field == "ապառնի":
        fields.future()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        english()

def sport():
    print("Սպորտի ոլորտներն են՝ \n1.ֆուտբոլ \n2.բասկետբոլ \n3.վոլեյբոլ \n4.ֆորմուլա 1 \n5.օլիմպիական խաղեր")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    field = field.lower()
    if field == "ֆուտբոլ":
        fields.foot()
    elif field == "բասկետբոլ":
        fields.basket()
    elif field == "վոլեյբոլ":
        fields.valley()
    elif field == "ֆոլմուլա 1":
        fields.f1()
    elif field == "օլիմպիական խաղեր":
        fields.olymp()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        sport()

def armenian_language():
    print("Հայոց լեզվի ոլորտներն են՝ \n1.ժամանակ \n2.եղանակ \n3.խոսքի մասեր \n4.հայոց լեզվի պատմություն")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    field = field.lower()
    if field == "ժամանակ":
        fields.jam()
    elif field == "եղանակ":
        fields.exanak()
    elif field == "խոսքի մասեր":
        fields.xosq()
    elif field == "հայոց լեզվի պատմություն":
        fields.lezvi_patm()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        armenian_language()


def literature():
    print("Հայ գրականության ոլորտներն են՝ \n1.Թումանյան \n2.Աբովյան \n3.Մաշտոց \n4.Նարեկացի \n5.Սայաթ-Նովա")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք = ")
    field = field.lower()
    if field == "թումանյան":
        fields.tum()
    elif field == "աբովյան":
        fields.abov()
    elif field == "մաշտոց":
        fields.mash()
    elif field == "նարեկացի":
        fields.nar()
    elif "սայաթ" in field:
        fields.sn()
    else:
        print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        literature()
