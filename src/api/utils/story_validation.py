from api.models import Intent, Utter

def intent_exists(id):
    return len(Intent.objects.filter(id=id)) > 0

def utter_exists(id):
    return len(Utter.objects.filter(id=id)) > 0

def validate_content_keys(content):
    return 'id' in content and 'type' in content

def validate_content(content_array):
    for content in content_array:
        if validate_content_keys(content):
            if content['type'] == 'intent':
                # validate intent
                if not intent_exists(content['id']):
                    return False
            elif content['type'] == 'utter':
                # validate utter
                if not utter_exists(content['id']):
                    return False
            else:
                # Invalid type
                return False
        else:
            # missing keys
            return False

        return True
            
        