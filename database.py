from google.cloud import datastore

datastore_client = datastore.Client.from_service_account_json('service-account.json')


def save(entity):
    datastore_client.put(entity)


def add_post(message):
    key = datastore_client.key('message', 'm')
    board = datastore_client.get(key)
    board['msg'].append(message)
    datastore_client.put(board)



def get_board():
    key = datastore_client.key('message', 'm')
    board = datastore_client.get(key)
    print(board)
    return board['msg']



def get_posts():
    return get_board()