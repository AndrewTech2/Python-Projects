import streamlit, Pylette, rgb2hex

streamlit.title("Colour Palette Generator")
image = streamlit.file_uploader("Image to generate (PNG, JPG, JPEG):", type=['png', 'jpg', 'jpeg'])
submit = streamlit.button("Submit")
if submit and image:
    colors = Pylette.extract_colors(image.read(), 10)
    streamlit.header("Most common 10 HEX colors")
    count = 1
    for color in colors:
        streamlit.write(f"{count}. {rgb2hex.rgb2hex(color.rgb)}")
        count += 1