# from django.contrib.auth import login, get_user_model
# from django.db.models import Q
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from urllib.parse import urlencode
# from django.views.generic import CreateView, DetailView, ListView
# from accounts.forms import CustomRegisterForm
# from accounts.models import User
# from publications.forms.search_form import SearchForm
# from publications.models import Publications
#
#
# # Create your views here.
# class RegisterView(CreateView):
#     model = get_user_model()
#     template_name = 'accounts/register.html'
#     form_class = CustomRegisterForm
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.get_success_url())
#
#     def get_success_url(self):
#         next_url = self.request.GET.get('next')
#         if not next_url:
#             next_url = self.request.POST.get('next')
#         if not next_url:
#             next_url = reverse('to_do_list:home')
#         return next_url
#
#
# class ProfileListView(ListView):
#     model = get_user_model()
#     template_name = 'accounts/accounts_list.html'
#     context_object_name = 'users'
#     paginate_by = 5
#     ordering = ("id",)
#     page_kwarg = 'page'
#
#     def dispatch(self, request, *args, **kwargs):
#         self.form = self.get_search_form()
#         self.search_value = self.get_search_value()
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=None, **kwargs)
#         context["form"] = self.form
#         if self.search_value:
#             context["query"] = urlencode({'search': self.search_value})
#             context["search_value"] = self.search_value
#         return context
#
#     def get_search_form(self):
#         return SearchForm(self.request.GET)
#
#     def get_search_value(self):
#         if self.form.is_valid():
#             return self.form.cleaned_data['search']
#         return None
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         print(queryset)
#         if self.search_value:
#             queryset = queryset.filter(Q(username__icontains=self.search_value) |
#                                        Q(first_name__icontains=self.search_value) |
#                                        Q(email__icontains=self.search_value))
#         return queryset
#
#
# class ProfileView(DetailView):
#     template_name = 'accounts/profile.html'
#     queryset = User.objects.all()
#     context_object_name = 'profile_user'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=None, **kwargs)
#         publications = Publications.objects.all()
#         context['publications'] = publications.filter(author__pk=self.object.pk).distinct()
#         return context
