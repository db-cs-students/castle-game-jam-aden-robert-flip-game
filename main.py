"""
Title:Flip
Creators:Robert,Aden
Description:u flip gravity
"""
info.set_life(3)
info.start_countdown(500)
bpress = 0
gravity = 0
player1 = sprites.create(img("""
    . . . . . . f f f f f f f . . .
    . . . . . f b 1 1 1 1 1 1 f . .
    . . . . . f b 1 1 1 1 1 1 f . .
    . . . . . f b 1 1 f 1 f 1 f . .
    . . . . . f b 1 1 f 1 f 1 f . .
    . . . . . f b 1 1 1 1 1 1 f . .
    . . . . . f b b b b b b b f . .
    . . . . . . f f f f f f f . . .
    . . . . . . f b 1 1 1 1 f . . .
    . . . . . . f b 1 1 1 1 f . . .
    . . . . . . f b 1 1 1 1 f . . .
    . . . . . . f b 1 1 1 1 f . . .
    . . . . . . f b 1 1 1 1 f . . .
    . . . . . . f b 1 1 1 1 f . . .
    . . . . . . f b 1 f f 1 f . . .
    . . . . . . f b b f b 1 f . . .
"""),
    SpriteKind.player)
    
scene.set_tile_map(img("""
    222222222222222222222222222222
    ......222222222222223333......
    ..............................
    ..............................
    ............................5.
    ............................5.
    ............................5.
    ..1111111...................5.
    ............................5.
    ............................5.
    ............................5.
    ............................5.
    ............................5.
    .........111111111111444....5.
    111111111222222222222111111111
    222222222222222222222222222222
"""))
scene.set_tile(1, img("""
    7 7 7 7 7 7 7 7 7 7 5 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 5 7 5 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 5 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    e 7 7 7 7 7 7 7 7 7 7 7 7 7 7 e
    e e e e e 7 7 7 e e e 7 7 e e e
    e e e e e e e e e e e e e e e e
    e e c e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e c e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e c e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
"""),True)
scene.set_tile(2, img("""
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e c e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e c e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e c e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e c e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
"""),True)
scene.set_tile(3, img("""
    1 d d d d d d d d 1 d d d d d d
    1 d d d d d d d d 1 d d d d d .
    1 d d d d d d d d 1 d d d d d .
    . 1 d d d d d d d . 1 d d d d .
    . 1 d d d d d d d . 1 d d d d .
    . 1 d d d d d d . . 1 d d d . .
    . . 1 d d d d d . . 1 d d d . .
    . . 1 d d d d d . . . 1 d d . .
    . . 1 d d d d . . . . 1 d d . .
    . . . 1 d d d . . . . 1 d d . .
    . . . 1 d d d . . . . . 1 . . .
    . . . 1 d d d . . . . . . . . .
    . . . . 1 d . . . . . . . . . .
    . . . . 1 d . . . . . . . . . .
    . . . . 1 d . . . . . . . . . .
    . . . . . 1 . . . . . . . . . .
"""))
scene.set_tile(4, img("""
    . . . . 1 . . . . . . . . . . .
    . . . 1 1 . . . . . . . 1 . . .
    . . . 1 d . . . . . . 1 d . . .
    . . . 1 d . . . . . . 1 d . . .
    . . . 1 d . . . . . . 1 d . . .
    . . 1 d d d . . . . 1 d d . . .
    . . 1 d d d . . . . 1 d d d . .
    . . 1 d d d . . . . 1 d d d . .
    . 1 d d d d . . . 1 d d d d . .
    . 1 d d d d d . . 1 d d d d . .
    . 1 d d d d d . 1 d d d d d . .
    . 1 d d d d d . 1 d d d d d d .
    1 d d d d d d . 1 d d d d d d .
    1 d d d d d d 1 d d d d d d d .
    1 d d d d d d 1 d d d d d d d .
    1 d d d d d d 1 d d d d d d d d
"""))
scene.set_tile(5, img("""
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
    . 5 5 5 . . . . . . . . . . . .
"""))
def on_forever():
    global gravity, bpress
    player1.vy = gravity
    scene.camera_follow_sprite(player1)
    if bpress == 0:
        gravity = 210
    else:
        gravity = -210
    if controller.B.is_pressed() and player1.is_hitting_tile(CollisionDirection.BOTTOM):
        bpress = 1
        player1.set_image(img("""
        . . . . . . . . f b b f b 1 f .
        . . . . . . . . f b 1 f f 1 f .
        . . . . . . . . f b 1 1 1 1 f .
        . . . . . . . . f b 1 1 1 1 f .
        . . . . . . . . f b 1 1 1 1 f .
        . . . . . . . . f b 1 1 1 1 f .
        . . . . . . . . f b 1 1 1 1 f .
        . . . . . . . . f b 1 1 1 1 f .
        . . . . . . . . f f f f f f f .
        . . . . . . . f b b b b b b b f
        . . . . . . . f b 1 1 1 1 1 1 f
        . . . . . . . f b 1 1 f 1 f 1 f
        . . . . . . . f b 1 1 f 1 f 1 f
        . . . . . . . f b 1 1 1 1 1 1 f
        . . . . . . . f b 1 1 1 1 1 1 f
        . . . . . . . . f f f f f f f .
        """))
    if controller.B.is_pressed() and player1.is_hitting_tile(CollisionDirection.TOP):
        bpress = 0
        player1.set_image(img("""
        . . . . . . f f f f f f f . . .
        . . . . . f b 1 1 1 1 1 1 f . .
        . . . . . f b 1 1 1 1 1 1 f . .
        . . . . . f b 1 1 f 1 f 1 f . .
        . . . . . f b 1 1 f 1 f 1 f . .
        . . . . . f b 1 1 1 1 1 1 f . .
        . . . . . f b b b b b b b f . .
        . . . . . . f f f f f f f . . .
        . . . . . . f b 1 1 1 1 f . . .
        . . . . . . f b 1 1 1 1 f . . .
        . . . . . . f b 1 1 1 1 f . . .
        . . . . . . f b 1 1 1 1 f . . .
        . . . . . . f b 1 1 1 1 f . . .
        . . . . . . f b 1 1 1 1 f . . .
        . . . . . . f b 1 f f 1 f . . .
        . . . . . . f b b f b 1 f . . .
        """))
        pass
    if controller.right.is_pressed():
        player1.vx = 100
    elif controller.left.is_pressed():
        player1.vx = -100
    else:
        player1.vx = 0

forever(on_forever)
#Enemies
