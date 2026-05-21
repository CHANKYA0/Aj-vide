from fastapi import APIRouter
router=APIRouter()
@router.get('/users')
def users(): return {'items':[]}
@router.get('/projects')
def projects(): return {'items':[]}
@router.get('/usage')
def usage(): return {'items':[]}
@router.get('/model-costs')
def model_costs(): return {'items':[]}
@router.patch('/settings')
def settings(payload:dict): return {'saved':True,'settings':payload}
