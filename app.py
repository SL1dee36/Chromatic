# app.py

from flask import Flask, render_template
from src.manager import ChromaticManager

app = Flask(__name__)
chromatic_manager = ChromaticManager(app)

@app.route('/')
def index():
    button_css = chromatic_manager.generate_css(
        'button',
        color='blue',
        padding='10px 20px',
        font_size='16px',
        border_radius='10px',
        box_shadow='2px 2px 4px rgba(0, 0, 0, 0.5)',
    )

    heading_css = chromatic_manager.generate_css(
        'heading',
        font_size='36px',
        font_weight='normal',
        text_align='center',
        color='blue',
        text_decoration='underline',
    )

    paragraph_css = chromatic_manager.generate_css(
        'paragraph',
        font_size='18px',
        text_align='justify',
    )

    link_css = chromatic_manager.generate_css(
        'link',
        color='green',
        hover_color='darkgreen',
    )

    return render_template('index.html', button_css=button_css, heading_css=heading_css,
                           paragraph_css=paragraph_css, link_css=link_css)

if __name__ == '__main__':
    app.run(debug=True)