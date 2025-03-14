from fastapi import FastAPI
from pydantic import BaseModel
import wolframalpha

# Wolfram|Alpha API Setup
APP_ID = "Q63VP5-Q77GXKTX2W"  # Replace with your actual App ID
client = wolframalpha.Client(APP_ID)

app = FastAPI()

# ✅ Ensure this model exactly matches the request JSON format
class ExpressionInput(BaseModel):
    expression: str

@app.post("/calculate")
def solve_expression(input: ExpressionInput):
    try:
        res = client.query(input.expression)
        result = next(res.results).text
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
