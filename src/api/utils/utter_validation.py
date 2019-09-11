def validate_utter(data):
    return ('name' in data and 
            'multiple_alternatives' in data and 
            'alternatives' in data)