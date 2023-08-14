def readPattern(line):
    pattern = []
    for char in line:
        if(char == '1' or char == '0'):
            pattern.append(char)
    patternString = ''.join(map(str,pattern))
    return patternString

patternsAll = ["" for x in range(130)]

with  open('patterns.txt') as readPatterns:
    lines = readPatterns.readlines()

for line in range(130):
    patternsAll[line] = readPattern(lines[line])

#print(patternsAll)

def find_Input_Bit_Pos(pat1, pat3):
    index = 0
    for value1, value2 in zip(pat1, pat3):
        
        if(value1 != value2):
            return index
        index = index + 1            
    return 0

def find_L_or_R_Bit_Pos(pat2, pat4):
    index = []
    counter = 0
    for value1, value2 in zip(pat2, pat4):
        
        if(value1 != value2):
            index.append(counter)
        counter = counter + 1 
    return index

InputPosBit = []
for arr in range(2,130,2):
    InputPosBit.append(find_Input_Bit_Pos(patternsAll[0], patternsAll[arr]))

#print("Bits position in the scan chain for input register")
#print(InputPosBit)

L_or_R_Bit_Pos_temp = []
for arr in range(3,130,2):
    L_or_R_Bit_Pos_temp.append(find_L_or_R_Bit_Pos(patternsAll[1], patternsAll[arr]))

L_or_R_Bit_Pos = []
for value1, value2 in zip(InputPosBit, L_or_R_Bit_Pos_temp):
    for toRemove in value2:
        if (toRemove != value1):
            L_or_R_Bit_Pos.append(toRemove)

L_Reg_Bit_Pos = [] 
R_Reg_Bit_Pos = []
for pos in range(1,64,2):
    L_Reg_Bit_Pos.append(L_or_R_Bit_Pos[pos])

for pos in range(0,64,2):
    R_Reg_Bit_Pos.append(L_or_R_Bit_Pos[pos])

#print("L register bit position in the scan chain ") 
#print(L_Reg_Bit_Pos)
#print("R register bit position in the scan chain") 
#print(R_Reg_Bit_Pos)

def permute(A, P, n):
    # For each element of P
    for i in range(n):
        next = i
        # Check if it is already
        # considered in cycle
        while (P[next] >= 0):
            # Swap the current element according
            # to the permutation in P
            t = A[i]
            A[i] = A[P[next]]
            A[P[next]] = t
             
            temp = P[next]
            # Subtract n from an entry in P
            # to make it negative which indicates
            # the corresponding move
            # has been performed
            P[next] -= n
            next = temp

table_L = [
    7, 15, 23, 31, 6, 14, 22, 30,
    5, 13, 21, 29, 4, 12, 20, 28,
    3, 11, 19, 27, 2, 10, 18, 26,
    1, 9,  17, 25, 0, 8,  16, 24
]
table_R = [
    7, 15, 23, 31, 6, 14, 22, 30,
    5, 13, 21, 29, 4, 12, 20, 28,
    3, 11, 19, 27, 2, 10, 18, 26,
    1, 9,  17, 25, 0, 8,  16, 24
]

permute(L_Reg_Bit_Pos,table_L,32)
permute(R_Reg_Bit_Pos,table_R,32)

#print("Final positions of bits in scan chain for L and R registers")
#print(L_Reg_Bit_Pos)
#print(R_Reg_Bit_Pos)

with  open('3_inputs.txt') as readPatterns:
    lines = readPatterns.readlines()

bitStreamInput1_0 = readPattern(lines[0])
bitStreamInput1_1 = readPattern(lines[1])
bitStreamInput1_2 = readPattern(lines[2])
bitStreamInput1_3 = readPattern(lines[3])
bitStreamInput1_4 = readPattern(lines[4])

bitStreamInput2_0 = readPattern(lines[5])
bitStreamInput2_1 = readPattern(lines[6])
bitStreamInput2_2 = readPattern(lines[7])
bitStreamInput2_3 = readPattern(lines[8])
bitStreamInput2_4 = readPattern(lines[9])

bitStreamInput3_0 = readPattern(lines[10])
bitStreamInput3_1 = readPattern(lines[11])
bitStreamInput3_2 = readPattern(lines[12])
bitStreamInput3_3 = readPattern(lines[13])
bitStreamInput3_4 = readPattern(lines[14])
#print(bitStreamInput1)
#print(bitStreamInput2)
#print(bitStreamInput3)

def Input_L_and_R_registers(bitStream):
    input_reg = []
    L_reg = []
    R_reg = []
    for i in InputPosBit:
        input_reg.append(bitStream[i])
    for i in L_Reg_Bit_Pos:
        L_reg.append(bitStream[i])
    for i in R_Reg_Bit_Pos:
        R_reg.append(bitStream[i])

    ret_Input11_reg = hex(int(''.join(map(str,input_reg)),2)).replace('0x','')
    ret_L_reg = hex(int(''.join(map(str,L_reg)),2)).replace('0x','')
    ret_R_reg = hex(int(''.join(map(str,R_reg)),2)).replace('0x','')

    return ret_Input11_reg.zfill(16), ret_L_reg.zfill(8), ret_R_reg.zfill(8)

