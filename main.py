import ararka
def main():
    print("Առարկաներն են՝ \n1.Պայտոն \n2.Մաթեմատիկա \n3.Հայոց Պատմություն \n4.Ֆիզիկա \n5.Անգլերեն \n6.Սպորտ \n7.Հայոց լեզու \n8.Հայ գրականություն")
    arark = input("Գրեք հարցի պատկանելիությունը = ")
    arark.lower()
    if arark == "պայտոն":
        ararka.python()
    elif arark == "մաթեմատիկա":
        ararka.mathem()
    elif arark == "հայոց պատմություն":
        ararka.patm()
    elif arark == "ֆիզիկա":
        ararka.fizika()
    elif arark == "անգլերեն":
        ararka.angl()
    elif arark == "սպորտ":
        ararka.sport()
    elif arark == "հայոց լեզու":
        ararka.lezu()
    elif arark == "հայ գրականություն":
        ararka.grak()
    else:
        print("Կներեք, բայց առարկայի մասին ինֆորմացիա չունեմ😔")
        main()

