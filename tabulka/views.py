from django.shortcuts import render, redirect
from .forms import FormDalsitabulka
from .models import DalsiTabulka

# Create your views here.
def create_record(request):
    if request.method == "POST":
        form = FormDalsitabulka(request.POST)
        if form.is_valid():
            data = form.changed_data
            new_record = DalsiTabulka(pet=data["pet"], sex=data["sex"])
            new_record.save()

        else:
            form = FormDalsitabulka()
        return render(request, 'tabulka/record_to_DB.html', {'form': form})
