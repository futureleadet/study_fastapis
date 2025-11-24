from fastapi import FastAPI
app = FastAPI()

# # http://localhost:8000/html
# @app.get("/html")
# async def root_html():
#     html_content = '''
#         <!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>Otter</title>
#         </head>
#         <body>
#             <div>My name is Otter!</div>
#         </body>
#         </html>
#         '''
#     return html_content

from fastapi.templating import Jinja2Templates
from fastapi import Request
templates = Jinja2Templates(directory="templates/")

# http://localhost:8000/
@app.get("/")
# async def root():
#     return {"message": "Hello, World!"}
async def main_page_html(request: Request):
    return templates.TemplateResponse("main_page.html"
                                      , {"request": request})

# # http://localhost:8000/main_html
# @app.get("/main_html")
# async def main_html(request: Request):
#     return templates.TemplateResponse("main.html"
#                                       , {"request": request})

# http://localhost:8000/main_html_context
@app.get("/main_html_context")
async def main_html_context(request: Request):
        # 템플릿에 전달할 데이터
    context = {
        "request": request,
        "title": "FastAPI + Jinja Example",
        "items": ["Apple", "Banana", "Cherry"],
        "user": {"name": "Sanghun", "age": 33}
    }
    return templates.TemplateResponse("main_context.html"
                                      , context)
#http://Localhost:8000/users/list
@app.get("/users/list")
async def users_list(request : Request):

    users = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 28, "city": "Daegu"}
    ]
    context = {
        "request" : request
        , "user_list": users
    }
    return templates.TemplateResponse("users/list.html"
                                      , context)




# # http://localhost:8000/main_page.html
# @app.get("/main_page.html")
# async def main_page_html(request: Request):
#     return templates.TemplateResponse("main_page.html"
#                                       , {"request": request})

# http://localhost:8000/restaurant_info.html
# @app.get("/restaurant_info.html")
# async def restaurant_info_html(request: Request):
#     return templates.TemplateResponse("restaurant_info.html"
#                                       , {"request": request})

# # http://localhost:8000/performance_info.html
# @app.get("/performance_info.html")
# async def performance_info_html(request: Request):
#     return templates.TemplateResponse("performance_info.html"
#                                       , {"request": request})

# # http://localhost:8000/popup_info.html
# @app.get("/popup_info.html")
# async def popup_info_html(request: Request):
#     return templates.TemplateResponse("popup_info.html"
#                                       , {"request": request})

# 정적 파일 설정
from fastapi.staticfiles import StaticFiles

app.mount("/images", StaticFiles(directory="resources/images"))
app.mount("/css", StaticFiles(directory="resources/css"))

pass
