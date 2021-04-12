from django.db import models


class LectureTicket(models.Model):
    name = models.TextField(max_length=40)
    cpf = models.TextField(max_length=14)
    born_date = models.DateTimeField()
    rg_pdf = models.FileField(upload_to='documents/')
    cpf_pdf = models.FileField(upload_to='documents/')
    contract_pdf = models.FileField(upload_to='documents/')
    status = models.TextField()
    cancel_reason = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'lectureticket'

    def get_date_format(self):
        return self.born_date.strftime('%d-%m-%Y')