# A degenerate gamblers' TTD calculator.
# ://itsN1X.github.io/8621_infty_die : JavaScript (ES8 compatible)
# ://itsN1X.github.io/8644_infty_die : Python (2.0 & 3 compatible)
# (C) 1996 Nikhil @itsN1X Pandita

def suma(sini, sinc, site):
	ssum=0
	for si in range(site):
		ssum=ssum+sini
		sini=sini*sinc
	return ssum
def llast(lini,linc,lite):
	llini=lini*(linc**(lite-1))
	return llini
def profun(a,b,c,d):
	x=d*llast(a,b,c)
	y=(suma(a,b,c))
	return (x-y)
def l(e,f,g,h):
    for k in range(g):
            i=k+1
            print(i,llast(e,f,i),suma(e,f,i),profun(e,f,i,h),(((h*llast(e,f,i))/(suma(e,f,i)))-1)*100)
# For use w/o imports;
# Utilities (On default)
iini = float(input("ini : "))
iinc = float(input("inc : "))
iite = int(input("ite : "))
wincon = int(input("wco : "))
l(iini,iinc,iite,wincon)
