#number

pi = 3.142

x = int(pi) #tukar float jd int
print(x)
print(x,type(x)) #print value and type of x

#string
w = 10.53
x = 4
p = w + x #float boleh campur dgn integer
print(p)

s = str(w) #tkr float jd string
y = str(x) #tkr int jd string

z = s + y
print(s)
print(y)
print(z)

#list
l = ["Ciku","Durian","Manggis"] #List
print(l)
print("The data type is : ",type(l))
tup = tuple(l)
print(type(tup))
L = list(("Ciku","Durian","Manggis")) #convert tuple to list, casting
print(type(L))