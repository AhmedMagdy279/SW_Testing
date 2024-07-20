from faker import Faker

test_data = Faker()


def user_pay_load():
    body = {
        "id": test_data.random_number(digits=6),
        "username": test_data.user_name(),
        "firstName": test_data.first_name(),
        "lastName": test_data.last_name(),
        "email": test_data.email(),
        "password": test_data.password(length=10),
        "phone": test_data.phone_number(),
        "userStatus": test_data.random_number(2)
    }
    return body
