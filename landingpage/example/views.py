from django.shortcuts import render, HttpResponseRedirect
from django.views import View


class Home(View):

    template = 'home/home.html'

    def get(self, request):   
        return render(request,self.template, {'page': 'home'})

    def post(self, request):
        subject = request.POST['subject']
        message = request.POST['message']

        print("Assunto: {} - Mensagem: {}".format(subject, message))
        return HttpResponseRedirect("/")


class About(View):

    template = 'about/about.html'

    def get(self, request):
        return render(request, self.template, {'page': 'about'})

    def post(self, request):
        subject = request.POST['subject']
        message = request.POST['message']

        print("Assunto: {} - Mensagem: {}".format(subject, message))
        return HttpResponseRedirect("/sobre")