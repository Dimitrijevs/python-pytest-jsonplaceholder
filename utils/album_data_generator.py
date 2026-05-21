from faker import Faker

fake = Faker()


def generate_album_payload() -> dict:
    return {
        "title": generate_album_title(),
        "userId": generate_album_user_id(),
    }

def generate_album_title() -> str:
    return fake.sentence(nb_words=3)

def generate_album_user_id() -> int:
    return fake.random_int(min=1, max=10)