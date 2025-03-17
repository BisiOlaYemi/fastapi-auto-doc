from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os
import traceback
import logging
from app.api.router import api_router
from app.core.config import settings

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Set logging level for all loggers
for name in logging.root.manager.loggerDict:
    logging.getLogger(name).setLevel(logging.DEBUG)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Automatically generate documentation for Python projects",
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Add error handling middleware
@app.middleware("http")
async def error_handling_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        logger.error(traceback.format_exc())
        return JSONResponse(
            status_code=500,
            content={"detail": str(e), "traceback": traceback.format_exc()}
        )

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    """Redirect to documentation dashboard."""
    return {"message": "Welcome to FastAPI Auto-Documentation", 
            "docs": f"{settings.API_V1_STR}/documentation/dashboard"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)