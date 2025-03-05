class cal():                             # Kalkulaatori klass
    def __init__(self,a,b):             # Konstruktor, mis võtab kaks sisendit
        self.a = a                      # Esimene sisend
        self.b = b                      # Teine sisend

    def liitmine(self):                # Liitmise funktsioon
        return self.a + self.b
    
    def lahutamine(self):              # Lahutamise funktsioon
        return self.a - self.b
    
    def korrutamine(self):             # Korrutamise funktsioon
        return self.a * self.b
    
    def jagamine(self):                # Jagamise funktsioon
        if self.b != 0:                # Kontroll, et ei jagataks nulliga
            return self.a / self.b
        else:
            return 'Nulliga jagamine pole lubatud'
    
    def jaak(self):                    # Jäägi leidmise funktsioon
        return self.a % self.b
    
    def astendamine(self):             # Astendamise funktsioon (a astmel b)
        return self.a ** self.b
    
    def keskmine(self):                # Keskmise leidmise funktsioon
        return (self.a + self.b) / 2
    
    def min_arv(self):                 # Miinimumarvu leidmine
        return min(self.a, self.b)
    
    def max_arv(self):                 # Maksimumarvu leidmine
        return max(self.a, self.b)

# Kasutajalt sisendite küsimine
a = int(input("Sisesta esimene number: "))           
b = int(input("Sisesta teine number: "))

kalk = cal(a,b)                         # Objekti loomine kalkulaatori klassist

while True:
    def menu():                         # Funktsioon, mis prindib menüü valikud
        x = ('1. Liitmine \n2. Lahutamine\n3. Korrutamine\n4. Jagamine\n5. Jäägi leidmine\n6. Astendamine\n7. Keskmine\n8. Miinimum\n9. Maksimum\n0. Välju')
        print(x)
    
    menu()                              # Menüü kuvamine
    valik = int(input('Sisesta üks valikutest: '))  # Kasutaja valiku küsimine
    
    if valik == 1:
        print("Vastus: ", kalk.liitmine())
    elif valik == 2:
        print("Vastus: ", kalk.lahutamine())
    elif valik == 3:
        print("Vastus: ", kalk.korrutamine())
    elif valik == 4:
        print("Vastus: ", kalk.jagamine())
    elif valik == 5:
        print("Vastus: ", kalk.jaak())
    elif valik == 6:
        print("Vastus: ", kalk.astendamine())
    elif valik == 7:
        print("Vastus: ", kalk.keskmine())
    elif valik == 8:
        print("Vastus: ", kalk.min_arv())
    elif valik == 9:
        print("Vastus: ", kalk.max_arv())
    elif valik == 0:
        print('Programmi lõpp')
        break
    else:
        print('Vale valik, proovi uuesti')



