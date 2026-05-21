from fastapi import APIRouter
router = APIRouter()
@router.post('/signup')
def signup(payload: dict): return {'message':'signed up','user':payload}
@router.post('/login')
def login(payload: dict): return {'token':'dev-token','user':payload.get('email')}
@router.post('/logout')
def logout(): return {'message':'logged out'}
@router.get('/me')
def me(): return {'id':1,'email':'demo@example.com'}
