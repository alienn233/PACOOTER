
import sys
import numpy as np
args=sys.argv
import sympy
####ec nr
h=sympy.Symbol('h')
z=sympy.Symbol('z')
v=sympy.Symbol('v ')
k =sympy.Symbol('k  ')
fec=((   z*k /(v-z))**(1/h))
####ec mdr1
h1=sympy.Symbol('h1')
z=sympy.Symbol('z')
v1=sympy.Symbol('v1 ')
k1 =sympy.Symbol('k1  ')
fec1=((   z*k1 /(v1-z))**(1/h1))
fec1 
fec1.evalf(subs={v1:97.61,h1:1.071, k1 :2.045  ,   z:50})
  #######tc nr
h2=sympy.Symbol('h2')
z=sympy.Symbol('z')
v2=sympy.Symbol('v2 ')
k2 =sympy.Symbol('k2  ')
ftc=((   z*k2 /(v2-z))**(1/h2))
ftc 
ftc.evalf(subs={v2:92.87,h2:1.099,k2 :5.02,z:50})


 ###########tc mdri
h3=sympy.Symbol('h3')
z=sympy.Symbol('z')
v3=sympy.Symbol('v3 ')
k3 =sympy.Symbol('k3  ')
ftc1=((   z*k3 /(v3-z))**(1/h3))
ftc1 
ftc1.evalf(subs={v3:89.79,h3:1.161,k3 :15.23,z:50})
 ###########




    #
HC=(((fec1/fec)-1)/((ftc1/ftc)-1))
vec =  []
vec1=[]
vtc=[]
vtc1=[]
a1=float( args[1]  ) /100
b1=float(args[4] )/100
c1=float(args[7] )/100
d1=float(args[10]  )/100
print(d1)
aa=float( args[1]  )
bb=float(args[4] )
cc=float(args[7] )
dd=float(args[10]  )
import pandas as pd


for a in np.arange(0, aa, a1):
    vec.append( (a,   fec.evalf(subs={v:args[1] , h:args[2] ,  k:args[3] ,z:a})  )      )
for b in np.arange(0,bb,  b1):
    vec1.append(    (b, fec1.evalf(subs={v1:args[4] , h1:args[5] , k1:args[6]  ,   z:b})      ) )
for c in np.arange(0,cc,  c1):
    vtc.append(    (c,          ftc.evalf(subs={v2:args[7] , h2:args[8] , k2:args[9] ,z:c})   ))
for d   in np.arange(0,dd,  d1):
    vtc1.append(    (d,          ftc1.evalf(subs={ v3:args[10] , h3:args[11] , k3:args[12] ,z:d})   ))
    #######
ffec=pd.DataFrame(vec, columns=['one','ec']) 
ffec1=pd.DataFrame(vec1, columns=['one','ec1']) 
fftc=pd.DataFrame(vtc, columns=['one','tc']) 
fftc1=pd.DataFrame(vtc1, columns=['one','tc1']) 
ffec=  ffec.fillna(0)
ffec1=  ffec1.fillna(0)
fftc=  fftc.fillna(0)
fftc1=  fftc1.fillna(0)
all2=(fftc1['tc1'] .astype("float")/fftc ['tc'] .astype("float")-1)
all1=(ffec1['ec1'] .astype("float")/ffec ['ec'].astype("float")-1)
    ############3
#outt1['tc' ]=fftc ['tc']
outt=all1/all2
outt1=pd.DataFrame(outt, columns=['hc' ])
outt1['tc' ]=fftc ['tc']
outt1['tc1' ]=fftc1 ['tc1']
outt1['ec' ]=ffec ['ec']
outt1['ec1' ]=ffec1 ['ec1']
outt1['cp' ] =1-outt1['hc' ].astype("float")
#outt1['cp' ]=outt1['B1' ].map(lambda x:("%.3f")%x)
outt1.to_csv(args[13],sep="\t",header=1)
ec5=ffec['ec'].astype("float")[50]
ec15=ffec1['ec1'] .astype("float")[50]
tc5=fftc['tc'] .astype("float")[50]
tc15=fftc1['tc1'] .astype("float")[50]
print(ec5,ec15,tc5,tc15)
