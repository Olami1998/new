from django.shortcuts import render, redirect
import os

# Create your views here.

from .models import MultipleImage
def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            MultipleImage.objects.create(images=image)
            images = MultipleImage.objects.all()
        return redirect('upView')
    
    return render(request, 'load.html')

def load(request):
    imagess = MultipleImage.objects.all().order_by('-date')
    return render(request, 'index.html', {'images': imagess})

#def deleteProduct(request, pk):
 #   prod = MultipleImage.objects.get(id=pk)
  #  if len(prod.image) > 0:
   #     os.remove(prod.images.path)
    #    prod.delete()
     #   messages.success(request, "Product deleted successfully")
      #  return redirect("upView")