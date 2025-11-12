import sys
import pygame
import app_logic # <<< Importing our new logic file
import os # Still needed for font loading path

# --- Pygame Setup ---
pygame.init() 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Recipe Converter") # <<< English

# --- Font Handling ---
# Attempts to load a custom font, falls back to default if not found.
FONT_REGULAR_PATH = None
try:
    font_file = os.path.join(os.path.dirname(__file__), "font.ttf")
    pygame.font.Font(font_file, 32) # Test-load
    FONT_REGULAR_PATH = font_file
    print(f"Successfully loaded custom font: {font_file}")
except Exception as e:
    print(f"Warning: Could not load 'font.ttf'. Using default Pygame font. Error: {e}")
    FONT_REGULAR_PATH = None # Will cause fallback in display_text

# --- Color Palette ---
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_GRAY = (235, 235, 235)
COLOR_GRAY = (220, 220, 220)
COLOR_GRAY_HOVER = (200, 200, 200)
COLOR_PRIMARY = (0, 123, 255)
COLOR_PRIMARY_HOVER = (0, 100, 230)
COLOR_DANGER = (220, 53, 69)
COLOR_DANGER_HOVER = (200, 40, 55)
COLOR_TEXT_GRAY = (100, 100, 100)
COLOR_TEXT_DARK = (33, 37, 41)


