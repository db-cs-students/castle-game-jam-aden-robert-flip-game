"""
Title:Flip
Creators:Robert,Aden
Description:u flip gravity
"""
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
    22222222222222222222..........
    ......22222222222222..........
    ..............................
    ..............................
    ..............................
    ..............................
    ..............................
    ..1111111.....................
    ..............................
    ..............................
    ..............................
    ..............................
    ..............................
    .........111111111111.........
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
    if controller.B.is_pressed() and player1.is_hitting_tile(CollisionDirection.TOP):
        bpress = 0
        pass
    if controller.right.is_pressed():
        player1.vx = 100
    elif controller.left.is_pressed():
        player1.vx = -100
    else:
        player1.vx = 0

forever(on_forever)
