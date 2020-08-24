from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class DashPageView(TemplateView):
    template_name = 'dashboard.html'

class UserPageView(TemplateView):
    template_name = 'user.html'

