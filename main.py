class Bank:
    def __init__(self, name, number_card, kod, balance):
        self.__name = name
        self.__num = number_card
        self.__kod = kod
        self.__balance = balance
        self.kartalar = []
        self.kartalar.append(number_card)

    def pul_otkazish(self, karta, ozini_karta_kodi, otkazish_summasi):
        if karta in self.kartalar and otkazish_summasi <= self.__balance and ozini_karta_kodi == self.__kod:
            self.__balance -= otkazish_summasi
            print("pul tushdi")
        else:
            print("O'tkazish muvaffaqiyatsiz.")

    def balance(self):
        print(f"Balans: {self.__balance}")


a = input("Ismingizni kiriting: ")
c = int(input("Karta raqamingizni kiriting: "))
d = int(input("Balansingizni kiriting: "))
x = int(input("Karta kodni kiriting: "))
b1 = Bank(a, c, x, d)

print("Ikkinchi user:\n")
b2 = Bank(input("Ismingizni kiriting: "),
           int(input("Karta raqamingizni kiriting: ")),
           int(input("Karta kodni kiriting: ")),
           int(input("Balansingizni kiriting: ")))


a1 = int(input("O'tkazmoqchi bo'lgan karta raqamingizni kiriting: "))
c1 = int(input("O'zingizning karta kodini kiriting: ")) 
f1 = int(input("O'tkazish summasini kiriting: "))
b1.pul_otkazish(a1, c1, f1)
b1.balance()
b2.balance()