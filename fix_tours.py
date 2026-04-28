import os
import django
from tours_app.models import TourPackage

def fix_images():
    images = [
        'tours/bali_beach.png',
        'tours/iceland_aurora.png',
        'tours/kyoto_spring.png',
        'tours/serengeti_safari.png'
    ]
    
    tours = TourPackage.objects.all()
    for i, tour in enumerate(tours):
        # Cycle through available images
        img_index = i % len(images)
        tour.image = images[img_index]
        tour.save()
        print(f"Updated {tour.title} with image {images[img_index]}")

if __name__ == '__main__':
    fix_images()
