
from fastapi import FastAPI,File
from fastapi.responses import FileResponse
import replicate

app = FastAPI()

api_token = "r8_PheLahCKZKwoZtIs5T6Q6Vnx6eTJh2F3Nzcbz"
client = replicate.Client(api_token=api_token)
def genimg(prompt):
    output = client.run(
    "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
    input={"prompt": prompt}
    )
    return output[0]



@app.get("/generate-image/")
def generate_image(prompt: str):
    image_filename = genimg(prompt)
    return {"image_url": image_filename}

