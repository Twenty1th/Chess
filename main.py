from game import Game

if __name__ == '__main__':
    game = Game()
    try:
        game.start()
    except KeyboardInterrupt:
        print("\nThank you for a game!")






