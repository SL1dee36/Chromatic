# src/manager.py

from src.Chromatic import Chromatic

class ChromaticManager:
    def __init__(self,app=None):
        self.chromatic = Chromatic()
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.extensions['chromatic'] = self
        app.context_processor(self.context_processor)

    def context_processor(self):
        return dict(chromatic=self.chromatic)
    
    def generate_css(self, element_type, **kwargs):
        return self.chromatic.generate_css(element_type, **kwargs)