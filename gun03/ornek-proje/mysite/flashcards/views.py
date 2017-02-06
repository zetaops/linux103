from django.shortcuts import render, redirect

from .models import Card
from random import randint


def index(request):
    cards = Card.objects.filter(correct=False)
    if cards:
        content = {'content': cards[0]}
    else:
        content = {'msg': 'Butun sorulari cevapladiniz. Yeni Sorular Ekleyiniz'}

    return render(request, 'flashcards/index.html', content)


def next_card(request, card_id):
    cards = Card.objects.exclude(id=card_id)
    cards = cards.filter(correct=False)

    if cards:
        card = cards[randint(0, len(cards)-1)]
        content = {'content': card}
    else:
        content = {'msg': 'Butun sorulari cevapladiniz. Yeni Sorular Ekleyiniz'}

    return render(request, 'flashcards/index.html', content)


def correct(request, card_id):
    card = Card.objects.get(pk=card_id)
    card.correct = True
    card.save()
    return redirect('index')


def correct_list(request):
    cards = Card.objects.filter(correct=True)
    if cards:
        content = {'content': cards}
    else:
        content = {'msg': 'hic dogru cevabiniz bulunmamaktadir.'}

    return render(request, 'flashcards/list.html', content)


def pending_list(request):
    cards = Card.objects.filter(correct=False)
    if cards:
        content = {'content': cards}
    else:
        content = {'msg': 'Butun Sorulari dogru cevapladiniz yada sorunuz bulunmamaktadir.'}

    return render(request, 'flashcards/list.html', content)
