import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')
django.setup()


from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
import sys
import pprint


def get_session_dictionary(session_index):
    session_store = SessionStore()
    sessions = Session.objects.all()
    session_dictionary = session_store.decode(sessions[int(session_index)].session_data)
    return session_dictionary


if __name__ == '__main__':
    if len(sys.argv) > 1:
        session_index = sys.argv[1]
        session_dictionary = get_session_dictionary(session_index)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(session_dictionary)
