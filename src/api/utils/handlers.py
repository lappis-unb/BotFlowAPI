from tempfile import TemporaryFile

def handle_uploaded_file(f):
    tmp = TemporaryFile(mode='w+b')
    for chunk in f.chunks():
        tmp.write(chunk)

    tmp.seek(0)

    return tmp