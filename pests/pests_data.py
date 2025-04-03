# pests/pests_data.py

class PestDiseaseItem:
    """
    A class representing a pest or disease affecting mangoes.
    
    Attributes:
        id (int): Unique identifier for the item.
        name (str): The name of the pest or disease.
        brief_description (str): A short description of the pest or disease.
        image_url (str): URL to an image representing the pest or disease.
        details (str): Detailed information about the pest or disease.
    """
    def __init__(self, id: int, name: str, brief_description: str, image_url: str, details: str) -> None:
        self.id = id
        self.name = name
        self.brief_description = brief_description
        self.image_url = image_url
        self.details = details

    def __repr__(self) -> str:
        return f"<PestDiseaseItem id={self.id} name={self.name}>"

# Multiple instances representing the items on the website.
ITEMS = [
    PestDiseaseItem(
        1, 
        "Anthracnose", 
        "Fungal disease with dark spots on fruits.", 
        "https://www.planetnatural.com/wp-content/uploads/2012/12/anthracnose-1.jpg", 
        "Anthracnose is a fungal disease causing fruit drop and lesions on mangoes."
    ),
    PestDiseaseItem(
        2, 
        "Powdery Mildew", 
        "White fungus on leaves.", 
        "https://www.gardendesign.com/pictures/images/400x320Exact_0x0/site_3/powdery-mildew-powdery-mildew-on-squash-leaf-shutterstock-com_13365.jpg", 
        "Powdery mildew affects mango leaves, reducing photosynthesis."
    ),
    PestDiseaseItem(
        3, 
        "Fruit Fly", 
        "Insect pest that damages fruits.", 
        "https://www.terro.com/media/Articles/TERRO/The-10-Most-Common-Fruit-Fly-Questions-Answered.jpg", 
        "Fruit flies lay eggs in mangoes, causing internal damage."
    ),
    PestDiseaseItem(
        4, 
        "Mealybug", 
        "Sap-sucking insect.", 
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Mealybugs_on_flower_stem%2C_Yogyakarta%2C_2014-10-31.jpg/960px-Mealybugs_on_flower_stem%2C_Yogyakarta%2C_2014-10-31.jpg", 
        "Mealybugs extract nutrients from the tree, leading to reduced growth."
    ),
    PestDiseaseItem(
        5, 
        "Scale Insect", 
        "Tiny insects that cling to leaves and stems.", 
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Wax_Scale.jpg/800px-Wax_Scale.jpg", 
        "Scale insects cluster on mango leaves and stems, inhibiting growth."
    ),
    PestDiseaseItem(
        6, 
        "Bacterial Canker", 
        "Bacterial disease causing cankers.", 
        "https://www.lovethegarden.com/sites/default/files/styles/og_image/public/content/articles/UK_advice-pests-diseases-bacterial-canker_main.jpg?itok=KT8LUF1p", 
        "Bacterial canker affects the bark and branches, reducing tree vigor."
    ),
    PestDiseaseItem(
        7, 
        "Leaf Spot", 
        "Fungal spots on leaves.", 
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/%27Cercospora_capsici.jpg/640px-%27Cercospora_capsici.jpg", 
        "Leaf spot reduces the photosynthetic area, often leading to defoliation."
    ),
]