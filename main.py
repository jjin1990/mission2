from quiz_game import QuizGame


game = QuizGame()
try:
    game.run()
except (KeyboardInterrupt, EOFError):
    print("\n프로그램을 종료합니다")
    game.save()