from BitVector.BitVector import *
import sys
import requests

ALGO_MODULUS    = BitVector(bitstring='10000011')
ALGO_EXPONENT   = 7
two_power_list  = []

'''
Wrapper to create a BitVector
'''
def bv(num):
        return BitVector(intVal = num, size = ALGO_EXPONENT)

'''
Takes a string and returns a list of BitVectors where each
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
        ret_val = bv_num
        power = power % 128
        for i in range(1, power):
                ret_val = ret_val.gf_multiply_modular(bv_num, ALGO_MODULUS, ALGO_EXPONENT)
        return ret_val

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
        return requests.post("https://172.27.26.181:9998/eaeae",json={"plaintext": string,"password":"4d85e2d75ba3d9e1ae200df7357e66c8","teamname":"OrderOfThePhoenix"}, verify=False).json()['ciphertext']

'''
Wrapper to multiply 2 BVs under given modulud
'''
def multiply_wrapper(bv1, bv2):
        return bv1.gf_multiply_modular(bv2, ALGO_MODULUS, ALGO_EXPONENT)

'''
Add Wrapper: Add two bitvectors
'''
def bv_add(bv1, bv2):
        summed_value = get_int_from_BV(bv1) ^ get_int_from_BV(bv2)
        return bv(summed_value)

'''
Main Code Breaking routine.
'''
def break_cipher():
        ciphertext_one   = encode_to_BV(query_server(list_to_str([0]*7 + [1])))
        ciphertext_two   = encode_to_BV(query_server(list_to_str([0]*7 + [2])))
        ciphertext_three = encode_to_BV(query_server(list_to_str([0]*7 + [3])))
        for i in range(128):
            if multiply_wrapper(ciphertext_one[7], two_power_list[i]) == ciphertext_two[7]:
                print("Exponent7:", i)
                e7 = i
                for j in range(128):
                    a_exponent = i*(i+1)
                    if exponentiate(bv(j), a_exponent) == ciphertext_one[7]:
                        a77 = j
                        print("A77:", j)

        ciphertext_one = encode_to_BV(query_server(list_to_str([0]*6 + [1] + [0])))
        ciphertext_two = encode_to_BV(query_server(list_to_str([0]*6 + [2] + [0])))
        for i in range(128):
            if multiply_wrapper(ciphertext_one[6], two_power_list[i]) == ciphertext_two[6]:
                print("Exponent6:", i)
                e6 = i
                for j in range(128):
                    a_exponent = i*(i+1)
                    if exponentiate(bv(j), a_exponent) == ciphertext_one[6]:
                        a66 = j
                        print("A66:", j)

        for i in range(128):
            bv1 = bv(i)
            a66_bv_exp = exponentiate(bv(a66), e6)
            term1 = multiply_wrapper(bv1, a66_bv_exp)
            a76_bv_exp = exponentiate(bv1, e7)
            term2 = multiply_wrapper(bv(a77), a76_bv_exp)
            if exponentiate(bv_add(term1, term2), e7) == ciphertext_one[7]:
                print("A76:", i)

        
        print("**************************** Shivam's Output ******************************************************")

        A = [[0]*8]*8
        #A is the matrix in problem. So A[6][6] if correctly calculated should be equal to a66 defined above by nikhil
        Exponent = [0]*8
        #similarly E[7] here should be equal to e7 defined by nikhil above

        for t in range(2):  # Here i am executing loop just 2 times for debuggging. For full result, it should be range(8)
            col = 7-t
            inp1 = [0]*8
            inp2 = [0]*8
            inp1[col] = 1
            inp2[col] = 2
            ciphertext_one = encode_to_BV(query_server(list_to_str(inp1)))
            ciphertext_two = encode_to_BV(query_server(list_to_str(inp2)))


            for i in range(128):
                if multiply_wrapper(ciphertext_one[col], two_power_list[i]) == ciphertext_two[col]:
                    print("Exponent ", col , " : ", i)
                    Exponent[col] = i
                    for j in range(128):
                        a_exponent = i*(i+1)
                        if exponentiate(bv(j), a_exponent) == ciphertext_one[col]:
                            A[col][col] = j
                            print("A:",col,col," : ", j)

            
            for i in range(col+1,8):
                for val in range(128):
                    bv1 = bv(val)
                    if(col == 6):
                        if(A[col][col] != a66):    #Here A[6][6] is equal to a66 till "A 7 6 : 65" is printed in output on executing, but after 
                                                   # then it's value is getting changed and so error is printed in output,which shouldn't happen
                                                   #That's why "A 7 6 : 82" also is getting staisfied.
                            print("error")
                        if(Exponent[col] != e6):
                            print("error")

                    exp = exponentiate(bv(A[col][col]),Exponent[col])
                    mysum = multiply_wrapper(bv1,exp)                     #First term in the sum
                                                         
                    for j in range(col+1, i):                        
                        exp = exponentiate(bv(A[j][col]),Exponent[j])
                        term = multiply_wrapper(bv(A[i][j]),exp)
                        mysum = bv_add(mysum, term)
                    if(col == 6):
                        if(Exponent[i] != e7):
                            print("error")
                        if(A[i][i] != a77):
                            print("error")
                    exp = exponentiate(bv1,Exponent[i])
                    term = multiply_wrapper(bv(A[i][i]),exp)
                    mysum = bv_add(mysum,term)


                    if exponentiate(mysum,Exponent[i]) == ciphertext_one[i]:
                        A[i][col] = val
                        print("A",i,col,": ",val)


                    







if __name__ == '__main__':
        calc_two_powers()
        break_cipher()



#In case of any doubt, call me !!!
