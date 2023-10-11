from django.shortcuts import render
from .forms import RegexQueryForm
import re

def query_regex(request):
    results = []
    if request.method == 'POST':
        form = RegexQueryForm(request.POST)
        if form.is_valid():
            input_string = form.cleaned_data['input_string']
            regex_pattern = form.cleaned_data['regex_pattern']
            
            # Perform the regex search
            matches = re.findall(regex_pattern, input_string)
            
            if matches:
                results = matches
            else:
                results = ["No matches found"]
    else:
        form = RegexQueryForm()
    
    return render(request, 'regrex/query.html', {'form': form, 'results': results})
