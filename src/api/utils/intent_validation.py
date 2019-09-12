from .validators import validate_name
from api.models import Intent

def validate_samples(data):
    samples = data['samples']

    if len(samples) < 1:
        return False

    for string in samples:
        if not isinstance(string, str):
            return False

    return True

def validate_intent(data, project_id):
    error_messages = []

    missing_keys = not ('name' in data and 'samples' in data)

    if missing_keys:
        error_messages.append('Missing keys')
        return False, error_messages

    if not validate_name(data, Intent, project_id):
        error_messages.append('Name should contain no special characters other than underscore')

    if not validate_samples(data):
        error_messages.append('There should be at least one sample')

    return (len(error_messages) < 1), error_messages

    