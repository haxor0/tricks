###########################################################"####################type de base
a=5
b=6.5
c=[1,2,3,[],False]
d={1:"fgd",2:"dfgdfg",3:"dfgdfgdfh"}
e=True
f={range(10)}#ensemble
g="fdg|dfg|dfg|d"
h=(1,2,3,'j',"dfgf")
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h))
################################################################################la convertion
print(float("8.22e10"))
print(int('a',16))#convertion tous les bases vers le decimal
print(int("17",8)) # 8 dans la base 10 c'est 8 toujours les doubles cottes le nombre octle a de 0 jusqua 7
print(str(c))
print(ord("a"))#char to ascci
print(chr(65))#ascci to char
print(bin(10))#decimal to binary
print(bin(10)[2:]) #pour avoir juste la partie binaire
print(int("11",2))#pour avoir l"entier a partir du binaire
print(list(oct(8)).count("1"))#convert 8 to octale -> convertion to liste char -> count var="1"
print(set(d))#set args has containner dict (keys) tuple list , non double
print(dict([(1,2),(3,"fghg")]))#list tuple to dict
print("|".join(d.values()))# value must be str
print(g.split("|"))#Strings to list with var = "|"
print([int(x) for x in ('1','29','-3')]) #convert list Strings to list integer
################################################################################l'affectation
i,*j=["rdfgdf","fdghdf","dfgdfgd",55,9,7]
print(i,j)
k,l,m="dfg",99,'gfhfgh'#paking
print(k,l,m)
k,m=m,k
print(k,m)#permut
################################################################################Indexation Conteneurs SÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©quences
print(g[::-1])#inverse while have negative step [tranche dÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©but:tranche fin:pas]
del c[1:]# delete from a list or update c[1:]=[5,6,9]
print(c)
print(len(g))#lenght of String g

if 1 in d: #in d.keys
   print("hahaha")

################################################################################Maths
from math import *
print(cos(pi))#return float
print(abs(6-9))

print(10,20,sep="",end="")#sep seperator end= finish not return in line
print(50)

o=[1,2,3,[]]
print(all(o),any(o))#return if all is True -> any one is true return true
o.insert(1,"dfgdf")#add value in index
print(o)
o.pop()#del the last one of the list and return it o.pop(indx)
print(o)
o.reverse()#its an action cant print it  onlu in list
print(o)

x=g.replace("|","*")#we cant modify g but we can creat other variable that can be have new version of g
print(x)

print(sorted(g))#sort strings char by char

import copy
q=copy.deepcopy(o)#copy by depth if u use q=g if u modify q u also modify g
print(q)

################################################################################OpÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©rations sur ChaÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â®nes
r="***********k*ijkf*g*nd*fgdfg sdfs sdfsdfsd***********"
print(r.split(" ",1))#if you want splite by n splites
print(r.startswith("ki",0,9)) #return boolean if String start with this prefix or specify when char star and finishr.startswith("*ki",2,9) de 2 jusqua 9 non inclus default index = 0 and second is only limit research
print(r.endswith("*",1,3))#3 non includ
print(r.strip("*"))#return a copy of String without char from beinging and the end of string -> lstrip left and rstrip for the right of String

s="fdskj fnsid"
print(s.upper())
print(s.swapcase())
print(s.ljust(20,"/"))#remplir par / jusqua obtenir 20 char in line -> rjust()

#def fct(x,y,z,*args,a=3,b=5,**kwargs) # avec *args is a tuples and **args is dict


print(id(q),id(r))#return adress
print ("My name is %s and weight is %d kg!" % ('Zara', 21)) #formating
#{value}{unit} ({time:%H:%M:%S})".format(value=3, unit="ppm", time=datetime.now())
print (r'C:\\nowhere')#pour echapper l'echapement

################################################################################
from string import *

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)#il est dans la classe str
str = "this is string example....wow!!!"
print (str.translate(trantab)) #remplacer caractere par d'autres

################################################################################

import calendar

cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)
###################################################################

x=["1","2","3","4"]
print(max(x) )
#attention pop a comme paramettre l index est non la valeur pour cela il faut utiliser la methode de remove
#' '.join("   je      fais du       python".split()) pour elimner les espaces
#print(print(time.clock())) pour savoir le temps d'execution de mon programme
#sorter by lenh
#li=['123','158','11','1547']
#li.sort(key=len)
#print(li)
#filter(lambda x: x>18 ,nom_list) // condition dur la liste majeurs = [a for a in ages if a > 18]

###################################################################
# regular expressions

##########################################################
import re

a=re.search("abc",'abcdef')
print(a.end(),a.start(),a.span(),a.group())
a=re.search("^abc","tabc")
# a=re.search("^abc","tabc")  ^ veut preciser if la chaine se trouve au debut sion retournee none et le $ si la chaine se trouve a la fin
# a=re.search("^ab*c","abbbbbbbbc") * veut dire une multiplicite de b ou zero vrai meme si b n'existe pas ; pas d'autre caracteres si vous voulez plus de 1 et non zero il faut changer le * pas + et si soi zero soit 1 pas plus on met ?
# a=re.search("^(abc){1,10}","abcabcabc") la recurence de abc doit est relier et {1,10} ; la recurence entre 1 et 10 et {1} exactement 1
# a=re.search("^(a[abc]*c){1}","abcabcabc") les crochets veut dure l'une des variable sont permise oui bien une liste [a-z]
# a=re.sub("(est)[ ]?([0-9]*)",r"\2 \1","votre age est ") la 1 "" la recurence la 2"" avec quoi en va remplacer et la "" la chaine a traité

# li.sort(key=lambda x:x[1]) facon de trier une liste celon un critere important

# dic1={a:b for b,a in dic.items()} tres importants inverser un dic

# import re
#
# a=re.search("^(0[16])[ ]?( ([0-9]){2}){4}$","06 99 62 63 12")
# b=re.compile("[0-9]+(.[0-9]+)?")
# print(b.search("123456.36"))



# import re
# a=re.compile("\[[a-z A-Z 0-9]+\]")
# b=a.sub("[?]","kjsdhfsdkjch[fcfgvxfc]kjcxhvx[?][cdvjklhdnxmlw]")
# print(b


#from fractions import Fraction si entier il retourne un entier sinon une fraction



#all(l[i][j+x]=="." for x in range(li[1]))













#important
#e=sum(1 for i in l1 if i > 0)



















