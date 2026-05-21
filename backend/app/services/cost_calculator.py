class CostCalculator:
    def estimate_text_cost(self, input_tokens: int, output_tokens: int, input_per_m: float, output_per_m: float) -> float:
        return (input_tokens / 1_000_000 * input_per_m) + (output_tokens / 1_000_000 * output_per_m)
