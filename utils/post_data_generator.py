from faker import Faker

fake = Faker()


def generate_post_payload() -> dict:
    return {
        "title": generate_post_title(),
        "body": generate_post_body(),
        "userId": generate_post_user_id(),
    }

def generate_post_title() -> str:
    return fake.sentence(nb_words=3)

def generate_post_body() -> str:
    return fake.paragraph(nb_sentences=4)

def generate_post_user_id() -> int:
    return fake.random_int(min=1, max=10)