from fastapi import HTTPException
from fastapi import Request

def get_state_repos(request: Request):
    repos = request.state.repos
    if repos is None:
        raise HTTPException(status_code=500, detail="Repositories not initialized in request state")
    return repos

def get_state_stores(request: Request):
    stores = request.state.stores
    if stores is None:
        raise HTTPException(status_code=500, detail="Stores repositories not initialized in request state")
    return stores