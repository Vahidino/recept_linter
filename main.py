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
    print("Your recipe has been converted to the EU standard.")

    config_path = "C:\\Users\\Shade\\Documents\\GitHub\\recept_linter\\config.json"
    config_path = config_path.replace("main.py", "config.json")

    with open(config_path, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)

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

    # Initialize Pygame and show the main menu
    pygame.init()
    game.show_main_menu()

    # Rest of your code goes here

if __name__ == "__main__":
    main()
