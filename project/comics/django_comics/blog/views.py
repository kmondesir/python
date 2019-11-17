from django.shortcuts import render

posts = [
{
  'author':'CoreyMS',
  'title':'Blog Post 1',
  'content':'First Post content',
  'date_posted':'August 27, 2019'
},
{
  'author':'MSCorey',
  'title':'Blog Post 2',
  'content':'Second Post content',
  'date_posted':'August 28, 2019'
}

]

# Create your views here.
def home(request):
  context = {
    'posts':posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title':'About'})