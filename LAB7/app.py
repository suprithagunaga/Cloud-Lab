[vi app.py]
from PIL import Image
import os
input_path='/data/input/image.jpg'
output_path='/data/output/resized.jpg'
print("Resizing image...")
image=Image.open(input_path)
image=image.resize((300,300))
image.save(output_path)
print("Image resized and saved!")

[vi Dockerfile]
FROM python:3.11-slim
RUN pip install pillow
WORKDIR /app
COPY app.py .
CMD ["python","app.py"]

[vi app.py]
from PIL import Image,ImageDraw,ImageFont
import os
input_path='/data/output/resized.jpg'
output_path='/data/output/watermarked.jpg'
print("Adding Watermark...")
image=Image.open(input_path)
draw=ImageDraw.Draw(image)
font=ImageFont.load_default()
draw.text((50,50),"Sample Watermark",fill=(0,255,128),font=font)
image.save(output_path)
print("Watermarked image saved!")


docker build -t resize-image ./resize
docker build -t watermark-image ./watermark
wget -O input/image.jpg https://picsum.photos/600/400


docker run --rm -v $(pwd)/input:/data/input -v $(pwd)/output:/data/output resize-image
docker run --rm -v $(pwd)/input:/data/input -v $(pwd)/output:/data/output watermark-image
python3 -m http.server 8080
