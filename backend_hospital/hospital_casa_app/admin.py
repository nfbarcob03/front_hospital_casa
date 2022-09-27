from django.contrib import admin
from .models.user import User
from .models.paciente import Paciente
from .models.medico import Medico
from .models.familiar import Familiar
from .models.signos_vitales import SignosVitales

admin.site.register(User)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Familiar)
admin.site.register(SignosVitales)
