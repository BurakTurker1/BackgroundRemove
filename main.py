from rembg.bg import remove
from PIL import Image

input_path = 'input.jpeg'#Orjinal fotograf
output_path = 'output.png'#arkaplan silinmiş hali

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
