# import settings for stripe API keys call
from django.conf import settings

from django.shortcuts import render

# importing generic for class based views
from django.views import generic

# importing forms and models for the Post itself
from .forms import PostForm

from .models import Post

# payment backend
import stripe

# stripe API settings
stripe.api_key=settings.STRIPE_TEST_SECRET_KEY # local
# stripe.api_key=settings.STRIPE_SECRET_KEY # production

# Create your views here.

# using a FormView to render forms
class NewPostView(generic.FormView):
    # declaring model
    model = Post

    # declaring template
    template_name = "post/new.html" 
    
    # declaring form
    form_class = PostForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY # private key
        # context['stripe_key'] = settings.STRIPE_PUBLISHABLE_KEY # production key
        return context

    def form_valid(self, form):

        # stripe integration
        amount = 200

        # create a stripe customer
        customer = stripe.Customer.create(
            email=self.request.POST['email'],
            description=self.request.POST['address'],
            source=self.request.POST['stripeToken']
        )

        # charge the stripe customer
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description='New post'
        )

        # saving post object
        post = form.save(commit=False)
        post.save() # saving job object for return data, used in URL of email body

        # redirect to home on success
        return redirect('home')
