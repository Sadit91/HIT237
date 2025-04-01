# pests/pests_data.py
class PItem:
    def __init__(self, id, name, description, image, details):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.details = details

class FungalPest(PItem):
    def __init__(self, id, name, description, image, details, treatment):
        super().__init__(id, name, description, image, details)
        self.treatment = treatment

class InsectPest(PItem):
    def __init__(self, id, name, description, image, details, control_method):
        super().__init__(id, name, description, image, details)
        self.control_method = control_method

# Create instances with varied data
itms = [
    FungalPest(1, "Anthracnose", "Fungal disease...", "https://ex.com/anth.jpg", "Causes fruit drop", "Apply fungicide X"),
    InsectPest(2, "Fruit Fly", "Insect pest...", "https://ex.com/ffly.jpg", "Damages fruits", "Use traps Y"),
    # Add additional items...
]
