import azure.functions as func
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="calculator")
def calculator(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Extracts data from incoming HTTP POST JSON payload (just like the slides)
        req_body = req.get_json()
        num1 = int(req_body.get('num1', 0))
        num2 = int(req_body.get('num2', 0))
        
        # Core Algorithm: Calculate the sum
        total = num1 + num2
        
        # Clean JSON Output Response
        return func.HttpResponse(
            json.dumps({"Sum": total}),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": "Invalid input payload"}),
            mimetype="application/json",
            status_code=400
        )
