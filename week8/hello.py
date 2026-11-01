import modal
from modal import Image

# Setup

app = modal.App("hello")  # names the Modal app.

# Image is Modal's recipe for the container your function runs in (OS + packages).
# Your laptop's libraries are not used unless you put them on this image.
# Image.debian_slim() starts from a small Debian Linux base with Python ("slim" = minimal OS).
# .pip_install("requests") installs requests inside that container; a local pip install does not count.
# We pass this image to @app.function so hello() runs in that environment.
image = Image.debian_slim().pip_install("requests")

# Hello!

# @app.function(image=image) registers a cloud function. When you call it via Modal, a container starts, runs the function, and shuts down.
# The function hits https://ipinfo.io/json and returns a string like Hello from São Paulo, São Paulo, BR!! — that city is where Modal placed the container, not where you are.
@app.function(image=image)
def hello() -> str:
    import requests

    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    city, region, country = data["city"], data["region"], data["country"]
    return f"Hello from {city}, {region}, {country}!!"


# New - added thanks to student Tue H.!

# Same idea, but region="eu" asks Modal to run in Europe, so the greeting should come from an EU location.
@app.function(image=image, region="eu")
def hello_europe() -> str:
    import requests

    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    city, region, country = data["city"], data["region"], data["country"]
    return f"Hello from {city}, {region}, {country}!!"
