from auth0.v2.management import Auth0
from random import randrange
from pprint import pprint as pp


AUTH0_DOMAIN = ""
AUTH0_CONNECTION = ""
AUTH0_TOKEN = ""
TEST_EMAIL_DOMAIN = ""
TEST_PASSWORD = ""
TEST_NUM_USERS = 20

def create_user(user):
    auth0 = Auth0(
        domain=AUTH0_DOMAIN,
        token=AUTH0_TOKEN,
    )

    auth0_client = Auth0(AUTH0_DOMAIN, AUTH0_TOKEN).users
    auth0_client.create(user)

def main():

    for _ in range(TEST_NUM_USERS):
        user = dict(
            connection=AUTH0_CONNECTION,
            email='steve-test{}@{}'.format(
                randrange(0, 1000, 2),
                TEST_EMAIL_DOMAIN
            ),
            name='Steve Jones',
            password=TEST_PASSWORD
        )

        pp(user)
        create_user(user)

if __name__ == '__main__':
    main()
