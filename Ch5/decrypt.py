from BitVector.BitVector import *
import sys
import requests
import itertools
from pyfinite import ffield
from pyfinite import genericmatrix

ALGO_MODULUS    = BitVector(bitstring='10000011')
ALGO_EXPONENT   = 7
two_power_list  = []
A_matrix        = []
E_vector        = []
Inverse_list    = [0, 1, 64, 85, 32, 51, 106, 109, 16, 113, 89, 104, 53, 88, 118, 17, 8, 15, 120, 107, 108, 121, 52, 116, 90, 61, 44, 80, 59, 92, 72, 41, 4, 77, 71, 98, 60, 103, 117, 114, 54, 31, 124, 65, 26, 48, 58, 100, 45, 70, 94, 5, 22, 12, 40, 97, 93, 78, 46, 28, 36, 25, 84, 125, 2, 43, 102, 91, 99, 81, 49, 34, 30, 87, 115, 105, 122, 33, 57, 82, 27, 69, 79, 101, 62, 3, 96, 73, 13, 10, 24, 67, 29, 56, 50, 123, 86, 55, 35, 68, 47, 83, 66, 37, 11, 75, 6, 19, 20, 7, 112, 119, 110, 9, 39, 74, 23, 38, 14, 111, 18, 21, 76, 95, 42, 63, 126, 1]
A_Inverse       = []

'''
Wrapper to create a BitVector
'''
def bv(num):
    return BitVector(intVal = num, size = ALGO_EXPONENT)

'''
Initialize the algorithm
'''
def initialize():
    for i in range(8):
        E_vector.append(0)
        A_matrix.append([bv(0)]*8)
'''
Takes a string and returns a list of encoded BitVectors
'''
def encode_to_BV(str):
    bv_list = []
    for i in range(0, len(str), 2):
        first_part  = ord(str[i]) - ord('f')
        second_part = ord(str[i+1]) - ord('f')
        number = (first_part << 4) + second_part
        bv_list.append(bv(number))
    return bv_list

'''
Get Integer from the BitVector Object
'''
def get_int_from_BV(bv_num):
    return int(str(bv_num), 2)

'''
Convert list of numbers to list of BVs
'''
def convert_to_BV(l):
    ret_val = []
    for i in range(len(l)):
        ret_val.append(bv(l[i]))
    return ret_val

'''
Convert list of numbers to string encoding.
'''
def list_to_str(l):
    ret_val = ""
    for i in range(len(l)):
        second_part = chr(ord('f') + (l[i] & 0b1111))
        first_part  = chr(ord('f') + ((l[i] & 0b1110000) >> 4))
        ret_val = ret_val + first_part + second_part
    return ret_val

'''
Calculate bv_num to the power 'power'
Takes a BV and int and returns a BV
'''
def exponentiate(bv_num, power):
    if power == 0:
        return bv(1)
    elif power == 1:
        return bv_num
    elif power % 2 == 0:
        half_power = exponentiate(bv_num, power >> 1)
        return bv_multiply(half_power, half_power)
    else:
        half_power = exponentiate(bv_num, power >> 1)
        return bv_multiply(bv_multiply(half_power, half_power), bv_num)

'''
Calculate powers of 2. Updates a list of BVs.
two_power_list[i] = 2^(i*i*i)
'''
def calc_two_powers():
    for i in range(128):
        two_power_list.append(exponentiate(bv(2), i*i*i))

'''
Put a post request to the server for ciphertext
'''
def query_server(string):
    fhand = open("required_texts","r")
    for line in fhand:
        if len(line) > 5:
            text_part = line.strip().split(']')[1].strip()
            if text_part.split()[0].strip() == string:
                fhand.close()
                return text_part.split()[1].strip()
    fhand.close()
    return requests.post("https://172.27.26.181:9998/eaeae",json={"plaintext": string,"password":"4d85e2d75ba3d9e1ae200df7357e66c8","teamname":"OrderOfThePhoenix"}, verify=False).json()['ciphertext']

'''
Wrapper to multiply 2 BVs under given modulus
'''
def bv_multiply(bv1, bv2):
    return bv1.gf_multiply_modular(bv2, ALGO_MODULUS, ALGO_EXPONENT)

'''
Add Wrapper: Add two bitvectors
'''
def bv_add(bv1, bv2):
    summed_value = get_int_from_BV(bv1) ^ get_int_from_BV(bv2)
    return bv(summed_value)


'''
Given an input, and keys A and E, it returns that output at 
output_index location for the given setting
'''
def calculate_output(inp, output_index, A, E):
    j = output_index
    for t in range(8):
        if inp[t] != 0:
            i = t
            value = bv(inp[t])
            break
    sum = bv(0)
    for k in range(i,j+1):
        sum = bv_add(sum, bv_multiply(exponentiate(value, E[i]*E[k]), bv_multiply(A[j][k], exponentiate(A[k][i], E[k]))))
    return exponentiate(sum, E[j]) 

'''
Display The Keys
'''
def display_key():
    for i in range(8):
        for j in range(8):
            print("%3d " % (get_int_from_BV(A_matrix[i][j])), end=" ")
        print("E: %3d " % (E_vector[i]))
    print(" ")