# Input #1
InputReg_0_1, L_reg_0_1, R_reg_0_1 = Input_L_and_R_registers(bitStreamInput1_1)
InputReg_1_1, L_reg_1_1, R_reg_1_1 = Input_L_and_R_registers(bitStreamInput1_2)
InputReg_2_1, L_reg_2_1, R_reg_2_1 = Input_L_and_R_registers(bitStreamInput1_3)
InputReg_3_1, L_reg_3_1, R_reg_3_1 = Input_L_and_R_registers(bitStreamInput1_4)
# Input #2
InputReg_0_2, L_reg_0_2, R_reg_0_2 = Input_L_and_R_registers(bitStreamInput2_1)
InputReg_1_2, L_reg_1_2, R_reg_1_2 = Input_L_and_R_registers(bitStreamInput2_2)
InputReg_2_2, L_reg_2_2, R_reg_2_2 = Input_L_and_R_registers(bitStreamInput2_3)
InputReg_3_2, L_reg_3_2, R_reg_3_2 = Input_L_and_R_registers(bitStreamInput2_4)
# Input #3
InputReg_0_3, L_reg_0_3, R_reg_0_3 = Input_L_and_R_registers(bitStreamInput3_1)
InputReg_1_3, L_reg_1_3, R_reg_1_3 = Input_L_and_R_registers(bitStreamInput3_2)
InputReg_2_3, L_reg_2_3, R_reg_2_3 = Input_L_and_R_registers(bitStreamInput3_3)
InputReg_3_3, L_reg_3_3, R_reg_3_3 = Input_L_and_R_registers(bitStreamInput3_4)

#print(InputReg_0_1)
#print("L0 and R0 input 1")
#print(L_reg_0_1)
#print(R_reg_0_1)
#print("L1 and R1")
#print(L_reg_1_1)
#print(R_reg_1_1)
#print("L0 and R0 input 2")
#print(L_reg_0_2)
#print(R_reg_0_2)   
#print("L1 and R1")
#print(L_reg_1_2)
#print(R_reg_1_2)
#print("L0 and R0 input 3")
#print(L_reg_0_3)
#print(R_reg_0_3)
#print("L1 and R1")
#print(L_reg_1_3)
#print(R_reg_1_3)

def hexToBin(hexadecimal, length):
    binary_Str = bin(int(hexadecimal, 16))[2:].zfill(length)
  
    return binary_Str

#print(hexToBin("AABB09182736CCDD",64))
#print(hexToBin("194CD072DE8C",48))  
#print(hexToBin("1CD9",32))

def permutation(toPermute, table , inputSize, verbose=False):
    res = 0
    for i in range(len(table)):
        mask = 1 << (inputSize - table[i])  # The only bit that should be one is the one that will get permuted at this round
        if verbose is True:
            print(bin(mask))
        bitPermuted = bool(toPermute & mask) << (len(table) - i - 1) # then we shift that bit ((bool)toPermute & mask)
                                                                     # at it's post permutation position
        res |= bitPermuted # remember that 0 | 1 = 1, 001 | 100 = 101, etc
    return res

