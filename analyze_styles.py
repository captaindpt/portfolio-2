import sys
import requests
from bs4 import BeautifulSoup
import re

def find_potential_main_content(soup):
    # Heuristics to find the main content area
    main_tags = soup.find_all('main')
    if main_tags:
        return main_tags[0]
    article_tags = soup.find_all('article')
    if article_tags:
        return article_tags[0]
    # Look for divs with common content-related classes/ids
    for class_name in ['content', 'post', 'entry', 'main-content', 'body']:
        elements = soup.find_all(class_=re.compile(class_name, re.I))
        if elements:
            # Find the largest one, potentially? Or the first? Let's try first.
            return elements[0]
    for id_name in ['content', 'main', 'post', 'body']:
        element = soup.find(id=id_name)
        if element:
            return element
    # Fallback to body if nothing specific is found
    return soup.body

def analyze_url(url):
    print(f"Attempting to analyze: {url}")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    print("\n--- Linked Stylesheets ---")
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href')
        if href:
            # Simple check if it's a relative or absolute URL
            if href.startswith('//'):
                 href = 'https:' + href
            elif href.startswith('/'):
                 # Attempt to construct full URL (basic)
                 from urllib.parse import urljoin
                 href = urljoin(url, href)
            print(href)

    print("\n--- Inline Styles (<style> tags) ---")
    # Note: Printing entire inline styles can be very long. Just indicating presence.
    style_tags = soup.find_all('style')
    if style_tags:
        print(f"Found {len(style_tags)} inline <style> tag(s). Content not printed.")
        # You could optionally print soup.find('style').string[:500] + '...' if needed

    print("\n--- Potential Main Content Analysis ---")
    main_content = find_potential_main_content(soup)
    if main_content:
        print(f"Found potential main content container: <{main_content.name}> (approx.)")

        # Look for common text elements within the main content
        paragraphs = main_content.find_all('p', limit=1)
        headings = main_content.find_all(['h1', 'h2', 'h3'], limit=1)

        if paragraphs:
            p_tag = paragraphs[0]
            print(f"  Sample paragraph (<p>) classes: {p_tag.get('class')}")
            print(f"  Sample paragraph inline style: {p_tag.get('style')}")
        else:
             print("  No <p> tags found in potential main content.")

        if headings:
             h_tag = headings[0]
             print(f"  Sample heading (<{h_tag.name}>) classes: {h_tag.get('class')}")
             print(f"  Sample heading inline style: {h_tag.get('style')}")
        else:
             print("  No <h1>, <h2>, or <h3> tags found in potential main content.")

    else:
        print("Could not identify a specific main content container.")

    print("\nNote: This script provides basic info. For detailed computed styles (font, size, spacing), use browser developer tools.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_styles.py <URL>")
        sys.exit(1)
    
    url_to_analyze = sys.argv[1]
    analyze_url(url_to_analyze) 