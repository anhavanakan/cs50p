def main():
    file = input('File name: ').strip().lower()
    print(extension(file))

def extension(filename):
    if filename.find('.gif') > -1:
        return 'image/gif'
    elif filename.find('.jpg') > -1:
        return 'image/jpeg'
    elif filename.find('.jpeg') > -1:
        return 'image/jpeg'
    elif filename.find('.png') > -1:
        return 'image/png'
    elif filename.find('.pdf') > -1:
        return 'application/pdf'
    elif filename.find('.txt') > -1:
        return 'text/plain'
    elif filename.find('.zip') > -1:
        return 'application/zip'
    else:
        return 'application/octet-stream'

main()
