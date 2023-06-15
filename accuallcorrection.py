"""this file contains the actual correction functions."""
import re

def ounces_to_grams(file, ounce_to_gram):
    """This function converts ounces to grams."""
    ounces_pattern = r'(\d+(\.\d+)?) ounces'
    matches = re.findall(ounces_pattern, file)

    for match in matches:
        ounces = float(match[0])
        grams = ounces * ounce_to_gram
        grams_formatted = f"{grams} Gram"
        file = re.sub(ounces_pattern, grams_formatted, file, count=1)

    return file


def pounds_to_kilograms(file, pound_to_kilogram):
    """This function converts pounds to kilograms."""
    pounds_pattern = r'(\d+(\.\d+)?) pounds'
    matches = re.findall(pounds_pattern, file)

    for match in matches:
        pounds = float(match[0])
        kilograms = pounds * pound_to_kilogram
        kilograms_formatted = f"{kilograms} Kilogram"
        file = re.sub(pounds_pattern, kilograms_formatted, file, count=1)

    return file


def gallons_to_liters(file, gallon_to_liter):
    """This function converts gallons to liters."""
    gallons_pattern = r'(\d+(\.\d+)?) gallons'
    matches = re.findall(gallons_pattern, file)

    for match in matches:
        gallons = float(match[0])
        liters = gallons * gallon_to_liter
        liters_formatted = f"{liters} Liter"
        file = re.sub(gallons_pattern, liters_formatted, file, count=1)

    return file


def quart_to_liters(file, quart_to_liter):
    """This function converts quarts to liters."""
    quarts_pattern = r'(\d+(\.\d+)?) quarts'
    matches = re.findall(quarts_pattern, file)

    for match in matches:
        quarts = float(match[0])
        liters = quarts * quart_to_liter
        liters_formatted = f"{liters} Liter"
        file = re.sub(quarts_pattern, liters_formatted, file, count=1)

    return file


def pints_to_liters(file, pint_to_liter):
    """This function converts pints to liters."""
    pints_pattern = r'(\d+(\.\d+)?) pints'
    matches = re.findall(pints_pattern, file)

    for match in matches:
        pints = float(match[0])
        liters = pints * pint_to_liter
        liters_formatted = f"{liters} Liter"
        file = re.sub(pints_pattern, liters_formatted, file, count=1)

    return file


def cups_to_liters(file, cup_to_liter):
    """This function converts cups to liters."""
    cups_pattern = r'(\d+(\.\d+)?) cups'
    matches = re.findall(cups_pattern, file)

    for match in matches:
        cups = float(match[0])
        liters = cups * cup_to_liter
        liters_formatted = f"{liters} Liter"
        file = re.sub(cups_pattern, liters_formatted, file, count=1)

    return file


def fluid_ounces_to_mililiters(file, fluid_ounce_to_milliliter):
    """This function converts fluid ounces to milliliters."""
    fluid_ounces_pattern = r'(\d+(\.\d+)?) fluid ounces'
    matches = re.findall(fluid_ounces_pattern, file)

    for match in matches:
        fluid_ounces = float(match[0])
        milliliters = fluid_ounces * fluid_ounce_to_milliliter
        milliliters_formatted = f"{milliliters} Milliliter"
        file = re.sub(fluid_ounces_pattern, milliliters_formatted, file, count=1)

    return file
