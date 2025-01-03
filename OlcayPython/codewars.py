def converter(mpg,mile):
    
    litres_convert = mpg * 4.5409188
    kilometres_convert = mile * 1.609334
    
    return round(litres_convert, 2),round(kilometres_convert, 2)

mpg = float(input("mpg: "))
mile = float(input("mile: "))

litres_convert,kilometres_convert = converter(mpg,mile)
print(litres_convert)
print(kilometres_convert)