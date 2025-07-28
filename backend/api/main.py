from fastapi import FastAPI
from fastapi import (Depends, Response, HTTPException, APIRouter)
from fastapi.middleware.cors import CORSMiddleware
from .config import VITE_FRONT_URL

from api.logs_management.resources import router as logs_management_router

app = FastAPI()

app.include_router(logs_management_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[VITE_FRONT_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
