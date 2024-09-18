from datetime import datetime


class Person:
    def __init__(self, first_name, last_name=None, patronymic=None, birth_date=None, death_date=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date) if death_date else None
        self.gender = gender

    def parse_date(self, date_str):
        if date_str:
            for fmt in ("%d.%m.%Y", "%d %m %Y", "%m/%d/%Y", "%d-%m-%Y", "%Y-%m-%d"):
                try:
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    continue
        return None

    def age(self):
        if self.death_date:
            return (self.death_date - self.birth_date).days // 365
        return (datetime.now() - self.birth_date).days // 365

    def __str__(self):
        death_info = f", помер: {self.death_date.strftime('%d.%m.%Y')}" if self.death_date else ""
        return f"{self.first_name} {self.last_name or ''} {self.patronymic or ''} {self.age()} років, " \
               f"{'чоловік' if self.gender == 'm' else 'жінка'}. Народився {self.birth_date.strftime('%d.%m.%Y')}{death_info}."
