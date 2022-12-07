import pygame
import json
import math


MAP_SIZE_COEFF = 5.14

pygame.init()
screen = pygame.display.set_mode([720, 720]) #pygame window size
screen.fill((255, 255, 255))
running = True


class Background(pygame.sprite.Sprite):
    def __init__(self, image, location, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.rotozoom(self.image, 0, scale)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def distance_between_points(position0, position1):
    #Get distance between 2 mouse position.
    x = abs(position0[0] - position1[0])
    y = abs(position0[1] - position1[1])
    dist_px = math.hypot(x, y)  #distance formula
    dist_cm = dist_px * MAP_SIZE_COEFF  #if we need to convert the distance to real world we multiply px with MAP_SIZE_COEFF 
    return int(dist_cm), int(dist_px)


def angle_btw_adj_lines(position0, position1, positionref):
    #Get angle between two lines respective to 'position reference'
    ax = positionref[0] - position0[0]
    ay = positionref[1] - position0[1]
    bx = positionref[0] - position1[0]
    by = positionref[1] - position1[1]
    # Get dot-product of position0 and position1.
    _dot = (ax * bx) + (ay * by)
    # Get magnitude of position0 and position1.
    _magA = math.sqrt(ax**2 + ay**2)
    _magB = math.sqrt(bx**2 + by**2)
    _rad = math.acos(_dot / (_magA * _magB))
    # Angle in degrees.
    angle = (_rad * 180) / math.pi
    return int(angle)



#Main capturing mouse program.
#Load background image.
bground = Background('Photos/image.png', [0, 0], 1.6)
screen.blit(bground.image, bground.rect)

path_waypoint = []
index = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #getting mouse events
            position = pygame.mouse.get_pos()  #gets the mouse position
            path_waypoint.append(position)
            if index > 0:
                pygame.draw.line(screen, (255, 0, 0), path_waypoint[index-1], position, 2) #drawing a line on screen, red color, combining prev and current index with 2px width
            index += 1
    pygame.display.update()


#Compute the waypoint (distance and angle).
#Append first position reference (dummy)
path_waypoint.insert(0, (path_waypoint[0][0], path_waypoint[0][1] - 10))

path_dist_cm = []
path_dist_px = []
path_angle = []
for index in range(len(path_waypoint)):
    # Skip the first and second index.
    if index > 1:
        dist_cm, dist_px = distance_between_points(path_waypoint[index-1], path_waypoint[index])
        path_dist_cm.append(dist_cm)
        path_dist_px.append(dist_px)

    # Skip the first and last index.
    if index > 0 and index < (len(path_waypoint) - 1):
        angle = angle_btw_adj_lines(path_waypoint[index-1], path_waypoint[index+1], path_waypoint[index])
        path_angle.append(angle)

# Print out the information.
print('path_waypoints: {}'.format(path_waypoint))
print('distance_cm: {}'.format(path_dist_cm))
print('distance_px: {}'.format(path_dist_px))
print('degree_angle: {}'.format(path_angle))

#Save waypoints into JSON file.

waypoints = []
for index in range(len(path_dist_cm)):
    waypoints.append({
        "distance in cm": path_dist_cm[index],
        "distance in px": path_dist_px[index],
        "angle_degree": path_angle[index]
    })

# Save to JSON file.
f = open('waypoint.json', 'w+')
path_waypoint.pop(0)
json.dump({
    "waypoint": waypoints,
    "position": path_waypoint
}, f, indent=4)
f.close()
