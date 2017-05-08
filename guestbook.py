import shelve
import string
import  sys
reload(sys)
sys.setdefaultencoding('utf-8')
DATA_FILE = 'guestbook.dat'


def save_data( comment, create_at):
    """
    save data from form submitted
    """
    database = shelve.open(DATA_FILE)
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']
    greeting_list.insert(
        0, { 'comment': comment, 'create_at': create_at})
    database['greeting_list'] = greeting_list
    database.close()

def load_data():
    """
    load saved data
    """
    database = shelve.open(DATA_FILE)
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list
def delete_data(msgindex):
    database = shelve.open(DATA_FILE)
    greeting_list = database.get('greeting_list', [])
    print type(greeting_list)
    print greeting_list
    msgindex=string.atoi(msgindex,10)
    del greeting_list[msgindex]
    database['greeting_list'] = greeting_list
    database.close()