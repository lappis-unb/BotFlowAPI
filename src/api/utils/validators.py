import re

from api.models import Project

def validate_name(data, model, project_id):
    project = Project.objects.filter(pk=project_id).first()

    if re.match("^[a-zA-Z0-9_]*$", data['name']):
        return True
    return False