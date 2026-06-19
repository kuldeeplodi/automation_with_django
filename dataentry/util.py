from django.apps import apps

def get_custom_model_name():
    defualt_name=['LogEntry','Permission','Group','User','ContentType','Session']

    custom_model=[]
    for model in apps.get_models():
        if model.__name__ not in defualt_name:
             custom_model.append(model.__name__)
    return custom_model