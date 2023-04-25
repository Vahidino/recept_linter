
def Ounces_to_Grams(file, Ounces_to_Grams):

    EU_validated = ""
    index = file.find(str(Ounces_to_Grams))

    separated_string = file[:index].strip()
    ounces = float(separated_string.split()[0])
    grams = ounces * Ounces_to_Grams
    
    form_1 = str(grams) + " Gram"           
    EU_validated = file.replace(separated_string, form_1)
    return EU_validated

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