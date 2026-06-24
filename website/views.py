from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings





def home(request):
    """Home page with hero, campaigns, news sections"""
    campaigns = [
        {
            'id': 1,
            'title': 'ترميم المساجد',
            'description': 'ساهم في ترميم وصيانة بيوت الله',
            'price': '500',
            'raised': 1250000,
            'goal': 2000000,
        },
        {
            'id': 2,
            'title': 'صيانة المساجد',
            'description': 'دعم أعمال الصيانة الدورية للمساجد',
            'price': '300',
            'raised': 850000,
            'goal': 1500000,
        },
        {
            'id': 3,
            'title': 'بناء المساجد',
            'description': 'شارك في بناء المساجد الجديدة',
            'price': '1000',
            'raised': 2100000,
            'goal': 3500000,
        },
    ]
    
    stats = {
        'projects': 181,
        'beneficiaries': 28581,
        'mosques_beneficiaries': 28001,
        'houses_beneficiaries': 580,
    }
    
    context = {
        'campaigns': campaigns,
        'stats': stats,
        'news_items': NEWS_ITEMS,  # ← أضف هذا السطر
    }
    return render(request, 'website/home.html', context)




# ── Replace your existing  about()  with this ──

# ─────────────────────────────────────────────────
# Paste these into your existing  views.py
# ─────────────────────────────────────────────────

def about(request):
    """About page – supplies stats for the banner counter"""
    stats = {
        'projects':              181,
        'beneficiaries':         28581,
        'mosques_beneficiaries': 28001,
        'houses_beneficiaries':  580,
    }
    context = {'stats': stats}
    return render(request, 'website/about.html', context)



# ── NEW: PDF viewer pages ──────────────────────────

def pdf_view_ar(request):
    """Embed the Arabic company profile PDF"""
    context = {
        'pdf_url':   '/static/pdf/profile_ar.pdf',
        'page_title': 'الملف التعريفي باللغة العربية',
    }
    return render(request, 'website/pdf_viewer.html', context)


def pdf_view_en(request):
    """Embed the English company profile PDF"""
    context = {
        'pdf_url':   '/static/pdf/profile_en.pdf',
        'page_title': 'Company Profile – English',
    }
    return render(request, 'website/pdf_viewer.html', context)


# ============================================================
# views.py  –  paste these two functions into your existing
#              views.py  (replace the current services / service_detail)
# ============================================================

# ── full service list ──────────────────────────────────────
# Each dict: id (slug for URL), title, description, icon (emoji), category
SERVICES = [
    # ── العامة ──
    {
        'id': 'complaints-suggestions',
        'title': 'الشكاوى والاقتراحات',
        'description': 'تقديم الشكاوى والاقتراحات لتحسين الخدمات',
        'icon': '💬',
        'category': 'عام',
    },
    {
        'id': 'partnership-request',
        'title': 'طلب شراكة',
        'description': 'التقدم بطلب شراكة مع الجمعية',
        'icon': '🤝',
        'category': 'عام',
    },

    # ── الحوكمة ──

    {
        'id': 'stakeholder-survey-results',
        'title': 'نتائج استطلاع أصحاب العلاقة',
        'description': 'الاطلاع على نتائج استطلاعات أصحاب العلاقة',
        'icon': '📈',
        'category': 'حوكمة',
    },

    # ── التطوع ──
    {
        'id': 'volunteer-registration',
        'title': 'تسجيل متطوع',
        'description': 'انضم إلى فريق المتطوعين في الجمعية',
        'icon': '🤝',
        'category': 'تطوع',
    },
    {
        'id': 'volunteer-page',
        'title': 'الاطلاع على صفحة المتطوع',
        'description': 'الاطلاع على صفحة المتطوع والمتابعة',
        'icon': '⏰',
        'category': 'تطوع',
    },

    # ── التوظيف ──
    {
        'id': 'job-application',
        'title': 'التقديم على وظيفة',
        'description': 'التقدم لشغل وظيفة شاغرة في الجمعية',
        'icon': '💼',
        'category': 'توظيف',
    },

    # ── التبرع ──
    {
        'id': 'donate-facilities-mosques',
        'title': 'طلب التواصل للتبرع للمرافق العامة والمساجد',
        'description': 'التواصل بخصوص التبرع لصيانة المرافق العامة والمساجد',
        'icon': '🕌',
        'category': 'تبرع',
    },
    {
        'id': 'donate-houses',
        'title': 'طلب التواصل للتبرع للمنازل',
        'description': 'التواصل بخصوص التبرع لصيانة وبناء المنازل',
        'icon': '🏠',
        'category': 'تبرع',
    },

    # ── المستفيدين ──
    {
        'id': 'beneficiary-contact-request',
        'title': 'طلب تواصل لمستفيد',
        'description': 'تقديم طلب تواصل مع الباحث الاجتماعي لمتابعة حالة المستفيد',
        'icon': '📞',
        'category': 'مستفيد',
    },
    {
        'id': 'register-beneficiary',
        'title': 'تسجيل مستفيد',
        'description': 'تسجيل مستفيد جديد في قاعدة بيانات الجمعية',
        'icon': '📝',
        'category': 'مستفيد',
    },
    {
        'id': 'update-beneficiary',
        'title': 'تحديث بيانات مستفيد',
        'description': 'تحديث وتعديل بيانات المستفيدين من خدمات الجمعية',
        'icon': '👤',
        'category': 'مستفيد',
    },
    {
        'id': 'inquiry-beneficiary',
        'title': 'استعلام عن حالة مستفيد',
        'description': 'الاستعلام عن حالة طلب مستفيد من خدمات الجمعية',
        'icon': '🔍',
        'category': 'مستفيد',
    },
]


