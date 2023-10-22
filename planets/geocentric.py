import math
import pygame
from constants import *

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Heliocentric Planet Movements")

# Run the simulation
running = True
clock = pygame.time.Clock()
list = []

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate the current positions of the planets
    earth_x, earth_y = width // 2, height // 2
    epicycle_x = earth_x + math.cos(pygame.time.get_ticks() * 0.0007) * mercury_distance
    epicycle_y = earth_y + math.sin(pygame.time.get_ticks() * 0.0007) * mercury_distance
    mercury_x = epicycle_x + math.cos(pygame.time.get_ticks() * 0.0020) * moon_distance
    mercury_y = epicycle_y + math.sin(pygame.time.get_ticks() * 0.0020) * moon_distance

    # Draw the planets
    pygame.draw.circle(screen, BLUE, (int(earth_x), int(earth_y)), earth_radius)
    pygame.draw.circle(screen, WHITE, (int(earth_x), int(earth_y)), mercury_distance, width=1)
    list.append((int(mercury_x), int(mercury_y)))
    for element in list:
        pygame.draw.circle(screen, GREEN, element, mercury_radius//5)
    

    pygame.draw.circle(screen, GREEN, (int(mercury_x), int(mercury_y)), mercury_radius)
    pygame.draw.circle(screen, RED, (int(epicycle_x), int(epicycle_y)), moon_distance, width=1)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the program
pygame.quit()
