x="i am divyadarsini"
q="I AM DIVYADARSINI"
m="dd oo dd ooo dd."
#capitalize() Converts the first character to upper case#
y=x.capitalize()
print(y)
#casefold() Converts string into lower case#
a=q.casefold()
print(a)
#center() Returns a centered string#
b=x.center(35)
print(b)
#count() Returns the number of times a specified value occurs in a string#
f=m.count("dd")
print(f)
t=m.count("dd",5,9)
print(t)
#encode() Returns an encoded version of the string#
l="My name is Ståle"
o=l.encode()
print(o)
#endswith() Returns true if the string ends with the specified value#
n=m.endswith(".")
print(n)
#expandtabs() Sets the tab size of the string#
w="H\te\tl\tl\to"
print(w.expandtabs())
print(w.expandtabs(2))
print(w.expandtabs(4))
print(w.expandtabs(10))
#find() Searches the string for a specified value and returns the position of where it was found#
e=q.find("DIVYADARSINI")
print(e)
#format() Formats specified values in a string#
t="For only {price:.2f} dollars!"
print(t.format(price = 49))
#index() Searches the string for a specified value and returns the position of where it was found#
v=q.find("DIVYADARSINI")
print(v)
#isalnum() Returns True if all characters in the string are alphanumeric#
h="DONKEY15"
f=h.isalnum()
print(f)
#isalpha() Returns True if all characters in the string are in the alphabet#
po="COMPANY"
pi=po.isalpha()
print(pi)
#isdecimal() Returns True if all characters in the string are decimals#
pa="\u0033"
pu=pa.isdecimal()
print(pu)
#isdigit() Returns True if all characters in the string are digits#
pe="56732"
pl=pe.isdigit()
print(pl)
#isidentifier() Returns True if the string is an identifier#
da = "MyFolder"
dc = "2bring"
print(da.isidentifier())
print(dc.isidentifier())
#islower() Returns True if all characters in the string are lower case#
op=x.islower()
print(op)
lp=q.islower()
print(lp)
#isnumeric() Returns True if all characters in the string are numeric#
io=pe.isnumeric()
print(io)
#isprintable() Returns True if all characters in the string are printable#
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)
#isspace() Returns True if all characters in the string are whitespaces#
num="    "
g=num.isspace()
print(g)
#istitle() Returns True if the string follows the rules of a title#
txt = "THIS IS NOW!"
x = txt.istitle()
print(x)
#isupper()	Returns True if all characters in the string are upper case#
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
#join()	Joins the elements of an iterable to the end of the string#
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
#ljust() Returns a left justified version of the string#
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
#lower() Converts a string into lower case#
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
#lstrip() Returns a left trim version of the string#
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
#maketrans() Returns a translation table to be used in translations#
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
#partition() Returns a tuple where the string is parted into three parts#
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
#replace() Returns a string where a specified value is replaced with a specified value#
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
#rfind() Searches the string for a specified value and returns the last position of where it was found#
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
#rindex() Searches the string for a specified value and returns the last position of where it was found#
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
#rjust() Returns a right justified version of the string#
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
#rpartition() Returns a tuple where the string is parted into three parts#
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
#rsplit() Splits the string at the specified separator, and returns a list#
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
#rstrip() Returns a right trim version of the string#
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
#split() Splits the string at the specified separator, and returns a list#
txt = "welcome to the jungle"
x = txt.split()
print(x)
#splitlines() Splits the string at line breaks and returns a list#
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
#startswith() Returns true if the string starts with the specified value#
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
#strip() Returns a trimmed version of the string#
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
#swapcase() Swaps cases, lower case becomes upper case and vice versa#
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
#title() Converts the first character of each word to upper case#
txt = "Welcome to my world"
x = txt.title()
print(x)
#translate() Returns a translated string#
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
#upper() Converts a string into upper case#
x="its me dd"
o=x.upper()
print(o)
#zfill() Fills the string with a specified number of 0 values at the beginning#
txt = "50"
x = txt.zfill(10)
print(x)
