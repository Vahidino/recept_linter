"""This is the main file of the program."""
import argparse
import json
import accuallcorrection as accuall_correction

def main():
    """This is the main function of the program."""
    print("Your recipe has been converted to the EU standard.")
    parser = argparse.ArgumentParser(prog='myprogram', description='Lintercleanter.', add_help=False)
    # add_help=False to remove the default help option

    parser.add_argument('-h', '--help', action='help', help='show this help message and exit')
    parser.add_argument('file', type=str, help='File to be corrected')
    parser.add_argument('-o', '--output', type=str, help='Output file')

    arg = parser.parse_args()  # parse the arguments

    config_path = "C:\\Users\\Shade\\Documents\\GitHub\\recept_linter\\config.json"
    # get the path to the config file
    config_path = config_path.replace("main.py", "config.json")
    # replace the file name with the config file name

    with open(config_path, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)

    ounces_to_grams_ratio = json_data["ounces_to_grams"]
    pounds_to_kilograms_ratio = json_data["pounds_to_kilograms"]
    gallons_to_liters_ratio = json_data["gallons_to_liters"]
    quart_to_liters_ratio = json_data["quarts_to_liters"]
    pints_to_liters_ratio = json_data["pints_to_liters"]
    cups_to_liters_ratio = json_data["cups_to_deciliters"]
    fluid_ounces_to_mililiters_ratio = json_data["fluid_ounces_to_mililiters"]

    file_dir = arg.file  # get the file path from the arguments
    with open(file_dir, "r", encoding="utf-8") as file:
        content = file.read()

    output_file = file_dir.split('.')[0] + '_EU_validated.' + file_dir.split('.')[1]

    eu_validated = accuall_correction.ounces_to_grams(content, ounces_to_grams_ratio)
    eu_validated = accuall_correction.pounds_to_kilograms(eu_validated, pounds_to_kilograms_ratio)
    eu_validated = accuall_correction.gallons_to_liters(eu_validated, gallons_to_liters_ratio)
    eu_validated = accuall_correction.quart_to_liters(eu_validated, quart_to_liters_ratio)
    eu_validated = accuall_correction.pints_to_liters(eu_validated, pints_to_liters_ratio)
    eu_validated = accuall_correction.cups_to_deciliters(eu_validated, cups_to_liters_ratio)
    eu_validated = accuall_correction.fluid_ounces_to_mililiters(eu_validated, fluid_ounces_to_mililiters_ratio)

    # Call the ingredient_linter function to get the list of ingredients
    ingredients = accuall_correction.ingredient_linter(content)

    # Fix the instructions formatting using the fix_instructions function
    fixed_instructions = accuall_correction.fix_instructions(content, ingredients)

    with open(output_file, 'w') as file:  # write to the output file
        file.write(fixed_instructions)

if __name__ == "__main__":
    main()
