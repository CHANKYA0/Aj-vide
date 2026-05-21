from app.services.ai_router import AIRouter
from app.services.cost_calculator import CostCalculator

def test_router():
    out = AIRouter().text('writer_model','hi')
    assert out

def test_cost():
    c = CostCalculator().estimate_text_cost(1_000_000,1_000_000,1,1)
    assert c == 2
