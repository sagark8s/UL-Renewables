import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", port=8560, host="0.0.0.0", reload=False, workers=4)
