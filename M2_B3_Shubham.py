outputf = ""
valid_tags = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']
with open('Shubham_Gedcome.ged', 'r') as inputfile:
    inputf = inputfile.readlines()
    inputf = [line.rstrip('\n') for line in inputf]
    for line in inputf:
        key = line.split(' ')
        outputf += f"--> {line}\n"
        matches = [word for word in key if (word == "INDI" or word == "FAM")]
        if len(matches) > 0:
            outputf += f"<-- {key[0]}|{key[2]}|Y|{key[1]}\n"
        else:
            argument = ""
            outputf += f"<-- {key[0]}|{key[1]}|"
            if len(key) > 2:
                for i in range(2, len(key)):
                    argument += f"{key[i]} "
                    argument_stripped = argument.rstrip()
            if key[1] in valid_tags:
                outputf += "Y"
            else:
                outputf += "N"
            if len(key) > 2:
                outputf += f"|{argument_stripped}"
            outputf += "\n"
            argument = ""
with open("outputfile.txt", "w") as output:
    output.write(outputf)
        