import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rectangle Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Rectangle properties
rect_width = 50
rect_height = 50
rect_x = (window_width - rect_width) // 2
rect_y = window_height - rect_height - 10  # Position the rectangle above the floor

# Floor properties
floor_height = 10
floor_width = window_width * 2  # Extend the floor width for scrolling effect

# Jump properties
initial_jump_velocity = -10  # Initial upward velocity when jumping
gravity = 0.5  # Gravity value

jumping = False  # Flag to track if the rectangle is currently jumping
jump_velocity = initial_jump_velocity  # Current vertical velocity

# Camera properties
camera_x = 0  # Camera position

# Game over flag and font
game_over = False
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move rectangle left or right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rect_x -= 5
    if keys[pygame.K_d]:
        rect_x += 5

    # Jump when SPACE is pressed
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        jump_velocity = initial_jump_velocity

    # Apply gravity
    if jumping:
        rect_y += jump_velocity
        jump_velocity += gravity

        # Check if the rectangle has landed
        if rect_y >= window_height - rect_height - floor_height:
            rect_y = window_height - rect_height - floor_height
            jump_velocity = initial_jump_velocity
            jumping = False

    # Check if the rectangle has reached the end of the floor
    if rect_x + rect_width >= floor_width:
        game_over = True

    # Adjust the camera position based on the rectangle's position
    if rect_x - camera_x < 200:
        camera_x -= 5
    elif rect_x - camera_x > window_width - 200:
        camera_x += 5

    # Draw the scene with camera offset
    window.fill(black)  # Clear the window

    pygame.draw.rect(window, white, (rect_x - camera_x, rect_y, rect_width, rect_height))  # Draw the rectangle
    pygame.draw.rect(window, white, (0 - camera_x, window_height - floor_height, floor_width, floor_height))  # Draw the floor

    if game_over:
        text = font.render("Game Over", True, red)
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        window.blit(text, text_rect)

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Quit the game
pygame.quit()
