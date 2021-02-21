from google.cloud import datastore

datastore_client = datastore.Client.from_service_account_json('service-account.json')

def save(entity):
    datastore_client.put(entity)


def addPost(screen_name, message, time):
    post = {'screen_name': screen_name, 'message': message, 'time': time}
    msg_board = get_board()
    msg_board.insert(0, post)
    save(msg_board)


def get_board():
    key = datastore_client.key('messages', 'm')
    board = datastore.Entity(key)
    if board is None:
        board['message_list'] = [{'screen_name': 'Filos Team', 'message': 'Welcome to Felos!', 'time': '2:20pm 2020-02-20'}]
    return board


def get_posts():
    return get_board()['message_list']