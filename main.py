import json
import os
import pygame
import sys
import tkinter as tk
from tkinter import messagebox
import game # The UI controller

def main():
    """
    Main entry point for the application.
    Loads configuration and starts the game/UI loop.
    """
    print("Starting Recipe Converter...")

    # --- Robust Config Loading ---
    # We must load config before initializing Pygame, as the app
    # cannot run without it.
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "config.json")
        
        with open(config_path, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            
    except FileNotFoundError:
        error_msg = f"CRITICAL ERROR: config.json was not found.\n\nThe application looked for it at:\n{config_path}\n\nPlease make sure config.json is in the same folder as main.py."
        print(error_msg)
        # We can't use Pygame (it's not init'd), so use Tkinter for the error
        tk_root = tk.Tk()
        tk_root.withdraw()
        messagebox.showerror("Fatal Error", error_msg)
        return # Exit the application
    except json.JSONDecodeError:
        error_msg = f"CRITICAL ERROR: config.json is corrupted and could not be read.\n\nPlease check the file for syntax errors."
        print(error_msg)
        tk_root = tk.Tk()
        tk_root.withdraw()
        messagebox.showerror("Fatal Error", error_msg)
        return # Exit the application
    except Exception as e:
        error_msg = f"An unknown error occurred while loading config:\n{e}"
        print(error_msg)
        tk_root = tk.Tk()
        tk_root.withdraw()
        messagebox.showerror("Fatal Error", error_msg)
        return # Exit the application

    # --- Start Pygame Application ---
    # We only get here if the config was loaded successfully.
    
    pygame.init()
    
    # Pass the loaded config data to the UI controller
    game.show_main_menu(json_data) 

if __name__ == "__main__":
    main()