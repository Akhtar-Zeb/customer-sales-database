import sys
import re
import csv

def main():

    input_file = input("Enter file path: ")
    parts = input_file.split("/")
    file_path, file_name = parts
    if file_name == "CUST.txt":
        customers(input_file)
    elif file_name == "PROD.txt":
        products(input_file)
    elif file_name == "TRANS.txt":
        transactions(input_file)
    elif file_name == "TRANBNS.txt":
        transactions_bonus(input_file)
    elif file_name == "TRANSRET.txt":
        transactions_return(input_file)
    elif file_name == "TRANBSRET.txt":
        transactions_bonus_return(input_file)
    else:
        print("File not found.")

        

def customers(inputfile):
    take_name = inputfile.split(".")
    second_parts = take_name[0].split("/")
    output_file = f"clean_data/{second_parts[1].lower()}_clean.csv"

    clean_data = []
    with open(inputfile, "r") as infile:
        for line in infile:
            parts = re.split(r'\s{2,}', line.strip())

            clean_data.append(parts)

    with open(output_file, "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["customer_id", "customer_name", "customer_location"])
        for line in clean_data:
            if len(line) >= 3:
                writer.writerow(line[:3])
            elif len(line) == 2:
                writer.writerow(line + [""])

def products(inputfile):
    pass

def transactions(inputfile):
    pass

def transactions_bonus(inputfile):
    pass

def transactions_return(inputfile):
    pass

def transactions_bonus_return(inputfile):
    pass


if __name__ == "__main__":
    main()