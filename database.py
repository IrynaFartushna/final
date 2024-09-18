import json
from person import Person

class Database:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search(self, query):
        return [person for person in self.people if person.matches(query)]

    def save_to_file(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump([{
                    'first_name': p.first_name,
                    'last_name': p.last_name,
                    'patronymic': p.patronymic,
                    'birth_date': p.birth_date.strftime('%d.%m.%Y') if p.birth_date else None,
                    'death_date': p.death_date.strftime('%d.%m.%Y') if p.death_date else None,
                    'gender': p.gender
                } for p in self.people], file, ensure_ascii=False, indent=4)  # Додано indent=4
            print("Дані збережено у файл:", filename)
        except Exception as e:
            print("Помилка при збереженні:", e)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.people = [Person(**item) for item in data]
            print("Дані завантажено з файлу:", filename)
        except Exception as e:
            print("Помилка при завантаженні:", e)

