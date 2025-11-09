# test_students.py
import pytest
from datetime import datetime
from models import Student

@pytest.mark.create
def test_add_student(db_session):
    """Тест на добавление студента"""
    student = Student(first_name="Иван", last_name="Иванов")
    db_session.add(student)
    db_session.commit()
    added_student = db_session.query(Student).filter_by(id=student.id).one()
    assert added_student.first_name == "Иван"
    assert added_student.last_name == "Иванов"

@pytest.mark.update
def test_update_student(db_session):
    """Тест на изменение данных студента"""
    student = Student(first_name="Иван", last_name="Иванов")
    db_session.add(student)
    db_session.commit()
    student.first_name = "Александр"
    db_session.commit()
    updated_student = db_session.query(Student).filter_by(id=student.id).one()
    assert updated_student.first_name == "Александр"

@pytest.mark.delete
def test_soft_delete_student(db_session):
    """Тест на мягкое удаление студента"""
    student = Student(first_name="Иван", last_name="Иванов")
    db_session.add(student)
    db_session.commit()
    student.deleted_at = datetime.now()
    db_session.commit()
    deleted_student = db_session.query(Student).filter_by(id=student.id).one()
    assert deleted_student.deleted_at is not None