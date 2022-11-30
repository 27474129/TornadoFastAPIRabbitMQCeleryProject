from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"success": True, "message": "Hello from FastAPI"}
