from api.models import Intent

def validate_intent(data):
    return 'name' in data and 'samples' in data