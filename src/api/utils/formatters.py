import json

def request_to_dict(request):
    str_args = request.body.decode('utf-8')
    json_data = json.loads(str_args)
    return json_data
