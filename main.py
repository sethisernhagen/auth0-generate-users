from auth0.v2.management import Auth0
from random import randrange
from pprint import pprint as pp


EMAIL_DOMAIN = ""
DOMAIN = ""
CONNECTION = ""
PASSWORD = ""
TOKEN = ""
NUM_USERS = 20

def create_user(user):
    auth0 = Auth0(
        domain=DOMAIN,
        token=TOKEN,
    )

    auth0_client = Auth0(DOMAIN, TOKEN).users
    auth0_client.create(user)

def main():

    for _ in range(NUM_USERS):
        user = dict(
            connection=CONNECTION,
            email='steve-test{}@{}'.format(
                randrange(0, 1000, 2),
                EMAIL_DOMAIN
            ),
            name='Steve Jones',
            password=PASSWORD
        )

        pp(user)
        create_user(user)

if __name__ == '__main__':
    main()
