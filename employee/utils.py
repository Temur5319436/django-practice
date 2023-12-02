from control.settings import BASE_DIR
from django.core.files.uploadedfile import InMemoryUploadedFile
from datetime import datetime


def store_image(image: InMemoryUploadedFile):
    contents = image.read()

    path = "/storage/images/" + str(int(datetime.now().timestamp())) + ".jpg"

    with open(f"{BASE_DIR}{path}", "wb") as f:
        f.write(contents)

    return path
