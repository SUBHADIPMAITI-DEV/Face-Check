from googlesearch import search
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import pytesseract
from PIL import Image
import random




# def fact_check_text(claim):
#     results = []
#     for url in search(claim, num_results=5):
#         try:
#             response = requests.get(url)
#             soup = BeautifulSoup(response.content, 'html.parser')
#             domain = urlparse(url).netloc
#             text = soup.get_text()
#             if claim.lower() in text.lower():
#                 results.append({"domain": domain, "link": url})
#         except Exception as e:
#             print("Error in fact_check_text:", e)  # Debugging
#     return results

def fact_check_text(claim):
    supporting_sources = []
    refuting_sources = []

    for url in search(claim, num_results=5):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            domain = urlparse(url).netloc
            text = soup.get_text()
            source = {
                "domain": domain,
                "link": url,
                "date": "Unknown"  # Placeholder for date extraction
            }
            # Randomly assign to supporting or refuting for demonstration purposes
            if random.choice([True, False]):
                supporting_sources.append(source)
            else:
                refuting_sources.append(source)
        except Exception as e:
            print("Error in fact_check_text:", e)

    confidence_score = round(random.uniform(0, 100), 2)

    # Debugging: Print the result to verify output
    result = {
        "claim": claim,
        "supporting_sources": supporting_sources,
        "refuting_sources": refuting_sources,
        "confidence_score": confidence_score
    }
    print("fact_check_text Result:", result)  # Debugging statement
    return result


def fact_check_image(image_path):
    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image).strip()
    except Exception as e:
        print("Error in fact_check_image:", e)
        return []

    if extracted_text:
        return fact_check_text(extracted_text)
    else:
        return []