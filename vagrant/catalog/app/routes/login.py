import random
import string

from flask import session as login_session
from .. import app


@app.route('/login')
def show_login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in xrange(32))
    login_session['state'] = state
    return "The current session state is %s" % login_session['state']
