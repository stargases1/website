"""
All website text and business details live in this one file.
Edit the values here, push to GitHub, and Render redeploys the site.

Lines marked  # CONFIRM  are placeholder values that still need to be
checked with Star Industrial Gases.
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
}

# Each gas: "specs" is a list of (label, [values]). The "Purity" value is shown large.
PRODUCTS = [
    {
        "id": "oxygen",
        "formula": "O<sub>2</sub>",
        "formula_text": "O2",
        "name": "Oxygen",
        "summary": "Industrial oxygen for gas cutting, welding and brazing.",
        "specs": [
            ("Purity", ["99.5%"]),                                     # CONFIRM
            ("Cylinder size", ["7 m³ (47 L) cylinder"]),               # CONFIRM
        ],
        "uses": ["Gas cutting of steel", "Oxy-fuel welding and brazing", "Metal fabrication shops"],
    },
    {
        "id": "carbon-dioxide",
        "formula": "CO<sub>2</sub>",
        "formula_text": "CO2",
        "name": "Carbon dioxide",
        "summary": "CO₂ for MIG welding, beverages and fire extinguisher refilling.",
        "specs": [
            ("Purity", ["99.9%"]),                                     # CONFIRM
            ("Cylinder size", ["30 kg cylinder"]),                     # CONFIRM
        ],
        "uses": ["MIG / CO₂ welding", "Soda and beverage dispensing", "Fire extinguisher refilling"],
    },
    {
        "id": "nitrogen",
        "formula": "N<sub>2</sub>",
        "formula_text": "N2",
        "name": "Nitrogen",
        "summary": "Inert nitrogen, as compressed gas or liquid, for purging, testing and cooling.",
        "specs": [
            ("Purity", ["99.99%"]),                                    # CONFIRM
            ("Available as", ["Gas: 7 m³ (47 L) cylinder", "Liquid nitrogen"]),  # CONFIRM
        ],
        "uses": ["Pipeline purging and pressure testing", "Food packaging", "Liquid nitrogen for cooling and freezing"],
    },
    {
        "id": "argon",
        "formula": "Ar",
        "formula_text": "Ar",
        "name": "Argon",
        "summary": "Argon in three grades, for TIG welding through to laboratory work.",
        "specs": [
            ("Grades", ["Commercial", "Grade 1", "UHP (ultra high purity)"]),
            ("Cylinder size", ["7 m³ (47 L) cylinder"]),               # CONFIRM
        ],
        "uses": ["TIG welding", "Stainless steel and aluminium welding", "Laboratory and analytical use (UHP)"],
    },
    {
        "id": "dissolved-acetylene",
        "formula": "C<sub>2</sub>H<sub>2</sub>",
        "formula_text": "DA",
        "formula_size": "long",
        "name": "Dissolved acetylene (DA)",
        "short_name": "DA",
        "summary": "Acetylene fuel gas for oxy-acetylene cutting, welding and heating.",
        "specs": [
            ("Supplied in", ["DA cylinders"]),                         # CONFIRM sizes
        ],
        "uses": ["Oxy-acetylene gas cutting", "Gas welding and brazing", "Heating and flame work"],
    },
    {
        "id": "gas-mixtures",
        "formula": "Mix",
        "formula_text": "mixture",
        "name": "Gas mixtures",
        "summary": "Shielding gas mixtures for cleaner, more consistent welds.",
        "specs": [
            ("Mixtures", ["Argon + CO₂", "Other blends on request"]),  # CONFIRM
        ],
        "uses": ["MIG welding of mild steel", "Stainless steel welding", "Mixtures made to your requirement"],
    },
]

INDUSTRIES = [
    ("Power plants", "Gases for maintenance, purging and testing."),
    ("Fertiliser and chemical plants", "Purging, blanketing and pressure testing."),
    ("Metal and steel industry", "Cutting, welding and processing of metals."),
    ("Fabrication and welding", "Workshops cutting, welding and joining steel."),
    ("Engineering and manufacturing", "Production units in Kota's industrial areas."),
    ("Food and beverage", "CO₂ for soda and nitrogen for packaging."),
    ("Fire safety", "CO₂ for refilling fire extinguishers."),
    ("Laboratories and institutes", "UHP argon and nitrogen for testing and research."),
]

# Client logos: save each file as static/img/clients/<slug>.png (or .svg / .jpg / .webp).
# Until a logo file exists, the client's name is shown instead.
CLIENTS = [
    ("dcm", "DCM Shriram"),                              # CONFIRM name
    ("om-metals", "Om Metals"),
    ("multimetals", "Multimetals"),
    ("cfcl", "Chambal Fertilisers (CFCL)"),
    ("kota-thermal", "Kota Super Thermal Power Station"),  # CONFIRM name
]