E = [
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

def expansion(inputMessage):
    return permutation(inputMessage, E, 32)


a1 = hex(expansion(int(hexToBin(R_reg_0_1,32),2)))
a2 = hex(expansion(int(hexToBin(R_reg_0_2,32),2)))
a3 = hex(expansion(int(hexToBin(R_reg_0_3,32),2)))
#print("a1, a2, a3 for 1st round (input 1,2,3)")
#print(a1)
#print(a2)   
#print(a3)
a11 = hex(expansion(int(hexToBin(R_reg_1_1,32),2)))
a22 = hex(expansion(int(hexToBin(R_reg_1_2,32),2)))
a33 = hex(expansion(int(hexToBin(R_reg_1_3,32),2)))
#print("a1, a2, a3 for 2nd round (input 1,2,3)")
#print(a11)
#print(a22)
#print(a33)
a111 = hex(expansion(int(hexToBin(R_reg_2_1,32),2)))
a222 = hex(expansion(int(hexToBin(R_reg_2_2,32),2)))
a333 = hex(expansion(int(hexToBin(R_reg_2_3,32),2)))
#print("a1, a2, a3 for 3rd round (input 1,2,3)")
#print(a11)
#print(a22)   
#print(a33)  

def split_A(a):
    A_bin = hexToBin(a, 48)
    A_array = []
    for i in range(8):
        A_array.append(A_bin[0+6*i:6+6*i])
    
    return A_array

a1_splitted = split_A(a1)
a2_splitted = split_A(a2)
a3_splitted = split_A(a3)
#print("Splitted a1, a2, a3 for 3 different inputs (round 1")
#print(a1_splitted)
#print(a2_splitted)
#print(a3_splitted)
a11_splitted = split_A(a11)
a22_splitted = split_A(a22)
a33_splitted = split_A(a33)
#print("Splitted a1, a2, a3 for 3 different inputs (round 2")
#print(a11_splitted)
#print(a22_splitted)
#print(a33_splitted)
a111_splitted = split_A(a111)
a222_splitted = split_A(a222)
a333_splitted = split_A(a333)
#print("Splitted a1, a2, a3 for 3 different inputs (round 3")
#print(a111_splitted)
#print(a222_splitted)
#print(a333_splitted)

# From equation (2), d is known: d = L0 ^ R1
def D_L0_xor_R1(L0,R1):
    return hex(int(L0,16) ^ int(R1,16)).replace('0x','').zfill(8)

def D_is_R(R):
    return hex(int(R,16)).replace('0x','').zfill(8)

d1 = D_L0_xor_R1(L_reg_0_1,R_reg_1_1)
d2 = D_L0_xor_R1(L_reg_0_2,R_reg_1_2)
d3 = D_L0_xor_R1(L_reg_0_3,R_reg_1_3)
#print(d1)
#print(d2)
#print(d3)
d11 = D_L0_xor_R1(L_reg_1_1,R_reg_2_1)
d22 = D_L0_xor_R1(L_reg_1_2,R_reg_2_2)
d33 = D_L0_xor_R1(L_reg_1_3,R_reg_2_3)
#print(d11)
#print(d22)
#print(d33)
d111 = D_L0_xor_R1(L_reg_2_1,R_reg_3_1)
d222 = D_L0_xor_R1(L_reg_2_2,R_reg_3_2)
d333 = D_L0_xor_R1(L_reg_2_3,R_reg_3_3)
#print(d111)
#print(d222)
#print(d333)

# From equation (3), c is known: c = inverse_permutation(d)
def C_inverse_permutation_D(d):
    d_bin = hexToBin(d,32)
    c = (d_bin[8]+""+d_bin[16]+""+d_bin[22]+""+d_bin[30]+""+d_bin[12]+""+d_bin[27]+""+d_bin[1]+""+d_bin[17]+""+
         d_bin[23]+""+d_bin[15]+""+d_bin[29]+""+d_bin[5]+""+d_bin[25]+""+d_bin[19]+""+d_bin[9]+""+d_bin[0]+""+
         d_bin[7]+""+d_bin[13]+""+d_bin[24]+""+d_bin[2]+""+d_bin[3]+""+d_bin[28]+""+d_bin[10]+""+d_bin[18]+""+
         d_bin[31]+""+d_bin[11]+""+d_bin[21]+""+d_bin[6]+""+d_bin[4]+""+d_bin[26]+""+d_bin[14]+""+d_bin[20])
    return hex(int(c,2)).replace('0x','').zfill(8)

c1 = C_inverse_permutation_D(d1)
c2 = C_inverse_permutation_D(d2)
c3 = C_inverse_permutation_D(d3)
#print("c1, c2, c3 inverse permutation 1st round (input 1,2,3)")
#print(c1)
#print(c2)
#print(c3)
c11 = C_inverse_permutation_D(d11)
c22 = C_inverse_permutation_D(d22)
c33 = C_inverse_permutation_D(d33)
#print("c1, c2, c3 inverse permutation 2nd round (input 1,2,3)")
#print(c11)
#print(c22)
#print(c33)
c111 = C_inverse_permutation_D(d111)
c222 = C_inverse_permutation_D(d222)
c333 = C_inverse_permutation_D(d333)
#print("c1, c2, c3 inverse permutation 3rd round (input 1,2,3)")
#print(c111)
#print(c222)
#print(c333)

def split_C_for_Sbox_inv(C):    
    C_bin = hexToBin(C, 32)
    C_array = []
    for i in range(8):
        C_array.append(C_bin[0+4*i:4+4*i])
    
    return C_array

array_c1 = split_C_for_Sbox_inv(c1)
array_c2 = split_C_for_Sbox_inv(c2)
array_c3 = split_C_for_Sbox_inv(c3)
#print("Splitted c1, c2, c3 round 1 (input 1,2,3)")
#print("C1 split: ", array_c1)
#print("C2 split: ", array_c2)
#print("C3 split: ", array_c3)

array_c11 = split_C_for_Sbox_inv(c11)
array_c22 = split_C_for_Sbox_inv(c22)
array_c33 = split_C_for_Sbox_inv(c33)
#print("Splitted c1, c2, c3 round 2 (input 1,2,3)")
#print("C1 split: ", array_c11)
#print("C2 split: ", array_c22)
#print("C3 split: ", array_c33)

array_c111 = split_C_for_Sbox_inv(c111)
array_c222 = split_C_for_Sbox_inv(c222)
array_c333 = split_C_for_Sbox_inv(c333)
#print("Splitted c1, c2, c3 round 3 (input 1,2,3)")
#print("C1 split: ", array_c111)
#print("C2 split: ", array_c222)
#print("C3 split: ", array_c333)

Sbox = [    
    [
        [14, 4,  13, 1,  2,  15, 11, 8,  3,  10, 6,  12, 5,  9,  0,  7],
        [0,  15, 7,  4,  14, 2,  13, 1,  10, 6,  12, 11, 9,  5,  3,  8],
        [4,  1,  14, 8,  13, 6,  2,  11, 15, 12, 9,  7,  3,  10, 5,  0],
        [15, 12, 8,  2,  4,  9,  1,  7,  5,  11, 3,  14, 10, 0,  6,  13]
    ],
    [
        [15, 1,  8,  14, 6,  11, 3,  4,  9,  7,  2,  13, 12, 0,  5,  10],
        [3,  13, 4,  7,  15, 2,  8,  14, 12, 0,  1,  10, 6,  9,  11, 5],
        [0,  14, 7,  11, 10, 4,  13, 1,  5,  8,  12, 6,  9,  3,  2,  15],
        [13, 8,  10, 1,  3,  15, 4,  2,  11, 6,  7,  12, 0,  5,  14, 9]
    ],
    [
        [10, 0,  9,  14, 6,  3,  15, 5,  1,  13, 12, 7,  11, 4,  2,  8],
        [13, 7,  0,  9,  3,  4,  6,  10, 2,  8,  5,  14, 12, 11, 15, 1],
        [13, 6,  4,  9,  8,  15, 3,  0,  11, 1,  2,  12, 5,  10, 14, 7],
        [1,  10, 13, 0,  6,  9,  8,  7,  4,  15, 14, 3,  11, 5,  2,  12]
    ],
    [
        [7,  13, 14, 3,  0,  6,  9,  10, 1,  2,  8,  5,  11, 12, 4,  15],   
        [13, 8,  11, 5,  6,  15, 0,  3,  4,  7,  2,  12, 1,  10, 14, 9],
        [10, 6,  9,  0,  12, 11, 7,  13, 15, 1,  3,  14, 5,  2,  8,  4],
        [3,  15, 0,  6,  10, 1,  13, 8,  9,  4,  5,  11, 12, 7,  2,  14]
    ],
    [
        [2,  12, 4,  1,  7,  10, 11, 6,  8,  5,  3,  15, 13, 0,  14, 9],
        [14, 11, 2,  12, 4,  7,  13, 1,  5,  0,  15, 10, 3,  9,  8,  6],
        [4,  2,  1,  11, 10, 13, 7,  8,  15, 9,  12, 5,  6,  3,  0,  14],
        [11, 8,  12, 7,  1,  14, 2,  13, 6,  15, 0,  9,  10, 4,  5,  3]
    ],
    [
        [12, 1,  10, 15, 9,  2,  6,  8,  0,  13, 3,  4,  14, 7,  5,  11],
        [10, 15, 4,  2,  7,  12, 9,  5,  6,  1,  13, 14, 0,  11, 3,  8],
        [9,  14, 15, 5,  2,  8,  12, 3,  7,  0,  4,  10, 1,  13, 11, 6],
        [4,  3,  2,  12, 9,  5,  15, 10, 11, 14, 1,  7,  6,  0,  8,  13]
    ],
    [
        [4,  11, 2,  14, 15, 0,  8,  13, 3,  12, 9,  7,  5,  10, 6,  1],
        [13, 0,  11, 7,  4,  9,  1,  10, 14, 3,  5,  12, 2,  15, 8,  6],
        [1,  4,  11, 13, 12, 3,  7,  14, 10, 15, 6,  8,  0,  5,  9,  2],
        [6,  11, 13, 8,  1,  4,  10, 7,  9,  5,  0,  15, 14, 2,  3,  12]
    ],
    [
        [13, 2,  8,  4,  6,  15, 11, 1,  10, 9,  3,  14, 5,  0,  12, 7],
        [1,  15, 13, 8,  10, 3,  7,  4,  12, 5,  6,  11, 0,  14, 9,  2],
        [7,  11, 4,  1,  9,  12, 14, 2,  0,  6,  10, 13, 15, 3,  5,  8],
        [2,  1,  14, 7,  4,  10, 8,  13, 15, 12, 9,  0,  3,  5,  6,  11]
    ]
]

#print(Sbox[0][0])   

def find_B(c,s_box):
    c_int = int(c,2)
    counter_row = 0
    row = []
    column = []
    for i in Sbox[s_box]:
        for j in i:
            if(j == c_int):
                row.append(counter_row)
                column.append(i.index(c_int))
        counter_row += 1
    
    possible_B = []
    for i, j in zip(row, column):
        i = bin(i).replace("0b","").zfill(2)
        j = bin(j).replace("0b","").zfill(4)
        possible_B.append(i[0]+""+j+""+i[1])
        
    return possible_B

def find_possible_comb_B_for_one_input(array_C):
    possible = []
    possible_arr = []
    for i in range(8):
        possible = find_B(array_C[i],i)
        possible_arr.append(possible)
    return possible_arr


my_array1 = find_possible_comb_B_for_one_input(array_c1)
my_array2 = find_possible_comb_B_for_one_input(array_c11)
my_array3 = find_possible_comb_B_for_one_input(array_c111)
#print(my_array1)

def what_bits_need_to_flip(a1, a2, a3):
    
    arr1 = []
    arr2 = []
    counter = 0
    for i, j in zip(a1,a2):
        
        if(i != j):
            arr1.append(counter)
        counter += 1
    counter = 0
    for i, j in zip(a1,a3):
        
        if(i != j):
            arr2.append(counter)
        counter += 1
 
    return arr1,arr2

bits_to_flip_1_1, bits_to_flip_1_2 = what_bits_need_to_flip(a1_splitted[0],a2_splitted[0],a3_splitted[0])
bits_to_flip_2_1, bits_to_flip_2_2 = what_bits_need_to_flip(a1_splitted[1],a2_splitted[1],a3_splitted[1])
bits_to_flip_3_1, bits_to_flip_3_2 = what_bits_need_to_flip(a1_splitted[2],a2_splitted[2],a3_splitted[2])
bits_to_flip_4_1, bits_to_flip_4_2 = what_bits_need_to_flip(a1_splitted[3],a2_splitted[3],a3_splitted[3])
bits_to_flip_5_1, bits_to_flip_5_2 = what_bits_need_to_flip(a1_splitted[4],a2_splitted[4],a3_splitted[4])
bits_to_flip_6_1, bits_to_flip_6_2 = what_bits_need_to_flip(a1_splitted[5],a2_splitted[5],a3_splitted[5])
bits_to_flip_7_1, bits_to_flip_7_2 = what_bits_need_to_flip(a1_splitted[6],a2_splitted[6],a3_splitted[6])
bits_to_flip_8_1, bits_to_flip_8_2 = what_bits_need_to_flip(a1_splitted[7],a2_splitted[7],a3_splitted[7])

bits_to_flip_1_11, bits_to_flip_1_22 = what_bits_need_to_flip(a11_splitted[0],a22_splitted[0],a33_splitted[0])
bits_to_flip_2_11, bits_to_flip_2_22 = what_bits_need_to_flip(a11_splitted[1],a22_splitted[1],a33_splitted[1])
bits_to_flip_3_11, bits_to_flip_3_22 = what_bits_need_to_flip(a11_splitted[2],a22_splitted[2],a33_splitted[2])
bits_to_flip_4_11, bits_to_flip_4_22 = what_bits_need_to_flip(a11_splitted[3],a22_splitted[3],a33_splitted[3])
bits_to_flip_5_11, bits_to_flip_5_22 = what_bits_need_to_flip(a11_splitted[4],a22_splitted[4],a33_splitted[4])
bits_to_flip_6_11, bits_to_flip_6_22 = what_bits_need_to_flip(a11_splitted[5],a22_splitted[5],a33_splitted[5])
bits_to_flip_7_11, bits_to_flip_7_22 = what_bits_need_to_flip(a11_splitted[6],a22_splitted[6],a33_splitted[6])
bits_to_flip_8_11, bits_to_flip_8_22 = what_bits_need_to_flip(a11_splitted[7],a22_splitted[7],a33_splitted[7])

bits_to_flip_1_111, bits_to_flip_1_222 = what_bits_need_to_flip(a111_splitted[0],a222_splitted[0],a333_splitted[0])
bits_to_flip_2_111, bits_to_flip_2_222 = what_bits_need_to_flip(a111_splitted[1],a222_splitted[1],a333_splitted[1])
bits_to_flip_3_111, bits_to_flip_3_222 = what_bits_need_to_flip(a111_splitted[2],a222_splitted[2],a333_splitted[2])
bits_to_flip_4_111, bits_to_flip_4_222 = what_bits_need_to_flip(a111_splitted[3],a222_splitted[3],a333_splitted[3])
bits_to_flip_5_111, bits_to_flip_5_222 = what_bits_need_to_flip(a111_splitted[4],a222_splitted[4],a333_splitted[4])
bits_to_flip_6_111, bits_to_flip_6_222 = what_bits_need_to_flip(a111_splitted[5],a222_splitted[5],a333_splitted[5])
bits_to_flip_7_111, bits_to_flip_7_222 = what_bits_need_to_flip(a111_splitted[6],a222_splitted[6],a333_splitted[6])
bits_to_flip_8_111, bits_to_flip_8_222 = what_bits_need_to_flip(a111_splitted[7],a222_splitted[7],a333_splitted[7])
#print(bits_to_flip1)
#print(bits_to_flip2)

def flip_bits_in_B(input, bits_to_flip1, bits_to_flip2):
    counter = 0
    output1 = []
    output2 = []
    if(len(bits_to_flip1) == 0):
        temp1 = ''.join(map(str,input)) 
    if(len(bits_to_flip1) == 1):
        for i in input:
            for j in i:
                if(counter == bits_to_flip1[0]):
                    j = str(int(j,2) ^ 1)
                output1.append(str(j))
                counter += 1
            temp1 = ''.join(map(str,output1)) 
            counter = 0
    elif(len(bits_to_flip1) == 2):
        for i in input:
            for j in i:
                if(counter == bits_to_flip1[0] or counter == bits_to_flip1[1]):
                    j = str(int(j,2) ^ 1)
                output1.append(str(j))
                counter += 1
            temp1 = ''.join(map(str,output1)) 
            counter = 0
    elif(len(bits_to_flip1) == 3):
        for i in input:
            for j in i:
                if(counter == bits_to_flip1[0] or counter == bits_to_flip1[1] or counter == bits_to_flip1[2]):
                    j = str(int(j,2) ^ 1)
                output1.append(str(j))
                counter += 1
            temp1 = ''.join(map(str,output1)) 
            counter = 0
    elif(len(bits_to_flip1) == 4):
        for i in input:
            for j in i:
                if(counter == bits_to_flip1[0] or counter == bits_to_flip1[1] or counter == bits_to_flip1[2] or counter == bits_to_flip1[3]):
                    j = str(int(j,2) ^ 1)
                output1.append(str(j))
                counter += 1
            temp1 = ''.join(map(str,output1)) 
            counter = 0
    elif(len(bits_to_flip1) == 5):
        for i in input:
            for j in i:
                if(counter == bits_to_flip1[0] or counter == bits_to_flip1[1] or counter == bits_to_flip1[2] or counter == bits_to_flip1[3] or counter == bits_to_flip1[4]):
                    j = str(int(j,2) ^ 1)
                output1.append(str(j))
                counter += 1
            temp1 = ''.join(map(str,output1)) 
            counter = 0
    elif(len(bits_to_flip1) == 6):
        for i in input:
            for j in i:
                if(counter == bits_to_flip1[0] or counter == bits_to_flip1[1] or counter == bits_to_flip1[2] or counter == bits_to_flip1[3] or counter == bits_to_flip1[4] or counter == bits_to_flip1[5]):
                    j = str(int(j,2) ^ 1)
                output1.append(str(j))
                counter += 1
            temp1 = ''.join(map(str,output1)) 
            counter = 0

    counter = 0
    if(len(bits_to_flip2) == 0):
        temp2 = ''.join(map(str,input))
    if(len(bits_to_flip2) == 1):
        for i in input:
            for j in i:
                if(counter == bits_to_flip2[0]):
                    j = str(int(j,2) ^ 1)
                output2.append(str(j))
                counter += 1
            temp2 = ''.join(map(str,output2)) 
            counter = 0
    elif(len(bits_to_flip2) == 2):
        for i in input:
            for j in i:
                if(counter == bits_to_flip2[0] or counter == bits_to_flip2[1]):
                    j = str(int(j,2) ^ 1)
                output2.append(str(j))
                counter += 1
            temp2 = ''.join(map(str,output2)) 
            counter = 0
    elif(len(bits_to_flip2) == 3):
        for i in input:
            for j in i:
                if(counter == bits_to_flip2[0] or counter == bits_to_flip2[1] or counter == bits_to_flip2[2]):
                    j = str(int(j,2) ^ 1)
                output2.append(str(j))
                counter += 1
            temp2 = ''.join(map(str,output2)) 
            counter = 0
    elif(len(bits_to_flip2) == 4):
        for i in input:
            for j in i:
                if(counter == bits_to_flip2[0] or counter == bits_to_flip2[1] or counter == bits_to_flip2[2] or counter == bits_to_flip2[3]):
                    j = str(int(j,2) ^ 1)
                output2.append(str(j))
                counter += 1
            temp2 = ''.join(map(str,output2)) 
            counter = 0
    elif(len(bits_to_flip2) == 5):
        for i in input:
            for j in i:
                if(counter == bits_to_flip2[0] or counter == bits_to_flip2[1] or counter == bits_to_flip2[2] or counter == bits_to_flip2[3] or counter == bits_to_flip2[4]):
                    j = str(int(j,2) ^ 1)
                output2.append(str(j))
                counter += 1
            temp2 = ''.join(map(str,output2)) 
            counter = 0
    elif(len(bits_to_flip2) == 6):
        for i in input:
            for j in i:
                if(counter == bits_to_flip2[0] or counter == bits_to_flip2[1] or counter == bits_to_flip2[2] or counter == bits_to_flip2[3] or counter == bits_to_flip2[4] or counter == bits_to_flip2[5]):
                    j = str(int(j,2) ^ 1)
                output2.append(str(j))
                counter += 1
            temp2 = ''.join(map(str,output2)) 
            counter = 0

    out1,out2 = [],[]
    for i in range(0, 24, 6):
        if(bits_to_flip1 == 0 and bits_to_flip2 != 0):
            out1 = temp1
            out2.append(temp2[i:i+6])
        elif(bits_to_flip2 == 0 and bits_to_flip1 != 0):
            out1.append(temp1[i:i+6])   
            out2 = temp2
        elif(bits_to_flip1 == 0 and bits_to_flip2 == 0):
            out1 = input
            out2 = input
        else:
            out1.append(temp1[i:i+6])
            out2.append(temp2[i:i+6])
    return out1, out2

out_1_1, out_1_2 = flip_bits_in_B(my_array1[0],bits_to_flip_1_1,bits_to_flip_1_2)
out_2_1, out_2_2 = flip_bits_in_B(my_array1[1],bits_to_flip_2_1,bits_to_flip_2_2)
out_3_1, out_3_2 = flip_bits_in_B(my_array1[2],bits_to_flip_3_1,bits_to_flip_3_2)
out_4_1, out_4_2 = flip_bits_in_B(my_array1[3],bits_to_flip_4_1,bits_to_flip_4_2)
out_5_1, out_5_2 = flip_bits_in_B(my_array1[4],bits_to_flip_5_1,bits_to_flip_5_2)
out_6_1, out_6_2 = flip_bits_in_B(my_array1[5],bits_to_flip_6_1,bits_to_flip_6_2)
out_7_1, out_7_2 = flip_bits_in_B(my_array1[6],bits_to_flip_7_1,bits_to_flip_7_2)
out_8_1, out_8_2 = flip_bits_in_B(my_array1[7],bits_to_flip_8_1,bits_to_flip_8_2)

out_1_11, out_1_22 = flip_bits_in_B(my_array2[0],bits_to_flip_1_11,bits_to_flip_1_22)
out_2_11, out_2_22 = flip_bits_in_B(my_array2[1],bits_to_flip_2_11,bits_to_flip_2_22)
out_3_11, out_3_22 = flip_bits_in_B(my_array2[2],bits_to_flip_3_11,bits_to_flip_3_22)
out_4_11, out_4_22 = flip_bits_in_B(my_array2[3],bits_to_flip_4_11,bits_to_flip_4_22)
out_5_11, out_5_22 = flip_bits_in_B(my_array2[4],bits_to_flip_5_11,bits_to_flip_5_22)
out_6_11, out_6_22 = flip_bits_in_B(my_array2[5],bits_to_flip_6_11,bits_to_flip_6_22)
out_7_11, out_7_22 = flip_bits_in_B(my_array2[6],bits_to_flip_7_11,bits_to_flip_7_22)
out_8_11, out_8_22 = flip_bits_in_B(my_array2[7],bits_to_flip_8_11,bits_to_flip_8_22)

out_1_111, out_1_222 = flip_bits_in_B(my_array3[0],bits_to_flip_1_111,bits_to_flip_1_222)
out_2_111, out_2_222 = flip_bits_in_B(my_array3[1],bits_to_flip_2_111,bits_to_flip_2_222)
out_3_111, out_3_222 = flip_bits_in_B(my_array3[2],bits_to_flip_3_111,bits_to_flip_3_222)
out_4_111, out_4_222 = flip_bits_in_B(my_array3[3],bits_to_flip_4_111,bits_to_flip_4_222)
out_5_111, out_5_222 = flip_bits_in_B(my_array3[4],bits_to_flip_5_111,bits_to_flip_5_222)
out_6_111, out_6_222 = flip_bits_in_B(my_array3[5],bits_to_flip_6_111,bits_to_flip_6_222)
out_7_111, out_7_222 = flip_bits_in_B(my_array3[6],bits_to_flip_7_111,bits_to_flip_7_222)
out_8_111, out_8_222 = flip_bits_in_B(my_array3[7],bits_to_flip_8_111,bits_to_flip_8_222)
#print(out_1_1)
#print(out_1_2)
#print("######")
#print(out_2_1)
#print(out_2_2)
#print("######")
#print(out_3_1)
#print(out_3_2)
#print("######")
#print(out_4_1)
#print(out_4_2)
#print("######")
#print(out_5_1)
#print(out_5_2)
#print("######")
#print(out_6_1)
#print(out_6_2)
#print("######")
#print(out_7_1)
#print(out_7_2)
#print("######")
#print(out_8_1)
#print(out_8_2)


def B_register(input0,input1,input2,output_C2,output_C3, sbox):
    row1, row2 = [],[]
    column1, column2 = [],[]
    for i in input1:
        row1.append(int((i[0]+""+i[5]),2))
        column1.append(int(i[1:5],2))
    for i in input2:
        row2.append(int((i[0]+""+i[5]),2))
        column2.append(int(i[1:5],2))
    
    result = []
    if  (sbox[row1[0]][column1[0]] == int(output_C2,2)):
        if(sbox[row2[0]][column2[0]] == int(output_C3,2)):
            result = input0[0]
        elif(sbox[row2[1]][column2[1]] == int(output_C3,2)):
            result = input0[1]
        elif(sbox[row2[2]][column2[2]] == int(output_C3,2)):
            result = input0[2]
        elif(sbox[row2[3]][column2[3]] == int(output_C3,2)):
            result = input0[3]
        else:
            result = input0[0]
    elif(sbox[row1[1]][column1[1]] == int(output_C2,2)):
        if(sbox[row2[0]][column2[0]] == int(output_C3,2)):
            result = input0[0]
        elif(sbox[row2[1]][column2[1]] == int(output_C3,2)):
            result = input0[1]
        elif(sbox[row2[2]][column2[2]] == int(output_C3,2)):
            result = input0[2]
        elif(sbox[row2[3]][column2[3]] == int(output_C3,2)):
            result = input0[3]
        else:
            result = input0[1]
    elif(sbox[row1[2]][column1[2]] == int(output_C2,2)):
        if(sbox[row2[0]][column2[0]] == int(output_C3,2)):
            result = input0[0]
        elif(sbox[row2[1]][column2[1]] == int(output_C3,2)):
            result = input0[1]
        elif(sbox[row2[2]][column2[2]] == int(output_C3,2)):
            result = input0[2]
        elif(sbox[row2[3]][column2[3]] == int(output_C3,2)):
            result = input0[3]
        else:
            result = input0[2]
    elif(sbox[row1[3]][column1[3]] == int(output_C2,2)):
        if(sbox[row2[0]][column2[0]] == int(output_C3,2)):
            result = input0[0]
        elif(sbox[row2[1]][column2[1]] == int(output_C3,2)):
            result = input0[1]
        elif(sbox[row2[2]][column2[2]] == int(output_C3,2)):
            result = input0[2]
        elif(sbox[row2[3]][column2[3]] == int(output_C3,2)):
            result = input0[3]
        else:
            result = input0[3]
    
    return result

print("############### TEST ##############")

result1 = B_register(my_array1[0],out_1_1,out_1_2,array_c2[0],array_c3[0],Sbox[0])
result2 = B_register(my_array1[1],out_2_1,out_2_2,array_c2[1],array_c3[1],Sbox[1])
result3 = B_register(my_array1[2],out_3_1,out_3_2,array_c2[2],array_c3[2],Sbox[2])
result4 = B_register(my_array1[3],out_4_1,out_4_2,array_c2[3],array_c3[3],Sbox[3])
result5 = B_register(my_array1[4],out_5_1,out_5_2,array_c2[4],array_c3[4],Sbox[4])
result6 = B_register(my_array1[5],out_6_1,out_6_2,array_c2[5],array_c3[5],Sbox[5])
result7 = B_register(my_array1[6],out_7_1,out_7_2,array_c2[6],array_c3[6],Sbox[6])
result8 = B_register(my_array1[7],out_8_1,out_8_2,array_c2[7],array_c3[7],Sbox[7])

B_reg_0 = hex(int(result1+""+result2+""+result3+""+result4+""+result5+""+result6+""+result7+""+result8,2)).replace("0x","").zfill(12)

result11 = B_register(my_array2[0],out_1_11,out_1_22,array_c22[0],array_c33[0],Sbox[0])
result22 = B_register(my_array2[1],out_2_11,out_2_22,array_c22[1],array_c33[1],Sbox[1])
result33 = B_register(my_array2[2],out_3_11,out_3_22,array_c22[2],array_c33[2],Sbox[2])
result44 = B_register(my_array2[3],out_4_11,out_4_22,array_c22[3],array_c33[3],Sbox[3])
result55 = B_register(my_array2[4],out_5_11,out_5_22,array_c22[4],array_c33[4],Sbox[4])
result66 = B_register(my_array2[5],out_6_11,out_6_22,array_c22[5],array_c33[5],Sbox[5])
result77 = B_register(my_array2[6],out_7_11,out_7_22,array_c22[6],array_c33[6],Sbox[6])
result88 = B_register(my_array2[7],out_8_11,out_8_22,array_c22[7],array_c33[7],Sbox[7])

B_reg_1 = hex(int(result11+""+result22+""+result33+""+result44+""+result55+""+result66+""+result77+""+result88,2)).replace("0x","").zfill(12)

result111 = B_register(my_array3[0],out_1_111,out_1_222,array_c222[0],array_c333[0],Sbox[0])
result222 = B_register(my_array3[1],out_2_111,out_2_222,array_c222[1],array_c333[1],Sbox[1])
result333 = B_register(my_array3[2],out_3_111,out_3_222,array_c222[2],array_c333[2],Sbox[2])
result444 = B_register(my_array3[3],out_4_111,out_4_222,array_c222[3],array_c333[3],Sbox[3])
result555 = B_register(my_array3[4],out_5_111,out_5_222,array_c222[4],array_c333[4],Sbox[4])
result666 = B_register(my_array3[5],out_6_111,out_6_222,array_c222[5],array_c333[5],Sbox[5])
result777 = B_register(my_array3[6],out_7_111,out_7_222,array_c222[6],array_c333[6],Sbox[6])
result888 = B_register(my_array3[7],out_8_111,out_8_222,array_c222[7],array_c333[7],Sbox[7])

B_reg_2 = hex(int(result111+""+result222+""+result333+""+result444+""+result555+""+result666+""+result777+""+result888,2)).replace("0x","").zfill(12)

Round_Key_1 = hex(int(a1,16) ^ int(B_reg_0,16))
print("Round key 1")
print(Round_Key_1)

Round_Key_2 = hex(int(a11,16) ^ int(B_reg_1,16))
print("Round key 2")
print(Round_Key_2)

Round_Key_3 = hex(int(a111,16) ^ int(B_reg_2,16))
print("Round key 3")
print(Round_Key_3)
