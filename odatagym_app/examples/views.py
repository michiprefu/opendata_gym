from django.shortcuts import render


def get_sardinia_svg_example(request):
    return render(request, 'sardinia_svg.html')
