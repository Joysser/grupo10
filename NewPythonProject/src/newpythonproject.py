# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

a=int(input('Introducir primer numero='))
b=int(input('Introducir segundo numero='))
c=int(input('Introducir tercer numero='))
d=(a+b+c)/3
if d <= 20 and d>=0:
    if d<=20 and d>=17:
        print 'Es muy bueno'
    else:
        if d<=16 and d>=14:
         print 'Es bueno'
        else:
            if d<=13 and d>= 11:
             print 'Es regular'
            else:
                    if d<=10 and d>=0:
                     print 'Es malo'
else:
    print 'numero invalido'
