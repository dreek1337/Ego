from src import app
from src.presentation.api.config import APIConfig

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, **APIConfig().dict())

