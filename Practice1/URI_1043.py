A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)

if(A<B+C and B<A+C and C<A+B):
    perimeter = A + B +C
    print("Perimetro = %0.1f"%perimeter)
else:
    area = ((A+B)/2)*C
    print("Area = %0.1f"%area)