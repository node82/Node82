def unzip():
    import zipfile
    filePath = '$PATH'
    extractPath = '$EPATH'
    with zipfile.ZipFile(filePath, 'r') as zip_ref:
        zip_ref.extractall(extractPath)
    
unzip()
