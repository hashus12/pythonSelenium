####### Data Types - variables ########
# Text Types #########
# str : string type - metinsel veri için kullandığımız veri tipi
text = "Hello World"
print(type(text))

# Numeric Types #########
# int : integer type - tam sayıları için kullandığımız veri tipi
number = 20
print(type(number))

# float : float type - kayan noktalı sayılar , noktalı sayılar için kullanılan veri tipi
floatingNumber = 20.5
print(type(floatingNumber))

# complex : complex type - karmaşık sayılar için kullanılan veri tipi real+imagj
complexNumber = 2 + 1j
print(type(complexNumber))

# Boolean Types ##########
# bool : bool type - sadece true ya da false değer tutmak için kullanılan veri tipi
boolean = True
print(type(boolean))

# Sequence Type ###
# range : range type - aralık belirtmek için kullanılan veri tipi
thisRange = range(6)
print(type(thisRange))

# Python Koleksiyonları (Diziler)
# Python programlama dilinde dört koleksiyon veri tipi vardır:

# Sequence Types ##########
# list : sıralı ve değiştirilebilir bir koleksiyondur. Yinelenen üyelere izin verir.
array = ["apple", "banana", "cherry"]
print(type(array))

# tuple : sıralı ve değiştirilemez bir koleksiyondur. Yinelenen üyelere izin verir.
thisTuple = ("apple", "banana", "cherry")
print(type(thisTuple))

# set : sırasız, değiştirilemez* ve indekslenmemiş bir koleksiyondur. Yinelenen üye yoktur.
thisSet = {"apple", "banana", "cherry"}
print(type(thisSet))

# Mapping Types ###########
# dict : Dictionary sıralı** ve değiştirilebilir bir koleksiyondur. Yinelenen üye yoktur. key ve value değerler vardır.
thisDict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(type(thisDict))

# frozenset : frozenset type - setin ögeleri zamanla değiştirilebilirken frozensetin ögeleri oluşturulduktan sonra aynı kalır.
thisFrozenset = frozenset({"apple", "banana", "cherry"})
print(type(thisFrozenset))

# bytes : bytes type - binary verileri tutmak için kullanılır. tek bytelık değişmez dizilerdir. sadece ASCII uyumlu verilerle kullanmalıyız. 
thisBytes = b"Hello"
print(type(thisBytes))

# bytearray : bytearray type - binary verileri tutmak için kullanılır. değiştirilebilir nesnelerdir.
thisByteArray = bytearray(5)
print(type(thisByteArray))

# memoryview : memoryview type - objeye başvuran bir bellek görünümü oluşturulabilir. obj buffer protokolü
thisMemoryview = memoryview(bytes(5))
print(type(thisMemoryview))

# NoneType : none type - null değerini tanımlamak için kullanılır. yada hiç değer yokken.
thisNone = None
print(type(thisNone))

##### Condition Blocks - Şart Blokları######
condition = 1
if(condition == True):
    print("condition true")
elif(condition == 2):
    print("condition is 2")
else:
    print("condition false")

###### kodlama.io da örnekleri ########

# kodlama.io sitesindeki ödev kısmındaki yazılar string veri tipinde kullanılmıştır 
# Örnek: 
amac = "Derste gördüğümüz 'Değişkenler' ve 'Şart Blokları' konularının pekiştirilmesi" 
# gibi veriler tutulmaktadır.
# sitedeki kamplar bir liste içerisinde dönmektedir.
# Örnek: 
liste = ["Yazılım Geliştirici Yetiştirme Kampı (JAVA * React)", "Yazılım Geliştirici Yetiştirme Kampı (Python & Selenium)"]
# gibi bir listede tutulmaktadır.
# Şart bloğ örneği olarak ödev yapıldıysa ödevin ikonu correct ikonuna dönüşür.
# Örnek:
odev = True
if(odev == True):
    print("ödev tamamlandı ve ikon değişti")
else:
    print("ödev tamamlanmadı ve ikon değişmedi")
