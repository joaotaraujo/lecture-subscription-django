from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import LectureTicket
from lecture_subscription.utils import save_pdf


def initial_screen(request):
    return render(request, 'index.html')


def search_screen(request):
    return render(request, 'search_tickets.html')


def adm_screen(request):
    if request.user.is_authenticated:
        return render(request, 'show_tickets.html', get_all_tickets())
    return render(request, 'login.html')


@login_required(login_url='/lecture_system/login/')
def ticket_info_screen(request, ticket_id):
    tickets = {'ticket': LectureTicket.objects.get(id=ticket_id)}
    return render(request, 'ticket_info.html', tickets)


def logout_user(request):
    logout(request)
    return redirect('/lecture_system/login')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'show_tickets.html', get_all_tickets())
        else:
            messages.error(request, "Usuario ou senha inválidos!")
    return redirect('/lecture_system/login')


def submit_ticket(request):
    if request.POST:
        name = request.POST.get('name')
        cpf = request.POST.get('cpf')
        born_date = request.POST.get('born_date')

        if not name or not cpf or not born_date:
            messages.error(request, "Erro: Preencha todos os campos!")
            return redirect('/')
        elif len(name) > 40:
            messages.error(request, "Erro: Seu nome deve ter no máximo 40 caracteres!")
            return redirect('/')
        # elif not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        #    messages.error(request, "Erro: formato de CPF inválido!")
        #    return redirect('/')

        try:
            rg_pdf = request.FILES['rg_pdf']
            cpf_pdf = request.FILES['cpf_pdf']
            contract_pdf = request.FILES['contract_pdf']

            rg_pdf_name = save_pdf(rg_pdf)
            cpf_pdf_name = save_pdf(cpf_pdf)
            contract_pdf_name = save_pdf(contract_pdf)
        except:
            messages.error(request, "Erro: Submeta todos os documentos!")
            return redirect('/')

        if LectureTicket.objects.filter(name=name):
            messages.error(request, "Erro: Esta pessoa já está inscrita!")
            return redirect('/')

        LectureTicket.objects.create(name=name,
                                     cpf=cpf,
                                     born_date=born_date,
                                     rg_pdf=rg_pdf_name,
                                     cpf_pdf=cpf_pdf_name,
                                     contract_pdf=contract_pdf_name,
                                     status='pendente',
                                     cancel_reason='')
        ticket_id = LectureTicket.objects.only('id').get(name=name).id
        messages.success(request, "{}{}{}".format("Inscrição ", ticket_id, " cadastrada com sucesso!"))

        return redirect('/')


def search_ticket(request):
    ticket_id = request.POST.get('ticket_id')

    if ticket_id == '':
        messages.error(request, 'Digite um número de inscrição.')
        return render(request, 'search_tickets.html')

    ticket = LectureTicket.objects.filter(id=ticket_id)
    if ticket:
        ticket = {'tickets': ticket}
        return render(request, 'search_tickets.html', ticket)
    else:
        messages.error(request, 'O número de inscrição não foi encontrado')
        return render(request, 'search_tickets.html')


def get_all_tickets():
    ticket = LectureTicket.objects.all()
    return {'tickets': ticket}


def edit_ticket(request, ticket_id):
    if request.POST:
        status = request.POST.get('select_status')
        if status == 'nao aceita':
            cancel_reason = request.POST.get('cancel_reason')
        else:
            cancel_reason = ''
        LectureTicket.objects.filter(id=ticket_id).update(status=status, cancel_reason=cancel_reason)

    messages.success(request, "{}{}{}".format("Inscrição ", ticket_id, " atualizada com sucesso!"))
    return redirect('/lecture_system/login')
