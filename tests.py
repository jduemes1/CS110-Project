def main():

#Screen width: 25
#Screen length: 25

    
    #creates ship
    print("##Testing Ship Model##")
    test_ship = ship.Ship()

    print("==Standard Right Input Test==")
    test_ship.moveRight(5)
    assert test_ship.getCoordinates() == (5,0)

    print("==Zero Right Input Test==")
    test_ship.moveRight(0)
    assert test_ship.getCoordinates() == (5,0)

    print("==Negative Right Input Test==")
    test_ship.moveRight(-1)
    assert test_ship.getCoordinates() == (4,0)
    
    print("==Standard Left Input Test==")
    test_ship.moveLeft(5)
    assert test_ship.getCoordinates() == (5,0)

    print("==Zero Left Input Test==")
    test_ship.moveLeft(0)
    assert test_ship.getCoordinates() == (5,0)

    print("==Negative Left Input Test==")
    test_ship.moveLeft(-1)
    assert test_ship.getCoordinates() == (4,0)

    print("## Testing Bullet Model##")
    test_bullet = bullet.Bullet()

    print("==Standard Spacebar Input Test==")
    test_bullet.Shoot(25)
    assert test_bullet.getCoordinates() == (25, 0)

    print("==Zero Spacebar Input Test==")
    test_bullet.Shoot(0)
    assert test_bullet.getCoordinates() == (0, 0)

    print("##Standard Enemy Input Test##")
    test_enemy = enemy.Enemy()

    print("==Standard Enemy Input Test==")
    test_enemy.Spawn(10, 25)
    assert test_enemy.getCoordinates() == (10, 25)

    print("==Standard Contact Input Test==")
    test_bullet.Hit(10, 10)
    assert test_enemy.getCoordinates() == (10, 10)

    print("==Max Contact Input Test==")
    test_bullet.Hit(0, 25)
    assert test_bullet.getCoordinates() == (0, 25)

main()
    

    
    
        
    
