#function to check if the tag is valid and create the output line
def check_valid(input_line):

    #list of valid tags
    valid_tags = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']
    #split input line into level, tag, and arguments
    inputs = input_line.split(' ',2)
    input_level = inputs[0]
    input_tag = inputs[1]
    #account for arguments vs empty arguments
    if len(inputs) > 2:
        input_args = inputs[2]
    else:
        input_args = ''
    #create output line and return based on if tag is valid or not
    if input_tag in valid_tags:
        output_line = input_level + '|' + input_tag + '|Y|' + input_args.replace('\n','')
    else:
        output_line = input_level + '|' + input_tag.replace('\n','') + '|N|'
    return output_line

#read gedcom file
gedcom_file = open('Desai_Aakash_SSW555.ged', 'r')

#print input line and output line created by check_valid function
for line in gedcom_file:
    print('--> ' + line)
    output = check_valid(line)
    print('<-- ' + output)
