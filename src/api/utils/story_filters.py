def filter_content_by_name(stories, name):
    filtered_list = []
    for story in stories:
        content = story['content']

        for element in content:
            if name in element['name']:
                filtered_list.append(story)
                break

    return filtered_list
