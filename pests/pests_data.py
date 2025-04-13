
# Pest and Disease Item Base Class
class pdi:
    def __init__(self, id: int, name: str, brief_description: str, image_url: str, details: str, control: str, impact: str) -> None:
        self.id = id
        self.name = name
        self.brief_description = brief_description
        self.image_url = image_url
        self.details = details
        self.control = control
        self.impact = impact

# Fungal Disease Subclass
class f_d01(pdi):
    def __init__(self, id: int, name: str, brief_description: str, image_url: str, details: str, control: str, impact: str, severity: str) -> None:
        super().__init__(id, name, brief_description, image_url, details, control, impact)
        self.severity = severity

# Insect Pest Subclass
class ip(pdi):
    def __init__(self, id: int, name: str, brief_description: str, image_url: str, details: str, control: str, impact: str, infestation_rate: str) -> None:
        super().__init__(id, name, brief_description, image_url, details, control, impact)
        self.infestation_rate = infestation_rate

# List of Items
ITEMS = [
    f_d01(
        1,
        "Anthracnose",
        "Fungal disease with dark spots on fruits.",
        "https://www.planetnatural.com/wp-content/uploads/2012/12/anthracnose-1.jpg",
        "Anthracnose is caused by Colletotrichum gloeosporioides. It causes dark lesions on mangoes, resulting in premature fruit drop and reduced marketability.",
        "Apply copper-based fungicides during flowering. Ensure proper pruning for air circulation and avoid overhead irrigation.",
        "Leads to fruit spoilage and significant reduction in yield during peak seasons.",
        "High"
    ),
    f_d01(
        2,
        "Powdery Mildew",
        "White powdery growth on young leaves and flowers.",
        "https://www.gardendesign.com/pictures/images/400x320Exact_0x0/site_3/powdery-mildew-powdery-mildew-on-squash-leaf-shutterstock-com_13365.jpg", 
        "Caused by Oidium mangiferae, it forms a white powder-like layer over the surface, hampering fruit development and reducing flower viability.",
        "Use sulfur-based sprays early in bloom. Improve air circulation through pruning.",
        "Severely reduces fruit set and results in unmarketable yields.",
        "Moderate"
    ),
    ip(
        3,
        "Fruit Fly",
        "Insect pest that damages fruits.",
        "https://www.terro.com/media/Articles/TERRO/The-10-Most-Common-Fruit-Fly-Questions-Answered.jpg", 
        "Fruit flies lay eggs inside ripening mangoes. Larvae feed on pulp, causing rotting and fruit drop.",
        "Use pheromone traps to monitor populations. Remove fallen fruits and apply bait sprays during fruit development.",
        "Damages internal fruit quality, causing economic loss and export rejections.",
        "High"
    ),
    ip(
        4,
        "Mango Hopper",
        "Sap-sucking pest that causes flower shedding.",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Mealybugs_on_flower_stem%2C_Yogyakarta%2C_2014-10-31.jpg/960px-Mealybugs_on_flower_stem%2C_Yogyakarta%2C_2014-10-31.jpg", 
        "Mango hoppers suck sap from inflorescences and young shoots. Their excretion encourages fungal growth, severely affecting pollination and fruit set.",
        "Use insecticides like imidacloprid pre- and post-flowering. Maintain orchard sanitation and prune infested branches.",
        "Can lead to nearly 60% flower drop under heavy infestation, lowering yield.",
        "Severe"
    ),
    f_d01(
        5,
        "Sooty Mold",
        "Black coating on leaves caused by honeydew excretion.",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Wax_Scale.jpg/800px-Wax_Scale.jpg", 
        "Sooty mold is a black fungus that grows on sugary honeydew. It reduces photosynthesis and impacts leaf health.",
        "Control honeydew-producing pests. Wash leaves with soap solution or prune heavily affected areas.",
        "Impairs photosynthesis and causes fruit blemishes reducing visual appeal.",
        "Low"
    ),
    ip(
        6,
        "Mealybug",
        "White waxy insect causing leaf curling and black mold.",
        "https://www.lovethegarden.com/sites/default/files/styles/og_image/public/content/articles/UK_advice-pests-diseases-bacterial-canker_main.jpg?itok=KT8LUF1p", 
        "Mealybugs attack trunk bases and tender shoots. Their wax and excretion promote mold development.",
        "Use grease bands and scrape trunk bark. Apply chlorpyrifos or neem oil during early infestation.",
        "Weakens trees and restricts flowering in severe cases.",
        "Moderate"
    ),
    ip(
        7,
        "Scale Insect",
        "Hard-shelled pest on stems sucking plant sap.",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/%27Cercospora_capsici.jpg/640px-%27Cercospora_capsici.jpg", 
        "Scales settle on bark and branches, appearing like crusty spots. They weaken branches by continuous sap-sucking.",
        "Introduce predatory beetles or apply horticultural oil in early infestation. Avoid over-fertilization.",
        "Leads to canopy thinning and long-term reduction in fruiting potential.",
        "Moderate"
    )
]
