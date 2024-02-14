import phonenumbers
import json
import csv

def parse_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(f"+{phone_number}", None)
        return parsed_number
    except phonenumbers.NumberParseException:
        return None

def convert_json_to_csv(input_file, output_file):
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for phone_number in data.keys():
            print("Processing phone number:", phone_number)
            parsed_number = parse_phone_number(phone_number)
            print("Parsed number:", parsed_number)
            if parsed_number:
                country_code = str(parsed_number.country_code)
                country = phonenumbers.region_code_for_number(parsed_number)
                number = str(parsed_number.national_number)
                writer.writerow([f"+{country_code}{number}", country])

if __name__ == "__main__":
    input_json_file = "./Data/test.json"
    output_csv_file = "./Data/test.csv"
    convert_json_to_csv(input_json_file, output_csv_file)
