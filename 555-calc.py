def t(r1, r2, c):
    return 0.694*(r1+r2)*c*10**3

def t0(r1, r2, c):
    return 0.694*r2*c*10**3

def t1(r1, r2, c):
    return 0.694*r1*c*10**3

def print_t(r1, r2, c):
    print(f"Period\t\t{t(r1,r2,c):.0f}ms")
    print(f"High Time\t{t1(r1,r2,c):.0f}ms")
    print(f"Low Time\t{t0(r1,r2,c):.0f}ms")

mult=1.21
r1=220*mult
r2=300000*mult
c=220*10**-6

print_t(r1,r2,c)


