from fastapi import FastAPI
app = FastAPI()

# http://localhost:8000/html
@app.get("/html")
async def root():
    return {"message": "Hello, World!"}
async def root_html():
    html_content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <div>My name is Otter!</div>
        </body>
        </html>
        '''
    return html_content
pass