'''
Main Code Breaking routine.
''' 
def break_cipher():
    e_a = [[] for i in range(8)]
    for i in [7, 6, 5, 4, 3, 2, 1, 0]:
        ciphertext_one   = encode_to_BV(query_server(list_to_str([0]*i + [1] + [0]*(7-i))))
        ciphertext_two   = encode_to_BV(query_server(list_to_str([0]*i + [2] + [0]*(7-i))))
        #Get diagonal element
        for m in range(128):
            if bv_multiply(ciphertext_one[i], two_power_list[m]) == ciphertext_two[i]:
                # E_vector[i].append(m)
                a_exponent = m*(m+1)
                for n in range(128):
                    if exponentiate(bv(n), a_exponent) == ciphertext_one[i]:
                        # A_matrix[i][i].append(bv(n))
                        e_a[i].append([m, bv(n)])

    a76_list = []
    for i in range(1,8):
        ciphertext_one   = encode_to_BV(query_server(list_to_str([0]*(i-1) + [1] + [0]*(8-i))))
        ciphertext_two   = encode_to_BV(query_server(list_to_str([0]*(i-1) + [2] + [0]*(8-i))))
        counter = 0
        e_a_current_possible = []
        e_a_prev_possible = []
        flag = 0
        for m in e_a[i]:
            for n in e_a[i-1]:
                e7  = m[0]
                a77 = m[1]
                e6  = n[0]
                a66 = n[1]
                a66_e6 = exponentiate(a66, e6)
                two_e6_e6 = exponentiate(bv(2), e6*e6)
                two_e6_e7 = exponentiate(bv(2), e6*e7)
                for t in range(128):
                    a76 = bv(t)
                    if exponentiate(bv_add(bv_multiply(a76, a66_e6), bv_multiply(a77, exponentiate(a76, e7))), e7) == ciphertext_one[i] and exponentiate(bv_add(bv_multiply(bv_multiply(two_e6_e6, a66_e6), a76), bv_multiply(two_e6_e7, bv_multiply(exponentiate(a76, e7), a77))) ,e7) == ciphertext_two[i]:
                        if i == 7:
                            a76_list.append([a76, a77, e7])
                        if m not in e_a_current_possible:
                            e_a_current_possible.append(m)
                        if n not in e_a_prev_possible:
                            e_a_prev_possible.append(n)
                        counter = counter + 1
                        flag = 1
                        A_matrix[i][i-1] = a76
            if flag == 1:
                break
        e_a[i] = e_a_current_possible
        e_a[i-1] = e_a_prev_possible
    for i in range(8):
        A_matrix[i][i] = e_a[i][0][1]
        E_vector[i]    = e_a[i][0][0]
    display_key()

    for p in range(2,8):
        for k in range(p,8):
            saved_values = []
            ciphertext_one   = encode_to_BV(query_server(list_to_str([0]*(k-p) + [1] + [0]*(7-k+p))))
            ciphertext_two   = encode_to_BV(query_server(list_to_str([0]*(k-p) + [2] + [0]*(7-k+p))))
            for i in range(128):
                A_matrix[k][k-p] = bv(i)
                if calculate_output([0]*(k-p) + [1] + [0]*(7-k+p), k, A_matrix, E_vector) == ciphertext_one[k] and calculate_output([0]*(k-p) + [2] + [0]*(7-k+p), k, A_matrix, E_vector) == ciphertext_two[k]:
                    saved_values.append(i)
            A_matrix[k][k-p] = bv(saved_values[0])
        display_key()

'''
Invert the A matrix.
'''
def invert_matrix():
    field = ffield.FField(7,gen=0x83)
    matrix = genericmatrix.GenericMatrix(size=(8,8), zeroElement=0, identityElement=1, add=field.Add, mul=field.Multiply, sub=field.Subtract, div=field.Divide)
    matrix.SetRow(0,[get_int_from_BV(i) for i in A_matrix[0]])
    matrix.SetRow(1,[get_int_from_BV(i) for i in A_matrix[1]])
    matrix.SetRow(2,[get_int_from_BV(i) for i in A_matrix[2]])
    matrix.SetRow(3,[get_int_from_BV(i) for i in A_matrix[3]])
    matrix.SetRow(4,[get_int_from_BV(i) for i in A_matrix[4]])
    matrix.SetRow(5,[get_int_from_BV(i) for i in A_matrix[5]])
    matrix.SetRow(6,[get_int_from_BV(i) for i in A_matrix[6]])
    matrix.SetRow(7,[get_int_from_BV(i) for i in A_matrix[7]])
    inverse = matrix.Inverse()
    for rownum in range(8):
        row = [bv(i) for i in inverse.GetRow(rownum)]
        A_Inverse.append(row)

'''
Inverse of the exponentiation part i.e. (E to the power -1).
'''
def invert_exponentiation(vec):
    result = []
    for i in range(8):
        v = vec[i]
        e = E_vector[i]
        inv =  Inverse_list[e]
        result.append(exponentiate(v, inv))
    return result

'''
Inverse of matrix multiplication step.
'''
def invert_A(vec):
    result = []
    for i in range(8):
        sum = bv(0)
        for j in range(8):
            sum = bv_add(sum, bv_multiply(A_Inverse[i][j], vec[j]))
        result.append(sum)
    return result

'''
Decrypt the input string using keys found.
'''
def decrypt(string):
    vec = encode_to_BV(string)
    vec = invert_exponentiation(vec)
    vec = invert_A(vec)
    vec = invert_exponentiation(vec)
    vec = invert_A(vec)
    vec = invert_exponentiation(vec)
    return [get_int_from_BV(i) for i in vec]

'''
Driver Code.
'''
if __name__ == '__main__':
    calc_two_powers()
    initialize()
    break_cipher()
    invert_matrix()
    encrypted_password = "fgffgnkqjfjlgrkolglnkklqirlgjlkh"
    part1 = encrypted_password[:16]
    part2 = encrypted_password[16:]
    password_ascii = decrypt(part1)+decrypt(part2)
    password = ""
    for i in password_ascii:
        password = password + chr(i)
    print(password)

