class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return "%s <%s>" % (self.name, self.email)

    def __eq__(self, other):
        return self.email.lower() == other.email.lower()

u1 = User("Гелиозавр", email="RAWR@mail.ru")
u2 = User(name="Орнитишийлар", email="rawr@mail.ru")
print(u1, u2)
print("Это один и тот же пользователь?", u1 == u2)