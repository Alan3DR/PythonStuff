from sys import argv
script, address, d = argv

##Data Format:##
#Constant Values
start = "02 "
cmd = "31 "
fixed_bytes ="30 32 "
end = "03"
run =        "31 30 44 34 " #D106 this is the same as reset. Double check!!!
reset =      "31 30 44 34 " 
#Addresses
# yaw_pos =    "31 30 43 38 " #D100
# yaw_speed =  "31 30 43 43 " #D102
# roll_pos =   "31 30 44 43 " #D110 
# roll_speed = "31 30 45 30 " #D112 
#D108   31 30 44 38 ???what is this?
motor={'yaw_pos': '31 30 43 38 ', 'yaw_speed' : '31 30 43 43 ',
 'roll_pos': '31 30 44 43 ', 'roll_speed': '31 30 45 30 '}

#Data Translation
ndec = int(d, base=10) #convert input to dec
nhex = format(ndec, '04X') #convert dec to hex
HLhex = nhex[2]+nhex[3]+nhex[0]+nhex[1] #swap hi and low
shex = '%s' %HLhex #convert hex to string
idec = [ord(r) for r in shex]#convert each charachter to ascii decimal
ihex = [format(y,'02X') for y in idec]#convert each ascii decimal to hex

#checks 
# print "Your decimal number is %d" %ndec
# print "Your hexadecimal number is %s" %nhex
# print "Your hexadecimal H <> L number is %s" %HLhex
# print shex
# print idec
# print "Your hex ascii decimal is"
# print ihex

data = '%s %s %s %s '% (ihex[0], ihex[1], ihex[2], ihex[3])
#checksum = " 00 00 "

#Output
#print "Desired command:"
#ETEcmd = start+cmd+motor[address]+fixed_bytes+data+end+o[len[o]-1]+ o[len[o]-2] 
#print ETEcmd
ETEchk = cmd+motor[address]+fixed_bytes+data+end
print ETEchk
ETE=ETEchk.split(' ') #split ETEchk into a string array
print ETE

#-- Checksum calculation --
#cksum = [(int(g,16) for g in ETEchkArray)]
cksum = format((int(ETE[0],16)+int(ETE[1],16)+int(ETE[2],16)+int(ETE[3],16)+
    int(ETE[4],16)+int(ETE[5],16)+int(ETE[6],16)+int(ETE[7],16)+int(ETE[8],16)+
    int(ETE[9],16)+int(ETE[10],16)+int(ETE[11],16)),'02X')
print "this is the checksum %s" %cksum
l=[ord(b) for b in cksum] #convert each character to ascii decimal
o=[format(n,'02X') for n in l] #convert each ascii decimal to hex
print o
size = len(o)
ck2 = ' %s' %o[size-1]
ck1 = ' %s' %o[size-2]
print ck1
print ck2

ETEcmd = start+cmd+motor[address]+fixed_bytes+data+end+ck1+ck2 
print ETEcmd





#####Notes#####
# YAW_POS D100 to pos 1234   02 31 31 30 43 38 30 32 44 32 30 34 03 34 43
# YAW_POS D100 to pos 1235   02 31 31 30 43 38 30 32 44 33 30 34 03 34 44

# Data format
# START | COMMAND |   PLC ADDRESS | FIXED BYTES |     DATA    | END | SUM
#                       D100                          1234
#  02   |   31    |  31 30 43 38  |    30 32    | 44 32 30 34 | 03  | 34 43

# D100   31 30 43 38    
# D102   31 30 43 43
# D106   31 30 44 34
# D110   31 30 44 43 
# D112   31 30 45 30 
# D108   31 30 44 38

# EXAMPLE OF DATA TRANSLATION     

# Decimal =  HEX = H <> L =    ASCII Hex
# 8000    = 1F40 =  401F  = 34 30 31 46       t=format(int(ord('0')),'02X')

# D100 YAW POS    02 31 31 30 43 38 30 32 34 30 31 46 03 34 44
# D102 YAW_SPEED  02 31 31 30 43 43 30 32 34 30 31 46 03 35 38
# D110 ROLL_POS   02 31 31 30 44 43 30 32 36 30 30 39 03 34 44
# D112 ROLL_SPEED 02 31 31 30 45 30 30 32 36 30 30 39 03 33 42
# D106 RUN   22   02 31 31 30 44 34 30 32 32 32 30 30 03 33 33
# D106 RESET 44   02 31 31 30 44 34 30 32 34 34 30 30 03 33 37

# 02 31 31 30 43 38 30 32 38 38 31 33 03 34 36


#Hexadecimal addition example:
# def add_hex2(hex1, hex2):
#     """add two hexadecimal string values and return as such"""
#     return hex(int(hex1, 16) + int(hex2, 16))
# print add_hex2('0xff', '0xff')  # 0x1fe

#print"\n\n"
# def addHex(hex1, hex2, hex3, hex4, hex5, hex6):
    # return format((int(hex1, 16) + int(hex2, 16)+ int(hex3, 16)+ int(hex4, 16)+ int(hex5, 16)+ int(hex6, 16)),'02X')
    

# print addHex(start, cmd, motor[address], fixed_bytes, data, end)



