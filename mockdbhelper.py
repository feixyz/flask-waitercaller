import datetime

MOCK_USERS = [{'email': 'test@123.com', 'salt': 'euIMf6MxxN8zN0YBh1yObEkVZfE=', 'hashed': '3ee4a0792c815a22a828642527bed5498f8e22ee134feb8c13882843af636c8747bcfce01e033e293994c11f4f3bdb89907233fb509961129000c92fe9a254af'}]

MOCK_TABLES = [{'_id': '1', 'number': '1', 'owner': 'test', 'url': 'mockurl'}]

MOCK_REQUESTS = [{'_id': '1', 'table_number': '1', 'table_id': '1', 'time': datetime.datetime.now()}]

class MockDBHelper:
    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get('email') == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({'email': email, 'salt': salt, 'hashed': hashed})

    def add_table(self, number, owner):
        newtable = {'_id': str(number), 'number': number, 'owner': owner}
        MOCK_TABLES.append(newtable)
        return newtable.get('_id')

    def update_table(self, table_id, url):
        for table in MOCK_TABLES:
            if table.get('_id') == table_id:
                table['url'] = url
                break

    def get_tables(self, owner):
        return MOCK_TABLES

    def get_table(self, table_id):
        for table in MOCK_TABLES:
            if table.get("_id") == table_id:
                return table

    def delete_table(self, table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get('_id') == table_id:
                del MOCK_TABLES[i]
                break

    def add_request(self, table_id, time):
        table = self.get_table(table_id)
        MOCK_REQUESTS.append({"_id": table_id, "owner": table["owner"], "table_number": table["number"], "table_id": table_id, "time": time})
        return True

    def get_requests(self, owner_id):
        return MOCK_REQUESTS

    def delete_request(self, request_id):
        for i, req in enumerate(MOCK_REQUESTS):
            if req['_id'] == request_id:
                del MOCK_REQUESTS[i]
                break