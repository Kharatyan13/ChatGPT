import fields
import time

def slow_print(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def python():
    slow_print("Պայտոն առարկայի ոլորտներն են՝ \n1.զանգվածներ \n2.պայմաններ \n3.ցիկլեր \n4.մաթեմատիկական գործողություններ \n5.տողեր")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "զանգված" in field:
        fields.array()
    elif "պայման" in field:
        fields.condition()
    elif "ցիկլ" in field:
        fields.cycle()
    elif "մաթեմատ" in field:
        fields.math()
    elif "տող" in field:
        fields.strg()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        python()

def mathematics():
    slow_print("Մաթեմատիկայի ոլորտներն են՝ \n1.հարթաչափություն \n2.տարածաչափություն \n3.տրիգոնոմետրիա \n4.հանրահաշիվ \n5.թեորեմներ")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "հարթ" in field:
        fields.flat()
    elif "տարած" in field:
        fields.solid()
    elif "տրիգոն" in field:
        fields.trigon()
    elif "հանրահաշ" in field:
        fields.algebra()
    elif "թեորեմ" in field:
        fields.theorem()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        mathematics()

def history():
    slow_print("Հայոց պատմության ոլորտներն են՝ \n1.Արտաշեսյաններ \n2.Արշակունիներ \n3.Բագրատունիներ \n4.Ռուբինյաններ \n5.Առաջին Հանրապետություն \n6.Երկրորդ Հանրապետություն \n7.Երրորդ Հանրապետություն")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "արտաշես" in field:
        fields.artashesyan()
    elif "արշակուն" in field:
        fields.arshakuni()
    elif "բագրատուն" in field:
        fields.bagratuni()
    elif "ռուբին" in field:
        fields.rubinyan()
    elif "առաջին" in field:
        fields.first()
    elif "երկրորդ" in field:
        fields.second()
    elif "երրորդ" in field:
        fields.third()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        history()

def physics():
    slow_print("Ֆիզիկայի ոլորտներն են՝ \n1.աստղագիտություն \n2.ֆիզիկա")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "աստղ" in field:
        fields.astro()
    elif "ֆիզիկ" in field:
        fields.physic()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        physics()

def english():
    slow_print("Անգլերենի ոլորտներն են՝ \n1.ներկա \n2.անցյալ \n3.ապառնի")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "ներկա" in field:
        fields.present()
    elif "անց" in field:
        fields.past()
    elif "ապառ" in field:
        fields.future()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        english()

def sport():
    slow_print("Սպորտի ոլորտներն են՝ \n1.ֆուտբոլ \n2.բասկետբոլ \n3.վոլեյբոլ \n4.ֆորմուլա 1 \n5.օլիմպիական խաղեր")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "ֆուտբոլ" in field:
        fields.foot()
    elif "բասկետ" in field:
        fields.basket()
    elif "վոլեյ" in field:
        fields.valley()
    elif "ֆորմուլ" in field:
        fields.f1()
    elif "օլիմպ" in field:
        fields.olymp()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        sport()

def armenian_language():
    slow_print("Հայոց լեզվի ոլորտներն են՝ \n1.ժամանակ \n2.եղանակ \n3.խոսքի մասեր \n4.հայոց լեզվի պատմություն")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "ժամանակ" in field:
        fields.jam()
    elif "եղանակ" in field:
        fields.exanak()
    elif "խոսք" in field:
        fields.xosq()
    elif "պատմ" in field:
        fields.lezvi_patm()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        armenian_language()

def literature():
    slow_print("Հայ գրականության ոլորտներն են՝ \n1.Թումանյան \n2.Աբովյան \n3.Մաշտոց \n4.Նարեկացի \n5.Սայաթ-Նովա")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "թուման" in field:
        fields.tum()
    elif "աբով" in field:
        fields.abov()
    elif "մաշտոց" in field:
        fields.mash()
    elif "նարեկ" in field:
        fields.nar()
    elif "սայաթ" in field:
        fields.sn()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        literature()

def diplomacy():
    slow_print("""Դիվանագիտության ոլորտներն են՝
    1.Առաջին աշխարհ
    2.Երկրորդ աշխարհ
    3.Երրորդ աշխարհ""")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "առաջ" in field:
        fields.first_world()
    elif "երկր" in field:
        fields.second_world()
    elif "երր" in field:
        fields.third_world()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        diplomacy()

def geography():
    slow_print("""Աշխարհագրության ոլորտներն են՝
    1.Առաջատար երկրներ
    2.Աշխարհամասեր
    3.Ռասաներ
    4.Ջրային աշխարհ
    5.Հավատք""")
    field = input("Գրեք, թե ինչ ոլորտից հարցեր ունեք՝ ").lower()
    if "առաջ" in field:
        fields.leading_countries()
    elif "աշխարհ" in field:
        fields.continents()
    elif "ռասա" in field:
        fields.race()
    elif "ջր" in field:
        fields.water()
    elif "հավ" in field:
        fields.religion()
    else:
        slow_print("Կներեք, բայց ոլորտի մասին ինֆորմացիա չունեմ😔 \nԸնտրեք տրված ոլորտներից մեկը:")
        geography()
