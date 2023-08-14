from subprocess import check_output as qx

input = 0x0000000000000000
inputArr = []
inputArr.append(hex(input).replace('0x','').zfill(16))
for i in range(64):
    temp = input ^ (1 << (63 - i))
    inputArr.append(hex(temp).replace('0x','').zfill(16))

#for i in inputArr:
#    print(i)

file1 = open("patterns.txt", "w")
for i in range(65): 
    cmd = r'C:\\Users\\artem\\Final\\des_as14836_windows_amd64.exe -input={} -rounds=2 -scan_emit -scan_only'.format(inputArr[i])
    output = qx(cmd)
    file1.write(output.decode('utf-8'))
file1.close()


input_1 = 0x0000000000000000#0xDEADBEEF12345678#
input_2 = 0x0000550000005500#0xBEEF12345678DEAD#
input_3 = 0x5500400110000401#0x1234DEADBEEF5678#

myInputs = []   

myInputs.append(hex(input_1).replace('0x','').zfill(16))                        
myInputs.append(hex(input_2).replace('0x','').zfill(16))
myInputs.append(hex(input_3).replace('0x','').zfill(16))
#print(myInputs)

file2 = open("3_inputs.txt", "w")
for i in range(3): 
    cmd = r'C:\\Users\\artem\\Final\\des_as14836_windows_amd64.exe -input={} -rounds=5 -scan_emit -scan_only'.format(myInputs[i])
    output = qx(cmd)
    file2.write(output.decode('utf- 8'))
file2.close()

#################################################################################################################################
#file3 = open("output_reg.txt", "w")
#for i in range(65): 
#    cmd = r'C:\\Users\\artem\\Final\\des_as14836_windows_amd64.exe -input={} -rounds=18 -scan_emit -scan_only'.format(inputArr[i])
#    output = qx(cmd)
#    file3.write(output.decode('utf-8'))
#file3.close()
#################################################################################################################################