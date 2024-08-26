# src/func.py

class ButtonCSSGenerator:
    """
    Класс для генерации CSS для кнопок.
    """

    def generate(self, color='blue', padding='10px 20px', font_size='16px',
                 border_radius='5px', border_width='1px', border_color='black',
                 background_hover='lightblue', text_color='white',
                 text_hover='black', box_shadow=None, transition='all 0.3s ease'):
        """
        Генерирует CSS для кнопки.

        Args:
            color (str): Цвет фона кнопки.
            padding (str): Отступы кнопки.
            font_size (str): Размер шрифта кнопки.
            border_radius (str): Радиус скругления углов кнопки.
            border_width (str): Толщина границы кнопки.
            border_color (str): Цвет границы кнопки.
            background_hover (str): Цвет фона кнопки при наведении.
            text_color (str): Цвет текста кнопки.
            text_hover (str): Цвет текста кнопки при наведении.
            box_shadow (str): Тень кнопки (например, '2px 2px 4px rgba(0, 0, 0, 0.5)').
            transition (str): Эффект перехода при наведении (например, 'all 0.3s ease').

        Returns:
            str: Сгенерированный CSS-код.
        """
        css = f"""
        .button {{
            background-color: {color};
            padding: {padding};
            font-size: {font_size};
            border-radius: {border_radius};
            border: {border_width} solid {border_color};
            color: {text_color};
            transition: {transition};
        }}

        .button:hover {{
            background-color: {background_hover};
            color: {text_hover};
        }}
        """

        if box_shadow:
            css += f"""
        .button {{
            box-shadow: {box_shadow};
        }}
        """

        return css
    
class HeadingCSSGenerator:
    """
    Класс для генерации CSS для заголовков.
    """

    def generate(self, font_size='24px', font_weight='bold', text_align='left',
                 color='black', text_decoration='none', font_family='sans-serif',
                 line_height='1.5', letter_spacing='normal', text_transform='none'):
        """
        Генерирует CSS для заголовка.

        Args:
            font_size (str): Размер шрифта заголовка.
            font_weight (str): Жирность шрифта заголовка (например, 'normal', 'bold', 'bolder', 'lighter', или число от 100 до 900).
            text_align (str): Выравнивание текста ('left', 'center', 'right', 'justify').
            color (str): Цвет текста заголовка.
            text_decoration (str): Декорация текста ('none', 'underline', 'overline', 'line-through').
            font_family (str): Семейство шрифтов (например, 'Arial', 'Helvetica', 'sans-serif').
            line_height (str): Межстрочный интервал.
            letter_spacing (str): Интервал между буквами (например, 'normal', '1px', '2px').
            text_transform (str): Трансформация текста ('none', 'uppercase', 'lowercase', 'capitalize').

        Returns:
            str: Сгенерированный CSS-код.
        """
        css = f"""
        .heading {{
            font-size: {font_size};
            font-weight: {font_weight};
            text-align: {text_align};
            color: {color};
            text-decoration: {text_decoration};
            font-family: {font_family};
            line-height: {line_height};
            letter-spacing: {letter_spacing};
            text-transform: {text_transform};
        }}
        """

        return css
    
class ParagraphCSSGenerator:
    """
    Класс для генерации CSS для параграфов.
    """

    def generate(self, font_size='16px', font_weight='normal', text_align='left',
                 color='black', line_height='1.5', letter_spacing='normal',
                 text_indent='0px', margin_bottom='1em'):
        """
        Генерирует CSS для параграфа.

        Args:
            font_size (str): Размер шрифта.
            font_weight (str): Жирность шрифта.
            text_align (str): Выравнивание текста.
            color (str): Цвет текста.
            line_height (str): Межстрочный интервал.
            letter_spacing (str): Интервал между буквами.
            text_indent (str): Отступ первой строки.
            margin_bottom (str): Нижний отступ.

        Returns:
            str: Сгенерированный CSS-код.
        """
        css = f"""
        .paragraph {{
            font-size: {font_size};
            font-weight: {font_weight};
            text-align: {text_align};
            color: {color};
            line-height: {line_height};
            letter-spacing: {letter_spacing};
            text-indent: {text_indent};
            margin-bottom: {margin_bottom};
        }}
        """

        return css

class LinkCSSGenerator:

    """
    Класс для генерации CSS для ссылок.
    """

    def generate(self, color='blue', text_decoration='underline',
                 hover_color='darkblue', hover_text_decoration='none'):
        """
        Генерирует CSS для ссылки.

        Args:
            color (str): Цвет ссылки.
            text_decoration (str): Декорация текста.
            hover_color (str): Цвет ссылки при наведении.
            hover_text_decoration (str): Декорация текста при наведении.

        Returns:
            str: Сгенерированный CSS-код.
        """
        css = f"""
        .link {{
            color: {color};
            text-decoration: {text_decoration};
        }}

        .link:hover {{
            color: {hover_color};
            text-decoration: {hover_text_decoration};
        }}
        """

        return css
    



