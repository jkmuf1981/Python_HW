from sqlalchemy import create_engine, text


class Database:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.scripts = {
            "clean_test_users": "DELETE FROM users WHERE user_email LIKE '%@example.com'",
            "insert_user": "INSERT INTO users(user_email, subject_id) VALUES (:email, :subject_id)",
            "select_user_by_email": "SELECT * FROM users WHERE user_email = :email",
            "update_user_subject_by_email": "UPDATE users SET subject_id = :subject_id WHERE user_email = :email",
            "delete_user_by_email": "DELETE FROM users WHERE user_email = :email"
        }

    def execute_script(self, script_name, params=None):
        if params is None:
            params = {}
        with self.engine.connect() as conn:
            with conn.begin():
                return conn.execute(text(self.scripts[script_name]), params)

    def select_script(self, script_name, params=None):
        if params is None:
            params = {}
        with self.engine.connect() as conn:
            result = conn.execute(text(self.scripts[script_name]), params)
            return result.mappings().all()
