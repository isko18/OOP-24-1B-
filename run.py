from main import User, UserService

user = UserService()

# user_service = User(name='Isko', email='isko@gmail.com', age=20)
# user.add_user(user_service)

# find = user.find_user_by_email('isko@gmail.com')
# if find:
#     print(f"Пользователь найден: {find.name}, {find.email}, {find.age}")

delete = user.delete_user_by_email('isko@gmail.com')