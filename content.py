"""
All website text and business details live in this one file.
Edit the values here, push to GitHub, and Render redeploys the site.

Lines marked  # CONFIRM  are placeholder values that still need to be
checked with Star Industrial Gases before the site goes live.
"""

BUSINESS = {
    "name": "Star Industrial Gases",
    "site_url": "https://starindustrialgases.in",   # the live domain, no trailing slash
    "city": "Kota",
    "phone_display": "095714 36929",
    "phone_tel": "+919571436929",
    "whatsapp": "919571436929",          # country code + number, no spaces or +
    "email": "",                          # add an email address to show it on the site
    "address_lines": [
        "A1, E-132, Road Number 5",
        "Indraprastha Industrial Area",
        "Kota, Rajasthan 324005",
    ],
    "map_query": "Star Industrial Gases, A1 E-132, Rd Number 5, Indraprastha Industrial Area, Kota, Rajasthan 324005",
    "hours": "Monday to Saturday, 9:00 am to 7:00 pm",                 # CONFIRM
    "service_area": "Kota city and nearby industrial areas",          # CONFIRM
    "certifications": [],  # e.g. ["PESO licensed", "GST registered"]  # CONFIRM
}

PRODUCTS = [
    {
        "id": "oxygen",
        "formula": "O<sub>2</sub>",
        "formula_text": "O2",
        "name": "Oxygen",
        "summary": "Industrial oxygen for gas cutting, welding and brazing.",
        "purity": "99.5%",                                             # CONFIRM
        "sizes": ["7 m³ (47 L) cylinder", "1.5 m³ (10 L) cylinder"],   # CONFIRM
        "uses": ["Gas cutting of steel", "Oxy-fuel welding and brazing", "Metal fabrication shops"],
    },
    {
        "id": "carbon-dioxide",
        "formula": "CO<sub>2</sub>",
        "formula_text": "CO2",
        "name": "Carbon dioxide",
        "summary": "CO₂ for MIG welding, beverages and fire extinguisher refilling.",
        "purity": "99.9%",                                             # CONFIRM
        "sizes": ["30 kg cylinder", "22.5 kg cylinder"],               # CONFIRM
        "uses": ["MIG / CO₂ welding", "Soda and beverage dispensing", "Fire extinguisher refilling"],
    },
    {
        "id": "nitrogen",
        "formula": "N<sub>2</sub>",
        "formula_text": "N2",
        "name": "Nitrogen",
        "summary": "Inert nitrogen for purging, pressure testing and packaging.",
        "purity": "99.99%",                                            # CONFIRM
        "sizes": ["7 m³ (47 L) cylinder"],                             # CONFIRM
        "uses": ["Pipeline purging and pressure testing", "Food packaging", "Tyre and accumulator filling"],
    },
    {
        "id": "argon",
        "formula": "Ar",
        "formula_text": "Ar",
        "name": "Argon",
        "summary": "High-purity argon for TIG welding of stainless steel and aluminium.",
        "purity": "99.999%",                                           # CONFIRM
        "sizes": ["7 m³ (47 L) cylinder"],                             # CONFIRM
        "uses": ["TIG welding", "Stainless steel and aluminium welding", "Laboratory use"],
    },
]

INDUSTRIES = [
    ("Fabrication and welding", "Workshops cutting, welding and joining steel."),
    ("Engineering and manufacturing", "Production units in Kota's industrial areas."),
    ("Chemical and process plants", "Purging, blanketing and pressure testing."),
    ("Food and beverage", "CO₂ for soda and nitrogen for packaging."),
    ("Construction and infrastructure", "On-site cutting and welding for structures."),
    ("Fire safety", "CO₂ for refilling fire extinguishers."),
    ("Automobile workshops", "Welding, cutting and nitrogen tyre filling."),
    ("Laboratories and institutes", "Argon and nitrogen for testing and research."),
]

REASONS = [
    ("Local to Kota", "Our filling station is in Indraprastha Industrial Area, close to the workshops and factories we supply."),
    ("Order by phone or WhatsApp", "Tell us the gas, cylinder size and quantity. No forms or accounts."),
    ("Four core gases", "Oxygen, carbon dioxide, nitrogen and argon, so one supplier covers most workshop needs."),
    ("Refills and new cylinders", "Bring your empty cylinders for refilling, or ask us for new ones."),  # CONFIRM
]

ORDER_STEPS = [
    ("Call or WhatsApp us", "Reach us on 095714 36929."),
    ("Tell us what you need", "The gas, cylinder size and how many cylinders."),
    ("Collect or receive delivery", "Pick up from our station or ask about delivery to your site."),  # CONFIRM
]
