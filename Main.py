import Controller
import End
import pygame
import Start

def main():
    pygame.init()
    start = True
    while start:
        front = Start.Start()
        if front.choice():
            control = Controller.Controller()
            begin = control.start()
            end = End.End(begin)
            if not end.choice():
                start = False
        else:
            end = End.End(0)
            if not end.choice():
                start = False
    end.close()

main()
