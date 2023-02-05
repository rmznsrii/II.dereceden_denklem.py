import math
print("2.Dereceden Denklem Hesaplama")
#import: yüklemektir.Modül çağırmak için kullanılır
#math:Modüldür.matematiksel işlemlerden yararlanmak için içerisine yazılmış fonksiyon ve kodları programımıza dahil ediyoruz.

print("------------------------------")
print("ax**2+bx+c=0") #print: çalıştırdıktan sonra görünmesini istediğimiz şeyleri bu alana yazarız (cümle ise tırnak içinde)
print("------------------------------")

#a,b ve c değerlerini belirlemek için bize sormasını isteyeceğiz bunun için ilk önce float içine alıp sayı belirtmesini istiyoruz input içerisinede nasıl soracağını
#tırnak içinde not ediyoruz.

# float:ondalık sayı belirtir (2.5,1.2,vs.)

#input:bize çalıştırınca soru sordurtur ekrana yansıtır (okul = input("hangi okula gidiyorsun?"))

a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))

d = b*b-4*a*c #diksriminant

if d<0: #eğer d küçüktür 0 ise
    print("--------------------------")
    print("gerçel sayılarda kök yok")

if d==0: #eğer d eşittir 0 ise
    print("-------------------------")
    print("kökler çakışık") #belirtmek için
    x=-b/(2*a) #kök değerini bulmak için yapılması gereken işlem (verinlenlere göre yapılıyor)
    print("x:",x) #x'in cevabını sötermek için tırna içinde x: yazılıp (,) sonrası x'in aldığı değeri karşısına vericek

if d>0: #eğer d büyüktür 0 ise
    print("--------------------------")
    print("gerçek iki kök var")
    x1 = (-b-math.sqrt(d)) / (2*a) #math.sqrt(d) = kökdiskriminant / math.sqrt(x) = kökx
    x2 = (-b+math.sqrt(d)) / (2*a)
    print("x1:",x1)
    print("x2:",x2)

#Float: gerçel sayıya dönüştürme
#int:tam sayıya dönüştürme
#math.sqrt(x) köklü sayı belirtir
# == --> direk eşittir anlamındadır
# != --> eşit değildir
# : --> ise
# if --> eğer