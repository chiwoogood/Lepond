from main.models import FooterMessage

def global_context(request):
    try:
        footer_message = FooterMessage.objects.last()
    except FooterMessage.DoesNotExist:
        footer_message = None

    return {
        'footer_message': footer_message,
    }