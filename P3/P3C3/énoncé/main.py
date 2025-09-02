import csv

def main():
    load(transform(extract()))

def transform(dict):
    for employee in dict:
        employee['salaire'] = int(employee['heures_travaillees']) * 15
        del employee['heures_travaillees']
    return dict

def load(dict):
    fieldnames = ('nom', 'salaire')
    with open('output.csv', 'w') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames, dialect='unix')
        writer.writeheader()
        writer.writerows(dict)
        output_csv.close()

def extract():
    employes = []

    with open('input.csv', 'r') as input_csv:
        reader = csv.DictReader(input_csv)
        for ligne in reader:
            employes.append(ligne)
    return employes

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
