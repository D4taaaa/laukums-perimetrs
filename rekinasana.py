class taisnsturis:
    def __init__(self, garums1, garums2):
        self.laukums = garums1*garums2
        self.perimetrs = (garums1*2) + (garums2*2)

    def printLaukums(self):
        print("Laukums taisnsturim: " + str(self.laukums))

    def printPerimetrs(self):
        print("Perimetrs taisnsturim: " + str(self.perimetrs))

class kvadrats():
    def __init__(self, garums):
        self.laukums = garums*garums
        self.perimetrs = garums*4
    def printLaukums(self):
        print("Laukums kvadratam: " + str(self.laukums))

    def printPerimetrs(self):
        print("Perimetrs kvadratam: " + str(self.perimetrs))

class trijsturis():
    def __init__(self, garums1, garums2, garums3):
        self.laukums = garums1*garums2/2
        self.perimetrs = garums1+garums2+garums3
    def printLaukums(self):
        print("Laukums trijsturim(taisnlenka): " + str(self.laukums))

    def printPerimetrs(self):
        print("Perimetrs trijsturim(taisnlenka): " + str(self.perimetrs))



#taisnsturim malu garumi
garums1taisnsturim = 2
garums2taisnsturim = 5

#kvadrata malas garums
garumsKvadratam = 8

#trijstura malu garumi
katete1 = 3
katete2 = 4
hipetanuza = 5
