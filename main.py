import json,os,re,time
from urllib.request import*
KN=(21,19,12,8,-8,-12,-19,-21);BD=(11,9,-9,-11);RD=(10,1,-10,-1);KG=BD+RD;DR={'N':KN,'B':BD,'R':RD}
V=(0,100,320,330,500,0,900);I=10**6
W="kkkklmmgljikkkkollmpmmoquuuukkkkaceecgklelmneknoelnoekmncgkkaceegiiiilkkimmmikmmillmiklmikkkgiiikkkljkkkjkkkjkkkjkkkjkkklmmmkkkkhjihjjkkghklfgkkefjjefiieeffccddgiijikkkiklljklljkllikllikkkgiij"
PS=[(ord(c)-107)*5 for i in range(0,192,4)for c in W[i:i+4]+W[i:i+4][::-1]]
SQ=[i for i in range(21,99)if 0<i%10<9]
MP=dict(zip("PNBRQKpnbrqk",(1,2,3,4,6,5,-1,-2,-3,-4,-6,-5)))
nd=0;BG=150000;DL=0
def fl(s):
 t=list(''.join(s[i:i+10]for i in range(110,-1,-10)).swapcase())
 r=t[112]+t[113]+t[110]+t[111]
 t[0:4]=r.translate({49:'3',50:'4',51:'1',52:'2'})
 t[110:114]='    '
 return''.join(t)
def fi(i):return 110-i+2*(i%10)
def pv(p,i):
 j=(9-i//10)*8+i%10-1;t=abs(MP[p])
 return V[t]+PS[(t-1)*64+(j if p<'a'else j^56)]
def sf(fen):
 a=fen.split()
 B=' '*21+re.sub(r'\d',lambda m:'.'*int(m.group()),a[0]).replace('/','  ')+' '*21
 if a[1]=='b':B=fl(B)
 c=a[2];z='KQkq'if a[1]=='w'else'kqKQ'
 B=''.join(str(i+1)if z[i]in c else' 'for i in range(4))+B[4:]
 s=sum(pv(B[i],i)*(2*B[i].isupper()-1)for i in SQ if B[i].isalpha())
 return(B,s)
def at(P,sq):
 B=P[0]
 if'p'in(B[sq-9],B[sq-11]):return 1
 for d in KN:
  if B[sq+d]=='n':return 1
 for d,w in zip(KG,('bq',)*4+('rq',)*4):
  j=sq+d
  if B[j]=='k':return 1
  while B[j]=='.':j+=d
  if B[j]in w:return 1
 return 0
def gn(P,cap=0):
 B=P[0]
 z=[];A=z.append
 for i in SQ:
  p=B[i]
  if p.isupper():
   if p=='P':
    for d in(-10,-9,-11):
     t=i+d;q=B[t]
     if q.islower()and d!=-10 or d==-10 and q=='.'and(not cap or i//10==3):
      if i//10==3:
       for pt in(6,4,3,2):A(i|t<<7|pt<<14)
      else:A(i|t<<7)
     if d==-10 and i//10==8 and q=='.'and B[i-20]=='.'and not cap:A(i|(i-20)<<7)
   else:
    for d in DR.get(p,KG):
     t=i
     while 1:
      t+=d;q=B[t]
      if q.islower()or(q=='.'and not cap):A(i|t<<7)
      if q!='.'or p not in'BQR':break
 if not cap and B[95]=='K'and not at(P,95):
  for r,h,d,t in((0,98,97,96),(1,91,93,94)):
   if B[r]==str(r+1)and B[h]=='R'and B[d]==B[t]=='.'and(r==0 or B[92]=='.')and not at(P,d)and not at(P,t):A(95|d<<7)
 return z
def mv(P,m):
 B,sc=P
 f=m&127;t=(m>>7)&127;p=B[f];q=B[t]
 np='NBR Q'[(m>>14)-2]if m>>14 else p
 ds=pv(np,t)-pv(p,f)+(pv(q,t)if q!='.'else 0)
 b=list(B);b[f]='.';b[t]=np
 if p=='K':
  b[0]=b[1]=' '
  if abs(t-f)==2:
   x=(98,96)if t>f else(91,94)
   b[x[0]]='.';b[x[1]]='R';ds+=pv('R',x[1])-pv('R',x[0])
 elif f in(91,98):b[f==91]=' '
 if q=='r'and t in(21,28):b[2+(t==21)]=' '
 return(fl(''.join(b)),-(sc+ds))
def bad(P):return at((fl(P[0]),),fi(P[0].find('k')))
Ab=Exception
def sr(P,a,b,d,pl):
 global nd
 nd+=1
 if nd>BG or time.time()>DL:raise Ab
 B=P[0];ck=at(P,B.find('K'));bs=-I
 if d<=0:
  if pl>90:return P[1]
  if not ck:
   bs=P[1]
   if bs>=b:return bs
   a=max(a,bs)
 else:
  pass
 l=gn(P,d<=0 and not ck)
 al=0
 for m in sorted(l,key=lambda m:-(V[abs(MP[B[(m>>7)&127]])]*16-V[abs(MP[B[m&127]])]//16 if B[(m>>7)&127]!='.'else 0)):
  P2=mv(P,m)
  if bad(P2):continue
  al=1
  s=-sr(P2,-b,-a,d-1,pl+1)
  if s>bs:bs=s
  if s>a:a=s
  if a>=b:break
 if not al:return-99999+pl if ck else bs if d<=0 else 0
 return bs
def uc(m,blk):
 f=m&127;t=(m>>7)&127
 if blk:f=fi(f);t=fi(t)
 return chr(96+f%10)+str(10-f//10)+chr(96+t%10)+str(10-t//10)+('nbr q'[(m>>14)-2]if m>>14 else'')
def rt(g):
 global nd,DL
 f=g["fen"];pos=sf(f);blk=f.split()[1]=='b'
 nd=0;DL=time.time()+5
 lg=[m for m in gn(pos)if not bad(mv(pos,m))]
 if not lg:return None
 bm=lg[0]
 for d in range(1,99):
  try:
   a=-I;b2=bm
   for m in lg:
    s=-sr(mv(pos,m),-I,-a,d-1,1)
    if s>a:a=s;b2=m
  except Ab:break
  bm=b2;lg.remove(bm);lg.insert(0,bm)
 return uc(bm,blk)
def po(pa,bo):return json.load(urlopen(os.getenv("MAKEFUN_ENV_URL")+pa,data=json.dumps(bo).encode()))
while __name__=="__main__":
 g=po("/game",{});s=g["status"]
 if s=="done":break
 while s=="your_move":
  try:u=rt(g)
  except:u=None
  L=g["legal_moves"];g=po("/move",{"game":g["game"],"move":u if u in L else L[0]});s=g["status"]
