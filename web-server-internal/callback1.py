# luisarandas 20-04-2024
import json
import logging

def log_error(error):    
    logger = logging.getLogger('webServerErrors')
    logger.error(str(error))

def onHTTPRequest(webServerDAT, request, response):
    try:
        if 'data' not in request or not request['data']:
            raise ValueError("No data provided in the request")
        data = json.loads(request['data'])
        print("Received request data:", data)
        if 'test_key' not in data:
            raise KeyError("Missing 'test_key' in data")
        if not isinstance(data['test_key'], str):
            raise TypeError("Expected a string for 'test_key'")
        if 'test_key' in data:
            param_value = data['test_key']
            if isinstance(param_value, str):
                response_data = "<b>Received:</b> " + param_value
            else:
                response_data = "<b>Error:</b> Incorrect type for 'test_key'. Expected a string."
                response['statusCode'] = 422  # Unprocessable Entity
                response['statusReason'] = 'Unprocessable Entity'
                response['data'] = response_data
                return response
        else:
            response_data = "<b>Error:</b> Missing or incorrect 'test_key' in request."
            response['statusCode'] = 400  # Bad Request
            response['statusReason'] = 'Bad Request'
            response['data'] = response_data
            return response
        # Success
        response['statusCode'] = 200  # OK
        response['statusReason'] = 'OK'
        response['data'] = response_data

    except json.JSONDecodeError:
        # Handle JSON parsing errors
        response['statusCode'] = 400
        response['statusReason'] = 'Bad Request'
        response['data'] = "<b>Error:</b> Invalid JSON format."
    except KeyError as ke:
        # Handle missing keys
        response['statusCode'] = 400
        response['statusReason'] = 'Bad Request'
        response['data'] = f"<b>Error:</b> Key error - {str(ke)}"
    except TypeError as te:
        # Handle type errors
        response['statusCode'] = 400
        response['statusReason'] = 'Bad Request'
        response['data'] = f"<b>Error:</b> Type error - {str(te)}"
    except Exception as e:
        # Generic error handling
        response['statusCode'] = 500
        response['statusReason'] = 'Internal Server Error'
        response['data'] = f'<b>Server Error:</b> Unexpected error - {str(e)}'
        log_error(e)
    return response



def onWebSocketOpen(webServerDAT, client, uri):
	return

def onWebSocketClose(webServerDAT, client):
	return

def onWebSocketReceiveText(webServerDAT, client, data):
	webServerDAT.webSocketSendText(client, data)
	return

def onWebSocketReceiveBinary(webServerDAT, client, data):
	webServerDAT.webSocketSendBinary(client, data)
	return

def onWebSocketReceivePing(webServerDAT, client, data):
	webServerDAT.webSocketSendPong(client, data=data);
	return

def onWebSocketReceivePong(webServerDAT, client, data):
	return

def onServerStart(webServerDAT):
	return

def onServerStop(webServerDAT):
	return


