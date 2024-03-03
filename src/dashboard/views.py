from django.db import connection
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Function untuk execute query
def execute_query(query, values=None):
    with connection.cursor() as cursor:
        cursor.execute(query, values)
        row = dictfetchall(cursor)
    return row

def insert_tasks(id, task_name):
    with connection.cursor() as cursor:
        cursor.execute("""
INSERT INTO 
    tasks 
VALUES 
(%s, %s, %s) 
RETURNING *
                       """, [id, task_name, False])
        row = cursor.fetchall()
    return row

def update_task(id, task_name, status):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE tasks SET name=%s, status=%s WHERE id=%s RETURNING *", [task_name, status, id])
        row = cursor.fetchall()
    return row

def read_task():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, status FROM tasks ORDER BY ID ASC")
        row = dictfetchall(cursor)
    return row

def delete_task(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE from tasks where id = %s", [id])
    return read_task()

def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# Create your views here.
@login_required
def index(request):
    # Insert value ke DB
    # result = execute_query("INSERT INTO tasks VALUES (%s, %s, %s) RETURNING *", [3, "Contoh 3", False])
    # result = update_task(1, "Task Nomor satu", True)
    result = execute_query("SELECT id, name, status FROM tasks")
    # result = delete_task(1)
    print(result)

    context = {
        "tasks": result
    }

    return render(request, "dashboard/index.html", context)

def delete(request):
    render(request, "dashboard/delete.html")

def update(request):
    render(request, "dashboard/update.html")