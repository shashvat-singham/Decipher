from __future__ import print_function
from sage.all import *

N = Integer(84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093)
message = Integer(58851190819355714547275899558441715663746139847246075619270745338657007055698378740637742775361768899700888858087050662614318305443064448898026503556757610342938490741361643696285051867260278567896991927351964557374977619644763633229896668511752432222528159214013173319855645351619393871433455550581741643299)
e = Integer(5)

def str_to_binary(part_message):
	return ''.join(['{0:08b}'.format(ord(x)) for x in part_message])

def solve(polynomial, N, beta, m, t, X):
	degree = polynomial.degree()
	n = degree*m + t
	polynomial_Z = polynomial.change_ring(ZZ)
	x = polynomial_Z.parent().gen()
	g = []
	for i in range(m):
	    for j in range(degree):
	        g.append((x * X)**j * N**(m - i) * polynomial_Z(x * X)**i)
	for i in range(t):
	    g.append((x * X)**i * polZ(x * X)**m)
	B = Matrix(ZZ, n)
	for i in range(n):
	    for j in range(i+1):
	        B[i, j] = g[i][j]
	B = B.LLL()
	new_polynomial = Integer(0) 
	for i in range(n):
	    new_polynomial += x**i * B[0 , i] / X**i
	potential_roots = new_polynomial.roots()
	roots = []
	for root in potential_roots:
	    if root[0].is_integer():
	        result = polynomial_Z(ZZ(root[0]))
	        if gcd(N, result) >= N**beta:
	            roots.append(ZZ(root[0]))
	return roots

def decrypt_message(part_message):
    global e, N, message
    binary_message = str_to_binary(part_message)
    for i in range(300):
        polynomial_ring = PolynomialRing(Zmod(N), names=('x',))
        x = polynomial_ring._first_ngens(1)[0]
        polynomial = ((int(binary_message, 2 ) << i) + x)**e - message		
        degree = polynomial.degree()
        beta = Integer(1)                                 
        epsilon = beta / Integer(7)                       
        m = ceil(beta**Integer(2)  / (degree * epsilon))     
        t = floor(degree * m * ((Integer(1) / beta) - Integer(1) ))    
        X = ceil(N**((beta**Integer(2) /degree) - epsilon)) 

        roots = solve(polynomial, N, beta, m, t, X)
        if roots:
        	print("Password is: ", end = "")
        	s = '{0:b}'.format(roots[0])
        	s = "0"*(8 - (len(s)%8)) + s
        	for i in range(0, len(s), 8):
        		print(chr(int(s[i:i+8], 2)), end="")
        	print()
        	return
    print("No root found!")

if __name__ == '__main__':
	part_message = 'This door has RSA encryption with exponent 5 and the password is '
	decrypt_message(part_message)