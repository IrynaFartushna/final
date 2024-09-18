from database import Database
from person import Person


def main():
    db = Database()

    while True:
        print("\nМеню:")
        print("1. Додати нову людину")
        print("2. Шукати людей")
        print("3. Зберегти у файл")
        print("4. Завантажити з файлу")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            first_name = input("Ім'я: ")
            last_name = input("Прізвище (не обов'язково): ")
            patronymic = input("По-батькові (не обов'язково): ")
            birth_date = input("Дата народження (дд.мм.рррр, дд мм рррр, мм/дд/рррр, дд-мм-рррр): ")
            death_date = input("Дата смерті (не обов'язково): ")
            gender = input("Стать (m/f): ").lower()
            person = Person(first_name, last_name, patronymic, birth_date, death_date, gender)
            db.add_person(person)
            print("Людину додано!")

        elif choice == '2':
            query = input("Введіть для пошуку (ім'я, прізвище або по-батькові): ")
            results = db.search(query)
            if results:
                for person in results:
                    print(person)
            else:
                print("Не знайдено записів.")

        elif choice == '3':
            filename = input("Введіть назву файлу для збереження: ")
            db.save_to_file(filename)
            print("Дані збережено!")

        elif choice == '4':
            filename = input("Введіть назву файлу для завантаження: ")
            db.load_from_file(filename)
            print("Дані завантажено!")

        elif choice == '5':
            print("Вихід з програми.")
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
