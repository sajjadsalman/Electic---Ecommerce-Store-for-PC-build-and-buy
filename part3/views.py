from django.shortcuts import render, redirect
from part3.models import Component, Computer
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def main_page(request):
    return render(request, 'part3/main_page.html')

def about_page(request):
    return render(request, 'part3/about.html')

def contact_page(request):
    return render(request, 'part3/contact.html')
@csrf_exempt
def feedback(request):
    return render(request, 'part3/feedback.html')
@csrf_exempt
def feedback_thankyou(request):
    return render(request, 'part3/feedback_thankyou.html')

def component_list(request):
    components = Component.objects.all()
    return render(request, 'part3/component_list.html', {'components': components})

def computer_list(request):
    computers = Computer.objects.all()
    return render(request, 'part3/computer_list.html', {'computers': computers})

@csrf_exempt
def swap_component(request, computer_id):
    computer = Computer.objects.get(pk=computer_id)
    categories = Component.objects.values_list('category', flat=True).distinct()
    components = Component.objects.all()

    if request.method == 'POST':
        for component in computer.components.all():
            new_component_id = request.POST.get(f'component_{component.id}')

            if new_component_id:
                new_component = Component.objects.get(pk=new_component_id)

                if component.category == new_component.category:
                    computer.components.remove(component)
                    computer.components.add(new_component)

    return render(request, 'part3/swap_component.html', {'computer': computer, 'categories': categories, 'components': components})

def order_summary(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)
    return render(request, 'part3/order_summary.html', {'computer': computer})

def order_complete(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)
    return render(request, 'part3/order_complete.html', {'computer': computer})
