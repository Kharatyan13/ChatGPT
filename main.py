import ararka
def main():
    print("Առարկաներն են՝ \n1.Պայտոն \n2.Մաթեմատիկա \n3.Հայոց Պատմություն \n4.Ֆիզիկա \n5.Անգլերեն \n6.Սպորտ \n7.Հայոց լեզու \n8.Հայ գրականություն")
    arark = input("Գրեք հարցի պատկանելիությունը = ")
    if arark == "Պայտոն":
        ararka.python()
    elif arark == "Մաթեմատիկա":
        ararka.mathem()
    elif arark == "Հայոց Պատմություն":
        ararka.patm()
    elif arark == "Ֆիզիկա":
        ararka.fizika()
    elif arark == "Անգլերեն":
        ararka.angl()
    elif arark == "Սպորտ":
        ararka.sport()
    elif arark == "Հայոց լեզու":
        ararka.lezu()
    elif arark == "Հայ գրականություն":
        ararka.grak()
    else:
        print("Կներեք, բայց առարկայի մասին ինֆորմացիա չունեմ😔")
        main()

