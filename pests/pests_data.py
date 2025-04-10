# Base class for Pest/Disease Items
class pdi:
    """
    A base class representing a pest or disease affecting mangoes.
    Common attributes shared by both pests and diseases.
    """
    def __init__(self, id: int, name: str, brief_description: str, image_url: str, details: str) -> None:
        self.id = id
        self.name = name
        self.brief_description = brief_description
        self.image_url = image_url
        self.details = details

    def __repr__(self) -> str:
        return f"<PestDiseaseItem id={self.id} name={self.name}>"

# Subclass for Fungal Diseases
class f_d01(pdi):
    """
    Represents a fungal disease affecting mangoes.
    Inherits from PestDiseaseItem, with possible additional attributes for fungal diseases.
    """
    def __init__(self, id: int, name: str, brief_description: str, image_url: str, details: str, severity: str) -> None:
        super().__init__(id, name, brief_description, image_url, details)
        self.severity = severity  # Specific to fungal diseases

    def __repr__(self) -> str:
        return f"<FungalDisease id={self.id} name={self.name} severity={self.severity}>"

# Subclass for Insect Pests
class ip(pdi):
    """
    Represents an insect pest affecting mangoes.
    Inherits from PestDiseaseItem, with possible additional attributes for insect pests.
    """
    def __init__(self, id: int, name: str, brief_description: str, image_url: str, details: str, infestation_rate: str) -> None:
        super().__init__(id, name, brief_description, image_url, details)
        self.infestation_rate = infestation_rate  # Specific to insect pests

    def __repr__(self) -> str:
        return f"<InsectPest id={self.id} name={self.name} infestation_rate={self.infestation_rate}>"

# Instances of pests and diseases using the subclasses
ITEMS = [
    f_d01(
        1, 
        "Anthracnose", 
        "Fungal disease with dark spots on fruits.", 
        "https://www.planetnatural.com/wp-content/uploads/2012/12/anthracnose-1.jpg", 
        "Anthracnose is a fungal disease causing fruit drop and lesions on mangoes.",
        "High"  # Severity level for fungal disease
    ),
    f_d01(
        2, 
        "Powdery Mildew", 
        "White fungus on leaves.", 
        "https://www.gardendesign.com/pictures/images/400x320Exact_0x0/site_3/powdery-mildew-powdery-mildew-on-squash-leaf-shutterstock-com_13365.jpg", 
        "Powdery mildew affects mango leaves, reducing photosynthesis.",
        "Moderate"
    ),
    ip(
        3, 
        "Fruit Fly", 
        "Insect pest that damages fruits.", 
        "https://www.terro.com/media/Articles/TERRO/The-10-Most-Common-Fruit-Fly-Questions-Answered.jpg", 
        "Fruit flies lay eggs in mangoes, causing internal damage.",
        "High"
    ),
    ip(
        4, 
        "Mealybug", 
        "Sap-sucking insect.", 
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Mealybugs_on_flower_stem%2C_Yogyakarta%2C_2014-10-31.jpg/960px-Mealybugs_on_flower_stem%2C_Yogyakarta%2C_2014-10-31.jpg", 
        "Mealybugs extract nutrients from the tree, leading to reduced growth.",
        "Moderate"
    ),
    ip(
        5, 
        "Scale Insect", 
        "Tiny insects that cling to leaves and stems.", 
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Wax_Scale.jpg/800px-Wax_Scale.jpg", 
        "Scale insects cluster on mango leaves and stems, inhibiting growth.",
        "Low"
    ),
    f_d01(
        6, 
        "Bacterial Canker", 
        "Bacterial disease causing cankers.", 
        "https://www.lovethegarden.com/sites/default/files/styles/og_image/public/content/articles/UK_advice-pests-diseases-bacterial-canker_main.jpg?itok=KT8LUF1p", 
        "Bacterial canker affects the bark and branches, reducing tree vigor.",
        "Severe"
    ),
    f_d01(
        7, 
        "Leaf Spot", 
        "Fungal spots on leaves.", 
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/%27Cercospora_capsici.jpg/640px-%27Cercospora_capsici.jpg", 
        "Leaf spot reduces the photosynthetic area, often leading to defoliation.",
        "Moderate"
    ),
]
