MOCK_USERS = [{'email': 'test', 'salt': 'euIMf6MxxN8zN0YBh1yObEkVZfE=', 'hashed': '3ee4a0792c815a22a828642527bed5498f8e22ee134feb8c13882843af636c8747bcfce01e033e293994c11f4f3bdb89907233fb509961129000c92fe9a254af'}]

MOCK_TABLES = [{'_id': '1', 'number': '1', 'owner': 'test', 'url': 'mockurl'}]

class MockDBHelper:
    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get('email') == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({'email': email, 'salt': salt, 'hashed': hashed})

    def add_table(self, number, owner):
        newtable = {'_id': number, 'number': number, 'owner': owner}
        MOCK_TABLES.append(newtable)
        return newtable.get('_id')

    def update_table(self, _id, url):
        for table in MOCK_TABLES:
            if table.get('_id') == _id:
                table['url'] = url
                break

    def get_tables(self, owner):
        return MOCK_TABLES

    def delete_table(self, _id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get('_id') == _id:
                del MOCK_TABLES[i]
                break

