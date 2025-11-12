"""
This file contains all the text transformation logic for the recipe linter.
Each function takes the file content as a string, finds all matches 
for a specific unit using regex, converts it, and formats it.
"""
import re

# --- FORMATTING HELPERS ---

def round_to_nearest_5(value):
    """Helper function to round a value to the nearest 5."""
    return int(5 * round(float(value) / 5))

def format_weight(grams):
    """
    Takes a gram value and returns a smart, kitchen-friendly string.
    - Under 1000g -> "g" (rounded to nearest 5g)
    - 1000g or more -> "Kg" (rounded to 1 decimal)
    """
    if grams < 1000:
        rounded_grams = round_to_nearest_5(grams)
        return f"{rounded_grams} g"
    else:
        kilograms = round(grams / 1000, 1)
        return f"{kilograms} Kg"

def format_volume(milliliters):
    """
    Takes a milliliter value and returns a smart, kitchen-friendly string.
    - Under 100 ml -> "ml" (rounded to nearest 5ml)
    - 100-999 ml  -> "dl" (rounded to 1 decimal)
    - 1000 ml or more -> "L" (rounded to 1 decimal)
    """
    if milliliters < 100:
        rounded_ml = round_to_nearest_5(milliliters)
        return f"{rounded_ml} ml"
    elif milliliters < 1000:
        deciliters = round(milliliters / 100, 1)
        return f"{deciliters} dl"
    else:
        liters = round(milliliters / 1000, 1)
        return f"{liters} L"

# --- PRE-PROCESSING FUNCTIONS ---

def convert_fractions_to_decimals(file_content):
    """
    Finds common text fractions (e.g., "1 1/2", "1/4") and converts
    them to decimal strings ("1.5", "0.25") so they can be
    parsed as floats by other functions.
    """
    # Handle mixed numbers first (e.g., "1 1/2" -> "1.5")
    file_content = re.sub(r'(\d+)\s+1/2', r'\1.5', file_content)
    file_content = re.sub(r'(\d+)\s+1/4', r'\1.25', file_content)
    file_content = re.sub(r'(\d+)\s+3/4', r'\1.75', file_content)
    file_content = re.sub(r'(\d+)\s+1/3', r'\1.33', file_content)
    file_content = re.sub(r'(\d+)\s+2/3', r'\1.66', file_content)
    
    # Handle standalone fractions (e.g., "1/2" -> "0.5")
    # \b = word boundary, prevents matching "1/2" in "11/2"
    file_content = re.sub(r'\b1/2\b', '0.5', file_content, flags=re.IGNORECASE)
    file_content = re.sub(r'\b1/4\b', '0.25', file_content, flags=re.IGNORECASE)
    file_content = re.sub(r'\b3/4\b', '0.75', file_content, flags=re.IGNORECASE)
    file_content = re.sub(r'\b1/3\b', '0.33', file_content, flags=re.IGNORECASE)
    file_content = re.sub(r'\b2/3\b', '0.66', file_content, flags=re.IGNORECASE)
    return file_content

def format_instructions_simple(file_content):
    """
    Improves readability of instructions by adding a blank line
    after a sentence-ending period (e.g., ". New sentence").
    """
    # Uses a positive lookahead (?=[A-Z]) to find a period, a space,
    # and then an uppercase letter, without consuming the letter.
    formatted_content = re.sub(r'\.\s+(?=[A-Z])', '.\n\n', file_content)
    return formatted_content

# --- UNIT CONVERSION FUNCTIONS ---

# --- Weight ---
def convert_ounces(file_content, grams_per_ounce):
    """Finds "ounce" or "oz" and converts to smart-formatted grams."""
    pattern = r'(\d+(\.\d+)?)\s+(ounces|ounce|ozs|oz)\b(\.?)'
    def repl(match):
        grams = float(match.group(1)) * grams_per_ounce
        return format_weight(grams)
    return re.sub(pattern, repl, file_content, flags=re.IGNORECASE)

def convert_pounds(file_content, grams_per_pound):
    """Finds "pound" or "lb" and converts to smart-formatted g/Kg."""
    pattern = r'(\d+(\.\d+)?)\s+(pounds|pound|lbs|lb)\b(\.?)'
    def repl(match):
        grams = float(match.group(1)) * grams_per_pound
        return format_weight(grams)
    return re.sub(pattern, repl, file_content, flags=re.IGNORECASE)

# --- Volume ---
def convert_gallons(file_content, ml_per_gallon):
    """Finds "gallon" or "gal" and converts to smart-formatted ml/dl/L."""
    pattern = r'(\d+(\.\d+)?)\s+(gallons|gallon|gal)\b(\.?)'
    def repl(match):
        milliliters = float(match.group(1)) * ml_per_gallon
        return format_volume(milliliters)
    return re.sub(pattern, repl, file_content, flags=re.IGNORECASE)

def convert_quarts(file_content, ml_per_quart):
    """Finds "quart" or "qt" and converts to smart-formatted ml/dl/L."""
    pattern = r'(\d+(\.\d+)?)\s+(quarts|quart|qts|qt)\b(\.?)'
    def repl(match):
        milliliters = float(match.group(1)) * ml_per_quart
        return format_volume(milliliters)
    return re.sub(pattern, repl, file_content, flags=re.IGNORECASE)

def convert_pints(file_content, ml_per_pint):
    """Finds "pint" or "pt" and converts to smart-formatted ml/dl/L."""
    pattern = r'(\d+(\.\d+)?)\s+(pints|pint|pts|pt)\b(\.?)'
    def repl(match):
        milliliters = float(match.group(1)) * ml_per_pint
        return format_volume(milliliters)
    return re.sub(pattern, repl, file_content, flags=re.IGNORECASE)

def convert_cups(file_content, ml_per_cup):
    """Finds "cup" or "c" and converts to smart-formatted ml/dl/L."""
    pattern = r'(\d+(\.\d+)?)\s+(cups|cup|c)\b(\.?)'
    def repl(match):
        milliliters = float(match.group(1)) * ml_per_cup
        return format_volume(milliliters)
    return re.sub(pattern, repl, file_content, flags=re.IGNORECASE)

def convert_fluid_ounces(file_content, ml_per_fl_oz):
    """Finds "fluid ounce" or "fl oz" and converts to smart-formatted ml/dl/L."""
    # This pattern is more complex to catch "fl. oz." "fl oz" etc.
    pattern = r'(\d+(\.\d+)?)\s+(fluid\s+ounce(s?)|fl(\.?)\s*oz(\.?))\b'
    def repl(match):
        milliliters = float(match.group(1)) * ml_per_fl_oz
        return format_volume(milliliters)
    return re.sub(pattern, repl, file_content, flags=re.IGNORECASE)

# --- Temperature ---
def convert_fahrenheit_to_celsius(file_content):
    """
    Finds Fahrenheit values (e.g., "350 F", "400°F") and converts to Celsius,
    rounded to the nearest 5°C for practical oven use.
    """
    # Pattern: (Number) (optional space/°) (F or Fahrenheit)
    pattern = r'(\d+(\.\d+)?)\s*(°?)\s*(F|Fahrenheit)\b'
    
    def repl(match):
        fahrenheit = float(match.group(1))
        celsius_exact = (fahrenheit - 32) * 5 / 9
        # Use our kitchen-friendly rounding
        celsius_rounded = round_to_nearest_5(celsius_exact)
        return f"{celsius_rounded}°C"

    return re.sub(pattern, repl, file_content, flags=re.IGNORECASE)