import subprocess
import tempfile
import pandas as pd

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse

from analizzatore_smf_123_2 import analizzatore_smf_123_2
from utils.charts import drawChartExec, drawChartTempo


df_for_excel = ()

def index(request):
    return render(request, 'home/home.html')

def seletore(request):
    return render(request, 'seletore/seletore.html')

def create_temporary_file(in_memory_file):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(in_memory_file.read())
        return temp_file.name

async def analizzatore(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        # save_file(uploaded_file)
        action_type = request.POST.get('action')
        match action_type:
            case "display":
                try:
                    # resultado = subprocess.check_output(['python', 'analizzatore_smf_123_2.py', '-', uploaded_file, '-e', 'document.xlsx'])
                    response = await analizzatore_smf_123_2(uploaded_file)
                    context = {
                        'smf_headers': response[0], 
                        'smf_df': response[1],
                        'medie_header': response[2], 
                        'medie_df': response[3],
                        'line_chart_exec': drawChartExec(response[0], response[2]),
                        'line_chart_tempo': drawChartTempo(response[0], response[2]),
                        'df': response[4], 
                        '_df_api_req_name': response[5],
                        }            
                    print("ate aqui")
                    return render(request, 'analizzatore/result.html', context=context)
                except subprocess.CalledProcessError:
                    return HttpResponse("Errore durante l'esecuzione analizador.exe")
            case "export":
                try:
                    response = await analizzatore_smf_123_2(uploaded_file)
                    # print("response[8]:")
                    # print(response[8])
                    excel_writer = response[8]
                    output_file_path = uploaded_file.name + ".xlsx"
                    # print(uploaded_file.name)
                    # excel_writer.save(output_file_path)

                    # Create an HTTP response with the Excel file
                    with open(excel_writer, 'rb') as excel_file:
                        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                        response['Content-Disposition'] = f'attachment; filename="{output_file_path}"'
                        # Add a custom header to indicate download completion
                        response['X-Download-Complete'] = 'true'
                        response['Location'] = '/result/'
                        # response.status_code = 301
                    return response
                except subprocess.CalledProcessError:
                    return HttpResponse("Errore durante l'esecuzione analizador.exe")
        # return HttpResponse("File processed successfully.")
    return render(request, 'analizzatore/fileform.html')

