from asyncio import selector_events
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import region, Candidato

def index(request):
    latest_question_list = region.objects.order_by('nombre')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'encuesta/index.html', context)

def detalle(request, id_region):
    candidato = get_object_or_404(Candidato, pk=id_region)
    return render(request, 'encuesta/detalle.html', {'candidato': candidato})

def votar(request, id_region):
    candidato = get_object_or_404(Candidato, pk=id_region)
    try:
        selected_candidato = region.candidato_set.get(pk=request.POST['candidato'])
    except (KeyError, Candidato.DoesNotexist):
        return render(request, 'encuesta/detalle.html', {
            'region': region,
            'error_message': "No haz seleccionado una opcion",
        })
    else:
        selected_candidato.votos +=1
        selected_candidato.save()
        return HttpResponseRedirect(reverse('encuesta:resultados', args=(region.id,)))

def resultados(request, id_region):
    region = get_object_or_404(region, pk=id_region)
    return render(request, 'encuesta/resultados.html', {'region': region})