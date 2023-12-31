import subprocess
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
def home(request):
    return render(request,'index.html')
# Create your views here.



def run_code(code):
    try:
        code='print('+ code +')'
        output=subprocess.check_output(['python','-c',code],
                                    universal_newlines=True,
                                    stderr=subprocess.STDOUT,
                                    timeout=30)
    except subprocess.CalledProcessError as e:
        output='公式输入有误'
    return output
    
@csrf_exempt
@require_POST
def compute(request):
    code = request.POST.get('code')
    result = run_code(code)
    return JsonResponse(data={'result': result})
