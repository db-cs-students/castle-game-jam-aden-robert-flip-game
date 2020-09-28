/** 
Title:Flip
Creators:Robert,Aden
Description:u flip gravity

 */
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
    . . . . . . f b 1 f f 1 f . . .
    . . . . . . f b b f b b f . . .
    . . . . . . f f f f f f f . . .
`)
tiles.setTilemap(tilemap`level`)
