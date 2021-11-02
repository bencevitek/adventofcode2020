#task1
validpasscount = 0
byrOK = 0
iyrOK = 0
eyrOK = 0
hgtOK = 0
hclOK = 0
eclOK = 0
pidOK = 0

with open('day4.txt') as f:
    for line in f:
        if line in ['\n', '\r\n']:
            if(byrOK == 1 and iyrOK == 1 and eyrOK == 1 and hgtOK == 1 and hclOK == 1 and eclOK == 1 and pidOK == 1):
                validpasscount += 1
            byrOK = 0
            iyrOK = 0
            eyrOK = 0
            hgtOK = 0
            hclOK = 0
            eclOK = 0
            pidOK = 0
        if 'byr:' in line:
            byrOK = 1
        if 'iyr:' in line:
            iyrOK = 1
        if 'eyr:' in line:
            eyrOK = 1
        if 'hgt:' in line:
            hgtOK = 1
        if 'hcl:' in line:
            hclOK = 1
        if 'ecl:' in line:
            eclOK = 1
        if 'pid:' in line:
            pidOK = 1

print(validpasscount)

f.close()

#task2
import re

validpasscount2 = 0
byrOK = 0
iyrOK = 0
eyrOK = 0
hgtOK = 0
hclOK = 0
eclOK = 0
pidOK = 0
with open('day4.txt') as f:
    for line in f:
        if line in ['\n', '\r\n']:
            if(byrOK == 1 and iyrOK == 1 and eyrOK == 1 and hgtOK == 1 and hclOK == 1 and eclOK == 1 and pidOK == 1):
                validpasscount2 += 1
            byrOK = 0
            iyrOK = 0
            eyrOK = 0
            hgtOK = 0
            hclOK = 0
            eclOK = 0
            pidOK = 0
        #if 'byr:' in line:
        if re.search('byr:(19[2-9][0-9]|200[0-3])($| )', line):
            byrOK = 1
        #if 'iyr:' in line:
        if re.search('iyr:20(1[0-9]|20)($| )', line):
            iyrOK = 1
        #if 'eyr:' in line:
        if re.search('eyr:20(2[0-9]|30)($| )', line):
            eyrOK = 1
        #if 'hgt:' in line:
        if re.search('hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)($| )', line):
            hgtOK = 1
        #if 'hcl:' in line:
        if re.search('hcl:#[0-9a-f]{6}($| )', line):
            hclOK = 1
        #if 'ecl:' in line:
        if re.search('ecl:(amb|blu|brn|gry|grn|hzl|oth)($| )', line):
            eclOK = 1
        #if 'pid:' in line:
        if re.search('pid:[0-9]{9}($| )', line):
            pidOK = 1

print(validpasscount2)

f.close()