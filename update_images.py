import os
import django
import requests
from django.core.files.base import ContentFile

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tours_project.settings')
django.setup()

from tours_app.models import TourPackage

# Mapping of keywords to reliable Unsplash IDs
IMAGE_MAP = {
    "himalayan": "1551524162-d0377e5c7a0a",
    "santorini": "1507501336603-6e31db2be73a",
    "swiss": "1506744038136-46273834b3fb",
    "alps": "1464817739974-0110991c7010",
    "egypt": "1503917988258-f87a78e3c995",
    "pyramids": "1503917988258-f87a78e3c995",
    "bali": "1537992153473-17369a0be4a9",
    "iceland": "1476610182048-b716b8518aae",
    "aurora": "1476610182048-b716b8518aae",
    "serengeti": "1516422213481-2950019680af",
    "safari": "1516422213481-2950019680af",
    "kyoto": "1493976040374-85c8e12f0c0e",
    "japan": "1493976040374-85c8e12f0c0e",
    "rome": "1552832230-c0197dd3ef73",
    "italy": "1552832230-c0197dd3ef73",
    "patagonia": "1517059224940-d4af9eec41b7",
    "phuket": "1589394815804-964ed76aeb33",
    "thailand": "1589394815804-964ed76aeb33",
    "machu": "1587595303484-0ac139c2794e",
    "peru": "1587595303484-0ac139c2794e",
    "reef": "1544551763-46a013bb70d5",
    "australia": "1544551763-46a013bb70d5",
    "riviera": "1534447677768-be436bb09401",
    "france": "1534447677768-be436bb09401",
    "fjord": "1473496169904-658ba7c44d8a",
    "norway": "1473496169904-658ba7c44d8a",
}

DEFAULT_IMAGE_ID = "1469441547158-0eb5b995e925"

def update_images():
    tours = TourPackage.objects.all()
    print(f"Starting update for {len(tours)} tours...")
    
    for tour in tours:
        found_id = None
        title_lower = tour.title.lower()
        loc_lower = tour.location.lower()
        
        for kw, img_id in IMAGE_MAP.items():
            if kw in title_lower or kw in loc_lower:
                found_id = img_id
                break
        
        if not found_id:
            found_id = DEFAULT_IMAGE_ID
            
        print(f"Updating {tour.title} with image ID {found_id}...")
        
        try:
            # Using 1200w for high quality in production
            img_url = f"https://images.unsplash.com/photo-{found_id}?auto=format&fit=crop&w=1200&q=80"
            response = requests.get(img_url, timeout=20)
            if response.status_code == 200:
                filename = f"{tour.title.lower().replace(' ', '_')}.jpg"
                tour.image.save(filename, ContentFile(response.content), save=True)
                print(f"Successfully updated {tour.title}")
            else:
                print(f"Failed to download image for {tour.title}: Status {response.status_code}")
        except Exception as e:
            print(f"Error updating {tour.title}: {e}")

if __name__ == "__main__":
    update_images()
    print("Done!")
