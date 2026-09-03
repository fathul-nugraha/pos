from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "barang/barang.html")
  
def masterBarang(request):
  return render(request, "barang/masterbarang.html")