from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from person_fbv.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'phone']


#This function lets you add another person in the list
def person_create(request, template_name='person_fbv/person_form.html'):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('person_fbv:person_list')
    return render(request, template_name, {'form':form})

#This function retrieves every individual's details saved in the list
def person_list(request, template_name='person_fbv/person_list.html'):
    person = Person.objects.all()
    data = {}
    data['object_list'] = person
    return render(request, template_name, data)

#This function will let you delete a person from the list
def person_delete(request, pk, template_name='person_fbv/person_confirm_delete.html'):
    person= get_object_or_404(Person, pk=pk)
    if request.method=='POST':
        person.delete()
        return redirect('person_fbv:person_list')
    return render(request, template_name, {'object':person})

#This function will let you update the details of any individual from the list
def person_update(request, pk, template_name='person_fbv/person_form.html'):
    person= get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_fbv:person_list')
    return render(request, template_name, {'form':form})
