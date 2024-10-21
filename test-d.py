import random
from sympy import nextprime, isprime, mod_inverse, gcd

if __name__ == '__main__':
    
    p=2912249246407350784176046272217635824348493994639691593570341100704567652062349668400102883536701013041993716182991702632322195215646016988444403408894047
    q=2912249246407350784176046272217635824348493994639691593570341100704567652062349668400102883536701013041993716182991702632322195215646016988444403408893193
    e=1995575452517690010426902032099454396416525926485025021429372404347955281889402055531821974453428782880046837780945342474924492574796687810572967923504125696071570418709255174818639523693393347814304438749638124234088410456894094454443253969104020932559318145085363866757557039812809578220097205389566761137
    d=17
    
    phi=(p-1)*(q-1)
    
    if gcd(e,phi) != 1 :
        print(f"failed!")
    
    print(f"success!")