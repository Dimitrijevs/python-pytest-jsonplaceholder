from faker import Faker

fake = Faker()


def generate_user_payload() -> dict:
    return {
        "name": generate_user_name(),
        "username": generate_user_username(),
        "email": generate_user_email(),
        "phone": generate_user_phone(),
        "website": generate_user_website(),
        "address": generate_user_address(),
        "company": generate_user_company(),
    }

def generate_user_name() -> str:
    return fake.name()

def generate_user_username() -> str:
    return fake.user_name()

def generate_user_email() -> str:
    return fake.email()

def generate_user_phone() -> str:
    return fake.phone_number()

def generate_user_website() -> str:
    return fake.domain_name()

def generate_user_address() -> dict:
    return {
        "street": fake.street_name(),
        "suite": fake.secondary_address(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "geo": {
            "lat": str(fake.latitude()),
            "lng": str(fake.longitude())
        }
    }

def generate_user_company() -> dict:
    return {
        "name": fake.company(),
        "catchPhrase": fake.catch_phrase(),
        "bs": fake.bs()
    }