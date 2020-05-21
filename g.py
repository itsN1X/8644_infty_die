# (C) 1996 Nikhil @itsN1X Pandita
## Gamblers calculator.
### https://itsn1x.github.io/8621_infty_die/ : JavaScript (ES8 compatible)
### https://itsn1x.github.io/8644_infty_die/ : Python (2.0 & 3 compatible)
def suma(sini, sinc, site):
	ssum=0
	for si in range(site):
		ssum=ssum+sini
		sini=sini*sinc
	return ssum
def llast(lini,linc,lite):
	llini=lini*(linc**(lite-1))
	return llini
def profun(a,b,c):
	x=wincon*llast(a,b,c)
	y=(suma(a,b,c))
	return (x-y)
iini = float(input("ini : "))
iinc = float(input("inc : "))
iite = int(input("ite : "))
wincon = int(input("wco : "))
print(profun(iini,iinc,iite))
