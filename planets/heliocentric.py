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

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate the current positions of the planets
    sun_x, sun_y = width // 2, height // 2
    earth_x = sun_x + math.cos(pygame.time.get_ticks() * 0.0005) * earth_distance
    earth_y = sun_y + math.sin(pygame.time.get_ticks() * 0.0005) * earth_distance
    moon_x = earth_x + math.cos(pygame.time.get_ticks() * 0.001) * moon_distance
    moon_y = earth_y + math.sin(pygame.time.get_ticks() * 0.001) * moon_distance
    mercury_x = sun_x + math.cos(pygame.time.get_ticks() * 0.0007) * mercury_distance
    mercury_y = sun_y + math.sin(pygame.time.get_ticks() * 0.0007) * mercury_distance
    venus_x = sun_x + math.cos(pygame.time.get_ticks() * 0.0006) * venus_distance
    venus_y = sun_y + math.sin(pygame.time.get_ticks() * 0.0006) * venus_distance
    mars_x = sun_x + math.cos(pygame.time.get_ticks() * 0.0004) * mars_distance
    mars_y = sun_y + math.sin(pygame.time.get_ticks() * 0.0004) * mars_distance

    # Draw the planets
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), sun_radius)
    pygame.draw.circle(screen, BLUE, (int(earth_x), int(earth_y)), earth_radius)
    pygame.draw.circle(screen, GREEN, (int(mercury_x), int(mercury_y)), mercury_radius)
    pygame.draw.circle(screen, RED, (int(venus_x), int(venus_y)), venus_radius)
    pygame.draw.circle(screen, RED, (int(mars_x), int(mars_y)), mars_radius)
    pygame.draw.circle(screen, WHITE, (int(moon_x), int(moon_y)), moon_radius)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the program
pygame.quit()
