from fastapi import FastAPI
import os
from datetime import datetime, timezone

import app.routes.api as api

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "dev")
GIT_SHA = os.getenv("GIT_SHA")  # optional for deployments


@app.get("/health", tags=["system"])
async def health_check():
    """
    Basic health-check endpoint for uptime monitoring.
    Returns service status and current server time in UTC.
    """
    return {
        "status": "ok",
        "service": "pippy-debugger-backend",
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/info", tags=["system"])
async def app_info():
    """
    Returns metadata about the backend.
    Useful for debugging deployments and verifying versions.
    """
    info = {
        "app": "pippy-debugger-backend",
        "version": APP_VERSION,
    }

    if GIT_SHA:
        info["git_sha"] = GIT_SHA

    return info


app.include_router(api.router)
