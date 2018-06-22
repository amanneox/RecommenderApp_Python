from django.http import QueryDict

from api.serializers import *
from rest_framework import status
from rest_framework.decorators import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import render
from django.http import HttpResponseRedirect


class CustomerAccessPermission(permissions.BasePermission):
    message = 'Auth Token required.'

    def has_permission(self, request, view):
        return True


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


# Create your views here.

@api_view(['GET', 'POST'])
def location_item_list(request):
    """
    Location based items
    """
    if request.method == 'POST':
        loc = QueryDict.dict(request.data)
        return Response(DataFilter.filter(DataFilter(), validated_data=loc))


@api_view(['GET', 'POST'])
def comment_list(request):
    """
    List all comment, or create a new comment.
    """
    if request.method == 'POST':
        validated_data = ([x for x in request.data.values()])
        serializer = CommentFilter.filter(CommentFilter(), validated_data=validated_data)
        return Response(serializer)

@api_view(['GET', 'POST'])
def admin_list(request):
    """
    List all Post, or create a new Post.
    """
    if request.method == 'GET':
        snippets = AdminUser.objects.all()
        serializer = AdminUserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdminUserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def item_list(request):
    """
    List all Post, or create a new Post.
    """
    if request.method == 'GET':
        snippets = Item.objects.all()
        serializer = ItemSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    """
    Retrieve, update or delete a Post snippet.
    """
    try:
        snippet = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def service_list(request):
    """
    List all Post, or create a new Post.
    """
    if request.method == 'GET':
        snippets = Service.objects.all()
        serializer = ServiceSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def service_detail(request, pk):
    """
    Retrieve, update or delete a Post snippet.
    """
    try:
        snippet = Service.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServiceSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def post_list(request):
    """
    List all Post, or create a new Post.
    """
    if request.method == 'GET':
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    """
    Retrieve, update or delete a Post snippet.
    """
    try:
        snippet = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a user snippet.
    """
    try:
        snippet = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def admin(request):
    context={}
    auth_cookie=request.COOKIES.get('auth_cookie', None)
    if not auth_cookie:
        return render(request, 'login.html', context)
    else:
        snippets = Item.objects.all()
        items = ItemSerializer(snippets, many=True)
        context={
            "items":items.data
        }
        return render(request,'admin/index.html',context)

def index(request):
    context = {}

    return render(request, 'index.html', context)


def apidoc(request):
    return render(request, 'api.html')


def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    if request.method=='POST':
        res=admin_list(request)

        if res.status_code==400:
            context={"error":"Unable to sign up"}
            return render(request, 'signup.html',context)
        context={"msg":"Successfully signed up"}
        return render(request,'login.html',context)

def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        req = request.POST
        mydict = QueryDict.dict(req)
        access=AdminLogin.admin_auth(AdminLogin(),mydict)
        if access:
            context={
            'token':mydict.get('csrfmiddlewaretoken'),
            'username':mydict.get('email'),
            'email':mydict.get('email')
            }
            response= HttpResponseRedirect("/admin")
            response.set_cookie('auth_cookie',value=context,path='/')
            return response
        else:
            context={
                "error":"Login Failed, Try Again"
            }
            return render(request,'login.html',context)

def logout(request):
    if request.method == 'GET':
        response = render(request, 'login.html')
        response.delete_cookie('auth_cookie')
        return response