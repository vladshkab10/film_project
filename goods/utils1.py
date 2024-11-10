from.models import Products
def get_user_likes(request):
    if request.user.is_authenticated:
        return Products.objects.all()