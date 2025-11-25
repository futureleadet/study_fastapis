from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from services.db import get_db_connection
from psycopg2.extras import DictCursor

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

#http://localhost:8000/todos/
@router.get("/{todo_id}")
def get_todo(request: Request, todo_id: str):
    conn = get_db_connection()
    with conn.cursor(cursor_factory=DictCursor) as cursor:
    # with conn.cursor() as cursor:
        cursor.execute("""SELECT id , item
                        FROM todo
                        WHERE id = '65a8a77d-415d-47eb-b149-e0589100e2ac';""")
        todo = cursor.fetchone()
    conn.close()
    
    context = {
        "reqeuet" : request,
        "todo" : todo
    }

    return templates.TemplateResponse("todos/merged_todo.html", context)

#http://localhost:8000/todos/
@router.get("/")
def get_todos_html(request: Request):
    conn = get_db_connection()
    with conn.cursor(cursor_factory=DictCursor) as cursor:
    # with conn.cursor() as cursor:
        cursor.execute("""SELECT id , item
                        FROM todo;""")
        todos = cursor.fetchall()
    conn.close()

    context = {
        "request" : request,
        "todos" : todos
    }

    return templates.TemplateResponse("todos/merged_todo.html", context)