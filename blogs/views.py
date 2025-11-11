# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.db import connection, OperationalError
# from django.http import HttpResponse
# from django.contrib import messages
# from .models import Post
# from .forms import PostForm, UserRegistrationForm
# from django.db import connection, OperationalError
# from django.contrib.admin.views.decorators import staff_member_required

# def home(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'blogs/home.html', {'posts': posts})

# @login_required
# def create_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('home')
#     else:
#         form = PostForm()
#     return render(request, 'blogs/create_post.html', {'form': form})

# @login_required
# def edit_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.user != post.author and not request.user.is_superuser:
#         return HttpResponse("Unauthorized", status=403)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blogs/edit_post.html', {'form': form})

# @login_required
# def delete_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.user == post.author or request.user.is_superuser:
#         post.delete()
#         return redirect('home')
#     else:
#         return HttpResponse("Unauthorized", status=403)

# def db_connection_check(request):
#     try:
#         connection.ensure_connection()
#         with connection.cursor() as cursor:
#             cursor.execute('SELECT 1')
#         return HttpResponse("Database: Connected", content_type="text/plain")
#     except OperationalError as e:
#         return HttpResponse(f"Database: Not connected — {e}", content_type="text/plain", status=500)

# def custom_404_view(request, exception):
#     return render(request, '404.html', status=404)

# def trigger_error(request):
#     return 1 / 0

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_staff = False
#             user.is_superuser = False
#             user.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}! You can now log in through the admin interface.')
#             return redirect('admin:login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'blogs/register.html', {'form': form})

# @staff_member_required
# def execute_raw_sql(request):
#     tables = []
#     result = None
#     error = None
#     query = ""
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("SHOW TABLES")
#             tables = [row[0] for row in cursor.fetchall()]
#     except OperationalError as e:
#         error = f"Database error: {e}"
#     if request.method == 'POST':
#         query = request.POST.get('query', '').strip()
#         if not query:
#             error = "Please enter a SQL query."
#         else:
#             try:
#                 with connection.cursor() as cursor:
#                     cursor.execute(query)
#                     if cursor.description:
#                         columns = [col[0] for col in cursor.description]
#                         rows = cursor.fetchall()
#                         result = {
#                             "columns": columns,
#                             "rows": rows,
#                             "count": len(rows)
#                         }
#                     else:
#                         connection.commit()
#                         result = {
#                             "message": f"Query executed successfully. {cursor.rowcount} rows affected."
#                         }
#             except Exception as e:
#                 error = f"Error executing query: {e}"
#     context = {
#         'tables': tables,
#         'result': result,
#         'error': error,
#         'query': query,
#     }
#     return render(request, 'blogs/execute_raw_sql.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import connection, OperationalError
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import Permission
from django.contrib.admin.views.decorators import staff_member_required
from .models import Post
from .forms import PostForm, UserRegistrationForm

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogs/home.html', {'posts': posts})

@login_required
def create_post(request):
    if not request.user.has_perm('blogs.can_create_post'):
        messages.error(request, "You don't have permission to create posts.")
        return redirect('home')

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blogs/create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.user.has_perm('blogs.can_edit_post'):
        messages.error(request, "You don't have permission to edit posts.")
        return redirect('home')
    if request.user != post.author and not request.user.is_superuser:
        return HttpResponse("Unauthorized", status=403)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/edit_post.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.user.has_perm('blogs.can_delete_post'):
        messages.error(request, "You don't have permission to delete posts.")
        return redirect('home')
    if request.user != post.author and not request.user.is_superuser:
        return HttpResponse("Unauthorized", status=403)
    post.delete()
    messages.success(request, "Post deleted successfully!")
    return redirect('home')

def db_connection_check(request):
    try:
        connection.ensure_connection()
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
        return HttpResponse("Database: Connected", content_type="text/plain")
    except OperationalError as e:
        return HttpResponse(f"Database: Not connected — {e}", content_type="text/plain", status=500)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def trigger_error(request):
    return 1 / 0

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False
            user.save()
            perms = Permission.objects.filter(codename__in=[
                'can_create_post',
                'can_edit_post',
                'can_delete_post'
            ])
            user.user_permissions.add(*perms)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in through the admin interface.')
            return redirect('admin:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blogs/register.html', {'form': form})

@staff_member_required
def execute_raw_sql(request):
    tables = []
    result = None
    error = None
    query = ""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = [row[0] for row in cursor.fetchall()]
    except OperationalError as e:
        error = f"Database error: {e}"
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()
        if not query:
            error = "Please enter a SQL query."
        else:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    if cursor.description:
                        columns = [col[0] for col in cursor.description]
                        rows = cursor.fetchall()
                        result = {
                            "columns": columns,
                            "rows": rows,
                            "count": len(rows)
                        }
                    else:
                        connection.commit()
                        result = {
                            "message": f"Query executed successfully. {cursor.rowcount} rows affected."
                        }
            except Exception as e:
                error = f"Error executing query: {e}"
    context = {
        'tables': tables,
        'result': result,
        'error': error,
        'query': query,
    }
    return render(request, 'blogs/execute_raw_sql.html', context)
