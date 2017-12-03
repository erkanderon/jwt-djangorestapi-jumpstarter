


def responseSerializer(code, data):

    if code != 200:
        status = "Error"
        if 'detail' in data:
            message = data['detail']
        elif 'error' in data:
            message = data['error'][0]
        else:
            message = data
        data = None
        return {"status": status, "code": code, "message": message, "data": data}

    if data == []:
        data = "No Data Found"
    else:
        data = [data]

    status = "OK"
    message = "Operation Succesful"
    return {"status": status, "code": code, "message": message, "data": data}
