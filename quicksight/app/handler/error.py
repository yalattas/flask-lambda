import os, requests

def general_error(error_trace):
    lambda_name = os.environ.get('AWS_LAMBDA_FUNCTION_NAME')
    lambda_region = os.environ.get('AWS_REGION')
    # Just to inform Yasser about the failure --------------------------------
    message = {
        "chat_id": 380689111,
        "text": f"lambda: {lambda_name} failed in region: {lambda_region}"
    }
    exception = {
        "chat_id": 380689111,
        "text": f"Exception is {str(error_trace)}"
    }
    print(str(error_trace))
    response = requests.get(url="https://api.telegram.org/bot<BOT_ID>/sendMessage", data=message)
    response = requests.get(url="https://api.telegram.org/bot<BOT_ID>/sendMessage", data=exception)
    # Just to inform Yasser about the failure --------------------------------