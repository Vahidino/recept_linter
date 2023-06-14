"""this file will do the covertion of the units to the EU standard."""
def ounces_to_grams(file, ounce_to_gram):
    """This function converts ounces to grams."""
    eu_validated = ""
    index = file.find(str(ounce_to_gram))

    separated_string = file[:index].strip()
    ounces = float(separated_string.split()[0])
    grams = ounces * ounce_to_gram

    form_1 = str(grams) + " Gram"
    eu_validated = file.replace(separated_string, form_1)
    return eu_validated

""" def Pounds_to_Kilograms(file, Pounds_to_Kilograms):
    EU_validated = ""    
    return EU_validated

def Gallons_to_Liters(file, Gallons_to_Liters):
    EU_validated = ""    
    return EU_validated 

def Quarts_to_Liters(file, Quarts_to_Liters):
    EU_validated = ""        
    return EU_validated

def Pints_to_Liters(file, Pints_to_Liters):
    EU_validated = ""
    return EU_validated

def Cups_to_Liters(file, Cups_to_Liters):
    EU_validated = ""    
    return EU_validated

def fluid_ounces_to_Liters(file, fluid_ounces_to_Liters):
    EU_validated = ""    
    return EU_validated
"""