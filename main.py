import json,os,sys
from urllib.request import Request,urlopen
sys.setrecursionlimit(100000)
KN=(21,19,12,8,-8,-12,-19,-21);KG=(11,10,9,1,-1,-9,-10,-11);BD=(11,9,-9,-11);RD=(10,1,-10,-1)
V=(0,100,320,330,500,900,0);M=100000;I=200000
W="kkkklmmgljikkkkollmpmmoquuuukkkkaceecgklelmneknoelnoekmncgkkaceegiiiilkkimmmikmmillmiklmikkkgiiikkkljkkkjkkkjkkkjkkkjkkklmmmkkkkgiijiklkilllkklljkllikllikkkgiijoqmkookkiggggeececcaeccaeccaecca"
PS=[(ord(c)-107)*5 for i in range(0,192,4)for c in W[i:i+4]+W[i:i+4][::-1]]
SQ=[r*10+f for r in range(9,1,-1)for f in range(1,9)]
MP=dict(zip("PNBRQKpnbrqk",(1,2,3,4,5,6,-1,-2,-3,-4,-5,-6)))
nd=0;BG=38000
def fl(s):return''.join(s[i*10:(i+1)*10]for i in range(11,-1,-1)).swapcase()
def fi(i):return(11-i//10)*10+i%10
def pv(p,i):
 j=(9-i//10)*8+i%10-1;t=abs(MP[p])
 return V[t]+PS[(t-1)*64+(j if p.isupper()else j^56)]
def sf(fen):
 a=fen.split()
 B=' '*20+''.join(' '+''.join('.'*int(ch)if ch.isdigit()else ch for ch in rw)+' 'for rw in a[0].split("/"))+' '*20
 if a[1]=='b':B=fl(B)
 s=sum((1 if p.isupper()else-1)*pv(p,i)for i in SQ for p in[B[i]]if p.isalpha())
 return(B,s)
def at(P,sq):
 B=P[0]
 if B[sq-9]=='p'or B[sq-11]=='p':return 1
 for ds,tt in((KN,'n'),(KG,'k'),(BD,'bq'),(RD,'rq')):
  for d in ds:
   j=sq+d
   if len(tt)>1:
    while B[j]=='.':j+=d
   if B[j]in tt:return 1
 return 0
def gn(P,cap=0):
 B=P[0]
 ms=[];A=ms.append
 for i in SQ:
  p=B[i]
  if not p.isupper():continue
  if p=='P':
   tg=[i+d for d in(-10,-9,-11)if(d==-10 and B[i+d]=='.')or(d!=-10 and B[i+d].islower())]
   if i//10==8 and B[i-10]=='.'and B[i-20]=='.'and not cap:A(i|(i-20)<<7)
   for t in tg:
    if i//10==3:
     for pt in(5,4,3,2):A(i|t<<7|pt<<14)
    elif not cap or B[t]!='.':A(i|t<<7)
  else:
   sl=p in'BQR'
   for d in(KN if p=='N'else BD if p=='B'else RD if p=='R'else KG):
    t=i
    while 1:
     t+=d;q=B[t]
     if q=='.':
      if not cap:A(i|t<<7)
     else:
      if q.islower():A(i|t<<7)
      break
     if not sl:break
 return ms
def mv(P,m):
 B,sc=P
 f=m&127;t=(m>>7)&127;p=B[f];q=B[t]
 np='NBRQ'[(m>>14)-2]if m>>14 else p
 ds=pv(np,t)-pv(p,f)+(pv(q,t)if q!='.'else 0)
 b=list(B);b[f]='.';b[t]=np
 return(fl(''.join(b)),-(sc+ds))
def bad(P):
 B=P[0]
 return at((fl(B),),fi(B.index('k')))
def ms(P,m):
 B=P[0];f=m&127;t=(m>>7)&127;v=B[t]
 return(V[abs(MP[v])]*16-V[abs(MP[B[f]])]//16 if v!='.'else 0)+V[m>>14]*16
class Ab(Exception):pass
def qs(P,a,b,pl):
 global nd
 nd+=1
 if nd>BG:raise Ab
 if pl>90:return P[1]
 ck=at(P,P[0].index('K'));bs=-I
 if not ck:
  bs=P[1]
  if bs>=b:return bs
  if bs>a:a=bs
 l=gn(P,not ck)
 al=0
 for m in sorted(l,key=lambda m:ms(P,m),reverse=True):
  P2=mv(P,m)
  if bad(P2):continue
  al=1;s=-qs(P2,-b,-a,pl+1)
  if s>bs:bs=s
  if s>a:a=s
  if a>=b:break
 if not al:return-M+pl if ck else bs
 return bs
def sr(P,a,b,d,pl):
 global nd
 if d<=0:return qs(P,a,b,pl)
 nd+=1
 if nd>BG:raise Ab
 ck=at(P,P[0].index('K'))
 bs=-I;al=0
 for m in sorted(gn(P),key=lambda m:ms(P,m),reverse=True):
  P2=mv(P,m)
  if bad(P2):continue
  al=1
  s=-sr(P2,-b,-a,d-1,pl+1)
  if s>bs:bs=s
  if s>a:a=s
  if a>=b:break
 if not al:return-M+pl if ck else 0
 return bs
def uc(m,blk):
 f=m&127;t=(m>>7)&127
 if blk:f=fi(f);t=fi(t)
 return chr(96+f%10)+str(10-f//10)+chr(96+t%10)+str(10-t//10)+('nbrq'[(m>>14)-2]if m>>14 else'')
def rt(g):
 global nd
 f=g["fen"];pos=sf(f);blk=f.split()[1]=='b'
 nd=0
 lg=[m for m in gn(pos)if not bad(mv(pos,m))]
 if not lg:return None
 bm=lg[0];d=1
 while 1:
  try:
   a=-I;b2=bm
   for m in lg:
    s=-sr(mv(pos,m),-I,-a,d-1,1)
    if s>a:a=s;b2=m
  except Ab:break
  bm=b2;lg.remove(bm);lg.insert(0,bm);d+=1
 return uc(bm,blk)
def po(pa,bo):return json.load(urlopen(Request(os.getenv("MAKEFUN_ENV_URL")+pa,data=json.dumps(bo).encode(),headers={"content-type":"application/json"})))
if __name__=="__main__":
 while 1:
  g=po("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   try:u=rt(g)
   except Exception:u=None
   L=g["legal_moves"];g=po("/move",{"game":g["game"],"move":u if u in L else L[0]})
