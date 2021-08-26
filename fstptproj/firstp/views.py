from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from InstagramAPI import InstagramAPI
from .services.reusable_object_processor import ReusableObjectsProcessor


@csrf_exempt
def index(request):
    if 'login' in request.POST and 'pass' in request.POST:
        login = request.POST['login'] if request.POST['login'] else None
        pswd = request.POST['pass'] if request.POST['pass'] else None
        
        if not login or not pswd:
            return HttpResponse("Login or password is empty")
        
        if 'api_filename' not in request.session:
            api = InstagramAPI(login, pswd)
            api.login()
            
            processor = ReusableObjectsProcessor(api)
            request.session['api_filename'] = processor.save()
        
        return HttpResponse("""
            Logged in!
        """)
    else:
        return HttpResponse("""
            <form method="POST">
                <input name="login" value="hiphop.movengroove" type="text">
                <input name="pass" value="7e2525314c25" type="text">
                <input type="submit">
            </form>
        """)


def test_session(request):
    processor = ReusableObjectsProcessor(filename = request.session['api_filename'])
    api = processor.load()
    api.searchUsername('serj.cool_esh')
    return HttpResponse("test_session view" + str(api.LastJson))
    
def method_processor(request, method):
    resp = {"status": "ok"}
    return JsonResponse(resp)
