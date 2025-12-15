def karacsonyfak_rendeles(magassag):
    for i in range(magassag):
        csillagok = 2 * i + 1
        szokozok = magassag - i - 1
        print(' ' * szokozok + '*' * csillagok)
    
    for _ in range(2):
        print(' ' * (magassag - 2) + '|||')

magassag = int(input("Add meg a fa magasságát: "))
karacsonyfak_rendeles(magassag)
