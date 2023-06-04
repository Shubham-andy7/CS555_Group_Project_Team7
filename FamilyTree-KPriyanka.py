'''
File name: FamilyTree-KPriyanka.py
Author: Priyanka Koul
Python Version: IDLE shell 3.11.3
Description: This program reads each line of GEDCOM as the input file and prints both input and expected output format of gedcom file.
'''

import sys

# Following are the level and valid strings used in the GEDCOM file
dict_level_valid_tags= {
 '0': {'INDI','HEAD','TRLR','NOTE','FAM'},
 '1': {'NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV'},
 '2': {'DATE'}
}


# Input file name: FamilyTree-KPriyanka.ged
fileName= "FamilyTree-KPriyanka.ged"

# Read every line if ged file is available
try:
    sys.stdout = open("Output_FamilyTree-KPriyanka.txt", "w")
    fp = open(fileName, 'r', encoding='utf-8')
    with fp:
        lines = fp.readlines()
        fp.close()
        for line in lines:
            line = line.rstrip("\n")
            if line != "" and line[0].isdigit():
                print("-->", line)
                valid_tags = dict_level_valid_tags.get(line[0])
                new_line = line.split()
                line_args = " ".join(new_line[2:])
                level = new_line[0]
                if valid_tags == None:
                    print(f"<-- {level}|{new_line[1]}|N|{line_args}")
                elif level == "0":
                    if len(new_line) > 2 and new_line[2] in valid_tags:
                        print(f"<-- {level}|{new_line[2]}|Y|{new_line[1]}")
                    elif new_line[1] in valid_tags:
                        tag = new_line[1]
                        if tag == "FAM"  or tag == "INDI":
                            if len(new_line) > 2:
                                print(f"<-- {level}|{tag}|N|{new_line[2]}")
                            else:
                                print(f"<-- {level}|{tag}|N|")
                        else:
                            print(f"<-- {level}|{tag}|Y|{line_args}")
                    else:
                        if new_line[2] == "INDI" or new_line[2] == "FAM":
                            print(f"<-- {level}|{new_line[2]}|N|{new_line[1]}")
                        else:
                            print(f"<-- {level}|{new_line[1]}|N|{line_args}")
                elif new_line[1] not in valid_tags:
                    print(f"<-- {level}|{new_line[1]}|N|{line_args}")
                else:
                    print(f"<-- {level}|{new_line[1]}|Y|{line_args}")
    sys.stdout.close()
# Create an exception if ged file is not found
except FileNotFoundError:
    print(f"Unable to open file {path} \n ")
