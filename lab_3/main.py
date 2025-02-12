from game.game import start_new_game
from game.bot import bot_test_game

if __name__ == "__main__":
    while True:
        print("\nДобро пожаловать в 'Морской бой'")
        print("1. Новая игра")
        print("2. Тестовая игра ботов")
        print("3. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            start_new_game()
        elif choice == "2":
            bot_test_game()
        elif choice == "3":
            print("Выход из игры. До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")
