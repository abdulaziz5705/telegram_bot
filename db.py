import psycopg2 as psql
from dotenv import load_dotenv
load_dotenv()
import os
class Database:
    @staticmethod
    async def connect(query, query_type):
        db = psql.connect(
            database=os.getenv("database"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )
        cursor = db.cursor()
        data = ["insert", "delete"]
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == "insert":
                return "inserted successfully"
        else:
            return cursor.fetchall()

    @staticmethod
    async def check_user_id(user_id: int):
        query = f"SELECT * FROM bot_users WHERE user_id = {user_id}"
        check_user = await Database.connect(query, query_type="select")
        if len(check_user) == 1:
            print(">>>>>>>>>>>", check_user)
            return True
        return False
