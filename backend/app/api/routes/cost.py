from fastapi import APIRouter
from app.services.cost_calculator import CostCalculator
router=APIRouter(); calc=CostCalculator()
@router.post('/estimate-project')
def estimate_project(payload:dict): return {'estimated_cost_usd':calc.estimate_text_cost(payload.get('input_tokens',0),payload.get('output_tokens',0),payload.get('input_per_m',1),payload.get('output_per_m',1))}
@router.post('/estimate-task')
def estimate_task(payload:dict): return estimate_project(payload)
@router.get('/books/{book_id}/usage')
def usage(book_id:int): return {'book_id':book_id,'items':[]}