def show_main_menu(config_data):
    """
    The main UI loop. Manages screen state and user input.
    """
    
    # 'current_screen' is our state manager: "main", "help", "options"
    current_screen = "main" 
    
    # Button rects, reset each frame
    convert_button_rect = None
    options_button_rect = None
    help_button_rect = None
    exit_button_rect = None
    back_button_rect = None
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
            
        # --- Event Loop ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # --- Mouse Click Handler ---
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    click_pos = event.pos
                    
                    if current_screen == "main":
                        if convert_button_rect and convert_button_rect.collidepoint(click_pos):
                            # --- Call the logic from app_logic ---
                            file_path = app_logic.open_file_dialog()
                            if file_path:
                                app_logic.convert_file(file_path, config_data)
                        elif options_button_rect and options_button_rect.collidepoint(click_pos):
                            current_screen = "options"
                        elif help_button_rect and help_button_rect.collidepoint(click_pos):
                            current_screen = "help"
                        elif exit_button_rect and exit_button_rect.collidepoint(click_pos):
                            pygame.quit()
                            sys.exit()
                            
                    elif current_screen == "help" or current_screen == "options":
                        # Both sub-screens have a back button
                        if back_button_rect and back_button_rect.collidepoint(click_pos):
                            current_screen = "main"

            # --- Keyboard Shortcut Handler ---
            elif event.type == pygame.KEYDOWN:
                if current_screen == "main":
                    if event.key == pygame.K_1:
                        file_path = app_logic.open_file_dialog()
                        if file_path:
                            app_logic.convert_file(file_path, config_data)
                    elif event.key == pygame.K_2:
                        current_screen = "options"
                    elif event.key == pygame.K_3:
                        current_screen = "help"
                    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_4:
                        pygame.quit()
                        sys.exit()
                
                elif (current_screen == "help" or current_screen == "options") and \
                     (event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE):
                    current_screen = "main"
        
        # --- Drawing Section ---
        window.fill(COLOR_LIGHT_GRAY) 
        
        is_hovering = False
        convert_button_rect, options_button_rect, help_button_rect, exit_button_rect, back_button_rect = None, None, None, None, None

        if current_screen == "main":
            display_text("Recipe Converter", (WINDOW_WIDTH // 2, 100), size=50, color=COLOR_TEXT_DARK)
            convert_button_rect = display_button("Convert", (WINDOW_WIDTH // 2, 220), mouse_pos, button_type="primary")
            options_button_rect = display_button("Options", (WINDOW_WIDTH // 2, 290), mouse_pos, button_type="default")
            help_button_rect = display_button("Help", (WINDOW_WIDTH // 2, 360), mouse_pos, button_type="default")
            exit_button_rect = display_button("Exit", (WINDOW_WIDTH // 2, 430), mouse_pos, button_type="danger")
            
            buttons = [convert_button_rect, options_button_rect, help_button_rect, exit_button_rect]
            if any(btn and btn.collidepoint(mouse_pos) for btn in buttons):
                is_hovering = True
        
        elif current_screen == "help":
            back_button_rect = display_help(mouse_pos)
            if back_button_rect and back_button_rect.collidepoint(mouse_pos):
                is_hovering = True
                
        elif current_screen == "options":
            back_button_rect = display_options(config_data, mouse_pos)
            if back_button_rect and back_button_rect.collidepoint(mouse_pos):
                is_hovering = True
        
        # Set cursor based on hover state
        if is_hovering:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()

# --- Sub-Screen Drawing Functions ---

def display_options(config_data, mouse_pos):
    """Draws the 'Options' screen, showing config values."""
    display_text("Settings", (WINDOW_WIDTH // 2, 70), size=40, color=COLOR_TEXT_DARK, align="center")
    display_text("These values are loaded from config.json", (WINDOW_WIDTH // 2, 110), size=20, color=COLOR_TEXT_GRAY, align="center")

    y_pos = 180
    key_x = WINDOW_WIDTH // 2 - 250
    val_x = WINDOW_WIDTH // 2 + 50 

    for key, val in config_data.items():
        display_text(f"{key}:", (key_x, y_pos), size=24, color=COLOR_TEXT_DARK, align="midleft")
        display_text(str(val), (val_x, y_pos), size=24, color=COLOR_BLACK, align="midleft")
        y_pos += 40

    back_rect = display_button("Back (Esc)", (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 60), mouse_pos, size=24, button_type="default")
    return back_rect

def display_help(mouse_pos):
    """Draws the 'Help' screen."""
    display_text("Help", (WINDOW_WIDTH // 2, 70), size=40, color=COLOR_TEXT_DARK, align="center")

    help_text = [
        "This program converts .txt files containing American recipes.",
        "",
        "1. Click 'Convert' to begin.",
        "2. Select the .txt file you want to convert.",
        "3. Choose where to save the new, converted file.",
        "",
        "The program will translate:",
        "  - Measurements (cups, oz, lb, etc.) to (dl, g, Kg, etc.)",
        "  - Temperatures (°F) to (°C)"
    ]
    y_pos = 150
    for line in help_text:
        display_text(line, (100, y_pos), size=22, color=COLOR_TEXT_DARK, align="midleft")
        y_pos += 35

    back_rect = display_button("Back (Esc)", (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 60), mouse_pos, size=24, button_type="default")
    return back_rect

# --- UI Component Drawing Functions ---

def display_button(text, position, mouse_pos, button_type="default", size=28, width=300, height=50):
    """
    Draws a button with text and a hover effect.
    Returns the button's pygame.Rect.
    """
    button_rect = pygame.Rect(0, 0, width, height)
    button_rect.center = position
    
    is_hovering = button_rect.collidepoint(mouse_pos)
    
    # Determine colors based on type and hover state
    if button_type == "primary":
        bg_color = COLOR_PRIMARY_HOVER if is_hovering else COLOR_PRIMARY
        text_color = COLOR_WHITE
    elif button_type == "danger":
        bg_color = COLOR_DANGER_HOVER if is_hovering else COLOR_DANGER
        text_color = COLOR_WHITE
    else: # "default"
        bg_color = COLOR_GRAY_HOVER if is_hovering else COLOR_GRAY
        text_color = COLOR_TEXT_DARK

    pygame.draw.rect(window, bg_color, button_rect, border_radius=8)
    
    # Draw text on top of button
    display_text(text, position, size=size, color=text_color, align="center")
    
    return button_rect

def display_text(text, position, size=32, color=(0, 0, 0), align="center"):
    """
    Renders text onto the screen with the custom font.
    Falls back to default font if custom font failed to load.
    """
    try:
        font = pygame.font.Font(FONT_REGULAR_PATH, size)
    except:
        # Fallback if FONT_REGULAR_PATH is None or font is corrupt
        font = pygame.font.Font(None, size + 4) # Default font is smaller
        
    text_surface = font.render(text, True, color)
    
    if align == "center":
        text_rect = text_surface.get_rect(center=position)
    elif align == "midleft":
        text_rect = text_surface.get_rect(midleft=position)
    elif align == "midright":
        text_rect = text_surface.get_rect(midright=position)
    else:
        text_rect = text_surface.get_rect(center=position)
        
    window.blit(text_surface, text_rect)
    return text_rect