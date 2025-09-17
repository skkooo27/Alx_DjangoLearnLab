from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from .forms import CustomUserCreationForm

# Function-based view to list all books
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = CustomUserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role-based views
def check_admin(user):
    return user.userprofile.role == 'Admin'

def check_librarian(user):
    return user.userprofile.role == 'Librarian'

def check_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(check_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Permission-based views
# These views enforce custom permissions defined in the Book model
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # Simple add view, assuming form
    if request.method == 'POST':
        # Handle form
        pass
    return render(request, 'relationship_app/add_book.html')

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Handle form
        pass
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
