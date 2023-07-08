from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..models import Message, Chat

@csrf_exempt
def message_list_create(request, chat_slug):
    try: 
        chat = Chat.objects.get(slug=chat_slug)
        
        if request.method == 'GET':
            messages = Message.objects.filter(chat=chat).order_by('created')
            data = [{
                'id': message.id,
                'message': message.message,
                'user': message.user.username,
                'created': message.created
            } for message in messages]
            
            return JsonResponse(data, safe=False)
        
        if request.method == 'POST':        
            user = request.user
            text = request.POST.get('text')
                                
            message = Message.objects.create(user=user, chat=chat, message=text)
            
            data = {'id': message.id, 
                    'user': message.user.username, 
                    'message': message.message}

            return JsonResponse('success', safe=False)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)
    except:
        return JsonResponse({'error': 'Invalid chat slug'}, status=404)

@csrf_exempt
def message_delete(request, pk):
    try:
        todo = Message.objects.get(pk=pk)
        
        if request.method == 'DELETE':
            todo.delete()
            return JsonResponse({
                'message': 'Message deleted successfully'
            }, status=204)
        
    except Message.DoesNotExist:
        return JsonResponse({'error': 'Message not found'}, status=404)