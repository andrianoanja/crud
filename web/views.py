from django.shortcuts import render,redirect
from web.models import Produit
from .formulaires import ProduitForm,InscriptionForm
from django.core.paginator import Paginator
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    produits = Produit.objects.all()
    recherche=request.GET.get('serch')
    if recherche !='' and recherche is not None:
        produits=Produit.objects.filter(designation__icontains=recherche)
    pagination = Paginator(produits, 4)
    page = request.GET.get('page')
    produits = pagination.get_page(page)
    context = {'produits':produits}
    return render(request,'index.html', context)

def ajouter(request):
    produit = ProduitForm()
    if request.method == "POST":
        produit = ProduitForm(request.POST)
        produit.save()
        messages.success(request, "Enregistrement succes")
        return redirect('/')
    return render(request,'ajouter.html',{'produit': produit } )

def update(request,myid):
    produit = Produit.objects.get(id=myid)
    produit = ProduitForm(request.POST or None,instance=produit)
    if produit.is_valid():
        produit.save()
        return redirect('/')
    context = {'produit':produit}
    return render(request,'update.html',context)

def delete(request, myid):
    delete = Produit.objects.get(id=myid)
    delete.delete()
    return redirect('/')

class inscrire(View):
    def get(self,request):
        signup = InscriptionForm()
        return render(request,'inscrire.html',{'signup':signup})
    def post(self,request):
        signup=InscriptionForm(request.POST)
        if signup.is_valid():
            
            signup.save()
            messages.success(request, "Enregistrement succes")
        else:
            messages.success(request, "Valo fara fahakelina ny mot de passe na tsy mitov na efa mi-existe lay utilisateur")
            return redirect('inscrire')
        return redirect('login')