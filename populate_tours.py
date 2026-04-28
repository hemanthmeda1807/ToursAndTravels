import os
import django
import requests
from django.core.files.base import ContentFile

# 1. Setup Django first!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tours_project.settings')
django.setup()

# 2. Now import models
from tours_app.models import Category, TourPackage

def populate():
    # Create Categories
    categories_data = [
        {"name": "Adventure", "desc": "Thrilling and exciting adventure tours."},
        {"name": "Relaxation", "desc": "Peaceful and relaxing getaways."},
        {"name": "Cultural", "desc": "Immerse yourself in rich cultures."},
        {"name": "Luxury", "desc": "Premium experiences with ultimate comfort."},
        {"name": "Budget", "desc": "Affordable tours for savvy travelers."},
    ]
    
    cats = {}
    for c in categories_data:
        cat, _ = Category.objects.get_or_create(name=c['name'], defaults={'description': c['desc']})
        cats[c['name']] = cat

    print("Categories ready.")

    # Tour Data with Unsplash Keywords
    packages = [
        {"cat": "Relaxation", "title": "Bali Beach Paradise", "loc": "Indonesia", "price": 1200, "days": 5, "img": "beach,bali", "feat": True},
        {"cat": "Adventure", "title": "Iceland Aurora", "loc": "Iceland", "price": 2500, "days": 7, "img": "aurora,iceland", "feat": True},
        {"cat": "Cultural", "title": "Kyoto Heritage", "loc": "Japan", "price": 1800, "days": 5, "img": "temple,kyoto", "feat": True},
        {"cat": "Adventure", "title": "Serengeti Safari", "loc": "Tanzania", "price": 1500, "days": 8, "img": "safari,africa", "feat": True},
        {"cat": "Adventure", "title": "Swiss Skydiving", "loc": "Switzerland", "price": 3200, "days": 4, "img": "skydiving,alps", "feat": False},
        {"cat": "Relaxation", "title": "Santorini Sunset", "loc": "Greece", "price": 2800, "days": 6, "img": "santorini,sunset", "feat": True},
        {"cat": "Cultural", "title": "Rome History", "loc": "Italy", "price": 950, "days": 3, "img": "colosseum,rome", "feat": False},
        {"cat": "Adventure", "title": "Patagonia Trek", "loc": "Chile", "price": 1900, "days": 12, "img": "mountains,patagonia", "feat": True},
        {"cat": "Relaxation", "title": "Phuket Escape", "loc": "Thailand", "price": 1100, "days": 6, "img": "phuket,thailand", "feat": False},
        {"cat": "Cultural", "title": "Machu Picchu", "loc": "Peru", "price": 2200, "days": 5, "img": "machupicchu", "feat": True},
        {"cat": "Adventure", "title": "Reef Diving", "loc": "Australia", "price": 2700, "days": 4, "img": "diving,reef", "feat": False},
        {"cat": "Luxury", "title": "Riviera Cruise", "loc": "France", "price": 4500, "days": 10, "img": "yacht,france", "feat": True},
        {"cat": "Cultural", "title": "Cairo Pyramids", "loc": "Egypt", "price": 850, "days": 4, "img": "pyramids,egypt", "feat": True},
        {"cat": "Adventure", "title": "Fjord Kayaking", "loc": "Norway", "price": 2100, "days": 6, "img": "kayak,norway", "feat": False},
    ]

    for p in packages:
        # Check if tour already exists to avoid duplicates
        if not TourPackage.objects.filter(title=p['title']).exists():
            tour = TourPackage(
                category=cats[p['cat']],
                title=p['title'],
                description=f"Experience the magic of {p['loc']} on this {p['days']}-day {p['cat'].lower()} tour.",
                location=p['loc'],
                price=p['price'],
                duration_days=p['days'],
                featured=p['feat']
            )
            
            # Download image from Unsplash
            try:
                img_url = f"https://source.unsplash.com/featured/800x600/?{p['img']}"
                response = requests.get(img_url)
                if response.status_code == 200:
                    filename = f"{p['title'].lower().replace(' ', '_')}.jpg"
                    tour.image.save(filename, ContentFile(response.content), save=False)
            except Exception as e:
                print(f"Could not download image for {p['title']}: {e}")
            
            tour.save()
            print(f"Created: {p['title']}")

    print("All tours populated successfully!")

if __name__ == '__main__':
    populate()
