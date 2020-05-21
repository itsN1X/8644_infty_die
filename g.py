# (C) 1996 Nikhil @itsN1X Pandita
## A d/gamblers calculator.
### https://itsn1x.github.io/8621_infty_die : JavaScript (ES8 compatible)
### https://itsn1x.github.io/8644_infty_die : Python (2.0 & 3 compatible)
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
            print(i,llast(e,f,i),suma(e,f,i),profun(e,f,i,h))
# For use w/o imports;
## Utilities (On by default)
iini = float(input("ini : "))
iinc = float(input("inc : "))
iite = int(input("ite : "))
wincon = int(input("wco : "))
print(profun(iini,iinc,iite,wincon))
l(iini,iinc,iite,wincon)
