from src import app, app_config

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, **app_config)
