class Person:
    def __init__(self, full_name, city, birth_date, position, experience):
        self.full_name = full_name
        self.city = city
        self.birth_date = birth_date
        self.position = position
        self.experience = experience

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'city': self.city,
            'birth_date': self.birth_date,
            'position': self.position,
            'experience': self.experience
        }