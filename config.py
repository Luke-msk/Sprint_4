from faker import Faker
import random
import string

faker = Faker("ru_RU")

name = faker.first_name_female()
surname = faker.last_name_female()
address = 'Москва, ' + faker.street_name()
phone_number = random.randint(11111111111, 99999999999)
comment = ''.join(random.choice(string.ascii_lowercase) for i in range(20))