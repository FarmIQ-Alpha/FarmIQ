def replace_commas_with_periods(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='windows-1250') as file:
        content = file.read()

    # Replace all commas with periods
    modified_content = content.replace(',', '.')

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='windows-1250') as file:
        file.write(modified_content)


# Specify the path to your CSV file
csv_file_path = 'podatki_v_csv/leto_podkategorija.csv'
replace_commas_with_periods(csv_file_path)

print("Commas in the CSV have been replaced with periods.")
