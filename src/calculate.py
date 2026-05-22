from fastapi import FastAPI

app = FastAPI()

def add_func(a: float, b: float) -> float:
    return a + b

# -------------------------

@app.get("/")
def home():
    return {"status": "Online", "message": "這是簡易計算機 API"}

@app.get("/add")
def calculate_add(a: float, b: float):
    # 呼叫輔助函數進行計算
    result = add_func(a, b)
    # 回傳 JSON 格式的計算結果
    return {"operation": "addition", "a": a, "b": b, "result": result}