import time
import main

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    main.main1()

#1
def diplomacy1():
    slow_print("""🌍 Առաջին աշխարհի դիվանագիտություն
Ընդհանուր սահմանում
Առաջին աշխարհ տերմինը ձևավորվել է Սառը պատերազմի ժամանակ՝ նկարագրելու արևմտյան, արդյունաբերապես զարգացած, կապիտալիստական երկրները, որոնք հիմնականում համակողմանիորեն սերտ կապեր ունեին ԱՄՆ-ի և ՆԱՏՕ-ի հետ։ Այս երկրները դիվանագիտական հարթակներում հանդես էին գալիս լիբերալ ժողովրդավարության, ազատ շուկայի տնտեսության, մարդու իրավունքների պաշտպանության և հավաքական անվտանգության դիրքերից։

📜 Պատմական հիմք
Սառը պատերազմի տարիներին (1947–1991) Առաջին աշխարհի դիվանագիտությունը ուղղված էր հիմնականում հետևյալ նպատակներին․

Խորհրդային ազդեցության զսպում (containment policy)
Աշխարհում կոմունիզմի տարածումը կանխելու համար ԱՄՆ-ն և նրա դաշնակիցները ստեղծեցին դաշինքներ (ՆԱՏՕ, CENTO, SEATO) ու ֆինանսական նախաձեռնություններ (օրինակ՝ Մարշալի ծրագիր)։

Միջազգային կազմակերպությունների զարգացում
Առաջին աշխարհի պետությունները գլխավոր դեր ունեցան ՄԱԿ-ի, Արժույթի միջազգային հիմնադրամի (IMF), Համաշխարհային բանկի, ԱՀԿ-ի (WTO) ձևավորման ու գործունեության մեջ։

Դիվանագիտություն՝ հենված ուժի վրա (power diplomacy)
Առաջին աշխարհը ուներ նաև «կոշտ ուժի» գործիքներ՝ ռազմական բազաներ, միջուկային զենք, դաշինքներ։

🕊️ Դիվանագիտական սկզբունքներ
Առաջին աշխարհի դիվանագիտությունը սովորաբար հիմնված է հետևյալ արժեքների վրա՝

Իրավունքի գերակայություն

Պայմանագրային պարտավորությունների կատարում

Միջազգային համագործակցություն

Մարդու իրավունքների պաշտպանություն

Տնտեսական ազատություն և համաշխարհային ինտեգրում

🤝 Քաղաքական դաշնակիցներ և ֆորմատներ
ՆԱՏՕ – անվտանգության ոլորտում

G7 / G20 – տնտեսության և համաշխարհային քաղաքականության կառավարման համար

Եվրամիություն – տարածաշրջանային ինտեգրման օրինակ

ՕԵԿ (OECD) – տնտեսական համագործակցության համատեքստում

🌐 Ժամանակակից ազդեցություն
Թեև Սառը պատերազմը ավարտվել է, առաջին աշխարհի դիվանագիտությունը այսօր էլ շարունակում է ձևավորել աշխարհակարգը՝

Ուկրաինայի պատերազմում աջակցություն Կիևին

Չինաստանի տնտեսական վերելքի զսպում՝ դիվանագիտական և տեխնոլոգիական ճանապարհներով

Կլիմայական դիվանագիտություն՝ համաձայնագրեր, ինչպիսին է Փարիզյան համաձայնագիրը

Մարդու իրավունքների պաշտպանություն՝ ՄԱԿ-ում և այլ հարթակներում""")
def countries1():
    slow_print("""🇺🇸 ԱՄՆ — Առաջատար գլոբալ դիվանագետ
Դիվանագիտական ռազմավարություն՝ գլոբալ առաջնորդություն, աշխարհակարգի ձևավորում։

Կարևոր ուղղություններ՝

Կոմունիզմի զսպում (Սառը պատերազմ)

ՆԱՏՕ-ի առաջնորդություն

Միջին Արևելքի դիվանագիտություն (Իսրայել, Սաուդյան Արաբիա, Իրաք)

Չինաստանի վերելքի զսպում

Միջազգային կազմակերպություններում՝ առանցքային դեր ՄԱԿ-ում, IMF-ում, ԱՀԿ-ում։

Դիվանագիտական գործիքներ՝ դեսպանատներ՝ գրեթե բոլոր երկրներում, ռազմական բազաներ՝ 70+ երկրում։

🇬🇧 Մեծ Բրիտանիա — Դիվանագիտական փորձի խորհրդանիշ
Դիվանագիտական ուղղություն՝ համաշխարհային ազդեցության պահպանում՝ նախկին գաղութային ցանցի հիմքով (Commonwealth)։

Կարևոր գոտիներ՝ Աֆրիկա, Հարավային Ասիա (Հնդկաստան, Պակիստան), Մերձավոր Արևելք։

Հատկություն՝ հմուտ «փափուկ ուժ» (soft power)՝ BBC, կրթություն, մշակույթ։

Բրեքսիթից հետո՝ փորձում է վերագտնել գլոբալ դիրքերը՝ «Global Britain» հայեցակարգով։

🇫🇷 Ֆրանսիա — Անկախ եվրոպական ձայն
Դիվանագիտության ոճը՝ երբեմն անկախ ՆԱՏՕ-ից և ԱՄՆ-ից։

Նախընտրելի դերակատարություն՝ Եվրոպայում ռազմավարական ինքնիշխանության ամրապնդում։

Աֆրիկայում՝ ազդեցիկ դեր (Ֆրանկոֆոն երկրներ)։

Միջուկային ուժ՝ ունի իր անկախ դոկտրինան («force de frappe»)։

Մշակութային դիվանագիտություն՝ ֆրանսիական լեզվի տարածում, համաշխարհային կինո/արվեստ։

🇩🇪 Գերմանիա — Տնտեսական հսկա, զգույշ դիվանագետ
Դիվանագիտության հիմնական ուղղությունը՝ խաղաղություն, ինտեգրում, եվրոպական միասնություն։

Հիմնական ուժը՝ տնտեսությունը։

ԵՄ առաջնորդ՝ եվրոպական քաղաքականության մեջ առանցքային դեր։

Մշակույթ՝ վավերացված փաստաթղթերի դիվանագիտություն, միջնորդության հմտություն։

🇯🇵 Ճապոնիա — Խաղաղ զարգացման մոդել
Սահմանադրությամբ՝ հրաժարվել է պատերազմից, բայց ունի զարգացած պաշտպանություն։

Արտաքին քաղաքականություն՝ կենտրոնացած է Ասիայի կայունության վրա։

Կապեր՝ սերտ համագործակցություն ԱՄՆ-ի հետ, հակազդեցություն Չինաստանին ու Հյուսիսային Կորեային։

Մշակութային դիվանագիտություն՝ «մեղմ ուժի» կարևոր աղբյուր (անիմե, տեխնոլոգիա, հյուրընկալություն)։

🇨🇦 Կանադա — Խաղաղարար և միջնորդ պետություն
Ուղղություն՝ մարդու իրավունքների պաշտպանություն, բազմամշակութայնության մոդել։

ՄԱԿ-ի առաքելություններ՝ խաղաղապահություն։

Հարաբերություններ՝ ԱՄՆ-ի մերձավոր գործընկեր, բայց պահպանում է ինքնուրույն դիրքորոշումներ (օրինակ՝ Իրաքի պատերազմին չմասնակցեց)։

""")
def union1():
    slow_print("""🤝 Հիմնական դաշինքներ և միություններ
1. ՆԱՏՕ (NATO) – Հյուսիսատլանտյան դաշինք
Հիմնադրվել է՝ 1949թ.
Անդամներ՝ ԱՄՆ, Կանադա, Մեծ Բրիտանիա, Ֆրանսիա, Գերմանիա, Իտալիա, և այլ եվրոպական երկրներ (այժմ՝ 32 անդամ)
Առաքելություն՝

Կոլեկտիվ պաշտպանություն (Հոդված 5՝ հարձակումը մեկի վրա՝ հարձակում է բոլորի վրա)

Ռազմավարական ռազմական և քաղաքական համագործակցություն

Ուկրաինայի պատերազմից հետո՝ ակտիվացել է
👉 ՆԱՏՕ-ն Առաջին աշխարհի դիվանագիտության ռազմական սյունն է։

2. G7 (Group of Seven)
Անդամներ՝ ԱՄՆ, Կանադա, Մեծ Բրիտանիա, Գերմանիա, Ֆրանսիա, Իտալիա, Ճապոնիա
Ոչ պաշտոնական անդամ՝ ԵՄ (Եվրամիություն)
Նպատակ՝

Համաշխարհային տնտեսության կառավարում

Քաղաքական և ֆինանսական ճգնաժամերի լուծում

Համակարգում նոր տեխնոլոգիաների, կլիմայի, անվտանգության հարցերը
👉 Դիվանագիտական «վերին սեղան»՝ առանց Ռուսաստանի, Չինաստանի։

3. Եվրոպական միություն (ԵՄ / EU)
Անդամներ՝ Գերմանիա, Ֆրանսիա, Իտալիա, Իսպանիա և այլ եվրոպական զարգացած երկրներ
Հիմնադրվել է՝ որպես ԵՀՄԱ (1951), դարձավ ԵՄ՝ 1993թ.
Նպատակներ՝

Տնտեսական ինտեգրում, միասնական շուկա

Դիվանագիտական և ռազմավարական համադաշնություն

Արտաքին քաղաքականություն (մասնակի համադրված, բայց ոչ լիարժեք)
👉 ԵՄ-ն ձևավորում է համատեղ արտաքին քաղաքականություն, սակայն որոշ երկրներ ունեն առանձին դիրքորոշում։

4. ՕԵԿ (OECD – Տնտեսական համագործակցության և զարգացման կազմակերպություն)
Անդամներ՝ Ամբողջ Առաջին աշխարհը և որոշ զարգացող երկրներ
Նպատակ՝

Համագործակցություն տնտեսության, կրթության, ֆինանսների ոլորտներում

Տվյալների փոխանակում և տնտեսական քաղաքականության համադում
👉 Դիվանագիտական փափուկ ազդեցության հարթակ է։

5. Five Eyes (Հնգաչք)
Անդամներ՝ ԱՄՆ, Մեծ Բրիտանիա, Կանադա, Ավստրալիա, Նոր Զելանդիա
Նպատակ՝

Հետախուզական տվյալների փոխանակում

Կիբերհետախուզություն, հակահաբեկչական աշխատանք
👉 Խիստ վստահության ցանց՝ դիվանագիտական ստվերային կողմում։

6. AUKUS (Ավստրալիա, Միացյալ Թագավորություն, ԱՄՆ)
Ստեղծվել է՝ 2021թ.
Նպատակ՝

Ռազմավարական պատասխան Չինաստանի վերելքին

Ծովային անվտանգության խորացված համագործակցություն (մասնավորապես՝ Հնդկացովային–Խաղաղօվկիանոսյան տարածաշրջան)
👉 Ավելացնում է ուժեղ ռազմավարական կապեր ԱՄՆ-ի առանցքի շուրջ։

7. Չմիացման շարժում (Non-Aligned Movement)
Չնայած սա Առաջին աշխարհին չի պատկանում, դիվանագիտության մեջ կարևոր է, որովհետև Առաջին աշխարհը հաճախ փորձում էր ազդեցություն տարածել այս շարժման երկրների վրա՝ դաշինքներից դուրս գտնվող պետությունների հետ դիվանագիտություն զարգացնելով։

🔄 Համակարգային դիվանագիտություն
Այս դաշինքների ու միությունների ներսում Առաջին աշխարհի պետությունները զարգացնում են նաև՝

Փափուկ ուժի դիվանագիտություն (soft power)՝ կրթություն, մշակույթ, լեզու

Տնտեսական ազդեցության դիվանագիտություն՝ սանկցիաներ, ներդրումներ

Գիտահետազոտական և տեխնոլոգիական համագործակցություն՝ արհեստական բանականություն, առողջապահություն, էներգետիկա

""")
def creation1():
    slow_print("""🧱 Ստեղծման պատմական հիմքերը
📅 1945թ․ – Երկրորդ համաշխարհային պատերազմից հետո
Աշխարհը ավերված էր, և մեծ թվով երկրներ կանգնած էին վերակառուցման առաջ։

Երկու հաղթող գերտերություն՝ ԱՄՆ և ԽՍՀՄ, ի հայտ եկան՝ որպես մրցակից գաղափարախոսությունների առաջնորդներ։

ԱՄՆ – կապիտալիզմ, ազատ շուկա, ժողովրդավարություն

ԽՍՀՄ – կոմունիզմ, կենտրոնացված տնտեսություն, միակուսակցական համակարգ

📅 1947–1949 – Սառը պատերազմի սկիզբ
ԱՄՆ սկսեց իր «զսպման քաղաքականությունը» (containment policy)՝ ԽՍՀՄ-ի ազդեցության տարածումը կանխելու համար։

Մարշալի ծրագիր (1948)՝ ԱՄՆ-ի կողմից ֆինանսական օգնություն Եվրոպայի վերակառուցման համար։ Սա տնտեսական հիմք դարձավ արևմտյան բլոկի ստեղծման համար։

Ստեղծվեց ՆԱՏՕ (1949)՝ արևմտյան երկրների ռազմական դաշինք։

🧭 «Առաջին աշխարհ» տերմինի ծագումը
1952թ. ֆրանսիացի սոցիոլոգ Ալֆրեդ Սովի (Alfred Sauvy) առաջարկեց աշխարհը բաժանել երեք «աշխարհների»՝

Առաջին աշխարհ – կապիտալիստական, արևմտյան երկրներ

Երկրորդ աշխարհ – կոմունիստական երկրներ (ԽՍՀՄ և դաշնակիցներ)

Երրորդ աշխարհ – չմիացած, զարգացող երկրներ (Աֆրիկա, Ասիա, Լատինական Ամերիկա)

Տերմինները տարածվեցին մամուլում և քաղաքական հռետորաբանության մեջ, չնայած ժամանակի ընթացքում ընկալվում էին ավելի գաղափարախոսական, քան ճշգրիտ։

🏛 Առաջին աշխարհի հիմքում գտնվող գաղափարախոսությունը
Լիբերալ ժողովրդավարություն

Ազատ շուկայական տնտեսություն

Մարդու իրավունքների պաշտպանություն

Արտաքին քաղաքականություն՝ ուղղված կոմունիզմի զսպմանը

Միջազգային համագործակցության ինստիտուտներ՝ ՄԱԿ, ԱՀԿ, ՕԵԿ, IMF, ՆԱՏՕ և այլն

🌍 Առաջին աշխարհի երկրների հիմնադիր կորիզը
ԱՄՆ՝ առաջնորդ և գլխավոր ֆինանսավորող

Մեծ Բրիտանիա

Ֆրանսիա

Կանադա

Ավստրալիա

Իտալիա

Բենիլյուքս երկրներ (Բելգիա, Նիդեռլանդներ, Լյուքսեմբուրգ)

Արևմտյան Գերմանիա

Ճապոնիա (ձևականորեն ոչ ՆԱՏՕ-ում, բայց արևմտյան դաշինքում)

🔚 Պատմական կարևոր դիտարկում
Առաջին աշխարհը դիվանագիտական միավոր չէր սկզբում, այլ գաղափարախոսական–քաղաքական խումբ։

Տասնամյակների ընթացքում այդ պետությունները սկսեցին ձևավորել ընդհանուր ինստիտուցիոնալ դաշտ, որը վերածվեց համաշխարհային համակարգի ողնաշարի։

""")
#2
def diplomacy2():
    slow_print("""🌐 Ինչ է «ներկայիս Երկրորդ աշխարհը»
Թեև Սառը պատերազմից հետո «Երկրորդ աշխարհ» հասկացությունը կարծես վերացավ, վերջին տարիներին այն վերաձևավորվել է՝ որպես այլընտրանք արևմտյան առաջնորդությամբ համաշխարհային կարգին։ Այսօրվա «Երկրորդ աշխարհը» ներառում է պետություններ, որոնք.

Հակաամերիկյան կամ արևմտյան գերիշխանությանն ընդդիմադիր են

Ունեն ավտորիտար կամ հիբրիդային ռեժիմներ

Ստեղծում են իրենց սեփական դաշինքները, տնտեսական ու ռազմաքաղաքական համագործակցության հարթակներ

Ունեն ռազմավարական միմյանց աջակցություն, հաճախ՝ արևմտյան սանկցիաներից պաշտպանվելու համատեքստում

🗺️ Ներկայիս «Երկրորդ աշխարհի» առանցքային երկրներ
Ռուսաստան

Չինաստան

Իրան

Հյուսիսային Կորեա

Սիրիա

Վենեսուելա

Բելառուս

Ղազախստան, Ուզբեկստան, որոշ Աֆրիկյան երկրներ

Հնդկաստանը՝ մասնակիորեն, որպես ռազմավարական հավասարակշռող դերակատար

🧭 Դիվանագիտական հիմնասյուներ
1. Արևմտյան ազդեցության սահմանափակում
Արհեստական բանականության, տեղեկատվության, ֆինանսների ու մշակույթի ոլորտներում՝ հակադրություն արևմտյան ստանդարտներին

Պաշտոնական հռետորաբանություն ընդդեմ «հիմնված կանոնների համաշխարհային կարգի», որը վերահսկում է ԱՄՆ-ն

2. Սուվերենության գերակշռություն միջազգային իրավունքից
Այս երկրներն հաճախ մերժում են միջազգային դատարանների, մարդու իրավունքների մարմինների «միջամտությունը»

Օրինակ՝ Ռուսաստանը հրաժարվել է Մարդու իրավունքների եվրոպական դատարանի որոշումներից

3. Աջակցություն ավտորիտար կառավարություններին
Երկարամյա առաջնորդների փոխադարձ պաշտպանություն (Օրինակ՝ Ռուսաստան–Բելառուս, Չինաստան–Սիրիա, Իրան–Վենեսուելա)

🛠️ Դիվանագիտական գործիքներ
1. ԲՌԻՔՍ (BRICS)
Բրազիլիա, Ռուսաստան, Հնդկաստան, Չինաստան, Հարավային Աֆրիկա
(2024-ից՝ Եգիպտոս, Իրան, ԱՄԷ, Եթովպիա)

Ստեղծում են այլընտրանք՝ G7-ին ու ԱՄՀ-ին

Աշխատում են նոր վճարային համակարգերի վրա (չփոխվում դոլարով)
🟰 ԲՌԻՔՍ-ը ներկայիս Երկրորդ աշխարհի դիվանագիտական տնտեսական հարթակն է։

2. Շանհայի համագործակցության կազմակերպություն (ՇՀԿ)
Չինաստան, Ռուսաստան, Հնդկաստան, Պակիստան, Կենտրոնական Ասիա

Հակաահաբեկչական համագործակցություն

Տարածաշրջանային անվտանգության հարցեր

Իրականում արևմտյան ռազմական համակարգերին հակակշիռ

3. Կոլեկտիվ անվտանգության պայմանագրի կազմակերպություն (ՀԱՊԿ)
Ռուսաստան, Հայաստան, Բելառուս, Ղազախստան, Ղրղզստան, Տաջիկստան

ՆԱՏՕ-ի ռուսական տարբերակն է՝ թույլ, սակայն դիվանագիտական առումով նշանակալից

4. Ինֆորմացիոն դիվանագիտություն (propaganda diplomacy)
Հսկայական մեդիա ցանցեր՝ RT (Ռուսաստան), CGTN (Չինաստան), PressTV (Իրան)

Դիվանագիտական քարոզչության միջոցով՝ քննադատում են արևմուտքի արտաքին քաղաքականությունը, պատկերը զարգացող աշխարհում խեղաթյուրում

5. Զենքի և էներգետիկայի դիվանագիտություն
Զենքի վաճառք և ռազմական աջակցություն միավորող երկրներին (ՌԴ–Իրան–Սիրիա)

Գազի և նավթի միջոցով կախվածություն՝ որպես քաղաքական լծակ (Ռուսաստան–Եվրոպա, Չինաստան–Ասիա)

📣 Դիվանագիտական հռետորաբանություն
«Բազմաբևեռ աշխարհակարգ» (multipolarity)

«Արևմուտքը հնացել է»

«Ազգերի ինքնիշխանության վերածնունդ»

«Ազատ ենք կոլոնիալ համակարգից» (հատկապես Աֆրիկայում)

📌 Օրինակներ ներկա դիվանագիտական մանևրներից
Դիվանագիտական գործողություն	                                Երկիր	         Նպատակ
Ռուսաստանի սերտ կապերը Աֆրիկայի ռազմական խունտաների հետ	     ՌԴ	        Արևմուտքի ազդեցության նվազեցում
Չինաստանի «Մեկ գոտի, մեկ ճանապարհ» նախաձեռնությունը	       Չինաստան	    Տնտեսական կախվածություն, ազդեցություն Ասիայում, Աֆրիկայում
Իրանի միջուկային բանակցությունների մանևրում	                 Իրան	    Արևմուտքի պատժամիջոցներից դուրս գալ, առանց զիջումների
ՀԱՄԱՊԱՏԱՍԽԱՆ բովանդակությամբ լրատվամիջոցների ստեղծում	 ՌԴ, Չինաստան	Մեդիա դիվանագիտություն, soft power

🔚 Եզրակացություն
Ներկայիս Երկրորդ աշխարհը դադարել է լինել կոմունիստական գաղափարախոսական բլոկ, բայց մնացել է որպես աշխարհաքաղաքական հակակշիռ արևմուտքին՝ այլ դիվանագիտական լեզվով, նոր միություններով և ռազմավարական միմյանց աջակցությամբ։""")
def countries2():
    slow_print("""🌍 Ներկայիս Երկրորդ աշխարհի առանցքային երկրները
🇷🇺 Ռուսաստան
Նախկին ԽՍՀՄ իրավահաջորդ

Ակտիվ մրցակցություն արևմուտքի, մասնավորապես՝ ԱՄՆ-ի և ՆԱՏՕ-ի հետ

Առաջնորդում ՀԱՊԿ-ը, ՇՀԿ-ում առաջատար խաղացող

🇨🇳 Չինաստան
Տնտեսապես հզոր, բայց քաղաքականորեն ավտորիտար պետություն

Արևմուտքի հետ ռազմավարական մրցակից

«Մեկ գոտի, մեկ ճանապարհ» նախաձեռնության միջոցով՝ ազդեցություն Ասիայում, Աֆրիկայում, Եվրոպայում

🇮🇷 Իրան
Արևմուտքի պատժամիջոցների ներքո

Իսլամական հեղափոխության դրոշով՝ աշխարհաքաղաքական առճակատում Իսրայելի, ԱՄՆ-ի և ԵՄ-ի հետ

Սերտ հարաբերություններ՝ Ռուսաստանի և Չինաստանի հետ

🇰🇵 Հյուսիսային Կորեա
Փակ ռեժիմ, հակաարևմտյան և միջուկային զինուժ ունեցող երկիր

Ռուսաստանի և Չինաստանի մերձավոր դաշնակից

🇧🇾 Բելառուս
Ալեքսանդր Լուկաշենկոյի ավտորիտար ռեժիմ

Սերտորեն կապված է Ռուսաստանի հետ՝ տնտեսապես, ռազմականորեն և քաղաքականորեն

Արևմուտքից մեկուսացած

🇻🇪 Վենեսուելա
Նիկոլաս Մադուրոյի սոցիալիստական վարչակարգ

ԱՄՆ-ի և ԵՄ-ի կողմից չճանաչված ղեկավարություն

Ունի սերտ հարաբերություններ՝ Ռուսաստանի, Իրանի, Չինաստանի հետ

🇸🇾 Սիրիա
Բաշար ալ-Ասադի ռեժիմը պահպանվել է Ռուսաստանի և Իրանի ռազմական աջակցությամբ

Արևմուտքում դիտարկվում է որպես մարդու իրավունքների խախտող ռեժիմ

🇰🇿 🇺🇿 🇹🇯 Կենտրոնական Ասիայի երկրներ
Տատանվող դիրքորոշում արևմուտքի և արևելքի միջև

Ընդհանուր առմամբ, մոտենում են ռուսական կամ չինական դիվանագիտական ուղղությանը՝ մասնավորապես՝ ՇՀԿ, ԵԱՏՄ կամ ՀԱՊԿ անդամակցությամբ

🌍 ԲՌԻՔՍ-ի նոր անդամներ (2024-ից)
Երկիր	               Դեր և միտում
🇪🇬 Եգիպտոս	Չի դիմադրում Արևմուտքին, բայց փնտրում է այլընտրանքներ
🇦🇪 ԱՄԷ	    Բազմավեկտոր քաղաքականություն, սերտանում Չինաստանի և Ռուսաստանի հետ
🇮🇷 Իրան	    Ակտիվ հակաարևմտյան դիրքորոշում
🇪🇹 Եթովպիա	Սերտ կապեր Չինաստանի հետ, փնտրում է Արևմուտքից անկախ ուղի

🟡 Մասնակի կամ տատանվող երկրներ
Այս երկրները ամբողջությամբ չեն պատկանում «Երկրորդ աշխարհին», սակայն ունեն հստակ հակաարևմտյան միտումներ կամ ռազմավարական հաշվարկներով համագործակցում են այդ բևեռի հետ։

🇮🇳 Հնդկաստան – Հավասարակշռում է Արևմուտքի և Ռուսաստանի միջև

🇹🇷 Թուրքիա – ՆԱՏՕ-ի անդամ է, բայց հաճախ գործում է անկախ և Ռուսաստանի, Չինաստանի հետ սերտ կապեր է պահպանում

🇷🇸 Սերբիա – Արևմուտքի հետ հարաբերությունները խառն են, ՌԴ-ի հետ՝ ավանդական մտերմություն

🔚 Եզրակացություն
Ներկայիս Երկրորդ աշխարհը չի սահմանափակվում գաղափարախոսական կոմունիզմով, այլ կենտրոնացած է արևմտյան գերիշխանության բալանսավորման վրա։ Դրա շրջանակում գործում են թե հստակ դաշնակիցներ, թե՝ ռազմավարական գործընկերներ։

""")
def union2():
    slow_print("""🛡️ Ռազմաքաղաքական դաշինքներ
1. 🟥 Հավաքական անվտանգության պայմանագրի կազմակերպություն (ՀԱՊԿ)
Նախաձեռնող՝ Ռուսաստանը

Անդամներ՝ Ռուսաստան, Բելառուս, Հայաստանը (2024-ից՝ դե ֆակտո պասիվ է), Ղազախստան, Ղրղզստան, Տաջիկստան

Նպատակ՝ ՆԱՏՕ-ի նման միություն՝ փոխադարձ պաշտպանության սկզբունքով

Իրական դերակատարություն՝ սահմանափակ և հիմնականում ներքին կայունության պահպանման գործիք (օր.՝ Ղազախստան, 2022)

2. 🟦 Շանհայի համագործակցության կազմակերպություն (ՇՀԿ)
Հիմնադրված՝ 2001-ին Չինաստանի և Ռուսաստանի նախաձեռնությամբ

Անդամներ՝ Չինաստան, Ռուսաստան, Հնդկաստան, Պակիստան, Ղազախստան, Ուզբեկստան, Տաջիկստան, Ղրղզստան, Իրան

Դիտորդներ/գործընկերներ՝ Բելառուս, Մոնղոլիա, Թուրքիա (դիտորդ)

Նպատակ՝ տարածաշրջանային կայունություն, հակաահաբեկչական պայքար, արևմտյան ռազմաքաղաքական ազդեցության զսպում

Հատուկ՝ Հնդկաստանը և Պակիստանը՝ հակառակորդներ, բայց միևնույն հարթակում

💰 Տնտեսական միություններ և նախաձեռնություններ
3. 🟨 ԲՌԻՔՍ (BRICS)
Անդամներ՝ Բրազիլիա, Ռուսաստան, Հնդկաստան, Չինաստան, Հարավային Աֆրիկա

Նոր անդամներ (2024-ից)՝ Իրան, Եգիպտոս, ԱՄԷ, Եթովպիա

Նպատակներ՝

Դոլարային համակարգին այլընտրանք

Նոր բանկային մեխանիզմներ (BRICS New Development Bank)

Աշխարհաքաղաքական բազմաբևեռություն

Դիվանագիտական լեզու՝ «համաշխարհային հյուսիս-հարավ հավասարակշռում»

4. 🟩 Եվրասիական տնտեսական միություն (ԵԱՏՄ)
Գլխավոր նախաձեռնող՝ Ռուսաստան

Անդամներ՝ Ռուսաստան, Բելառուս, Ղազախստան, Հայաստան, Ղրղզստան

Նպատակ՝ միասնական շուկա, մաքսային միություն

Իրականում՝ Ռուսական տնտեսական ազդեցության պահպանում տարածաշրջանում

5. 🟫 Մեկ գոտի, մեկ ճանապարհ (Belt and Road Initiative, BRI)
Ինիցիատիվ՝ Չինաստանի

Մասնակիցներ՝ 150+ երկիր՝ Ասիայից մինչև Աֆրիկա, Եվրոպա

Նպատակ՝ ենթակառուցվածքային ներդրումների միջոցով տնտեսական կախվածություն Չինաստանից

Բովանդակություն՝ ճանապարհներ, նավահանգիստներ, երկաթուղիներ, թվային տեխնոլոգիաներ

Քաղաքական նպատակը՝ Չինաստանի գլոբալ ազդեցության աճ արևմուտքի հաշվին

📡 Տեղեկատվական և մեդիա դիվանագիտություն
6. 📺 Պետական վերահսկվող միջազգային մեդիա հարթակներ
Սրանք օգտագործվում են դիվանագիտական քարոզչության և արևմտյան պատկերն աղավաղելու կամ հակազդելու համար։

Մեդիա հարթակ	Երկիր	Նպատակ
RT (Russia Today)	Ռուսաստան	Արևմտյան քաղաքական համակարգերի քննադատություն
CGTN (China Global Television Network)	Չինաստան	Չինաստանի տեսակետների արտահանում
PressTV	Իրան	Իսլամական հեղափոխության քարոզում և Արևմուտքի քննադատություն
TeleSUR	Վենեսուելա (սատարում՝ Կուբա, Բոլիվիա)	Սոցիալիստական արժեքների խթանում

🤝 Քաղաքական-դիվանագիտական փոխադարձ աջակցման բլոկներ
7. 🧱 Հյուսիսային Կորեայի և Իրանի բևեռ
Չի ձևակերպված միություն, բայց կա փոխադարձ աջակցություն և տեխնոլոգիական փոխանցում, հատկապես՝ հրթիռային ու ռազմատեխնիկական ոլորտում

Սերտ կապեր՝ Ռուսաստանի և Չինաստանի հետ՝ պատժամիջոցների շրջանցման, արևմտյան ճնշումներին դիմակայելու նպատակով

📌 Եզրակացություն
Երկրորդ աշխարհը ներկայումս չունի մեկ միասնական գերկառույց՝ ինչպես ՆԱՏՕ-ն կամ ԵՄ-ը։ Փոխարենը ձևավորվել են մասնակիորեն ծավալվող, միմյանց համադրվող դաշինքներ, որոնք

ծառայում են՝ տնտեսական անկախացման,

ռազմաքաղաքական անվտանգային այլընտրանքների ստեղծման,

և դիվանագիտական քարոզչական ճակատ ձևավորելու նպատակներին։""")
def creation2():
    slow_print("""Երկրորդ աշխարհի դաշինքների առաջացումը՝ պատմական ակնարկ
1. Սառը պատերազմ և Երկրորդ աշխարհ հասկացության ծագում
1947–1991

Երկրորդ աշխարհը առաջին հերթին սահմանվեց որպես կոմունիստական սոցիալիստական պետությունների բևեռ՝ գլխավորում Խորհրդային Միությունը, և նրանց դաշնակիցները:

ԽՍՀՄ-ն ստեղծեց սեփական ռազմական, տնտեսական ու քաղաքական դաշինքներ՝ օրինակ՝ Հավաքական անվտանգության պայմանագրի կազմակերպության նախնական տարբերակը՝ Կազմակերպություն Варшавский договор (ՆԱՏՕ-ի հակակշիռ):

Հետևաբար, առաջին և երկրորդ աշխարհների տարբերակումը սկիզբ առավ գաղափարախոսական, ռազմական և քաղաքական հակասություններով:

2. Խորհրդային Միության փլուզում (1991) և կոլապսի հետևանքները
ԽՍՀՄ փլուզումից հետո շատ կոմունիստական ռեժիմներ փլուզվեցին կամ փոխեցին իրենց դիվանագիտական կողմնորոշումը:

Սակայն որոշ պետություններ՝ Ռուսաստանի գլխավորությամբ, մնացին արևմտյան ազդեցության դեմ համախմբված:

Այդ ժամանակ ձևավորվեց մի նոր տեսակ «Երկրորդ աշխարհ»՝ ավելի բազմաբևեռ, ոչ գաղափարական, այլ աշխարհաքաղաքական շահերի վրա հիմնված բևեռ:

3. ՀԱՊԿ-ի և ՇՀԿ-ի ձևավորում (1990-ականներ և 2000-ականներ)
ՀԱՊԿ-ը ստեղծվեց 1992-ին՝ որպես Ռուսաստանի և Կենտրոնական Ասիայի նախկին խորհրդային երկրների ռազմական-քաղաքական դաշինք, հակադրվելու ՆԱՏՕ-ի հյուսիսային ընդլայնմանը:

ՇՀԿ-ն ձևավորվեց 2001-ին Չինաստանի, Ռուսաստանի, Կենտրոնական Ասիայի և այլ երկրների մասնակցությամբ՝ որպես տարածաշրջանային անվտանգության և տնտեսական համագործակցության հարթակ՝ մաքսային սահմանների, ահաբեկչության և թմրամիջոցների թրաֆիկինգի դեմ պայքարելու նպատակով:

4. Չինաստանի տնտեսական վերելքը և ԲՌԻՔՍ-ի ստեղծումը (2000-ականներ, 2010-ականներ)
Չինաստանը դարձավ աշխարհաքաղաքական մեծ խաղացող՝ տնտեսական հզորացման արդյունքում:

2009-ին ձևավորվեց ԲՌԻՔՍ խումբը, որին սկզբնականում մասնակցում էին Բրազիլիա, Ռուսաստանում, Հնդկաստան, Չինաստան և Հարավային Աֆրիկա:

Նպատակը՝ տնտեսական համագործակցություն և արևմտյան տնտեսական հսկողությանը այլընտրանք ստեղծելն էր:

5. Իրանի, Հյուսիսային Կորեայի և այլ պետությունների ընդգրկումը
Իրանը, Հյուսիսային Կորեան և որոշ այլ պետություններ, որոնք Արևմուտքի հետ լարված հարաբերություններ ունեին, դարձան կամավորորեն կամ հարկադրաբար այս բևեռի մաս՝ որոնելով պաշտպանություն և տնտեսական աջակցություն:

Իրանի և Ռուսաստանի միջեւ ռազմավարական համագործակցությունը ակտիվացավ 2000-ականների կեսերից, մասնավորապես Սիրիայի պատերազմից հետո:

6. ԵԱՏՄ և տնտեսական ինտեգրման խորացում (2010-ականներ)
Ռուսաստան, Բելառուս, Ղազախստան, Հայաստան և Ղրղզստան ստեղծեցին Եվրասիական տնտեսական միությունը՝ փորձելով պահպանել տնտեսական ազդեցությունը և համագործակցությունը նախկին ԽՍՀՄ տարածքում՝ հակազդելու Եվրամիության տնտեսական գրավչությանը:

7. «Մեկ գոտի, մեկ ճանապարհ» նախաձեռնության մեկնարկը (2013)
Չինաստանի նախագահ Սի Ցզինփինի կողմից ներկայացված նախագիծը մետաղալարերով կապեց Ասիան, Եվրոպան և Աֆրիկան՝ ենթակառուցվածքների և տնտեսական կապերի նոր ցանց ստեղծելով:

Սա մեծացրեց Չինաստանի քաղաքական և տնտեսական ազդեցությունը և ընդգրկեց բազմաթիվ երկրներ՝ դարձնելով իրենք ևս մասնակիորեն «Երկրորդ աշխարհ» բևեռի մաս:

8. BRICS-ի ընդլայնումը (2023-2024)
BRICS-ի անդամների ցանկի ընդլայումը (Իրան, Եգիպտոս, ԱՄԷ, Եթովպիա) ցույց է տալիս ավելի լայն և բազմաբևեռ բևեռի ձգտում՝ ներառելով զարգացող տնտեսություններ, որոնք չեն մտնում հստակ արևմտյան կամ առաջին աշխարհների շրջանակ:

💡 Եզրակացություն
«Երկրորդ աշխարհ» բևեռի առաջացումը երկար պրոցես է, որը սկսվել է Սառը պատերազմի ժամանակ և շարունակվել խորհրդային համակարգի փլուզումից հետո: Այն դեպի ավելի բազմաբևեռ, շահերի վրա հիմնված միջազգային համակարգի ձևավորում է, որտեղ դաշնակցությունները խարսխված են ռազմաքաղաքական և տնտեսական շահերի վրա՝ ոչ գաղափարախոսական:""")
#3
def diplomacy3():
    slow_print("""🔹 1. Երրորդ աշխարհի դիվանագիտության բնութագիրը
Երրորդ աշխարհը, որպես հասկացություն, ի սկզբանե կիրառվել է սառը պատերազմի ժամանակ՝ բաժանելով աշխարհը երեք բևեռների․

Առաջին աշխարհ – Արևմտյան կապիտալիստական երկրներ,

Երկրորդ աշխարհ – ԽՍՀՄ և նրա դաշնակիցներ,

Երրորդ աշխարհ – Անկախ և զարգացող երկրներ՝ հիմնականում Ասիայում, Աֆրիկայում և Լատինական Ամերիկայում։

Այսօր այդ տերմինը երբեմն փոխարինվում է «զարգացող երկրներ», «հարավային երկրներ», կամ «Գլոբալ Հարավ» հասկացություններով, սակայն նրանց դիվանագիտությունը շարունակում է ունենալ որոշակի յուրահատկություններ՝ պայմանավորված պատմական, տնտեսական և աշխարհաքաղաքական գործոններով։

🔹 2. Հիմնական նպատակներ
📌 Զարգացման ապահովում՝ տնտեսական օգնության, ներդրումների ու տեխնոլոգիական փոխանցման միջոցով։

📌 Անկախության պահպանում՝ խուսափելով մեծ տերությունների ազդեցությունից։

📌 Մարդասիրական և բնապահպանական հարցերում ձայն ունենալ։

📌 Տարածաշրջանային կայունության ապահովում։

📌 Աշխարհաքաղաքական շահերի համահարթեցում՝ հանուն ազգային անվտանգության։

🔹 3. Դիվանագիտական գործիքակազմ
🤝 Չմիավորման շարժում – Երրորդ աշխարհի երկրների պատմական պլատֆորմն է, որն այսօր էլ փորձում է վերաիմաստավորվել։

🌍 Բազմակողմ համագործակցություն – ՄԱԿ, Աֆրիկյան Միություն, Ասեան, CELAC (Լատինական Ամերիկա), BRICS+։

⚖️ Հավասարակշռության քաղաքականություն – Չինաստան-ԱՄՆ-ԵՄ հակասությունների ֆոնին, փոքր երկրները փորձում են մանևրել։

🔹 4. Դիվանագիտության հիմնական ուղղություններ
🟠 Աշխարհաքաղաքական բազմաբևեռություն
Երրորդ աշխարհի երկրները ձգտում են նվազեցնել կախվածությունը Արևմուտքից և ավելացնել համագործակցությունը Չինաստանի, Ռուսաստանի, Հնդկաստանի և տարածաշրջանային այլ ուժերի հետ։ Օրինակ՝

Աֆրիկյան երկրները համագործակցում են Չինաստանի հետ «Մեկ գոտի, մեկ ճանապարհ» նախաձեռնության շրջանակում։

Լատինական Ամերիկայի երկրները խորացնում են հարաբերությունները Ռուսաստանի ու Չինաստանի հետ՝ հակազդելու ԱՄՆ-ի ճնշումներին։

🟠 Էկոնոմիկայի դիվանագիտություն
Էներգետիկ ռեսուրսներ, հումք, հանքային պաշարներ՝ կարևոր դիվանագիտական լծակներ են։

Միջազգային ներդրումների ներգրավում՝ հատկապես ենթակառուցվածքների, գյուղատնտեսության, կապի ոլորտներում։

🟠 Մարդասիրական և կլիմայական դիվանագիտություն
Եղանակային փոփոխություններից ամենաշատը տուժող են զարգացող երկրները։

Նրանք դիվանագիտական հարթակներում պահանջում են փոխհատուցում ու օգնություն հարուստ երկրներից։

🔹 5. Մարտահրավերներ
⚠️ Ներքին անկայունություն, հակամարտություններ, կոռուպցիա՝ բարդացնում են վստահելի արտաքին քաղաքականություն ձևավորելը։

⚠️ Էկոնոմիկայի կախվածություն արտաքին աջակցությունից։

⚠️ Դիվանագիտական ռեսուրսների սակավություն՝ մասնագետների, դեսպանատների, ինստիտուտների պակաս։

⚠️ Գերակա դարձած մեծ տերությունների մրցակցությունը՝ երբեմն բևեռացնում է երրորդ աշխարհի դիրքորոշումները։

🔹 6. Նոր միտումներ
📈 BRICS+ ընդլայնում – Չինաստան, Հնդկաստան, Բրազիլիա և այլ երկրներ նոր հարթակներ են ստեղծում Հարավի համար։

📱 Թվային դիվանագիտության զարգացում՝ սոցցանցերի, մեդիայի միջոցով ազդեցության տարածում։

🌐 Դիվերսիֆիկացված գործընկերություններ՝ միաժամանակ գործընկերություն ԱՄՆ-ի, Չինաստանի և ԵՄ-ի հետ։

🔹 7. Օրինակներ
Նիգերիան զարգացնում է հարաբերությունները ինչպես ԱՄՆ-ի, այնպես էլ Չինաստանի հետ՝ շահագրգռված լինելով ներդրումների և անվտանգային օգնության հարցերում։

Բրազիլիան Լուլա դա Սիլվայի նախագահության օրոք կրկին ակտիվացել է որպես Հարավի ձայն՝ միջնորդելով Ուկրաինայի պատերազմի և այլ գլոբալ հարցերում։

Ինդոնեզիան որդեգրել է «անկախ և ակտիվ արտաքին քաղաքականություն», համատեղելով Արևմուտքի ու Ասիայի հետ համագործակցությունը։

""")
def countries3():
    slow_print("""🌍 Աֆրիկա
Նիգերիա
Նավթային դիվանագիտություն – Նիգերիան Աֆրիկայի ամենաբազմամարդ երկիրն է և հանդիսանում է նավթ արտահանող երկրների կազմակերպության (OPEC) անդամ։ Նավթը նրա հիմնական արտաքին քաղաքական գործիքն է, որն օգտագործվում է ազդեցություն գործելու համաշխարհային գործընկերների վրա։

Հավասարակշռված դիվանագիտություն ԱՄՆ-ի, Չինաստանի և ԵՄ-ի միջև – Նիգերիան ձգտում է պահել հավասարակշռություն՝ համագործակցելով բոլոր ուժերի հետ, հատկապես Չինաստանի՝ ենթակառուցվածքային ծրագրերում ներգրավվածության շնորհիվ։

Տարածաշրջանային առաջնորդություն – Արևմտյան Աֆրիկայում ակտիվ դիվանագիտական և ռազմական դերակատարություն ունի՝ մասնավորապես ECOWAS շրջանակներում։

Էթովպիա
Ջրային դիվանագիտություն – «Մեծ Եթովպական Ամրոց» (GERD) ջրամբարի կառուցումը դարձել է վեճի առարկա Եգիպտոսի և Սուդանի հետ՝ կապված Նեղոսի ջրերի օգտագործման հետ։

Աֆրիկյան Միությունում առանցքային դեր – Ադիս Աբեբան Աֆրիկյան Միության կենտրոնն է, ինչը Եթովպիային տալիս է կարևոր դեր Աֆրիկայի միասնական քաղաքականության ձևավորման մեջ։

🇨🇩 Կոնգոյի Դեմոկրատական Հանրապետություն (ԶԱՀ)
Հանքարդյունաբերության դիվանագիտություն – Երկիրը տիրապետում է աշխարհում ամենամեծ կոբալտի, լիթիումի և պղնձի պաշարներից, ինչը նրան դարձնում է կարևոր գործընկեր՝ տեխնոլոգիական արդյունաբերության համար։

Անվտանգային ճնշումներ – Զինված խմբավորումների առկայությունը և միջազգային խաղաղապահ ուժերի ներկայությունը երկրի արտաքին քաղաքականության առանցքային հարցերից են։

🌏 Ասիա
Ինդոնեզիա
«Անկախ և ակտիվ» արտաքին քաղաքականություն – Ինդոնեզիան որդեգրել է չեզոքություն՝ խուսափելով ԱՄՆ-Չինաստան հակամարտության մեջ ընկնելուց։

G20 անդամություն – Առաջնորդում է զարգացող երկրների խնդիրների բարձրացումը գլոբալ տնտեսական հարթակներում։

Մշակութային «մեղմ ուժ» – Որպես աշխարհում ամենամեծ մահմեդական բնակչություն ունեցող երկիր՝ Ինդոնեզիան հանդես է գալիս որպես հանդուրժողականության և բազմամշակութայնության օրինակ։

Վիետնամ
Հավասարակշռման ռազմավարություն – Վիետնամը միաժամանակ սերտ կապեր է պահպանում ԱՄՆ-ի, ԵՄ-ի և Չինաստանի հետ։

Արտադրական ուժային կենտրոն – Արտաքին ներդրումներով Վիետնամը դարձել է գլոբալ արտադրական շղթայի կարևոր մասը։

Անվտանգային զգայունություն – Հարավչինական ծովի շուրջ վեճերն ու Չինաստանի նկրտումները ստիպում են Վիետնամին դիվանագիտորեն ամրացնել իր դիրքերը։

Բանգլադեշ
Կլիմայի պաշտպանություն – Բանգլադեշը համարվում է կլիմայական փոփոխություններից առավել տուժող երկրներից, և իր դիվանագիտության մեջ առաջ է մղում կլիմայական արդարության հարցը։

Աշխատանքային միգրացիայի դիվանագիտություն – Միլիոնավոր աշխատողներ աշխատում են արտերկրում, և նրանցից եկող փոխադրումները կենսական են երկրի տնտեսության համար։

Չինաստան-Հնդկաստան բալանս – Երկիրը մանևրում է այս երկու հսկաների միջև՝ պահպանելով անկախ արտաքին քաղաքականություն։

🌎 Լատինական Ամերիկա
Բրազիլիա
BRICS խմբում առաջնորդող դիրք – Բրազիլիան հանդես է գալիս որպես Հարավի ձայն՝ Չինաստանի, Հնդկաստանի, Ռուսաստանի և Հարավային Աֆրիկայի հետ համատեղ պահանջելով ավելի արդար գլոբալ համակարգ։

Միջնորդական դիվանագիտություն – Նախագահ Լուլա դա Սիլվայի օրոք Բրազիլիան փորձում է միջնորդ լինել համաշխարհային հակամարտություններում, այդ թվում՝ Ուկրաինայի հարցում։

Կլիմայի առաջամարտիկ – Ամազոնի անտառների պահպանումը դարձել է դիվանագիտական «մեղմ ուժ»՝ Արևմուտքի հետ փոխադարձ համաձայնությունների հասնելու համար։

Մեքսիկա
Միգրացիոն դիվանագիտություն – ԱՄՆ-ի հետ հարաբերություններում միգրացիան կարևոր լծակ է դարձել։

Լատինամերիկյան ինտեգրման ջատագով – Մեքսիկան ակտիվ մասնակցում է տարածաշրջանային դաշինքներին (CELAC, ALBA, Pacific Alliance)՝ նպաստելով Լատինական Ամերիկայի ինքնիշխանությանը։

🔚 Եզրակացություն
Երրորդ աշխարհի երկրներն այսօր ավելի ակտիվ են, քան երբևէ։ Նրանք չեն սահմանափակվում միայն օգնություն ստանալով՝ այլ դառնում են գլոբալ խնդիրների նախաձեռնողներ՝ կլիմա, զարգացում, խաղաղություն և արդարություն։ Նրանց դիվանագիտությունը խելամիտ մանևրների, նոր դաշինքների և սեփական շահերի ավելի հստակ պաշտպանության ուղիով է ընթանում։""")
def union3():
    slow_print("""🌎 Գլոբալ և միջտարածաշրջանային դաշինքներ
1. 🟤 Չմիավորման Շարժում (Non-Aligned Movement – NAM)
Հիմնադրվել է 1961թ., Բելգրադում։

Նպատակն էր՝ չմիանալ ոչ արևմտյան (ՆԱՏՕ), ոչ խորհրդային (Վարշավյան պայմանագիր) բլոկներին։

Անդամներ – ավելի քան 120 երկիր՝ հիմնականում Աֆրիկայից, Ասիայից ու Լատինական Ամերիկայից։

Ներկայում՝ խոսափող է Գլոբալ Հարավի խնդիրների՝ խաղաղություն, զարգացում, կլիմա, ինքնիշխանություն։

2. 🟤 G77 (Group of 77)
Հիմնադրվել է 1964թ.՝ ՄԱԿ-ում՝ որպես զարգացող երկրների բանակցային հարթակ։

Անդամների թիվը՝ 130+։

Նպատակ՝ զարգացող երկրների համատեղ դիրքորոշման ձևավորում տնտեսական, գիտական և տեխնոլոգիական հարցերում։

Ակտիվ դերակատարություն է ունենում ՄԱԿ-ի Կլիմայական կոնֆերանսներում։

3. 🟤 BRICS / BRICS+
Բրազիլիա, Ռուսաստան, Հնդկաստան, Չինաստան, Հարավային Աֆրիկա։

2024-ից՝ BRICS+՝ նոր անդամներով՝ Եգիպտոս, Եթովպիա, Իրան, Արաբական Միացյալ Էմիրություններ, և այլն։

Նպատակներ․

Համաշխարհային ֆինանսական համակարգի դիվերսիֆիկացում (դոլարի փոխարինում),

Համատեղ ներդրումային բանկ (NDB),

Գլոբալ Հարավի շահերի պաշտպանություն։

🌍 Տարածաշրջանային միություններ
Աֆրիկա
🟢 Աֆրիկյան Միություն (African Union – AU)
55 պետություն։

Նպատակ՝ համաֆրիկյան ինտեգրում, անվտանգություն, մարդասիրություն, համատեղ տնտեսություն։

Ստեղծվել է՝ որպես ՕԱԱ-ի (Organization of African Unity) իրավահաջորդ։

🟢 ECOWAS (Արևմտյան Աֆրիկայի Պետությունների Տնտեսական Համայնք)
Նպատակ՝ տնտեսական ինտեգրում, խաղաղություն ու անվտանգության ապահովում։

Նիգերիան, Սենեգալը և այլ երկրներ դաշինքի հենասյուներն են։

Ասիա
🟡 ASEAN (Association of Southeast Asian Nations)
10 պետություն՝ Ինդոնեզիա, Վիետնամ, Թաիլանդ, Մալայզիա, Ֆիլիպիններ և այլն։

Նպատակ՝ տարածաշրջանային համագործակցություն՝ առևտրի, անվտանգություն, մշակույթ։

Ակտիվ քաղաքական մանևրում է ԱՄՆ-ի և Չինաստանի ազդեցությունների միջև։

🟡 SAARC (South Asian Association for Regional Cooperation)
Հարավային Ասիայի 8 պետություն՝ Հնդկաստան, Պակիստան, Բանգլադեշ, Նեպալ, Շրի Լանկա և այլն։

Նպատակներ՝ տնտեսական ինտեգրում, աղքատության հաղթահարում։

Լատինական Ամերիկա
🔵 CELAC (Community of Latin American and Caribbean States)
Ստեղծվել է 2010-ին, որպես ALBA-ի և այլ բլոկների ընդլայնում։

Նպատակ՝ ԱՄՆ-ից անկախ արտաքին քաղաքականություն մշակել։

Անդամներ՝ 33 պետություն։

🔵 MERCOSUR (Mercado Común del Sur)
Տնտեսական միություն՝ Բրազիլիա, Արգենտինա, Ուրուգվայ, Պարագվայ։

Նպատակ՝ ազատ առևտուր, տնտեսական ինտեգրում։

🔵 ALBA (Bolivarian Alliance for the Peoples of Our America)
Վենեսուելա, Կուբա, Բոլիվիա, Նիկարագուա և այլ երկրներ։

Ձևավորվել է հակաամերիկյան տնտեսական ու գաղափարախոսական հենքով։

📌 Արտաքին ուժերի հետ ալյանսներ
Բազմաթիվ երրորդ աշխարհի երկրներ միաժամանակ անդամակցում են կամ համագործակցում և՛ արևմտյան, և՛ ոչ արևմտյան դաշինքներին՝ ապահովելով բազմաբևեռ դիվանագիտություն․

Դաշինք	                                             Բնույթը	                         Զարգացող երկրների դերը
Բելտ և Ճանապարհ (Belt and Road Initiative)	     Չինական գլոբալ տնտեսական նախագիծ	   Աֆրիկայի, Ասիայի, Լատինական Ամերիկայի շատ երկրներ ստացել են ենթակառուցվածքային ներդրումներ
ԱՄՀ / Համաշխարհային Բանկ	                     Արևմտյան ֆինանսական կառույցներ	       Մեծ կախվածություն՝ վարկերի ու պայմանական բարեփոխումների միջոցով
ՄԱԿ համակարգ	                                 Բազմակողմ հարթակ	                   G77, NAM, BRICS երկրների միջոցով զարգացողները ունեն ուժեղ ձայն

🔚 Եզրահանգում
Երրորդ աշխարհի երկրների դիվանագիտությունը հիմնվում է՝

🤝 միությունների վրա՝ միջազգային համախմբման համար,

⚖️ բազմաբևեռության վրա՝ գերիշխանությունը պահպանելու նպատակով,

🌐 համաշխարհային կարգի բարեփոխման պահանջի վրա։""")
def creation3():
    slow_print("""Երրորդ աշխարհի ստեղծումը պատմականորեն կապված է Սառը պատերազմի ժամանակաշրջանի աշխարհաքաղաքական բևեռացման հետ։ «Երրորդ աշխարհ» հասկացությունը ծնվել է ոչ թե աշխարհագրական կամ տնտեսական, այլ քաղաքական պատճառներով։ Ահա դրա ստեղծման հիմնական փուլերը.

📌 1. Ծագումը և նշանակությունը
«Երրորդ աշխարհ» տերմինը առաջին անգամ գործածեց ֆրանսիացի տնտեսագետ Ալֆրեդ Սովին 1952 թվականին՝ համեմատելով այն ֆրանսիական հեղափոխության «երրորդ դասի» հետ՝ որպես ոչ համարվող, բայց քաղաքական գործոն դառնալու հավակնող ուժ։ Տերմինը վերաբերեց այն պետություններին, որոնք չցանկացան միանալ ոչ Միացյալ Նահանգների ղեկավարած կապիտալիստական (Առաջին աշխարհ), ոչ էլ Խորհրդային Միության ղեկավարած կոմունիստական (Երկրորդ աշխարհ) բլոկին։

🌍 2. Ո՞վքեր էին «երրորդ աշխարհը»
Դրանք հիմնականում նորանկախ երկրներ էին Ասիայից, Աֆրիկայից և Լատինական Ամերիկայից, որոնք ապազգայնացվել էին եվրոպական գաղութատիրությունից 1940-70-ականներին։ Օրինակ՝

Հնդկաստան

Եգիպտոս

Գանա

Ինդոնեզիա

Ալժիր

Վիետնամ

Կուբա

Արգենտինա

Էթովպիա

Նիկարագուա

Այս երկրները ձգտում էին պահպանել անկախ արտաքին քաղաքականություն և զարգանալ սեփական մոդելով։

🕊️ 3. Չմիավորված շարժում (Non-Aligned Movement - NAM)
Երրորդ աշխարհի քաղաքական հիմքն է դարձել Չմիավորվածների Շարժումը, որը հիմնադրվել է 1961-ին Բելգրադում՝ Հնդկաստանի վարչապետ Ջավահարլալ Ներուի, Եգիպտոսի նախագահ Գամալ Աբդել Նասերի և Հարավսլավիայի առաջնորդ Տիտոյի նախաձեռնությամբ։

🔹 Շարժման նպատակները՝

Չմիանալ որևէ ռազմաքաղաքական դաշինքի

Հարգել ինքնիշխանությունը

Պայքարել գաղութացման և նորագաղութացման դեմ

Աջակցել համաշխարհային արդարությանը և զարգացող երկրների տնտեսական աճին

🌐 4. Դիվանագիտական միություններ և տնտեսական նախաձեռնություններ
Երրորդ աշխարհի երկրները ստեղծեցին նաև միություններ, որոնք փորձեցին համախմբել զարգացմանն ու համագործակցությանը։

    Միություն	                            Հիմնադրման տարեթիվ	                 Նպատակ
Չմիավորվածների Շարժում (NAM)	                1961	             Քաղաքական չեզոքություն, հակագաղութայինություն
G77	                                            1964	             Զարգացող երկրների տնտեսական շահերի պաշտպանություն ՄԱԿ-ում
ԲՐԻՔՍ	                                        2006	             Բազմաբևեռ աշխարհակարգի խթանում, փոխադարձ տնտեսական աջակցություն
Աֆրիկյան Միություն (AU)	                        2001	             Աֆրիկյան պետությունների միավորում և համախմբում
ԱՍԵԱՆ	                                        1967	             Հարավարևելյան Ասիայի երկրների տնտեսական և քաղաքական ինտեգրացիա

🧭 5. Երրորդ աշխարհը այսօր
Թեև տերմինը այսօր հաճախ համարում են հնացած կամ նույնիսկ նվաստացուցիչ, դրա ժառանգությունն այսօր շարունակում են ներկայացնել՝

Զարգացող երկրներ կամ Համաշխարհային հարավ

Բազմաբևեռ դիվանագիտություն

BRICS+ դաշինքի ընդլայնում

Չմիավորված շարժման վերակենդանացում

🔚 Եզրակացություն
Երրորդ աշխարհի գաղափարը ծնվել է որպես ձայն չունեցող երկրների ինքնության, դիմադրության և ինքնուրույնության ձգտում։ Չնայած գլոբալ քաղաքական քարտեզը փոխվել է, դրա հիմքում եղած արժեքներն ու պայքարները մնում են արդիական. խոսքը մշակութային ինքնիշխանության, տնտեսական արդարության ու բազմաբևեռ աշխարհի մասին է։""")

