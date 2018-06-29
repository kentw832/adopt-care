from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from apps.landing.views import LandingView
from apps.accounts.views import UserViewSet
from apps.core.api import (
    OrganizationViewSet, FacilityViewSet, ProviderProfileViewSet, ProviderTitleViewSet,
    ProviderRoleViewSet, ProviderSpecialtyViewSet, DiagnosisViewSet,  MedicationViewSet,
    ProcedureViewSet, )
from apps.patients.api import (
    PatientProfileViewSet, PatientDiagnosisViewSet, ProblemAreaViewSet,
    PatientProcedureViewSet, )

from apps.accounts.views import ObtainAuthToken, social_auth, \
    RequestPasswordChange, ResetPassword, ValidateUserView

admin.site.site_title = admin.site.index_title = "CareAdopt Backend"
admin.site.site_header = mark_safe('<img src="{img}" alt="{alt}"/> {alt}'.format(
    img=settings.STATIC_URL + 'favicon.ico',
    alt=admin.site.site_title,
))

router = DefaultRouter()
# Accounts
router.register(r'users', UserViewSet, base_name='users')
# Core
router.register(r'organizations', OrganizationViewSet, base_name='organizations')
router.register(r'facilities', FacilityViewSet, base_name='facilities')
router.register(
    r'provider_profiles', ProviderProfileViewSet, base_name='provider_profiles')
router.register(r'provider_titles', ProviderTitleViewSet, base_name='provider_titles')
router.register(r'provider_roles', ProviderRoleViewSet, base_name='provider_roles')
router.register(
    r'provider_specialties', ProviderSpecialtyViewSet, base_name='provider_specialties')
router.register(r'diagnosis', DiagnosisViewSet, base_name='diagnosis')
router.register(r'medications', MedicationViewSet, base_name='medications')
router.register(r'procedures', ProcedureViewSet, base_name='procedures')
# Patients
router.register(
    r'patient_profiles', PatientProfileViewSet, base_name='patient_profiles')
router.register(r'problem_areas', ProblemAreaViewSet, base_name='problem_areas')
router.register(
    r'patient_diagnosis', PatientDiagnosisViewSet, base_name='patient_diagnosis')
router.register(
    r'patient_procedures', PatientProcedureViewSet, base_name='patient_procedures')

urlpatterns = [
    url(r'^favicon.ico$', RedirectView.as_view(
        url=settings.STATIC_URL + 'favicon.ico')),

    url(r'^api/', include(router.urls)),
    url(r'^$', LandingView.as_view(), name='landing-page'),

    # Administration
    url(r'^admin/', include(admin.site.urls)),

    # General Api
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', ObtainAuthToken.as_view()),
    url(r'^social/(?P<backend>[^/]+)/', social_auth),
    url(r'reset-password/(?P<email>[a-zA-Z0-9-.+@_]+)/$',
        RequestPasswordChange.as_view(), name='reset-password'),
    url(r'reset/(?P<reset_key>[a-z0-9\-]+)/$',
        ResetPassword.as_view(), name='reset-request'),
    url(r'validate/(?P<validation_key>[a-z0-9\-]+)/$',
        ValidateUserView.as_view(), name='user-validation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)