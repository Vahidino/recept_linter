"""this file contains the actual correction functions."""
import re

def ounces_to_grams(file, ounce_to_gram):
    """This function converts ounces to grams."""
    ounces_pattern = r'(\d+(\.\d+)?) ounces'
    matches = re.findall(ounces_pattern, file)

    for match in matches:
        ounces = float(match[0])
        grams = round(ounces * ounce_to_gram, 2)
        grams_formatted = f"{grams} g"
        file = re.sub(ounces_pattern, grams_formatted, file, count=1)

    return file


def pounds_to_kilograms(file, pound_to_kilogram):
    """This function converts pounds to kilograms."""
    pounds_pattern = r'(\d+(\.\d+)?) lb'
    matches = re.findall(pounds_pattern, file)

    for match in matches:
        pounds = float(match[0])
        kilograms = round(pounds * pound_to_kilogram, 2)
        kilograms_formatted = f"{kilograms} Kg"
        file = re.sub(pounds_pattern, kilograms_formatted, file, count=1)

    return file


def gallons_to_liters(file, gallon_to_liter):
    """This function converts gallons to liters."""
    gallons_pattern = r'(\d+(\.\d+)?) gallons'
    matches = re.findall(gallons_pattern, file)

    for match in matches:
        gallons = float(match[0])
        liters = round(gallons * gallon_to_liter, 2)
        liters_formatted = f"{liters} L"
        file = re.sub(gallons_pattern, liters_formatted, file, count=1)

    return file


def quart_to_liters(file, quart_to_liter):
    """This function converts quarts to liters."""
    quarts_pattern = r'(\d+(\.\d+)?) quarts'
    matches = re.findall(quarts_pattern, file)

    for match in matches:
        quarts = float(match[0])
        liters = round(quarts * quart_to_liter, 2)
        liters_formatted = f"{liters} L"
        file = re.sub(quarts_pattern, liters_formatted, file, count=1)

    return file


def pints_to_liters(file, pint_to_liter):
    """This function converts pints to liters."""
    pints_pattern = r'(\d+(\.\d+)?) pints'
    matches = re.findall(pints_pattern, file)

    for match in matches:
        pints = float(match[0])
        liters = round(pints * pint_to_liter, 2)
        liters_formatted = f"{liters} L"
        file = re.sub(pints_pattern, liters_formatted, file, count=1)

    return file


def cups_to_deciliters(file, cup_to_deciliter):
    """This function converts cups to liters."""
    cups_pattern = r'(\d+(\.\d+)?) cups'
    matches = re.findall(cups_pattern, file)

    for match in matches:
        cups = float(match[0])
        deciliter = round(cups * cup_to_deciliter,2)
        deciliters_formatted = f"{deciliter} Dl"
        file = re.sub(cups_pattern, deciliters_formatted, file, count=1)

    return file


def fluid_ounces_to_mililiters(file, fluid_ounce_to_milliliter):
    """This function converts fluid ounces to milliliters."""
    fluid_ounces_pattern = r'(\d+(\.\d+)?) fluid ounces'
    matches = re.findall(fluid_ounces_pattern, file)

    for match in matches:
        fluid_ounces = float(match[0])
        milliliters = round(fluid_ounces * fluid_ounce_to_milliliter, 2)
        milliliters_formatted = f"{milliliters} Ml"
        file = re.sub(fluid_ounces_pattern, milliliters_formatted, file, count=1)

    return file

def ingredient_linter(file):
    """This function performs linting for ingredient formatting."""
    ingredients = []
    lines = file.splitlines()

    ingredient_keywords = ["ounces", "lb", "gallons", "quarts", "pints", "cups", "fluid ounces"]  # Add more keywords as needed

    for line in lines:
        for keyword in ingredient_keywords:
            if keyword in line:
                ingredients.append(line)
                break

    return ingredients



def fix_instructions(file, ingredients):
    """This function fixes the instructions formatting and converts measurements."""
    for ingredient in ingredients:
        file = file.replace(f"{ingredient}.", f"{ingredient}.\n")

    return file
