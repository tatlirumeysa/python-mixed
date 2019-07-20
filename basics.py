'czesc!'
type('czesc!')

a='rumeysa'
for i in a:
    print(a[i])

mlt=1
elimizdekisayi=[5,6,7,5,6,4]
for i in elimizdekisayi:
    mlt*=elimizdekisayi[len(elimizdekisayi)-1]
    
print(mlt)


divmod(4,2)

a='rumeysa'
liste1=[1,2.9,'v','r']
liste2=list(a)
list3=[liste1,liste2]
print(list3)

#out of range problem here
liste_kare=[1,2,3,[1,4,9]]
for i in liste_kare:
    if(i==5):
        break
    else:
        print("sayimiz: "+str(i)+" karesi: "+str(liste_kare[4][i]))
        

name="rumeysa"
name[-2]
name[1:-1]
        
"{2+2}+{10%3}"

name = "john smith"
name.title()
name.strip()
name.find("smith") 

10/3
10//3

10**3
"bag"<"apple"

def fizz_buzz(num):
    if num % 3 == 0 :
        print("fizz")
    elif num % 5 == 0 :
        print("buzz")
    elif num%3==0 and num%5==0 :
        print("FizzBuzz")
    else:
        print(num)
        
fizz_buzz(4)

fizz_buzz(15)
