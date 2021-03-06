from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from sofia_bank.main.views.bank_information import AboutUsView, ContactView, FeedbackView, FeedbackMessageView
from sofia_bank.main.views.generic import HomeView, DashboardView
from sofia_bank.main.views.products import CreateLoanView, ProductsAndServicesView, CreateSavingView, LoanDetailView, \
    NeedsView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),

    path('about-us/', AboutUsView.as_view(), name='bank info'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('feedback/feedback-message/', FeedbackMessageView.as_view(), name='feedback message'),

    path('dashboard/<int:pk>/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/loan-detail/<int:pk>/', LoanDetailView.as_view(), name='loan detail'),

    path('needs/', NeedsView.as_view(), name='customer needs'),
    path('products-services/', ProductsAndServicesView.as_view(), name='products and services'),
    path('products-services/loans/', CreateLoanView.as_view(), name='loans'),
    path('products-services/savings/', CreateSavingView.as_view(), name='savings and deposit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)