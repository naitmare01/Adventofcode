M,N={},{}
v,w=0,~0
Z=int
for x in open("input"):
 L,R=x.split(" = ")
 if"me">L:v,w=[Z(R.replace("X",b),2)for b in"01"];o=R;continue
 l=Z(L[4:-1]);M[l]=Z(R)&w|v;s={0}
 for c in o:s={x*2+(c=="1")for x in s}|{2*x+1for x in s if"W"<c}
 for q in s:N[l&~w|q>>1]=Z(R)
for x in M,N:print(sum(x.values()))