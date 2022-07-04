# from cgi import print_exception
# from turtle import title
import permissions

class Category:
    def __init__(self, title):
        self.title = title

    def ___str__(self):
        return self.title

class Product:
    def __init__(self, title, price, description, quantity):
        self.title = title
        self.price = price
        self.desc = description
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} [{self.quantity}] - ${self.price}\n{self.desc[:20]}"

class Comment:
    def __init__(self, user, product, body):
        permissions.login_required(user)
        from datetime import datetime
        self.user = user 
        self.product = product
        self.body = body
        self.created_at = datetime.now()


    def __str__(self):
        return f'{self.user.email} [{self.created_at}] - {self.body}'


class User:
    def __init__(self, email, name, sex):
        self.email = email
        self.name = name 
        self.sex = sex
        self.__password = None
        self.is_authenticated = False
        print("успешно создан юзер  {self.email}")

    def register(self, password, password_confirm):
        if password != password_confirm:
            raise Exception("Пароли не совпадают")
        self.__password = password
        print("успешно зарегистрировался юзер  {self.email}")

    def login(self, password,):
        if self.__password != password:
            raise Exception("Пароль не верный")
        self.is_authenticated = True
        print("успешно залогинился юзер  {self.email}")

    def logout(self):
        permissions.login_required(self)
        self.is_authenticated = False
        print(f"успешно вышел юзер {self.email}")

    def __str__(self):
        return self.email






# user1 = User("hello@gmail.com", "hello", "f")
# user1.Register("123456789", "123456789")
# # print(user1.__password) = password