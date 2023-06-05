def get_ind_fam_details(gedcomfile):
    individuals = []
    individual = []

    is_individual = False

    for line in gedcomfile:
        if "INDI" in line:
            if individual:
                individuals.append(individual)
            individual = [line]
            is_individual = True
        elif is_individual:
            if line.startswith(("0 @", "1 @", "2 @")):
                individuals.append(individual)
                individual = []
                is_individual = False
            else:
                individual.append(line)

    if individual:
        individuals.append(individual)
    

    # Return Families
    return []


def display_gedcom_table(individuals, families):
    # Print Individuals table
    print("Individuals:")
    for individual in individuals:
        print(individual)

    # Print Families table
    print("Families:")
    for family in families:
        print(family)


if __name__ == "__main__":
    with open("Shubham_Gedcome.ged", "r") as gedcomf:
        gedcomfile = gedcomf.readlines()
        gedcomfile = [line.rstrip('\n') for line in gedcomfile]

        # Retrieve the Individuals and Family from the input file
        individuals, families = get_ind_fam_details(gedcomfile)

        # Print The details using Pretty Table Library
        display_gedcom_table(individuals, families)
