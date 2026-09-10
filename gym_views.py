from mysql import connector
from datetime import datetime

class DbConnect:
    def get_connection(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Ansa@123",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None
class GymMemberManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.connection = super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from member where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from member"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="insert into member(name,place,mobile_no,plan,fee,joined_date) values(%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("New member added successfully...")
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from member where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            print(records)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from member where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            if records!=None:
                query="delete from member where id=%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Member deleted successfully...")
            else:
                print("Member not found...")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update member set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Gym details updated successfully")

            else:
                print("Member not found...")

        except Exception as e:
            print(e)

# connection_instance=DbConnect()
# print(connection_instance.get_connection())
#
# member_instance=GymMemberManager()
# # member_instance.post(name="Manu",place="Kollam",mobile_no="8709674939",plan="4 months",fee=4000,joined_date=datetime.today())
# member_instance.get()
# print("------------")
# member_instance.retrieve(id=1)
# member_instance.delete(id=1)
# member_instance.get()
# print("---------------------")
# member_instance.put(2,place="Thrissur")
# member_instance.get()