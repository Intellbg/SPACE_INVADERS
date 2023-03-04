import pygame

def change_image_on_event(screen, event, old_image_path, new_image_path):
    
    # Load the old and new images
    old_image = pygame.image.load(old_image_path)
    new_image = pygame.image.load(new_image_path)

    # Check for the specified Pygame event
    if event.type == pygame.KEYDOWN:
        # Replace the old image with the new image
        screen.blit(new_image, (0, 0))
        # Update the display
        pygame.display.update()
    else:
        # Display the old image
        screen.blit(old_image, (0, 0))
        # Update the display
        pygame.display.update()