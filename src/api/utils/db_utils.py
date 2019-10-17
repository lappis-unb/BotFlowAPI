def bulk_update_unique(items, attr='name'):
    """
    Save a list of elements that have a new value for the given attribute.
    """
    if not items:
        return []

    objects = type(items[0]).objects
    query = {attr + '__in': [x.name for x in items]}
    repeated = objects.filter(**query).values_list(attr, flat=True)
    
    # Check the database
    if repeated:
        print(f'Repeated values for {attr}:', ', '.join(repeated))
        repeated = set(repeated)
        items = [x for x in items if getattr(x, attr) not in repeated]
    
    # Check internal consistency
    values = set()
    items_final = []
    for item in items:
        value = getattr(item, attr)
        if value in values:
            print(f'Duplicated entry:', value)
        else:
            items_final.append(item)
    
    return objects.bulk_create(items)
