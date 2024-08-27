import os
from fastapi.security import APIKeyHeader
from fastapi import HTTPException, Security, status


ASSISTANT_API_KEY = os.getenv("ASSISTANT_API_KEY")
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header == ASSISTANT_API_KEY:
        return api_key_header

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API Key."
    )
