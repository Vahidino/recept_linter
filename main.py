# -*- coding: utf-8 -*-
import argparse
import json
import accuallcorrection as accuallcorrection 
def main():
   
    print("Your recepie has been converted to the EU standard.")    
    parser = argparse.ArgumentParser(prog='myprogram',description='Lintercleanter.', add_help=False) # add_help=False to remove the default help option
  
  
    parser.add_argument('-h', '--help', action='help', help='show this help message and exit')
    parser.add_argument('file', type=str, help='File to be corrected')
    parser.add_argument('-o', '--output', type=str, help='Output file')

    arg = parser.parse_args() # parse the arguments
    

    config_path = "C:\\Users\\User\\Desktop\\recept-reengeder\\config.json" # get the path to the config file
    config_path = config_path.replace("main.py", "config.json") # replace the file name with the config file name
    
    json_file = open(config_path, "r", encoding="utf-8").read()
    json_data = json.loads(json_file)

    Ounces_to_Grams = json_data["Ounces_to_Grams"]
    """Pounds_to_Kilograms = json_data["Pounds_to_Kilograms"]
    Gallons_to_Liters = json_data["Gallons_to_Liters"]
    Quarts_to_Liters = json_data["Quarts_to_Liters"]
    Pints_to_Liters = json_data["Pints_to_Liters"]
    Cups_to_Liters = json_data["Cups_to_Liters"]
    fluid_ounces_to_Liters = json_data["fluid_ounces_to_Liters"]"""

    file_dir = arg.file # get the file path from the arguments
    file = open(file_dir, "r", encoding="UTF-8").read() # öppnar filen
    
    output_file = file_dir.split('.')[0] + '_EU_validated.' + file_dir.split('.')[1]

    EU_validated = accuallcorrection.Ounces_to_Grams(file, Ounces_to_Grams)
    """EU_validated = accuallcorrection.Pounds_to_Kilograms(EU_validated, Pounds_to_Kilograms)
    EU_validated = accuallcorrection.Gallons_to_Liters(EU_validated, Gallons_to_Liters)
    EU_validated = accuallcorrection.Quarts_to_Liters(EU_validated, Quarts_to_Liters)
    EU_validated = accuallcorrection.Pints_to_Liters(EU_validated, Pints_to_Liters)
    EU_validated = accuallcorrection.Cups_to_Liters (EU_validated, Cups_to_Liters)
    EU_validated = accuallcorrection.fluid_ounces_to_Liters(EU_validated, fluid_ounces_to_Liters)"""

    with open(output_file, 'w') as f: # skriver till outputfilen
        f.write(EU_validated)

if __name__ == "__main__":
    main()
