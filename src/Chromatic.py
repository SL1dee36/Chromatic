# Chromatic.py
from src.func import ButtonCSSGenerator, HeadingCSSGenerator, ParagraphCSSGenerator, LinkCSSGenerator

class Chromatic:
    """
    Основной класс для генерации CSS.
    """

    def __init__(self):
        self.button_generator = ButtonCSSGenerator()
        self.heading_generator = HeadingCSSGenerator()
        self.paragraph_generator = ParagraphCSSGenerator()
        self.link_generator = LinkCSSGenerator()

    def generate_css(self, element_type, **kwargs):
        """
        Генерирует CSS для заданного типа элемента.

        Args:
            element_type (str): Тип элемента.
            **kwargs: Параметры для генерации CSS.

        Returns:
            str: Сгенерированный CSS-код.
        """
        if element_type == 'button':
            return self.button_generator.generate(**kwargs)
        elif element_type == 'heading':
            return self.heading_generator.generate(**kwargs)
        elif element_type == 'paragraph':
            return self.paragraph_generator.generate(**kwargs)
        elif element_type == 'link':
            return self.link_generator.generate(**kwargs)
        else:
            raise ValueError(f"Неподдерживаемый тип элемента: {element_type}")

    def button(self):
        return ButtonStyleBuilder(self.button_generator)

class ButtonStyleBuilder:

    def __init__(self, generator) -> None:
        self.generator = generator
        self.params = {}

    def color(self, color):
        self.params['color'] = color
        return self
    
    def padding(self, padding):
        self.params['padding'] = padding
        return self
    
    def font_size(self, font_size):
        self.params['font_size'] = font_size
        return self
    
    def generate(self):
        return self.generator.generate(**self.params)
    
