import requests
vk_token = '0af2d01ff90e1041bc135127d25aa6199e4c7ae4fe9baa719d025719ad6b799cdcb1284c1e33a9a6f8dbe'


class User:

    def __init__(self, id_user, token):
        self.token = token
        self.id_user = id_user

    def __str__(self):
        return f'https://vk.com/id{self.id_user}'

    def __and__(self, other):
        users = []
        user_1_id = self.id_user
        user_2_id = other.id_user
        params = self.get_mutual(user_1_id, user_2_id)
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params
        )
        for user_id in response.json()['response']:
            new_user = User(user_id, vk_token)
            print(new_user)
            users.append(new_user)
        return users

    def get_mutual(self, usr1, usr2):
        return {
            'access_token': self.token,
            'v': 5.107,
            'method': 'friends.getMutual',
            'source_uid': usr1,
            'target_uid': usr2,
        }


user1 = User('23225635', vk_token)
user2 = User('66121880', vk_token)
mutual_user_list = user1 & user2