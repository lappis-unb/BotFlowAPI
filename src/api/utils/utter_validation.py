from .validators import validate_name

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

def validate_utter(data):
    missing_keys = not ('name' in data and 
            'multiple_alternatives' in data and 
            'alternatives' in data)

    if missing_keys:
        return False

    if not validate_name(data):
        return False

    if not validate_multiple_alternatives(data):
        return False

    if not validate_alternatives(data):
        return False

    return True