import json

def readUsers():
    user_db = open('users.json','r')
    user_data = user_db.read()
    user_data_list = json.loads(user_data)
    return user_data_list


class User:
    def __init__(self,first_name,last_name,user_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
    def insert(self):
        # creating json data
        user_data = {
            'first_name':self.first_name,
            'last_name':self.last_name,
            'user_name':self.user_name,
            'password':self.password
        }
       
        # reading from file

        user_db = open('users.json','r')
        db_data=user_db.read()
        db_data_list = json.loads(db_data)
        db_data_list.append(user_data)
        user_db.close()

        # append to file
        user_db = open('users.json','w')
        json.dump(db_data_list,user_db)
        user_db.close()


    def delete(self):
        # reading all users 
        users= readUsers()
        #   filter user with user name
        def filter_user(user):
            if user['user_name'] == self.user_name:
                return False
            else:
                return True

        filtered = filter(filter_user,users)
        filtered=list(filtered)

        # append to file
        user_db = open('users.json','w')
        json.dump(filtered,user_db)
        user_db.close()
       
        


r = User('robert','dev','docsploit','12345')
r.delete()

# f = User('muhammed','faris','faris404','54321')
# f.delete()
