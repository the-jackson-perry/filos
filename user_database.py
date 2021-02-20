from google.cloud import datastore

datastore_client = datastore.Client.from_service_account_json('service-account.json')

def save(entity):
    datastore_client.put(entity)


def create_user(email, user_id):
    user = get_user_by_id(user_id)
    user['screenName'] = 'defaultScreenName'
    user['email'] = email
    user['id'] = user_id
    user['friends'] = []
    user['conversations'] = {'Filos Team':['We hope you enjoy our project!','Welcome to Filos!']}
    user['color-scheme'] = 'default'
    user['profile_photo'] = '/static/images/default_user.png'
    user['bio'] = 'This is a default bio.'
    save(user)


def user_exists(user_id):
    return get_user_by_id(user_id) is not None
    

def get_user_by_id(user_id):
    key = datastore_client.key('user', user_id)
    return datastore.Entity(key)