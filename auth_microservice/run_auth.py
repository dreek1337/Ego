from src_auth import (
    app,
    site_config,
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, **site_config)
