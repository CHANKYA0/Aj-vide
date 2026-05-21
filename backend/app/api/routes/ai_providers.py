from fastapi import APIRouter
router=APIRouter()
PROVIDERS=[]
@router.get('')
def list_providers(): return {'items':PROVIDERS}
@router.post('')
def create_provider(payload:dict): PROVIDERS.append(payload); return payload
@router.patch('/{provider_id}')
def patch_provider(provider_id:int,payload:dict): return {'provider_id':provider_id,'changes':payload}
@router.post('/test')
def test_provider(payload:dict): return {'ok':True,'payload':payload}
