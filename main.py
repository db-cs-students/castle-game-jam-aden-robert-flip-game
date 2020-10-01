"""
Title:Flip
Creators:Robert,Aden
Description:u flip gravity
"""
#Game Setup
game.splash("Level 1-1", "Press 'B' to flip gravity!")
info.set_life(3)
level = 0
#Sprite Setup
gary = sprites.create(img("""
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
"""))
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
"""))
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
"""),SpriteKind.player)
#Tilemaps and Levels
if level == 0:
    scene.set_tile_map(img("""
        222222222222222222222.................222222222222
        ....................2.................222222....5.
        ......................................2.........5.
        ................................................5.
        ................................................5.
        ..............................................1111
        ..............................................2222
        ..................................................
        ..................................................
        ..................................................
        ....................222222223332222222............
        11.........................2...2..................
        221111............................................
        222222111..................................1......
        22222222211111111111111............111111112......
        62222222222222222222222444444444444222222222444444
    """))
elif level == 1:
    scene.set_tile_map(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . 1 1 1 1 . . . . . . .
        1 1 1 1 1 1 2 2 2 1 1 1 1 1 1 1
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    """))
elif level == 2:
    pass
else:
    pass
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
    1 d d d d d d b c 1 d d d d b c
    1 d d d d d d b c 1 d d d d b c
    1 d d d d d b b c 1 d d d b b c
    . 1 d d d d b b c . 1 d d b c .
    . 1 d d d d b b c . 1 d d b c .
    . 1 d d d d b c . . 1 d b c . .
    . . 1 d d d b c . . 1 d b c . .
    . . 1 d d b b c . . . 1 b c . .
    . . 1 d d b c . . . . 1 b c . .
    . . . 1 d b c . . . . 1 b c . .
    . . . 1 d b c . . . . . b . . .
    . . . 1 d b c . . . . . b . . .
    . . . . 1 b . . . . . . . . . .
    . . . . 1 b . . . . . . . . . .
    . . . . 1 b . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""),True)
scene.set_tile(4, img("""
    . . . . 1 . . . . . . . . . . .
    . . . 1 1 . . . . . . . 1 . . .
    . . . 1 b . . . . . . 1 d . . .
    . . . 1 b . . . . . . 1 b . . .
    . . . 1 b . . . . . . 1 b . . .
    . . 1 d b c . . . . 1 d b . . .
    . . 1 d b c . . . . 1 d b c . .
    . . 1 d b c . . . . 1 d b c . .
    . 1 d d b c . . . 1 d d b c . .
    . 1 d d b b c . . 1 d d b c . .
    . 1 d d b b c . 1 d d d b b c .
    . 1 d d b b c . 1 d d d b b c .
    1 d d d d b c . 1 d d d b b c .
    1 d d d d b c c d d d d d b b c
    1 d d d d b c c d d d d d b b c
    1 d d d d b c c d d d d d b b c
"""),True)
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
"""),True)
scene.set_tile(6, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
#Forever Commands
def on_forever():
    #Gravity
    global gravity, bpress
    player1.ay = gravity
    scene.camera_follow_sprite(player1)
    if bpress == 0:
        gravity = 250
    else:
        gravity = -250
    if controller.B.is_pressed() and player1.is_hitting_tile(CollisionDirection.BOTTOM):
        bpress = 1
        player1.set_image(img("""
            . . . . . . f b 1 f 1 1 f . . .
            . . . . . . f b 1 f f 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b b b b b f . . .
            . . . . . . f f f f f f f . . .
            . . . . . f b 1 1 1 1 1 1 f . .
            . . . . . f b 1 1 1 1 1 1 f . .
            . . . . . f b 1 1 f 1 f 1 f . .
            . . . . . f b 1 1 f 1 f 1 f . .
            . . . . . f b 1 1 1 1 1 1 f . .
            . . . . . f b b b b b b b f . .
            . . . . . . f f f f f f f . . .
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
    #Enemies
    gary.ay = gravity/2
    if gary.is_hitting_tile(CollisionDirection.TOP) or gary.is_hitting_tile(CollisionDirection.BOTTOM):
        gary.follow(player1, 50)
    else :gary.follow(player1, 0)
    if player1.overlaps_with(gary):
        info.change_life_by(-1)
        player1.set_position(80, 104)
        player1.say("ouch", 1000, 15, 0)
        scene.camera_shake(4)
        gary.set_position(0, 0)
        gary.destroy()
    #Jump
    """
    if controller.A.is_pressed() and gravity > 0 and player1.is_hitting_tile(CollisionDirection.BOTTOM):
        player1.vy = -100
    elif controller.A.is_pressed() and gravity < 0 and player1.is_hitting_tile(CollisionDirection.TOP):
        player1.vy = 100
    """
#Death
def on_hit_tile(sprite):
    player1.set_position(80, 104)
    info.change_life_by(-1)
    scene.camera_shake(4)
    player1.say("ouch", 1000, 15, 0)
scene.on_hit_tile(SpriteKind.player, 3, on_hit_tile)
def on_hit_tile2(sprite):
    player1.set_position(80, 104)
    info.change_life_by(-1)
    scene.camera_shake(4)
    player1.say("ouch", 1000, 15, 0)
scene.on_hit_tile(SpriteKind.player, 4, on_hit_tile)
def on_hit_tile3(sprite):
    level = 1
scene.on_hit_tile(SpriteKind.player, 5, on_hit_tile3)
forever(on_forever)
#Enemies

scene.place_on_random_tile(gary, 6)
#Left, right, up, and down
def on_update():
    if controller.dx() > 0 and gravity < 0:
        player1.set_image(img("""
            . . . . . . f b 1 f 1 1 f . . .
            . . . . . . f b 1 f f 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b 1 1 1 1 f . . .
            . . . . . . f b b b b b f . . .
            . . . . . . f f f f f f f . . .
            . . . . . f b 1 1 1 1 1 1 f . .
            . . . . . f b 1 1 1 1 1 1 f . .
            . . . . . f b 1 1 f 1 f 1 f . .
            . . . . . f b 1 1 f 1 f 1 f . .
            . . . . . f b 1 1 1 1 1 1 f . .
            . . . . . f b b b b b b b f . .
            . . . . . . f f f f f f f . . .
        """))
    elif controller.dx() < 0 and gravity < 0:
        player1.set_image(img("""
            . . . . . . f 1 b f 1 b f . . .
            . . . . . . f 1 f f 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f b b b b b f . . .
            . . . . . . f f f f f f f . . .
            . . . . . f 1 1 1 1 1 1 b f . .
            . . . . . f 1 1 1 1 1 1 b f . .
            . . . . . f 1 f 1 f 1 1 b f . .
            . . . . . f 1 f 1 f 1 1 b f . .
            . . . . . f 1 1 1 1 1 1 b f . .
            . . . . . f b b b b b b b f . .
            . . . . . . f f f f f f f . . .
        """))
    elif controller.dx() > 0:
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
    elif controller.dx() < 0:
        player1.set_image(img("""
            . . . . . . f f f f f f f . . .
            . . . . . f 1 1 1 1 1 1 b f . .
            . . . . . f 1 1 1 1 1 1 b f . .
            . . . . . f 1 f 1 f 1 1 b f . .
            . . . . . f 1 f 1 f 1 1 b f . .
            . . . . . f 1 1 1 1 1 1 b f . .
            . . . . . f b b b b b b b f . .
            . . . . . . f f f f f f f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 1 1 1 b f . . .
            . . . . . . f 1 f f 1 b f . . .
            . . . . . . f 1 b f b b f . . .
        """))
    if controller.A.is_pressed() and player1.is_hitting_tile(CollisionDirection.BOTTOM):
        player1.vy = -100
    if controller.A.is_pressed() and player1.is_hitting_tile(CollisionDirection.TOP):
        player1.vy = 100
game.on_update(on_update)
#Changing levels
