import gradio as gr
import requests
from PIL import Image
import io
import urllib.parse

def aznik_style_transfer(input_image, style_prompt):
    if input_image is None or not style_prompt:
        return None
    
    formatted_prompt = urllib.parse.quote(f"{style_prompt}, masterpiece, highly detailed, 8k resolution")
    image_url = f"https://image.pollinations.ai/prompt/{formatted_prompt}?width=512&height=512&seed=42&nologo=true"
    
    response = requests.get(image_url)
    if response.status_code == 200:
        return Image.open(io.BytesIO(response.content))
    else:
        return None

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎨 Aznik AI Studio\n### Custom Photo Style Transfer & Filters Studio")
    with gr.Row():
        with gr.Column():
            img_in = gr.Image(label="Upload Photo")
            prompt_in = gr.Textbox(label="Enter Style Prompt", placeholder="e.g., 3D Pixar Cartoon, Anime, Oil Painting")
            btn = gr.Button("✨ Transform Image", variant="primary")
        with gr.Column():
            img_out = gr.Image(label="Aznik AI Result")

    btn.click(fn=aznik_style_transfer, inputs=[img_in, prompt_in], outputs=img_out)

demo.launch(server_name="0.0.0.0", server_port=7860)
