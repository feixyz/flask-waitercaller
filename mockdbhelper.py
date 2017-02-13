MOCK_USERS = [{'email': 'test', 'salt': 'euIMf6MxxN8zN0YBh1yObEkVZfE=', 'hashed': '3ee4a0792c815a22a828642527bed5498f8e22ee134feb8c13882843af636c8747bcfce01e033e293994c11f4f3bdb89907233fb509961129000c92fe9a254af'}]

class MockDBHelper:
    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get('email') == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({'email': email, 'salt': salt, 'hashed': hashed})