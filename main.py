#6-misol
# Mashina klassi
class Mashina:
    def __init__(self, rang, tezlik, narx):
        self.rang = rang
        self.tezlik = tezlik
        self.narx = narx

m1 = Mashina("qora", 220, 20000)
m2 = Mashina("oq", 180, 15000)
m3 = Mashina("qizil", 250, 30000)

#7-misol
class Telefon:
    def __init__(self, narx, kamera, batareya):
        self.narx = narx
        self.kamera = kamera
        self.batareya = batareya

t1 = Telefon(300, "48MP", "4000mAh")
t2 = Telefon(500, "64MP", "5000mAh")
t3 = Telefon(800, "108MP", "6000mAh")


#8-misol
class Kitob:
    def __init__(self, nomi, yili, janr):
        self.nomi = nomi
        self.yili = yili
        self.janr = janr

k1 = Kitob("Alkimyogar", 1988, "roman")
k2 = Kitob("1984", 1949, "distopiya")
k3 = Kitob("Sherlok Holms", 1892, "detektiv")


#9-misol
class Talaba:
    def __init__(self, ism, fakultet, baho):
        self.ism = ism
        self.fakultet = fakultet
        self.baho = baho

s1 = Talaba("Ali", "IT", 90)
s2 = Talaba("Vali", "Iqtisod", 85)
s3 = Talaba("Hasan", "Tibbiyot", 92)


#9-misol
class Kompyuter:
    def __init__(self, protsessor, gpu, monitor):
        self.protsessor = protsessor
        self.gpu = gpu
        self.monitor = monitor

c1 = Kompyuter("i5", "GTX 1650", "22inch")
c2 = Kompyuter("i7", "RTX 3060", "24inch")
c3 = Kompyuter("Ryzen 7", "RTX 4070", "seinch")

