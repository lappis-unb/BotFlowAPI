from .validators import validate_name

def validate_samples(data):
    samples = data['samples']

    if len(samples) < 1:
        return False

    for string in samples:
        if not isinstance(string, str):
            return False

    return True

def validate_intent(data):
    missing_keys = not ('name' in data and 'samples' in data)

    if missing_keys:
        return False

    if not validate_name(data):
        return False

    if not validate_samples(data):
        return False

    return True

    