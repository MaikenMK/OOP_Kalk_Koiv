class cal():                            
    def __init__(self,a,b):             
        self.a = a
        self.b = b

    def liitmine(self):                
        return self.a + self.b
    def lahutamine(self):               
        return self.a - self.b
    def korrutamine(self):              
        return self.a * self.b
    def jagamine(self):                 
        return self.a / self.b
    def jaak(self):                     
        return self.a % self.b
    def ruutjuur(self):                 
        return self.a ** self.b
a = int(input("Sisesta esimene number: "))          
b = int(input("Sisesta teine number: "))

kalk = cal(a,b)                         
while True:
    def menu():
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine. ')
        print(x)
    menu()
    valik = int(input('Sisesta üks valikutest: '))
    if valik == 1:
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == 2:
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == 3:
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5:
        print("Vastus: ",kalk.jaak())
        break
    elif valik == 6:
        print("Vastus: ",kalk.ruutjuur())
        break
    elif valik == 0:
        print('Sisesta uuesti üks liitmise operaator')
        break

class Kalkulaator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def liitmine(self):
        return self.a + self.b

    def lahutamine(self):
        return self.a - self.b

    def korrutamine(self):
        return self.a * self.b

    def jagamine(self):
        if self.b == 0:
            return "Viga: jagamine nulliga pole lubatud!"
        return self.a / self.b

    def jaak(self):
        return self.a % self.b

    def ruutjuur(self):
        return self.a ** 0.5

    def ruut(self):
        return self.a ** 2

    def protsent(self):
        return (self.a * self.b) / 100

def menu():
    """Kuvab kalkulaatori valikute menüü."""
    print("Vali üks valikutest:")
    print("1. Liitmine")
    print("2. Lahutamine")
    print("3. Korrutamine")
    print("4. Jagamine")
    print("5. Jäägi leidmine")
    print("6. Ruutjuure leidmine")
    print("7. Ruut")
    print("8. Protsent")
    print("0. Välju")

def main():

    try:
        a = float(input("Sisesta esimene number: "))
        b = float(input("Sisesta teine number: "))
    except ValueError:
        print("Sisesta kehtiv number!")
        return

    kalk = Kalkulaator(a, b)

    while True:
        menu()
        try:
            valik = int(input("Sisesta üks valikutest: "))
        except ValueError:
            print("Sisesta kehtiv valik!")
            continue

        if valik == 1:
            print(f"Vastus: {kalk.liitmine()}")
        elif valik == 2:
            print(f"Vastus: {kalk.lahutamine()}")
        elif valik == 3:
            print(f"Vastus: {kalk.korrutamine()}")
        elif valik == 4:
            print(f"Vastus: {kalk.jagamine()}")
        elif valik == 5:
            print(f"Vastus: {kalk.jaak()}")
        elif valik == 6:
            print(f"Vastus: {kalk.ruutjuur()}")
        elif valik == 7:
            print(f"Vastus: {kalk.ruut()}")
        elif valik == 8:
            print(f"Vastus: {kalk.protsent()}")
        elif valik == 0:
            print("Programmist väljumine...")
            break
        else:
            print("Vale valik, proovi uuesti!")

if __name__ == "__main__":
    main()



