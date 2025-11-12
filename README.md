Recipe Converter
A standalone Python application designed to parse and convert American recipes into metric units, making them easy to use for a global audience. The app features a clean, multi-screen graphical user interface built with Pygame.

💡 About The Project
This project was built to solve a common problem: finding a recipe online only to discover all measurements are in obscure imperial units like cups, ounces, and pounds, with temperatures in Fahrenheit.

This tool not only converts these units but also intelligently formats them into kitchen-friendly values (e.g., 0.7 Kg becomes 700 g) and improves the readability of the instructions.

The project is built entirely in Python, using Pygame for the UI rendering and Tkinter for handling native OS file dialogs.

✨ Key Features
Smart Weight Conversion: Converts pounds (lb) and ounces (oz) to grams.

Smart Logic: Automatically displays values < 1000g as g (e.g., 700 g) and values > 1000g as Kg (e.g., 1.2 Kg).

Smart Volume Conversion: Converts cups, gallons, quarts, pints, and fluid ounces (fl oz) to milliliters.

Smart Logic: Automatically selects the best unit to display: ml, dl, or L (e.g., 946 ml becomes 9.5 dl).

Temperature Conversion: Finds and converts temperatures from Fahrenheit (°F, F) to Celsius (°C), rounding to the nearest 5°C for practical oven use.

Fraction Handling: Automatically finds and converts text fractions (e.g., 1 1/2 cups, 1/4 oz) into decimals before conversion.

Instruction Linter: Improves readability by automatically inserting blank lines between instruction steps.

Polished GUI:

Clean, multi-screen interface (Main, Options, Help).

Custom font rendering.

Interactive buttons with color-coded hover effects (Primary, Default, Danger).

Robust & Stable:

Strong error handling for missing files (config.json) or read/write errors.

Clean project architecture with a "Separation of Concerns" (SoC) model.

🏗️ Project Architecture
The project is structured with a clean separation of concerns to make it maintainable and scalable:

/Recipe-Linter
│
├── 📜 main.py
│   └── (Entry Point) Initializes Pygame, loads configuration, and starts the UI.
│
├── 🖥️ game.py
│   └── (UI Controller) Manages all UI state, rendering (Pygame), and user input.
│
├── ⚙️ app_logic.py
│   └── (Logic/Action Handler) Handles all file I/O (Tkinter dialogs) and triggers conversions.
│
├── 🔬 accuallcorrection.py
│   └── (Conversion Engine) Contains all the core regex, text-parsing, and unit conversion logic.
│
├── 📄 config.json
│   └── Stores all conversion ratios (e.g., "pounds_to_grams": 453.5).
│
├── 🖼️ font.ttf
│   └── The custom font asset used for rendering all text.
│
├── 📦 requirements.txt
│   └── A list of all Python dependencies (Pygame).
│
└── 📖 README.md
    └── (You are here!)
🚀 How To Run
Clone the repository:

Bash

git clone https://github.com/Vahidino/recept_linter.git
cd recept-linter
Set up a virtual environment (Recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies: The project relies on Pygame, which is listed in requirements.txt.

Bash

pip install -r requirements.txt
Get the font: This project uses a custom font. Please download a .ttf font (e.g., Roboto from Google Fonts) and place it in the root folder, renaming it to font.ttf.

Run the application:

Bash

python main.py