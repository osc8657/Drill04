from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 800
#노트북이 작아서 위쪽 경계가 잘려서 안보여서 캔버스 높이를 낮췄습니다.
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running

    global dirx, diry

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dirx, diry = 0, 0

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 108, 130, 108, 130, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if 0 <= x <= TUK_WIDTH:
        x += dirx * 50
    else:
        x -= dirx * 50

    if 0 <= y <= TUK_HEIGHT:
        y += diry * 50
    else:
        y -= diry * 50
    delay(0.05)

close_canvas()


