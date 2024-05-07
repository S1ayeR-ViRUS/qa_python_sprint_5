import faker


class AuthTestData:
    AUTH_EMAIL = 'artem_ruzin_8_123@yandex.ru'
    AUTH_PASSWORD = 'P@ssw0rd'
    INCORRECT_PASSWORD = '1234'


class UserTestDataGenerator:

    def generator():
        fake = faker.Faker()
        user_test_data = {'name': fake.name(), 'email': fake.email(), 'password': fake.password()}
        return user_test_data