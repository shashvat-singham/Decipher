import sys
alphabets = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']

#!/usr/bin/python

expand = [32,1,2,3,4,5,
       4,5,6,7,8,9,
       8,9,10,11,12,13,
       12,13,14,15,16,17,
       16,17,18,19,20,21,
       20,21,22,23,24,25,
       24,25,26,27,28,29,
       28,29,30,31,32,1]

pc1 = [57,49,41,33,25,17,9,
       1,58,50,42,34,26,18,
       10,2,59,51,43,35,27,
       19,11,3,60,52,44,36,
       63,55,47,39,31,23,15,
       7,62,54,46,38,30,22,
       14,6,61,53,45,37,29,
       21,13,5,28,20,12,4]

pc2 = [14,17,11,24,1,5,
       3,28,15,6,21,10,
       23,19,12,4,26,8,
       16,7,27,20,13,2,
       41,52,31,37,47,55,
       30,40,51,45,33,48,
       44,49,39,56,34,53,
       46,42,50,36,29,32]

s1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
      [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
      [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
      [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

s2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
      [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
      [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
      [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

s3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
      [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
      [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
      [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

s4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
      [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
      [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
      [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

s5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
      [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
      [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
      [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

s6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
      [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
      [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
      [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

s7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
      [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
      [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
      [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

s8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
      [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
      [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
      [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

perm = [16,7,20,21,
        29,12,28,17,
        1,15,23,26,
        5,18,31,10,
        2,8,24,14,
        32,27,3,9,
        19,13,30,6,
        22,11,4,25]

inv_perm = [
	9, 17, 23, 31,
	13, 28, 2, 18,
	24, 16, 30, 6,
	26, 20, 10, 1,
	8, 14, 25, 3,
	4, 29, 11, 19,
	32, 12, 22, 7,
	5, 27, 15, 21,
]

ip = [58,50,42,34,26,18,10,2,
      60,52,44,36,28,20,12,4,
      62,54,46,38,30,22,14,6,
      64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,
      59,51,43,35,27,19,11,3,
      61,53,45,37,29,21,13,5,
      63,55,47,39,31,23,15,7]

ipinv = [8,40,16,48,24,56,32,64,
         7,39,15,47,23,55,31,63,
         6,38,14,46,22,54,30,62,
         5,37,13,45,21,53,29,61,
         4,36,12,44,20,52,28,60,
         3,35,11,43,19,51,27,59,
         2,34,10,42,18,50,26,58,
         1,33,9,41,17,49,25,57]

ip_inverse = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

ipinv_inverse = [57,49,41,33,25,17,9,1,
                59,51,43,35,27,19,11,3,
                61,53,45,37,29,21,13,5,
                63,55,47,39,31,23,15,7,
                58,50,42,34,26,18,10,2,
                60,52,44,36,28,20,12,4,
                62,54,46,38,30,22,14,6,
                64,56,48,40,32,24,16,8]

sBoxes = [s1, s2, s3, s4, s5, s6, s7, s8]
shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
'''
Encodes input string to the format used
'''
def encodestring(str):
    encoding = 0
    count = 0
    rev = ""
    for i in str:
        rev = i + rev
    for i in rev:
        mapping = (ord(i) - ord('f')) % 16
        encoding = encoding + ((mapping & 0xf) << (4*count))
        count = count + 1
    return encoding

'''
Return string from encoding.
'''
def get_str_encoding(number):
    str = ""
    num = number
    for i in range(16):
        ch = chr(ord('f') + (num & 0xf))
        str = ch + str
        num = num >> 4
    return str

'''
Returns S-Box mapping
'''
def sbox_map(sbox, inp):
    row_number = ((inp &0b100000) >> 4) + (inp & 1)
    column_number = (inp & 0b11110) >> 1
    return sbox[row_number][column_number]

'''
Returns the differential table for the S-Box.
Output is a dictionary of the form:
(input_xor, output_xor) -> List of all possible pairs i.e.
List of 2 element tuple
'''
def Sbox_differential(sbox):
    differential = dict()

    for i in range(64):
        for j in range(16):
            differential[(i,j)] = []

    for input1 in range(64):
        output1 = sbox_map(sbox, input1)
        for input2 in range(64):
            output2 = sbox_map(sbox, input2)
            input_xor = input1 ^ input2
            output_xor = output1 ^ output2
            differential[(input_xor, output_xor)].append((input1, input2))
    return differential

'''
Function to visualize differential table
'''
def preety_print_differential(differential):
    print("%11x %5x %5x %5x %5x %5x %5x %5x %5x %5x %5x %5x %5x %5x %5x %5x" % (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
    for i in range(64):
        print("%5x %5d %5d %5d %5d %5d %5d %5d %5d %5d %5d %5d %5d %5d %5d %5d %5d" % (i, len(differential[(i,0)]), len(differential[(i,1)]), len(differential[(i,2)]), len(differential[(i,3)]), len(differential[(i,4)]), len(differential[(i,5)]), len(differential[(i,6)]), len(differential[(i,7)]), len(differential[(i,8)]), len(differential[(i,9)]), len(differential[(i,10)]), len(differential[(i,11)]), len(differential[(i,12)]), len(differential[(i,13)]), len(differential[(i,14)]), len(differential[(i,15)])))

'''
Returns bits of number in a list
output[0] is MSB. For 64-bit numbers
'''
def get_bit_list(number):
    output = [0]*64
    for i in range(64):
        output[i] = (number & (1 << (63-i))) >> (63-i)
    return output

'''
Returns bits of number in a list
output[0] is MSB. For 6-bit numbers
'''
def get_bit_list_6(number):
    output = [0]*6
    for i in range(6):
        output[i] = (number & (1 << (5-i))) >> (5-i)
    return output

'''
Convert a list of bits to number.
bit_list[0] is MSB
'''
def bit_list_to_number(bit_list):
    number = 0
    for i in range(len(bit_list)):
        number = number + (bit_list[i] << (len(bit_list)-1-i))
    return number

'''
Key Schedule: sw1=0 for encryption
'''
def expand_key(sw1, key, r):
    key_bits = get_bit_list(key)
    CD = [0]*56
    key_schedule = []
    for i in range(16):
        key_schedule.append([0]*48)
    for i in range(56):
        CD[i] = key_bits[pc1[i] - 1]
    for i in range(r):
        for j in range(shifts[i]):
            t1 = CD[0]
            t2 = CD[28]
            for k in range(27):
                CD[k] = CD[k+1]
                CD[k+28] = CD[k+29]
            CD[27] = t1
            CD[55] = t2
        j = i if sw1 == 0 else (r-i-1)
        for k in range(48):
            key_schedule[j][k] = CD[pc2[k] - 1]
    return key_schedule

def expand_key2(sw1, key_bits, r):
    CD = [0]*56
    key_schedule = []
    for i in range(16):
        key_schedule.append([0]*48)
    for i in range(56):
        CD[i] = key_bits[pc1[i] - 1]
    for i in range(r):
        for j in range(shifts[i]):
            t1 = CD[0]
            t2 = CD[28]
            for k in range(27):
                CD[k] = CD[k+1]
                CD[k+28] = CD[k+29]
            CD[27] = t1
            CD[55] = t2
        j = i if sw1 == 0 else (r-i-1)
        for k in range(48):
            key_schedule[j][k] = CD[pc2[k] - 1]
    return key_schedule

'''
DES Expansion
'''
def expansion(l):
    return [l[x-1] for x in expand]

'''
Apply permutation.
'''
def apply_permutation(block, p):
    return [block[x-1] for x in p]

'''
Reverse permutation
'''
def reverse_permutation(block, p):
    input_block = [0]*len(block)
    for i in range(len(p)): #p[i] means i'th bit of output is p[i]'th bit of input
        input_block[p[i]-1] = block[i]
    return input_block

'''
Compute xor
'''
def compute_xor(l1, l2):
    return [x^y for x,y in zip(l1,l2)]

'''
Compute Binary string
'''
def bin_string(val, bitsize): #Return the binary value as a string of the given size
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

'''
Apply S-Boxes
'''
def apply_sboxes(l):
    subblocks = []
    for i in range(0,48,6):
        subblocks.append(l[i:i+6])
    result = []
    for i in range(len(subblocks)): #For all the sublists
        block = subblocks[i]
        row = int(str(block[0])+str(block[5]),2)#Get the row with the first and last bit
        column = int(''.join([str(x) for x in block[1:][:-1]]),2) #Column is the 2,3,4,5th bits
        val = sBoxes[i][row][column] #Take the value in the SBOX appropriated for the round (i)
        bin = bin_string(val, 4)#Convert the value to binary
        result += [int(x) for x in bin]#And append it to the resulting list
    return result

'''
Compute DES for rounds number of rounds
'''
def des(input_num, key_schedule, rounds, flag="ENCRYPT"):
    input_bit_list = get_bit_list(input_num)
    LR = [0]*64
    preS = [0]*48
    f = [0]*32
    final_output = [0]*64
    input_bit_list = apply_permutation(input_bit_list, ip)
    left_half, right_half = input_bit_list[:32], input_bit_list[32:] #right_half is LSBs
    tmp = None
    for i in range(rounds):
        right_expand = expansion(right_half)
        if flag == "ENCRYPT":
            tmp = compute_xor(right_expand, key_schedule[i])
        else:
            tmp = compute_xor(right_expand, key_schedule[rounds-i-1])
        tmp = apply_sboxes(tmp)
        tmp = apply_permutation(tmp, perm)
        tmp = compute_xor(tmp, left_half)
        left_half = right_half
        right_half = tmp
    return bit_list_to_number(apply_permutation(left_half + right_half, ipinv))

def des_decrypt(output_num, key_schedule, rounds):
    output_bit_list = get_bit_list(output_num)
    LR = [0]*64
    preS = [0]*48
    f = [0]*32
    final_output = [0]*64
    output_bit_list = apply_permutation(output_bit_list, ipinv_inverse)
    left_half, right_half = output_bit_list[:32], output_bit_list[32:] #right_half is LSBs
    tmp = None
    for i in range(rounds):
        right_expand = expansion(left_half)
        tmp = compute_xor(right_expand, key_schedule[rounds-i-1])
        tmp = apply_sboxes(tmp)
        tmp = apply_permutation(tmp, perm)
        tmp = compute_xor(tmp, right_half)
        right_half = left_half
        left_half = tmp
    return bit_list_to_number(apply_permutation(left_half + right_half, ip_inverse))
'''
Right means least significant 32 bits or LR[32:]
'''

def get_one_input(index):
    right_half    = [0]*32
    left_half1    = [0]*32
    left_half2    = [0]*32
    left_half2[index] = 1
    first_input   = left_half1 + right_half
    second_input  = left_half2 + right_half
    return [reverse_permutation(first_input, ip), reverse_permutation(second_input, ip)]

def get_one_input_2(index1, index2):
    right_half    = [0]*32
    left_half1    = [0]*32
    left_half2    = [0]*32
    left_half1[index1] = 1
    left_half2[index2] = 1
    first_input   = left_half1 + right_half
    second_input  = left_half2 + right_half
    return [reverse_permutation(first_input, ip), reverse_permutation(second_input, ip)]

def get_one_input_3(index1):
    right_half    = [0]*32
    left_half1    = [1]*32
    left_half2    = [0]*32
    left_half2[index1] = 1
    first_input   = left_half1 + right_half
    second_input  = left_half2 + right_half
    return [reverse_permutation(first_input, ip), reverse_permutation(second_input, ip)]

def break_cipher(chosen_pairs):
    differentials = list()
    differentials.append(Sbox_differential(s1))
    differentials.append(Sbox_differential(s2))
    differentials.append(Sbox_differential(s3))
    differentials.append(Sbox_differential(s4))
    differentials.append(Sbox_differential(s5))
    differentials.append(Sbox_differential(s6))
    differentials.append(Sbox_differential(s7))
    differentials.append(Sbox_differential(s8))
    key_part = list()
    key_part.append(set([i for i in range(64)]))
    key_part.append(set([i for i in range(64)]))
    key_part.append(set([i for i in range(64)]))
    key_part.append(set([i for i in range(64)]))
    key_part.append(set([i for i in range(64)]))
    key_part.append(set([i for i in range(64)]))
    key_part.append(set([i for i in range(64)]))
    key_part.append(set([i for i in range(64)]))
    counter = 0
    for pair in chosen_pairs:
        counter = counter + 1
        input1 = pair[0][0]
        input2 = pair[0][1]
        output1 = pair[1][0]
        output2 = pair[1][1]
        L0_1, R0_1 = apply_permutation(input1, ip)[:32], apply_permutation(input1, ip)[32:]
        L0_2, R0_2 = apply_permutation(input2, ip)[:32], apply_permutation(input2, ip)[32:]
        R2_1, R3_1 = reverse_permutation(output1, ipinv)[:32], reverse_permutation(output1, ipinv)[32:]
        R2_2, R3_2 = reverse_permutation(output2, ipinv)[:32], reverse_permutation(output2, ipinv)[32:]
        R2_1_expand = expansion(R2_1)
        R2_2_expand = expansion(R2_2)
        input_xor = compute_xor(R2_1_expand, R2_2_expand)

        output_xor = reverse_permutation(compute_xor(compute_xor(R3_1, L0_1), compute_xor(R3_2, L0_2)), perm)
        possibilities = 1
        for i in range(8):
            input_xor_bit = input_xor[6*i:6*(i+1)]
            output_xor_bit = output_xor[4*i:4*(i+1)]
            possible_inputs = differentials[i][(bit_list_to_number(input_xor_bit), bit_list_to_number(output_xor_bit))]
            possible_keys = set()
            for one_possibility in possible_inputs:
                possible_keys.add(one_possibility[0] ^ bit_list_to_number(R2_1_expand[6*i:6*(i+1)]))
            key_part[i] = key_part[i].intersection(possible_keys)
            possibilities = possibilities * len(key_part[i])
        print("#Key possibilities after %2d pairs : %d" % (counter, possibilities))
    third_key = []
    for i in range(8):
        third_key = third_key + get_bit_list_6(list(key_part[i])[0])
    keymap = [i for i in range(64)]
    temp  = expand_key2(0, keymap, 3)
    master_key = [-1]*64
    for i in range(48):
        master_key[temp[2][i]] = third_key[i]
    key_schedule = expand_key2(0,master_key,3)

    unknown = set()
    for i in range(48):
        if(key_schedule[1][i] == -1):
            unknown.add(temp[1][i])
        if(key_schedule[0][i] == -1):
            unknown.add(temp[0][i])
    final_master_key = [0]*64
    for t1 in range(2):
        for t2 in range(2):
            for t3 in range(2):
                for t4 in range(2):
                    for t5 in range(2):
                        for t6 in range(2):
                            for t7 in range(2):
                                for t8 in range(2):
                                    master_key[18] = t1;
                                    master_key[21] = t2;
                                    master_key[25] = t3;
                                    master_key[44] = t4;
                                    master_key[45] = t5;
                                    master_key[51] = t6;
                                    master_key[54] = t7;
                                    master_key[56] = t8;
                                    temp_key_schedule = expand_key2(0,master_key,3)
                                    test = 1
                                    for pair in chosen_pairs:
                                        input1 = pair[0][0]
                                        output1 = pair[1][0]
                                        if(des(bit_list_to_number(input1),temp_key_schedule,3) != bit_list_to_number(output1)):
                                            test = 0
                                            break
                                    if(test == 1):
                                        final_master_key = master_key.copy()
    return final_master_key




if __name__ == "__main__":
    s1_differential = Sbox_differential(s1)
    s2_differential = Sbox_differential(s2)
    s3_differential = Sbox_differential(s3)
    s4_differential = Sbox_differential(s4)
    s5_differential = Sbox_differential(s5)
    s6_differential = Sbox_differential(s6)
    s7_differential = Sbox_differential(s7)
    s8_differential = Sbox_differential(s8)

    chosen_pairs = []
    inpair_1 = get_one_input(0)
    out_pair1 = [get_bit_list(encodestring("qqffonmtfhoptjio")), get_bit_list(encodestring("ppmhrshtghsougkf"))]
    chosen_pairs.append([inpair_1, out_pair1])

    inpair_2 = get_one_input(1)
    out_pair2 = [get_bit_list(encodestring("qqffonmtfhoptjio")), get_bit_list(encodestring("qqfnnnmtjlrpqjif"))]
    chosen_pairs.append([inpair_2, out_pair2])

    inpair_3 = get_one_input(2)
    out_pair3 = [get_bit_list(encodestring("qqffonmtfhoptjio")), get_bit_list(encodestring("pqgpsohtjhrqtfgo"))]
    chosen_pairs.append([inpair_3, out_pair3])

    inpair_4 = get_one_input(3)
    out_pair4 = [get_bit_list(encodestring("qqffonmtfhoptjio")), get_bit_list(encodestring("upkpnnmpgfnqtrio"))]
    chosen_pairs.append([inpair_4, out_pair4])

    inpair_5 = get_one_input(4)
    out_pair5 = [get_bit_list(encodestring("qqffonmtfhoptjio")), get_bit_list(encodestring("uqguonmtjlnqmrij"))]
    chosen_pairs.append([inpair_5, out_pair5])

    inpair_6 = get_one_input(5)
    out_pair6 = [get_bit_list(encodestring("qqffonmtfhoptjio")), get_bit_list(encodestring("pqfkooktfhopmkis"))]
    chosen_pairs.append([inpair_6, out_pair6])

    inpair_7 = get_one_input(6)
    out_pair7 = [get_bit_list(encodestring("qqffonmtfhoptjio")), get_bit_list(encodestring("tpgkrogpgfopmsis"))]
    chosen_pairs.append([inpair_7, out_pair7])

    inpair_8 = get_one_input(7)
    out_pair8 = [get_bit_list(encodestring("qqffonmtfhoptjio")), get_bit_list(encodestring("shgkfrhqjkrphkms"))]
    chosen_pairs.append([inpair_8, out_pair8])

    inpair_9 = get_one_input_2(16,31)
    out_pair9 = [get_bit_list(encodestring("lukjnrltfqfqtjqp")), get_bit_list(encodestring("qqlnnrmtkhrnukif"))]
    chosen_pairs.append([inpair_9, out_pair9])

    inpair_10 = get_one_input_2(17,30)
    out_pair10 = [get_bit_list(encodestring("hujforlujiottfiq")), get_bit_list(encodestring("qplforutglonpghs"))]
    chosen_pairs.append([inpair_10, out_pair10])

    inpair_11 = get_one_input_2(19,29)
    out_pair11 = [get_bit_list(encodestring("pqjgqsluriqttjmu")), get_bit_list(encodestring("uqfgnoulfhrtpfhr"))]
    chosen_pairs.append([inpair_11, out_pair11])

    inpair_12 = get_one_input_2(20,28)
    out_pair12 = [get_bit_list(encodestring("tpggpohsrmumtjmt")), get_bit_list(encodestring("tptgrrtmiirruglr"))]
    chosen_pairs.append([inpair_12, out_pair12])

    inpair_13 = get_one_input_3(25)
    out_pair13 = [get_bit_list(encodestring("qisilfnfinnjfhps")), get_bit_list(encodestring("pqffsfmuhlnttjmo"))]
    chosen_pairs.append([inpair_13, out_pair13])


    final_master_key = break_cipher(chosen_pairs)
    print("The correct keys are:")
    print("Master Key : " + str(final_master_key))
    print("First key  : " + str(expand_key2(0,final_master_key,3)[0]))
    print("Second key : " + str(expand_key2(0,final_master_key,3)[1]))
    print("Thrd key   : " + str(expand_key2(0,final_master_key,3)[2]))
    print("The decrypted passoword is: ")
    print(get_str_encoding(des_decrypt(encodestring("krgoksgrjgmmmlnq"),expand_key2(0,final_master_key,3),3)))
    print(get_str_encoding(des_decrypt(encodestring("tngkotsjhnsmonkg"),expand_key2(0,final_master_key,3),3)))
     
