import subject
def main():
    print("""GPT "Թվային մարտիկ".1""")
    print("Տվյալ GPT-ի առարկայական բազաներն են՝ \n1.Պայտոն \n2.Մաթեմատիկա \n3.Հայոց Պատմություն \n4.Ֆիզիկա \n5.Անգլերեն \n6.Սպորտ \n7.Հայոց լեզու \n8.Հայ գրականություն \n9.Դիվանագիտություն \n10.Աշխարհագրություն")
    sub = input("Գրեք հարցի պատկանելիությունը՝  ")
    sub = sub.lower()
    if sub == "պայտոն":
        subject.python()
    elif sub == "մաթեմատիկա":
        subject.mathematics()
    elif sub == "հայոց պատմություն":
        subject.history()
    elif sub == "ֆիզիկա":
        subject.physics()
    elif sub == "անգլերեն":
        subject.english()
    elif sub == "սպորտ":
        subject.sport()
    elif sub == "հայոց լեզու":
        subject.armenian_language()
    elif sub == "հայ գրականություն":
        subject.literature()
    elif sub == "դիվանագիտություն":
        subject.diplomacy()
    elif sub == "աշխարհագրություն":
        subject.geography()
    else:
        print("Կներեք, բայց առարկայի մասին ինֆորմացիա չունեմ😔")
        main()


if __name__ == '__main__':
    main()
