# (C) 1996 Nikhil @itsN1X Pandita
# ://itsN1X.github.io/8621_infty_die : JavaScript (ES8 compatible)
# ://itsN1X.github.io/8644_infty_die : Python (2.0 & 3 compatible)
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
            print(str("#"+str(i)+"="+str('%.8f'%llast(e,f,i))+"\tTL="+str('%.8f'%suma(e,f,i))+"\tNP="+str('%.8f'%profun(e,f,i,h))+"\t+"+str('%.8f'%((((h*llast(e,f,i))/(suma(e,f,i)))-1)*100))+"%"))
iini= float(input("ini : "))
iinc= float(input("inc : "))
iite= int(input("ite : "))
wincon= int(input("wco : "))
l(iini,iinc,iite,wincon)
