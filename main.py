from fastapi import FastAPI
app = FastAPI()

from routes.todos import router as todos_router
app.include_router(todos_router, prefix="/todos")

from fastapi.templating import Jinja2Templates
from fastapi import Request
templates = Jinja2Templates(directory="templates/")

# http://localhost:8000/
# @app.get("/")
#  async def root():
#      return {"message": "Hello, World!"}
# async def main_page_html(request: Request):
#     return templates.TemplateResponse("main_page.html"
#                                       , {"request": request})

# # http://localhost:8000/main_html
# @app.get("/main_html")
# async def main_html(request: Request):
#     return templates.TemplateResponse("main.html"
#                                       , {"request": request})

# http://localhost:8000/main_html_context
# @app.get("/main_html_context")
# async def main_html_context(request: Request):
#         # 템플릿에 전달할 데이터
#     context = {
#         "request": request,
#         "title": "FastAPI + Jinja Example",
#         "items": ["Apple", "Banana", "Cherry"],
#         "user": {"name": "Sanghun", "age": 33}
#     }
#     return templates.TemplateResponse("main_context.html"
#                                       , context)
# #http://Localhost:8000/users/list
# @app.get("/users/list")
# async def users_list(request : Request):

#     users = [
#     {"name": "Alice", "age": 25, "city": "Seoul"},
#     {"name": "Bob", "age": 30, "city": "Busan"},
#     {"name": "Charlie", "age": 28, "city": "Daegu"}
#     ]
#     context = {
#         "request" : request
#         , "user_list": users
#     }
#     return templates.TemplateResponse("users/list.html"
#                                       , context)

# http://Localhost:8000/board/detail_json
# @app.get("/board/detail_json")
# async def products_list(request : Request):

#     # 이 데이터 블록을 다시 입력하거나, 들여쓰기 및 쉼표를 확인합니다.
#     products = [
#         {"name": "Laptop", "price": 1200, "tags": ["electronics", "office"]},
#         {"name": "Smartphone", "price": 800, "tags": ["mobile", "electronics"]},
#         {"name": "Keyboard", "price": 100, "tags": ["accessories"]}
#     ]
    
#     context = {
#         "request" : request,
#         "products_list": products
#     }
#     return templates.TemplateResponse("products/list.html", context)


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
# http://localhost:8000/board/detail_json?title=Third%20Post&content=This%20is%20the%20third%20post
@app.get("/board/detail_json")
async def board_details_json(request : Request):
    #    request.method
    #    request.query_params
    params = dict(request.query_params)
    # return{"title": "Third Post", "content": "This is the third post."}
    return {"title": params["title"], "content": params["content"]}

# http://localhost:8000/board/detail_post_json?title=Third%20Post&content=This%20is%20the%20third%20post
@app.post("/board/detail_post_json")
async def board_details_post_post_json(request : Request):
    #    request.method
    #    request.query_params
    params = dict(await request.form())
    
    # return{"title": "Third Post", "content": "This is the third post."}
    return {"title": params["title"], "content": params["content"]}

# http://localhost:8000/board/detail_html/{detail_id}
@app.get("/board/detail_html/{detail_id}")
async def main_html(request: Request, detail_id):
    return templates.TemplateResponse("boards/detail.html"
                                      , {"request": request})

# http://localhost:8000/board/{detail_id}detail.html
@app.get("/board/detail_html")
async def main_html(request: Request):
    return templates.TemplateResponse("boards/detail.html"
                                      , {"request": request})

# 정적 파일 설정
from fastapi.staticfiles import StaticFiles

app.mount("/images", StaticFiles(directory="resources/images"))
app.mount("/css", StaticFiles(directory="resources/css"))

pass
