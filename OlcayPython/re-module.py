import re

# re module

str = "Python Kursu: Python Programlama Rehberiniz - 40 Saat"

# #re.findall()

# result = re.findall("python",str)
# result = len(result)

# # re.split()

# result = re.split(" ",str)
# result = re.split("r",str)

# re.sub()

# result = re.sub(" ", "*",str)  #bütün boşluk karakterlerini * ile değiştir strde
# result = re.sub("\s","*",str)

#re.search()

# result = re.search("python",str)  #python ı (0 ve 6) arasında bulduk diyor.
# result = result.span()  #direkt konumunu söyledi
# result = result.end() #bitiş
# result = result.group() #bulduğu karakteri gönderir 

#regular expression
""""

    [] - Köşeli parantezler arasına yazılan bütün karakter aranır.
        [abc] => a      :1 match
                ac      :2 match
                Python  :NO matches
            
        [a-e]  => [abcde]
        [1-5]  => [12345]
        [0-39] => [01239]

        [^abc]  => abc dışındaki karakterler.
        [^0-9]  => rakam olmayan karakterler.
        [^abc]  => abc dışındaki karakterler.

"""
# result = re.findall("[abc]", str)
# result = re.findall("[sat]", str)
# result = re.findall("[a-e]", str)
# result = re.findall("[a-z]", str)
# result = re.findall("[0-5]",str)
# result = re.findall("[^abc]" ,str)
# result = re.findall("[^0-9]" ,str)
"""
    . - Herhangi bir tek karakteri belirtir.
        .. =>   a       : No match
                ab      : 1 match
                abc     : 2 match
                abcd    : 2 match
"""

result = re.findall("...", str)
result = re.findall("Py..on", str)

"""
     ^ - Belirtilen string karakterlerle başlıyor mu?

        ^a =>   a:      1 match
                abc:    1 match
                bac:    No match

"""
result = re.findall("^P",str)

"""
    $ - Belirtilen karakterle bitiyor mu?
        a$ =>  a:       1 match
               lamba:   1 match
               Python:  No match
"""

# result = re.findall("t$", str)
# result = re.findall("saat$", str)
# result = re.findall("saatt$", str)


"""
    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
            ma*n => mn:     1 match
                    man:    1 match
                    maaan:  1 match
                    main:   No match (a'nın arkasından n gelmiyor)
"""
# result = re.findall("sa*t",str)

"""
    + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.
        ma+n => mn:     1 match
                    man:    1 match
                    maaan:  1 match
                    main:   No match (a'nın arkasından n gelmiyor)
"""
# result = re.findall("sa+t",str)

"""
 ? - Bir karakterin sıfır ya da bir kez olmasını kontrol eder.
        ma?n => mn:     1 match
                    man:    1 match
                    maaan:  1 match
                    main:   No match (a'nın arkasından n gelmiyor)
"""

# result = re.findall("sa?t", str)
"""
    {} - Karakter sayısını kontrol eder.
        al{2}       => a karakterinin arkasına l karakteri 2 kez tekrarlanmalı.
        al{2,3}     => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlanmalı.
        [0-9]{2,4}  => en az 2 en çok 4 basamaklı sayılar.
"""
# result = re.findall("a{2}", str)
# result = re.findall("[0-9]{2}", str)


"""
    | - Alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        a|b => a ya da b
            cde     =>  no match
            ade     =>  1 match
            acdbea =>   3 match
"""

"""
    () - gruplamak için kullanılır.
        (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""


"""
     \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterini arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.
    
    \A - Belirtilen karakter string in başında mı?
        \Athe => the string in başında mı

    result = re.findall("\APython",str)
    result = re.findall("saat\Z",str)

    \Z - Belirtilen karakter string in sonunda mı?
        the\Z => the string in sonunda mı
    
    \b - Belirtilen karakter string in başında ya da sonunda mı?
        \bthe => the kelimenin başında mı
        the\b => the kelimenin sonunda mı
    
    \B - Belirtilen karakter string in başında ya da değil mi?
        \Bthe => the kelimenin başında değil mi
        the\B => the kelimenin sonunda değil mi
    
    \d - [0-9] ile aynı anlama gelir yani rakamlar arar.
        \d => 12abc34
    
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
        \D => 1ab44_50
    
    \s - Boşluk karakterlerini arar.
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri
    \W - \w nin tam tersi
"""

print(result)