import sys
import tkinter as tk
from tkinter import filedialog
import pygame
import accuallcorrection as accuall_correction

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Recipe Converter")

# Variable to track the state of help display
showing_help = False

def show_main_menu():
    global showing_help
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Code to handle 'Convert' option
                    # Open a file dialog to select the TXT file to convert
                    file_path = open_file_dialog()
                    if file_path:
                        # Convert the selected file
                        game.convert_file(file_path, ounces_to_grams_ratio, pounds_to_kilograms_ratio, gallons_to_liters_ratio,
                                          quart_to_liters_ratio, pints_to_liters_ratio, cups_to_liters_ratio,
                                          fluid_ounces_to_milliliters_ratio)
 
                elif event.key == pygame.K_2:
                    # Code to handle 'Options' option
                    # Handle options functionality
                    handle_options()
                elif event.key == pygame.K_3:
                    # Code to handle 'Help' option
                    # Toggle the help display state
                    showing_help = not showing_help
                elif event.key == pygame.K_BACKSPACE:
                    # Code to handle 'Backspace' key
                    # Return to the main menu
                    showing_help = False
        
        # Clear the screen
        window.fill((255, 255, 255))
        
        # Display the main menu options
        display_text("1. Convert", (WINDOW_WIDTH // 2, 200))
        display_text("2. Options", (WINDOW_WIDTH // 2, 250))
        display_text("3. Help", (WINDOW_WIDTH // 2, 300))
        
        # If help is currently being displayed, show the help text and back button
        if showing_help:
            display_help()
        
        # Update the display
        pygame.display.update()

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def convert_file(file_path, ounce_to_gram, pound_to_kilogram, gallon_to_liter, quart_to_liter, pints_to_liters_ratio, cups_to_deciliter, fluid_ounce_to_milliliter):
    # Read the file content
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Perform the necessary corrections using the provided conversion ratios
    converted_content = accuall_correction.ounces_to_grams(content, ounce_to_gram)
    converted_content = accuall_correction.pounds_to_kilograms(converted_content, pound_to_kilogram)
    converted_content = accuall_correction.gallons_to_liters(converted_content, gallon_to_liter)
    converted_content = accuall_correction.quart_to_liters(converted_content, quart_to_liter)
    converted_content = accuall_correction.pints_to_liters(converted_content, pints_to_liters_ratio)
    converted_content = accuall_correction.cups_to_deciliters(converted_content, cups_to_deciliter)
    converted_content = accuall_correction.fluid_ounces_to_mililiters(converted_content, fluid_ounce_to_milliliter)

    # Write the converted content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(converted_content)


def handle_options():
    # Handle the options functionality
    # ...
    pass

def display_help():
    # Clear the screen
    window.fill((255, 255, 255))

    # Display help information on the Pygame window
    help_text = [
        "Help information",
        "To use the program, select the 'Convert' option and select the TXT file to convert.",
        # Add more help text if needed
    ]

    # Display the help text
    y = 100
    for line in help_text:
        display_text(line, (WINDOW_WIDTH // 2, y))
        y += 50

    # Display the back button
    display_text("Back", (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50), size=24, color=(255, 0, 0))

def display_text(text, position, size=32, color=(0, 0, 0)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    window.blit(text_surface, text_rect)

def display_converted_content(content):
    # Clear the screen
    window.fill((255, 255, 255))

    # Display the converted content on the Pygame window
    display_text("Converted Content:", (WINDOW_WIDTH // 2, 100))
    display_text(content, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), size=24)

    # Display the back button
    display_text("Back", (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50), size=24, color=(255, 0, 0))

# Call the show_main_menu function to start the program
show_main_menu()
