from api.models import Intent, Utter, Story

def intent_exists(id):
    return len(Intent.objects.filter(id=id)) > 0

def utter_exists(id):
    return len(Utter.objects.filter(id=id)) > 0

def checkpoint_exists(id):
    return len(Story.objects.filter(id=id)) > 0

def validate_content_keys(content):
    return 'id' in content and 'type' in content

def validate_content(content_array):
    for content in content_array:
        is_valid = True

        if validate_content_keys(content):
            if content['type'] == 'intent':
                # validate intent
                if not intent_exists(content['id']):
                    is_valid = False

            elif content['type'] == 'utter':
                # validate utter
                if not utter_exists(content['id']):
                    is_valid = False

            elif content['type'] == 'checkpoint':
                # validate checkpoint
                if not checkpoint_exists(content['id']):
                    is_valid = False
            else:
                # invalid type
                is_valid = False
        else:
            # missing keys
            is_valid = False

        if not is_valid:
            return False

    return True

def validate_story(data):
    missing_keys = not ('content' in data)

    if missing_keys:
        return False

    return True

def delete_related_stories(deleted_obj, type_str):
        stories = Story.objects.all()
        stories_to_update = set()

        for story in stories:
            for element in story.content:
                if element['type'] == type_str and element['id'] == deleted_obj.id:
                    story.delete()