def services(request):
    """Main services listing page."""
    return render(request, 'website/services.html', {'services': SERVICES})


def service_detail(request, service_id):
    """
    Coming-soon page for every service.
    Looks up the title from SERVICES so the page
    can display the correct service name.
    """
    # find the matching service or fall back to a generic title
    title = 'الخدمة'
    for s in SERVICES:
        if s['id'] == service_id:
            title = s['title']
            break

    return render(request, 'website/service_detail.html', {
        'service_title': title,
    })




def service_detail(request, service_id):
    """Individual service detail page"""
    context = {'service_id': service_id}
    return render(request, 'website/service_detail.html', context)


@require_http_methods(["GET", "POST"])
def beneficiary_contact_request(request):
    """Service form: طلب تواصل لمستفيد – sends details to soc.res@emaar.org.sa"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        details = request.POST.get('details', '').strip()

        try:
            send_mail(
                subject='طلب تواصل لمستفيد',
                message=f'الاسم: {name}\nرقم الجوال: {mobile}\n\nالتفاصيل:\n{details}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['dm@emaar.org.sa'],
                fail_silently=False,
            )
        except Exception:
            pass  # email failure should not block the user confirmation

        return render(request, 'website/beneficiary_contact_request.html', {'success': True})

    return render(request, 'website/beneficiary_contact_request.html', {'success': False})


def campaigns(request):
    """Campaigns listing page"""
    campaigns_list = [
        {'title': 'ترميم المساجد', 'description': 'ساهم في ترميم وصيانة بيوت الله', 'price': '500', 'raised': 285000, 'goal': 500000},
        {'title': 'ترميم المنازل', 'description': 'ساعد في ترميم منازل الأسر المحتاجة', 'price': '300', 'raised': 156000, 'goal': 300000},
    ]
    context = {'campaigns': campaigns_list}
    return render(request, 'website/campaigns.html', context)


@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'success'})
    return render(request, 'website/contact.html')

def zakat_calculator(request):
    context = {
        'gold_price': 250,
        'silver_price': 3
    }
    return render(request, 'website/zakat_calculator.html', context)

def bank_accounts(request):
    accounts = [
        {'id': 1, 'title': 'العام', 'account_number': '552608010227728', 'iban': 'SA3480000552608010227728', 'color': 'blue'},
        {'id': 2, 'title': 'المشاريع', 'account_number': '552608010522227', 'iban': 'SA3980000552608010522227', 'color': 'green'},
        {'id': 3, 'title': 'الصدقة', 'account_number': '552608010522201', 'iban': 'SA6280000552608010522201', 'color': 'purple'},
    ]
    context = {'accounts': accounts}
    return render(request, 'website/bank_accounts.html', context)

def sms_donation(request):
    return render(request, 'website/sms_donation.html')

@require_http_methods(["GET", "POST"])
def staff_login(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'success'})
    return render(request, 'website/staff_login.html')


# ============================================================
# views.py  –  paste into your existing views.py
#
#   • SECTIONS  list  (10 items, each is a plain dict)
#   • governance()            – main listing page
#   • 10 sub-page views       – each renders governance_detail.html
#
# urls.py already has all the paths (confirmed from project).
# ============================================================

# ── SVG <path> / <polyline> snippets (no <svg> wrapper) ──
# These are inserted via {{ item.icon_path|safe }} in the template.

SECTIONS = [
    # ── row 1 ──
    {
        'title': 'درجة تقييم الحوكمة',
        'description': 'اطلع على نتائج تقييم الحوكمة ومعايير الامتثال',
        'url_name': 'website:governance_rating',
        'icon_bg': '#3b82f6',
        'icon_path': '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    },
    {
        'title': 'اللوائح والسياسات',
        'description': 'جميع اللوائح والسياسات المعتمدة في الجمعية',
        'url_name': 'website:governance_policies',
        'icon_bg': '#a855f7',
        'icon_path': '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
    },
    {
        'title': 'القوائم المالية',
        'description': 'الميزانيات المالية للأعوام السابقة',
        'url_name': 'website:governance_financial',
        'icon_bg': '#22c55e',
        'icon_path': '<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>',
    },

    # ── row 2 ──
    {
        'title': 'الاجتماعات',
        'description': 'محاضر اجتماعات الجمعية العمومية',
        'url_name': 'website:governance_meetings',
        'icon_bg': '#f97316',
        'icon_path': '<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/>',
    },
    {
        'title': 'اللجان الدائمة',
        'description': 'معلومات عن اللجان الدائمة في الجمعية',
        'url_name': 'website:governance_committees',
        'icon_bg': '#7c3aed',
        'icon_path': '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/>',
    },
    {
        'title': 'أملاك واستثمارات الجمعية',
        'description': 'معلومات عن أملاك واستثمارات الجمعية',
        'url_name': 'website:governance_assets',
        'icon_bg': '#10b981',
        'icon_path': '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    },

    # ── row 3 ──
    {
        'title': 'التقرير السنوي',
        'description': 'التقارير السنوية للجمعية',
        'url_name': 'website:governance_annual',
        'icon_bg': '#6366f1',
        'icon_path': '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="15" x2="8" y2="21"/><line x1="12" y1="13" x2="12" y2="21"/><line x1="16" y1="11" x2="16" y2="21"/>',
    },
    {
        'title': 'الخطة الاستراتيجية',
        'description': 'الخطة الاستراتيجية للجمعية',
        'url_name': 'website:governance_strategic',
        'icon_bg': '#ec4899',
        'icon_path': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/><line x1="12" y1="2" x2="12" y2="5"/><line x1="12" y1="19" x2="12" y2="22"/>',
    },
    {
        'title': 'الهيكل التنظيمي',
        'description': 'الهيكل التنظيمي للجمعية',
        'url_name': 'website:governance_structure',
        'icon_bg': '#14b8a6',
        'icon_path': '<rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>',
    },

    # ── row 4 ──
    {
        'title': 'أعضاء الجمعية العمومية',
        'description': 'قائمة أعضاء الجمعية العمومية',
        'url_name': 'website:governance_general_members',
        'icon_bg': '#06b6d4',
        'icon_path': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    },
    {
        'title': 'أعضاء مجلس الإدارة',
        'description': 'قائمة أعضاء مجلس الإدارة الحالي',
        'url_name': 'website:governance_board_members',
        'icon_bg': '#f59e0b',
        'icon_path': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="11" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/>',
    },
    {
        'title': 'التقارير',
        'description': 'جميع التقارير الدورية والسنوية',
        'url_name': 'website:governance_reports',
        'icon_bg': '#8b5cf6',
        'icon_path': '<path d="M13 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V9z"/><polyline points="13 2 13 9 20 9"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
    },
]



# ── main listing view ──────────────────────────────────────
def governance(request):
    """Render the governance cards grid."""
    return render(request, 'website/governance.html', {
        'sections': SECTIONS,
    })


# ── 10 individual sub-page views ──────────────────────────
# Each one renders the shared coming-soon template with its title.

def governance_rating(request):
    """درجة تقييم الحوكمة – score banner + progress bars + certificate PDF."""
    return render(request, 'website/governance_rating.html')


def governance_policies(request):
    """اللوائح والسياسات – 2 لوائح + 9 سياسات as PDF download cards."""
    return render(request, 'website/governance_policies.html')


def governance_financial(request):
    """القوائم المالية – 4 year cards (2021-2024) linking to budget PDFs."""
    return render(request, 'website/governance_financial.html')




# ── Replace these 3 functions in views.py ──────────────────

def governance_meetings(request):
    """الاجتماعات – محاضر وفرز أصوات مجموعة بحسب السنة."""
    return render(request, 'website/governance_meetings.html')


def governance_committees(request):
    """اللجان الدائمة – حالياً لا توجد لجان."""
    return render(request, 'website/governance_committees.html')


def governance_assets(request):
    """أملاك واستثمارات الجمعية – حالياً لا توجد أملاك."""
    return render(request, 'website/governance_assets.html')

def governance_annual(request):
    return render(request, 'website/annual_reports.html', {
        'section_title': 'التقرير السنوي',
    })

def governance_strategic(request):
    return render(request, 'website/governance_detail.html', {
        'section_title': 'الخطة الاستراتيجية',
    })

def governance_operational(request):
    return render(request, 'website/governance_detail.html', {
        'section_title': 'الخطة التشغيلية',
    })

def governance_reports(request):
    return render(request, 'website/reports.html', {
        'section_title': 'التقارير',
    })

# ── أضف هذه الدالة إلى views.py ──

def volunteers(request):
    """صفحة التطوع – فريق إعمار التطوعي"""
    return render(request, 'website/volunteers.html')




# ============================================================
# views.py  –  paste / replace these into your existing views.py
#
#   • NEWS_ITEMS  list (3 items – matches homepage)
#   • news()            – listing page
#   • news_detail()     – single-article page
# ============================================================

# ── Shared news data (single source of truth) ─────────────
# ============================================================
# views.py  –  تحديث بيانات الأخبار
# ============================================================

# ── بيانات الأخبار المشتركة (مصدر واحد للحقيقة) ─────────────
NEWS_ITEMS = [
    {
        'slug':        'ksrelief-mou-signing',
        'title':       'وقّع مركز الملك سلمان للإغاثة مذكرة تفاهم مع جمعية إعمار',
        'category':    'شراكات',
        'date':        '24 يناير 2026',
        'image':       'images/news1.png',
        'description': (
            'برعاية وحضور معالي د. عبدالله الربيعة، وبحضور معالي نائب وزير الخارجية '
            'المهندس وليد بن عبدالكريم الخريجي، وقّع مركز الملك سلمان للإغاثة مذكرة تفاهم '
            'مع جمعية إعمار لتقديم خدمات الصيانة والترميم.'
        ),
        'body': (
            '<p>برعاية وحضور معالي د. عبدالله الربيعة، وبحضور معالي نائب وزير الخارجية '
            'المهندس وليد بن عبدالكريم الخريجي، وقّع مركز الملك سلمان للإغاثة مذكرة تفاهم '
            'مع جمعية إعمار لتقديم خدمات صيانة وترميم وتطوير وتشغيل المباني والمرافق عبر '
            'مهندسين وفنيين متطوعين؛ دعمًا للفئات المحتاجة بالسكن المناسب وإعادة تأهيل مبانٍ '
            'مجتمعية ضمن برامج المركز لعام 2026.</p>'
            '<p>تأتي هذه المذكرة في إطار التعاون المستمر بين المملكة العربية السعودية '
            'والمنظمات الإنسانية لتقديم الدعم للمحتاجين في مختلف أنحاء العالم.</p>'
            '<p><strong>أهداف المذكرة:</strong></p>'
            '<p>• تقديم خدمات الصيانة والترميم للمباني والمرافق</p>'
            '<p>• توفير السكن المناسب للفئات المحتاجة</p>'
            '<p>• إعادة تأهيل المباني المجتمعية</p>'
            '<p>• تفعيل دور المتطوعين من المهندسين والفنيين</p>'
        ),
    },
    {
        'slug':        'governance-score-achievement',
        'title':       'حصلت جمعية إعمار على درجة 95.52 في الحوكمة',
        'category':    'إنجازات',
        'date':        '30 دسمبر 2025',
        'image':       'images/news2.png',
        'description': (
            'حصلت جمعية إعمار على درجة 95.52 في الحوكمة من المركز الوطني لتنمية '
            'القطاع غير الربحي، مما يعكس التزام الجمعية بأعلى معايير الشفافية والمساءلة.'
        ),
        'body': (
            '<p>في إنجاز نوعي يعكس التزام جمعية إعمار بأعلى معايير الحوكمة والشفافية، '
            'حصلت الجمعية على درجة 95.52 في تقييم الحوكمة من المركز الوطني لتنمية '
            'القطاع غير الربحي.</p>'
            '<p>يأتي هذا الإنجاز نتيجة للجهود المتواصلة التي بذلتها الجمعية في تطوير '
            'أنظمتها الإدارية والمالية، وتعزيز الشفافية في جميع عملياتها.</p>'
            '<p><strong>أبرز معايير التقييم:</strong></p>'
            '<p>• الشفافية المالية والإدارية</p>'
            '<p>• جودة الإفصاح والتقارير</p>'
            '<p>• فعالية اللجان والمجلس</p>'
            '<p>• إدارة المخاطر والامتثال</p>'
            '<p>• السياسات واللوائح الداخلية</p>'
            '<p>وأكد مسؤولو الجمعية أن هذا الإنجاز يعكس التزامهم المستمر بتحقيق أعلى '
            'معايير الجودة في خدمة المستفيدين والمتبرعين.</p>'
        ),
    },
    {
        'slug':        'international-work-license',
        'title':       'يُسلّم جمعية إعمار ترخيص العمل في الخارج',
        'category':    'تراخيص',
        'date':        '12 أكتوبر 2025',
        'image':       'images/news3.png',
        'description': (
            'يأتي منح هذه الشهادة تنفيذًا لتوجيهات القيادة الكريمة بتمكين الجمعيات الأهلية '
            'من توسيع نطاق أعمالها الإنسانية والإغاثية عالميًا.'
        ),
        'body': (
            '<p>في خطوة تعزز دور المملكة العربية السعودية في العمل الإنساني العالمي، '
            'سلّم مركز الملك سلمان للإغاثة والأعمال الإنسانية جمعية إعمار بمنطقة المدينة '
            'المنورة ترخيص العمل في الخارج.</p>'
            '<p>يأتي منح هذه الشهادة تنفيذًا لتوجيهات القيادة الكريمة بتمكين الجمعيات الأهلية '
            'من توسيع نطاق أعمالها الإنسانية والإغاثية عالميًا، وتعزيز مساهمتها في تحقيق '
            'مستهدفات رؤية السعودية 2030 في العمل التطوعي والقطاع غير الربحي.</p>'
            '<p><strong>أهمية الترخيص:</strong></p>'
            '<p>• توسيع نطاق العمل الإنساني للجمعية خارج المملكة</p>'
            '<p>• المساهمة في تحقيق مستهدفات رؤية السعودية 2030</p>'
            '<p>• تعزيز دور المملكة في العمل الإنساني العالمي</p>'
            '<p>• نقل الخبرات السعودية في مجال الصيانة والترميم</p>'
            '<p>وأعرب مسؤولو الجمعية عن شكرهم وتقديرهم للقيادة الرشيدة على هذه الثقة، '
            'مؤكدين التزامهم بتمثيل المملكة بأفضل صورة في العمل الإنساني الدولي.</p>'
        ),
    },
]

def news(request):
    """News listing page – 3 cards matching the homepage."""
    return render(request, 'website/news.html', {
        'news_items': NEWS_ITEMS,
    })


def news_detail(request, slug):
    """Single news article page – look up by slug."""
    # Find the matching item; fall back to first item if slug unknown
    news_item = NEWS_ITEMS[0]          # safe default
    for item in NEWS_ITEMS:
        if item['slug'] == slug:
            news_item = item
            break

    return render(request, 'website/news_detail.html', {
        'news_item': news_item,
    })



# في نهاية ملف views.py الحالي، استبدل قسم SECTIONS وأضف الدوال الجديدة

SECTIONS = [
    # ── row 1 ──
    {
        'title': 'درجة تقييم الحوكمة',
        'description': 'اطلع على نتائج تقييم الحوكمة ومعايير الامتثال',
        'url_name': 'website:governance_rating',
        'icon_bg': '#3b82f6',
        'icon_path': '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    },
    {
        'title': 'اللوائح والسياسات',
        'description': 'جميع اللوائح والسياسات المعتمدة في الجمعية',
        'url_name': 'website:governance_policies',
        'icon_bg': '#a855f7',
        'icon_path': '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
    },
    {
        'title': 'القوائم المالية',
        'description': 'الميزانيات المالية للأعوام السابقة',
        'url_name': 'website:governance_financial',
        'icon_bg': '#22c55e',
        'icon_path': '<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>',
    },

    # ── row 2 ──
    {
        'title': 'الاجتماعات',
        'description': 'محاضر اجتماعات الجمعية العمومية',
        'url_name': 'website:governance_meetings',
        'icon_bg': '#f97316',
        'icon_path': '<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/>',
    },
    {
        'title': 'اللجان الدائمة',
        'description': 'معلومات عن اللجان الدائمة في الجمعية',
        'url_name': 'website:governance_committees',
        'icon_bg': '#7c3aed',
        'icon_path': '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/>',
    },
    {
        'title': 'أملاك واستثمارات الجمعية',
        'description': 'معلومات عن أملاك واستثمارات الجمعية',
        'url_name': 'website:governance_assets',
        'icon_bg': '#10b981',
        'icon_path': '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    },

    # ── row 3 ──
    {
        'title': 'التقرير السنوي',
        'description': 'التقارير السنوية للجمعية',
        'url_name': 'website:governance_annual',
        'icon_bg': '#6366f1',
        'icon_path': '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="15" x2="8" y2="21"/><line x1="12" y1="13" x2="12" y2="21"/><line x1="16" y1="11" x2="16" y2="21"/>',
    },
    {
        'title': 'الخطة الاستراتيجية',
        'description': 'الخطة الاستراتيجية للجمعية',
        'url_name': 'website:governance_strategic',
        'icon_bg': '#ec4899',
        'icon_path': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/><line x1="12" y1="2" x2="12" y2="5"/><line x1="12" y1="19" x2="12" y2="22"/>',
    },
    {
        'title': 'الهيكل التنظيمي',
        'description': 'الهيكل التنظيمي للجمعية',
        'url_name': 'website:governance_structure',
        'icon_bg': '#14b8a6',
        'icon_path': '<rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>',
    },

    # ── row 4 ──
    {
        'title': 'أعضاء الجمعية العمومية',
        'description': 'قائمة أعضاء الجمعية العمومية',
        'url_name': 'website:governance_general_members',
        'icon_bg': '#06b6d4',
        'icon_path': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    },
    {
        'title': 'أعضاء مجلس الإدارة',
        'description': 'قائمة أعضاء مجلس الإدارة الحالي',
        'url_name': 'website:governance_board_members',
        'icon_bg': '#f59e0b',
        'icon_path': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="11" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/>',
    },
    {
        'title': 'التقارير',
        'description': 'جميع التقارير الدورية والسنوية',
        'url_name': 'website:governance_reports',
        'icon_bg': '#8b5cf6',
        'icon_path': '<path d="M13 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V9z"/><polyline points="13 2 13 9 20 9"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
    },
]


# الدوال الموجودة (لا تغيير)
def governance(request):
    """Render the governance cards grid."""
    return render(request, 'website/governance.html', {'sections': SECTIONS})

def governance_rating(request):
    return render(request, 'website/governance_rating.html')

def governance_policies(request):
    return render(request, 'website/governance_policies.html')

def governance_financial(request):
    return render(request, 'website/governance_financial.html')

def governance_meetings(request):
    return render(request, 'website/governance_meetings.html')

def governance_committees(request):
    return render(request, 'website/governance_committees.html')

def governance_assets(request):
    return render(request, 'website/governance_assets.html')

def governance_annual(request):
    return render(request, 'website/annual_reports.html', {'section_title': 'التقرير السنوي'})

def governance_reports(request):
    return render(request, 'website/reports.html', {'section_title': 'التقارير'})


# ═══════════════════════════════════════════════════════════
# الدوال الجديدة - أضفها في نهاية ملف views.py
# ═══════════════════════════════════════════════════════════

def governance_strategic(request):
    """الخطة الاستراتيجية - PDF viewer page"""
    return render(request, 'website/governance_strategic.html')


def governance_structure(request):
    """الهيكل التنظيمي - صورة الهيكل التنظيمي"""
    return render(request, 'website/governance_structure.html')


def governance_general_members(request):
    """أعضاء الجمعية العمومية"""
    members = [
        'د. كمال محمد عثمان',
        'م. عبدالله فهد الردادي',
        'أ. عمر هاشم برزنجي',
        'أ. يوسف أيمن عبدالغني',
        'أ. أحمد بكر زيدان',
        'أ. عمر عبد الخالق محبوب',
        'م. محمد عبدالباسط محمود',
        'م. أحمد كمال عثمان',
        'م. منير عبدالحميد بخش',
        'أ. عبدالله صلاح كردي',
        'م. عامر عبد الكريم بخاري',
        'م. زياد احمد حامد',
        'د. خلود شاكر كشك',
    ]
    return render(request, 'website/governance_general_members.html', {'members': members})


def governance_board_members(request):
    """أعضاء مجلس الإدارة"""
    board_members = [
        {'name': 'كمال محمد حسين عثمان', 'position': 'رئيس مجلس الإدارة'},
        {'name': 'عبداللّٰه بن فهد بن سالم الردادي', 'position': 'نائب رئيس مجلس الإدارة'},
        {'name': 'عمر هاشم بن محمد برزنجي', 'position': 'عضو مجلس الإدارة'},
        {'name': 'يوسف ايمن عبدالغني احمد', 'position': 'عضو مجلس الإدارة'},
        {'name': 'احمد بكر احمد زيدان', 'position': 'عضو مجلس الإدارة'},
    ]

    context = {
        'board_members': board_members,
        'term_number': 2,
        'remaining_years': 'حتى 25-12-2029',
    }
    return render(request, 'website/governance_board_members.html', context)




    # ═══════════════════════════════════════════════════════════
# صفحة الشركاء - Partners Page
# أضف هذه الدالة في نهاية ملف views.py الموجود
# ═══════════════════════════════════════════════════════════

def partners(request):
    """صفحة الشركاء - شركاء إعمار وشركاء الإحسان"""
    
    # شركاء إعمار (الشركات والمؤسسات) - صور من 1.jpg إلى 31.jpg
    partner_logos = list(range(1, 32))  # [1, 2, 3, ..., 31]
    
    # شركاء الإحسان (المشاهير والمؤثرين)
    influencers = [
        {'name': 'رجاء عبدالله', 'title': 'مؤثرة ومشهورة', 'initial': 'ر'},
        {'name': 'رسمية السناني', 'title': 'مؤثرة ومشهورة', 'initial': 'ر'},
        {'name': 'عليا الشريف', 'title': 'مؤثرة ومشهورة', 'initial': 'ع'},
        {'name': 'وعد النافع', 'title': 'مؤثرة ومشهورة', 'initial': 'و'},
        {'name': 'منى الشيخ', 'title': 'مؤثرة ومشهورة', 'initial': 'م'},
        {'name': 'خالد الشيخ', 'title': 'مؤثر ومشهور', 'initial': 'خ'},
        {'name': 'مسور الشريف (مستر توفير)', 'title': 'مؤثر ومشهور', 'initial': 'م'},
        {'name': 'أماني السبع', 'title': 'مؤثرة ومشهورة', 'initial': 'أ'},
        {'name': 'رغدة حجر', 'title': 'مؤثرة ومشهورة', 'initial': 'ر'},
        {'name': 'غدير الحربي', 'title': 'مؤثرة ومشهورة', 'initial': 'غ'},
        {'name': 'ثريا الحربي', 'title': 'مؤثرة ومشهورة', 'initial': 'ث'},
        {'name': 'أحلام الصاعدي', 'title': 'مؤثرة ومشهورة', 'initial': 'أ'},
    ]
    
    context = {
        'partner_logos': partner_logos,
        'influencers': influencers,
    }
    
    return render(request, 'website/partners.html', context)