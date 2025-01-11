import qrcode, streamlit

streamlit.title("QR Code Generator")
url = streamlit.text_input(label='URL:', placeholder='Start typing any URL...')
generate = streamlit.button(label='Generate')
if url and generate:
    qr = qrcode.make(url)
    qr.save('qr.png')
    streamlit.image('qr.png')