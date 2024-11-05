def EV():
    I = int(input("Zadejte zde hodnotu I: "))
    print("--------------------------")
    U = int(input("Zadejte zde hodnotu U: "))
    if I <= 0:
        print("Tohle je nevalidní vstup. Číslo, které jste zadal, mělo hodnotu méně než 1 (I)")
    elif U <= 0:
        print("Tohle je nevalidní vstup. Číslo, které jste zadal, mělo hodnotu méně než 1 (U)")
    else:
        o = print("Výsledek elektrického výkonu je -", I*U, "Watt(ů)")
        return o


def EP():
    P = int(input("Zadejte zde hodnotu P: "))
    print("--------------------------")
    U = int(input("Zadejte zde hodnotu U: "))
    if P <= 0:
        print("Tohle je nevalidní vstup. Číslo, které jste zadal, mělo hodnotu méně než 1 (P)")
    elif U <= 0:
        print("Tohle je nevalidní vstup. Číslo, které jste zadal, mělo hodnotu méně než 1 (U)")
    else:
        o = print("Výsledek elektrického proudu je -", P/U, "Amper")
        return o


def NA():
    P = int(input("Zadejte zde hodnotu P: "))
    print("--------------------------")
    I = int(input("Zadejte zde hodnotu I: "))
    if I <= 0:
        print("Tohle je nevalidní vstup. Číslo, které jste zadal, mělo hodnotu méně než 1 (I)")
    elif P <= 0:
        print("Tohle je nevalidní vstup. Číslo, které jste zadal, mělo hodnotu méně než 1 (P)")
    else:
        o = print("Výsledek napětí je -", P/I, "Volt(ů)")
        return o




while True:
    print("Vyberte, jakou neznámou Elektrického výkonu chcete vypočítat (vyberte číslo pozice proměnné, kterou chcete vypočítat): ")
    vyber = input(" 1. EL. výkon (P) 2. Napětí (U) 3. EL. proud (I) - ")

    if vyber == "1":
        EV()

    elif vyber == "2":
        NA()

    elif vyber == "3":
        EP()

    else:
        print("Tohle je nevalidní vstup volby (musíte zadat například 1, 2...)")
    

    pokracovat = input("Chcete pokračovat v počítání? (ano/ne) ").lower()

    if pokracovat != 'ano':
        print("Snad jsem byl užitečný...")
        break