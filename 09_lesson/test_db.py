from database import Database

DB_CONNECTION = "Вставить свою строку"
db = Database(DB_CONNECTION)


def test_add_user():
    db.execute_script("clean_test_users")
    email = "testuser@example.com"
    db.execute_script("insert_user", {"email": email, "subject_id": 1})
    rows = db.select_script("select_user_by_email", {"email": email})
    assert len(rows) == 1
    assert rows[0]["user_email"] == email


def test_update_user_subject():
    db.execute_script("clean_test_users")
    email = "updateuser@example.com"
    db.execute_script("insert_user", {"email": email, "subject_id": 1})
    db.execute_script("update_user_subject_by_email", {"email": email, "subject_id": 2})
    rows = db.select_script("select_user_by_email", {"email": email})
    assert rows[0]["subject_id"] == 2


def test_delete_user():
    db.execute_script("clean_test_users")
    email = "deleteuser@example.com"
    db.execute_script("insert_user", {"email": email, "subject_id": 1})
    db.execute_script("delete_user_by_email", {"email": email})
    rows = db.select_script("select_user_by_email", {"email": email})
    assert len(rows) == 0
