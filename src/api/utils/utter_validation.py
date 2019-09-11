from .validators import validate_name
from api.models import Utter

def validate_alternatives(data):
    alternatives = data['alternatives']

    if len(alternatives) < 1:
        return False

    for alternative_list in alternatives:
        for alternative in alternative_list:
            if not isinstance(alternative, str):
                return False

    return True

def validate_multiple_alternatives(data):
    return isinstance(data['multiple_alternatives'], bool)

def validate_utter(data, project_id):
    error_messages = []

    missing_keys = not ('name' in data and 
            'multiple_alternatives' in data and 
            'alternatives' in data)

    if missing_keys:
        error_messages.append('Missing keys')
        return False, error_messages

    if not validate_name(data, Utter, project_id):
        error_messages.append('Name should contain no special characters other than underscore')

    if not validate_multiple_alternatives(data):
        error_messages.append('Multiple alternatives field should be a boolean')

    if not validate_alternatives(data):
        error_messages.append('Invalid alternatives')

    return (len(error_messages) < 1), error_messages