import subject
import time

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)

def main():
    slow_print("""GPT "Թվային մարտիկ".1\n""")
    slow_print("Տվյալ GPT-ի առարկայական բազաներն են՝ \n1.Պայտոն \n2.Մաթեմատիկա \n3.Հայոց Պատմություն \n4.Ֆիզիկա \n5.Անգլերեն \n6.Սպորտ \n7.Հայոց լեզու \n8.Հայ գրականություն \n9.Դիվանագիտություն \n10.Աշխարհագրություն\n")
    sub = input("Գրեք հարցի պատկանելիությունը՝ ")
    sub = sub.lower()

    if "պայտոն" in sub:
        subject.python()
    elif "մաթեմ" in sub:
        subject.mathematics()
    elif "պատմ" in sub:
        subject.history()
    elif "ֆիզ" in sub:
        subject.physics()
    elif "անգլ" in sub:
        subject.english()
    elif "սպորտ" in sub:
        subject.sport()
    elif "հայ" in sub and "լեզ" in sub:
        subject.armenian_language()
    elif "գրակ" in sub:
        subject.literature()
    elif "դիվան" in sub:
        subject.diplomacy()
    elif "աշխարհ" in sub:
        subject.geography()
    else:
        slow_print("Կներեք, բայց առարկայի մասին ինֆորմացիա չունեմ😔\n")
        main1()


def main1():
    slow_print("Ցանկանու՞մ եք ևս մեկ հարց տալ:")
    yes_no = input("Գրեք այո կամ ոչ: - ")
    yes_no = yes_no.lower()
    if "այո" in yes_no:
        slow_print("\nԿրկին ներկայացնեմ առարկայական բազաները՝ \n1.Պայտոն \n2.Մաթեմատիկա \n3.Հայոց Պատմություն \n4.Ֆիզիկա \n5.Անգլերեն \n6.Սպորտ \n7.Հայոց լեզու \n8.Հայ գրականություն \n9.Դիվանագիտություն \n10.Աշխարհագրություն\n")
        sub = input("Գրեք հարցի պատկանելիությունը՝ ")
        sub = sub.lower()

        if "պայտոն" in sub:
            subject.python()
        elif "մաթեմ" in sub:
            subject.mathematics()
        elif "պատմ" in sub:
            subject.history()
        elif "ֆիզ" in sub:
            subject.physics()
        elif "անգլ" in sub:
            subject.english()
        elif "սպորտ" in sub:
            subject.sport()
        elif "հայ" in sub and "լեզ" in sub:
            subject.armenian_language()
        elif "գրակ" in sub:
            subject.literature()
        elif "դիվան" in sub:
            subject.diplomacy()
        elif "աշխարհ" in sub:
            subject.geography()
        else:
            slow_print("Կներեք, բայց առարկայի մասին ինֆորմացիա չունեմ😔\n")
            main1()
    else:
        slow_print("""Շնորհակալություն GPT "Թվային Մարտիկ".1-ից օգտվելու համար:
          Ուրախ էի օգտակար լինել։ Ցանկացած հարցի դեպքում կարող եք նորից գրել։😊 """)




if __name__ == '__main__':
    main()

    # text = """"""
    # for char in text:
    #     print(char, end="", flush=True)
    #     time.sleep(0.01)
    # main.main1()