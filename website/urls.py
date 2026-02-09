# ═══════════════════════════════════════════════════════════
# تحديث ملف urls.py - إضافة رابط صفحة الشركاء
# أضف هذا السطر في قسم urlpatterns في ملف urls.py
# ═══════════════════════════════════════════════════════════

# أضف هذا السطر بعد path('news/<slug:slug>/', ...) وقبل path('contact/', ...)


# ═══════════════════════════════════════════════════════════
# الملف الكامل بعد التعديل:
# ═══════════════════════════════════════════════════════════

from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/<str:service_id>/', views.service_detail, name='service_detail'),
    path('campaigns/', views.campaigns, name='campaigns'),
    
    # ══════════════ GOVERNANCE SECTION ══════════════
    path('governance/', views.governance, name='governance'),
    path('governance/rating/', views.governance_rating, name='governance_rating'),
    path('governance/policies/', views.governance_policies, name='governance_policies'),
    path('governance/financial/', views.governance_financial, name='governance_financial'),
    path('governance/meetings/', views.governance_meetings, name='governance_meetings'),
    path('governance/committees/', views.governance_committees, name='governance_committees'),
    path('governance/assets/', views.governance_assets, name='governance_assets'),
    path('governance/annual/', views.governance_annual, name='governance_annual'),
    path('governance/strategic/', views.governance_strategic, name='governance_strategic'),
    path('governance/reports/', views.governance_reports, name='governance_reports'),
    path('governance/structure/', views.governance_structure, name='governance_structure'),
    path('governance/general-members/', views.governance_general_members, name='governance_general_members'),
    path('governance/board-members/', views.governance_board_members, name='governance_board_members'),
    
    path('news/', views.news, name='news'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    
    # ══════════════ صفحة الشركاء (جديدة) ══════════════
    path('partners/', views.partners, name='partners'),
    
    path('contact/', views.contact, name='contact'),
    path('zakat-calculator/', views.zakat_calculator, name='zakat_calculator'),
    path('bank-accounts/', views.bank_accounts, name='bank_accounts'),
    path('sms-donation/', views.sms_donation, name='sms_donation'),
    path('staff-login/', views.staff_login, name='staff_login'),
    path('profile-ar/', views.pdf_view_ar, name='pdf_view_ar'),
    path('profile-en/', views.pdf_view_en, name='pdf_view_en'),
    path('services/', views.services, name='services'),
    path('volunteers/', views.volunteers, name='volunteers'),
]
