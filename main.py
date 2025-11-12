import json
import pygame
import game
import accuallcorrection as accuall_correction

# Global variables for conversion ratios
ounces_to_grams_ratio = 0.0
pounds_to_kilograms_ratio = 0.0
gallons_to_liters_ratio = 0.0
quart_to_liters_ratio = 0.0
pints_to_liters_ratio = 0.0
cups_to_liters_ratio = 0.0
fluid_ounces_to_milliliters_ratio = 0.0

def main():
<<<<<<< Updated upstream
    print("Your recipe has been converted to the EU standard.")
=======
   
    print("Your recepie has been converted to the EU standard.")  
     
    parser = argparse.ArgumentParser(prog='myprogram',description='Lintercleanter.', add_help=False) # add_help=False to remove the default help option
  
  
    parser.add_argument('-h', '--help', action='help', help='show this help message and exit')
    parser.add_argument('file', type=str, help='File to be corrected')
    parser.add_argument('-o', '--output', type=str, help='Output file')
>>>>>>> Stashed changes

    config_path = "C:\\Users\\Shade\\Documents\\GitHub\\recept_linter\\config.json"
    config_path = config_path.replace("main.py", "config.json")

    with open(config_path, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)

<<<<<<< Updated upstream
    # Update the global variables with the conversion ratios
    global ounces_to_grams_ratio
    ounces_to_grams_ratio = json_data["ounces_to_grams"]
    global pounds_to_kilograms_ratio
    pounds_to_kilograms_ratio = json_data["pounds_to_kilograms"]
    global gallons_to_liters_ratio
    gallons_to_liters_ratio = json_data["gallons_to_liters"]
    global quart_to_liters_ratio
    quart_to_liters_ratio = json_data["quarts_to_liters"]
    global pints_to_liters_ratio
    pints_to_liters_ratio = json_data["pints_to_liters"]
    global cups_to_liters_ratio
    cups_to_liters_ratio = json_data["cups_to_deciliters"]
    global fluid_ounces_to_milliliters_ratio
    fluid_ounces_to_milliliters_ratio = json_data["fluid_ounces_to_milliliters"]

    # Initialize pygame
    pygame.init()
    game.show_main_menu()  # This line is moved inside the main() function
=======
    Ounces_to_Grams = json_data["Ounces_to_Grams"]

    Pounds_to_Kilograms = json_data["Pounds_to_Kilograms"]

    """Gallons_to_Liters = json_data["Gallons_to_Liters"]
    Quarts_to_Liters = json_data["Quarts_to_Liters"]
    Pints_to_Liters = json_data["Pints_to_Liters"]
    Cups_to_Liters = json_data["Cups_to_Liters"]
    fluid_ounces_to_Liters = json_data["fluid_ounces_to_Liters"]"""

    file_dir = arg.file # get the file path from the arguments
    file = open(file_dir, "r", encoding="UTF-8").read() # öppnar filen
    
    output_file = file_dir.split('.')[0] + '_EU_validated.' + file_dir.split('.')[1]

    EU_validated = accuallcorrection.Ounces_to_Grams(file, Ounces_to_Grams)
    EU_validated = accuallcorrection.Pounds_to_Kilograms(EU_validated, Pounds_to_Kilograms)
    """EU_validated = accuallcorrection.Gallons_to_Liters(EU_validated, Gallons_to_Liters)
    EU_validated = accuallcorrection.Quarts_to_Liters(EU_validated, Quarts_to_Liters)
    EU_validated = accuallcorrection.Pints_to_Liters(EU_validated, Pints_to_Liters)
    EU_validated = accuallcorrection.Cups_to_Liters (EU_validated, Cups_to_Liters)
    EU_validated = accuallcorrection.fluid_ounces_to_Liters(EU_validated, fluid_ounces_to_Liters)"""

    with open(output_file, 'w') as f: # skriver till outputfilen
        f.write(EU_validated)
>>>>>>> Stashed changes

if __name__ == "__main__":
    main()