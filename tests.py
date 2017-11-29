def main():

#Screen width: 1000
#Screen length: 700        

class test_startscreen:
    #creates the starting screen of the game
    print("##Testing Startup Screen Model##")
    print("PLAY")
    assert test_startupscreen == PLAY

class test_playerscreen:
    #creates the screen for choosing your character
    print("##Testing Startup Screen 2 Model##"
    print("CHOOSE YOUR CHARACTER")
    assert test_startupscreen2 == CHARACTER

class test_controller:
    #sets up the controller for the game
    print("Testing Controller##")
    if test_controller = K_LEFT
          test_controller.move(-1)
    if test_controller = K_RIGHT
          test_controller.move(1)
    
class test_ship:           
    #creates ship
    print("##Testing Ship Model##")
    test_ship = ship.Ship()
    test_ship.getCoordinates(0, 0)

    #tests right inputs
    print("==Standard Right Input Test==")
    test_ship.moveRight(5)
    assert test_ship.getCoordinates() == (5,0)
    
    #when player does not move right
    print("==Zero Right Input Test==")
    test_ship.moveRight(0)
    assert test_ship.getCoordinates() == (5,0)
    
    #when player moves left
    print("==Negative Right Input Test==")
    test_ship.moveRight(-1)
    assert test_ship.getCoordinates() == (4,0)
    
    #tests left inputs
    print("==Standard Left Input Test==")
    test_ship.moveLeft(5)
    assert test_ship.getCoordinates() == (5,0)

    #when player does not move left
    print("==Zero Left Input Test==")
    test_ship.moveLeft(0)
    assert test_ship.getCoordinates() == (5,0)

    #when player moves right
    print("==Negative Left Input Test==")
    test_ship.moveLeft(-1)
    assert test_ship.getCoordinates() == (4,0)

class test_bullet:
    #creates bullet
    print("## Testing Bullet Model##")
    test_bullet = bullet.Bullet()

    #tests spacebar input
    print("==Standard Spacebar Input Test==")
    test_bullet.Shoot(1)
    assert test_bullet.shot() == 1

    #when player does not shoot
    print("==Zero Spacebar Input Test==")
    test_bullet.Shoot(0)
    assert test_bullet.shot() == 0

class test_score:
    #creates scoreboard
    print("## Testing ScoreBoard Model##")
    test_scoreboard = score.Board()

    #tests scoreboard input
    print("==Scoreboard Input Test==")
    test_scoreboard.increase(1)
    assert test_scoreboard.increase() += 1

class test_alien:    
    #creates alien
    print("##Standard Alien Input Test##")
    test_alien = alien.Alien()

    #tests enemy spawning
    print("==Standard Enemy Input Test==")
    test_alien.Spawn(400, 700)
    assert test_alien.getCoordinates() == (400, 700)

    #tests alien movement (moves straight down along the screen)
    print("==Standard Enemy Movement Test==")
    test_alien.Spawn(500, 700)
    test_alien.movement(500, 699)
    assert test_alien.getCoordinates() == (500, 699)
    
    #tests when bullet hits alien
    print("==Standard Contact Input Test==")
    test_bullet.Hit(10, 10)
    test_bullet.kill()
    assert test_alien.getCoordinates() == (10, 10)
    assert test_alien.delete()
    assert test_bullet.delete()
    assert test_scoreboard.increase() += 1
    
    #tests when bullet goes off the top of the screen
    print("==Max Contact Input Test==")
    test_bullet.Hit(0, 700)
    assert test_bullet.getCoordinates() == (0, 700)
    assert test_bullet.delete()

main():
    

    
    
        
    

