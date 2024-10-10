from fastapi import FastAPI

app=FastAPI()

@app.get("/api_endpoint")
async def first_api():
    return {"message":"This is the first API endpoint"}