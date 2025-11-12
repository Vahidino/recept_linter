import os
import tkinter as tk
from tkinter import filedialog, messagebox
import accuallcorrection

# Hide the main Tkinter window
tk_root = tk.Tk()
tk_root.withdraw()

def open_file_dialog():
    """
    Shows an "Open File" dialog and returns the selected file path.
    """
    file_path = filedialog.askopenfilename(
        title="Select a recipe .txt file to convert",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    return file_path

def save_file_dialog(original_filename):
    """
    Shows a "Save As" dialog, suggesting a new filename, 
    and returns the selected save path.
    """
    suggested_name = original_filename.replace(".txt", "_converted.txt")
    file_path = filedialog.asksaveasfilename(
        title="Save converted recipe as...",
        initialfile=suggested_name,
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    return file_path

def convert_file(file_path, config_data):
    """
    The main conversion logic. Reads, processes, and saves the file.
    Shows success or error messages to the user.
    """
    
    # --- 1. Read File ---
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        messagebox.showerror("File Error", f"Could not read the file:\n{e}")
        return

    # --- 2. Run Conversions ---
    try:
        # Step 2a: Fix fractions first
        converted_content = accuallcorrection.convert_fractions_to_decimals(content)

        # Step 2b: Convert weights (to g/Kg)
        converted_content = accuallcorrection.convert_ounces(converted_content, config_data["ounces_to_grams"])
        converted_content = accuallcorrection.convert_pounds(converted_content, config_data["pounds_to_grams"])

        # Step 2c: Convert volumes (to ml/dl/L)
        converted_content = accuallcorrection.convert_gallons(converted_content, config_data["gallons_to_milliliters"])
        converted_content = accuallcorrection.convert_quarts(converted_content, config_data["quarts_to_milliliters"])
        converted_content = accuallcorrection.convert_pints(converted_content, config_data["pints_to_milliliters"])
        converted_content = accuallcorrection.convert_cups(converted_content, config_data["cups_to_milliliters"])
        converted_content = accuallcorrection.convert_fluid_ounces(converted_content, config_data["fluid_ounces_to_milliliters"])
        
        # Step 2d: Convert temperature
        converted_content = accuallcorrection.convert_fahrenheit_to_celsius(converted_content)

        # Step 2e: Format instructions
        final_content = accuallcorrection.format_instructions_simple(converted_content)
        
    except KeyError as e:
        error_msg = f"Configuration file error: Missing key {e}.\nPlease check your config.json."
        print(f"CONFIG ERROR: Missing key {e}")
        messagebox.showerror("Config Error", error_msg)
        return
    except Exception as e:
        error_msg = f"An unknown error occurred during conversion:\n{e}"
        print(f"CONVERSION ERROR: {e}")
        messagebox.showerror("Error", error_msg)
        return

    # --- 3. Get Save Path ---
    original_filename = os.path.basename(file_path) 
    save_path = save_file_dialog(original_filename)

    if not save_path:
        # User clicked "Cancel" in the save dialog
        print("Save operation cancelled by user.")
        return

    # --- 4. Write File ---
    try:
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(final_content)
        
        success_msg = f"Recipe successfully converted and saved to:\n{save_path}"
        print(f"SUCCESS: File saved to {save_path}")
        messagebox.showinfo("Conversion Complete", success_msg)
        
    except Exception as e:
        print(f"Error writing file: {e}")
        messagebox.showerror("File Error", f"Could not save the file:\n{e}")