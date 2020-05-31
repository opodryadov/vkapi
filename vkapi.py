import requests
vk_token = 'e0685bbc592aa4142f9988669619e412ba30258616cd7650fc378e2c3512f37725504cdf9b0df7cc3e4b4'


class User:

    def __init__(self, id_user, token):
        self.token = token
        self.id_user = id_user

    def get_params(self):
        return {
            'access_token': self.token,
            'v': 5.107,
            'method': 'friends.getMutual',
            'source_uid': user1.id_user,
            'target_uid': user2.id_user,
        }

    def __and__(self, other):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params
        )
        return response.json()['response']


user1 = User('23225635', vk_token)
user2 = User('66121880', vk_token)
mutual_user_list = user1 & user2
for item in mutual_user_list:
    print('https://vk.com/id' + str(item))