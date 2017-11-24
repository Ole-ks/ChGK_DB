from django.contrib import admin
from .models import Question
from .models import Blitz
from .models import Package
from .models import PackageDetail

admin.site.register(Question)
admin.site.register(Blitz)
admin.site.register(Package)
admin.site.register(PackageDetail)