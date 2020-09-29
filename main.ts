/** 
Title:Flip
Creators:Robert,Aden
Description:u flip gravity

 */
info.setLife(3)
info.startCountdown(500)
let bpress = 0
let gravity = 0
let player1 = sprites.create(img`
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
`, SpriteKind.Player)
scene.setTileMap(img`
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
`)
scene.setTile(1, img`
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
`, true)
scene.setTile(2, img`
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
`, true)
scene.setTile(3, img`
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
`)
scene.setTile(4, img`
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
`)
scene.setTile(5, img`
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
`)
forever(function on_forever() {
    
    player1.vy = gravity
    scene.cameraFollowSprite(player1)
    if (bpress == 0) {
        gravity = 210
    } else {
        gravity = -210
    }
    
    if (controller.B.isPressed() && player1.isHittingTile(CollisionDirection.Bottom)) {
        bpress = 1
        player1.setImage(img`
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
        `)
    }
    
    if (controller.B.isPressed() && player1.isHittingTile(CollisionDirection.Top)) {
        bpress = 0
        player1.setImage(img`
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
        `)
        
    }
    
    if (controller.right.isPressed()) {
        player1.vx = 100
    } else if (controller.left.isPressed()) {
        player1.vx = -100
    } else {
        player1.vx = 0
    }
    
})
