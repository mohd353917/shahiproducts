from django.shortcuts import render


def index(request):
    products = [
        {
            "title": "Turmeric Powder",
            "description": "Perfect combinaion of Fragrance and Taste/ 100% Natural Food Spices STAY HOME STAY SAFE.",
            "image": "/static/img/turmeric1.jpg",
        },
        {
            "title": "Coriander Powder",
            "description": "Perfect combinaion of Fragrance and Taste/ 100% Natural Food Spices STAY HOME STAY SAFE.",
            "image": "/static/img/coriander1.jpg",
        },
        {
            "title": "Red Chilli Powder",
            "description": "Perfect combinaion of Fragrance and Taste/ 100% Natural Food Spices STAY HOME STAY SAFE.",
            "image": "/static/img/red.jpg",
        },
        {
            "title": "Garam Masala",
            "description": "Perfect combinaion of Fragrance and Taste/ 100% Natural Food Spices STAY HOME STAY SAFE.",
            "image": "/static/img/red.jpg",
        },
    ]
    return render(
        request, template_name="home/index.html", context={"products": products}
    )


def about(request):
    return render(request, template_name="home/about.html")


def contact_us(request):
    return render(request, template_name="home/contact-us.html")


def Login(request):
    return render(request, template_name="home/login.html")


def faqs(request):
    return render(request, template_name="home/faq.html")


def shahi_society(request):
    return render(request, template_name="home/shahi-society.html")


def turmeric(request):
    return render(request, template_name="home/turmeric.html")
