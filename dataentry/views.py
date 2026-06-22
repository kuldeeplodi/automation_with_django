from django.shortcuts import render,redirect
from .util import get_custom_model_name
from uploads.models import UploadFile
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages
from .task import import_data_task

# Create your views here.


def import_data(request):
    if request.method == "POST":
            file_path=request.FILES.get("file_path")
            model_name=request.POST.get("model_name")

            upload=UploadFile.objects.create(file=file_path,model_name=model_name)

            relative_path=str(upload.file.url)
            base_url=str(settings.BASE_DIR)
            
            file_path=base_url+relative_path
            
            import_data_task.delay(file_path,model_name)
            
            return redirect('import_data')
    else:
        custom_model=get_custom_model_name()
        context={
            'custom_model':custom_model
        }

    return render(request,'dataentry/import_data.html',context)



