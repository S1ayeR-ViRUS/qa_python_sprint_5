import faker


class UserTestDataGenerator:

    def generator():
        fake = faker.Faker()
        user_test_data = {'name': fake.name(), 'email': fake.email(), 'password': fake.password()}
        return user_test_data
