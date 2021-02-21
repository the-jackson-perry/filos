from google.cloud import datastore

datastore_client = datastore.Client.from_service_account_json('service-account.json')

def add_post(screen_name, message, time):
    post = {'screen_name': screen_name, 'message': message, 'time': time}
    msg_board = get_board()
    msg_board['message_list'].append(post)
    print(msg_board)
    datastore_client.put(msg_board)


def get_board():
    key = datastore_client.key('messages', 'm')
    board = datastore.Entity(key)
    print(board)
    try:
        board['message_list']
    except:
        board['message_list'] = [{'screen_name': 'Filos Team', 'message': 'Welcome to Filos!', 'time': '2:20pm 2020-02-20'}]

    print(board)
    return board


def get_posts():
    return get_board()['message_list']