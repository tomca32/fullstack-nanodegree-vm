import random
import string


def generate_csrf_token():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in xrange(32))
