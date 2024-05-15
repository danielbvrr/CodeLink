from django.utils import timezone
from alarme.models import RegistroMovimentaca

registro = RegistroMovimentacao.objects.create(
    data_hora=timezone.now(),
    alarme_id=2,
    raspberry_id=3,
    dispositivo_id='0338a66a-d0a4-4f17-b597-66966f91459e'
)
registro.save()
