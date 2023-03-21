import os

def change_file_extension(folder_path, old_extension, new_extension):
    # Loop para percorrer todos os arquivos na pasta e subdiretórios
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Verifica se o arquivo possui a extensão antiga
            if file.endswith(old_extension):
                # Separa o nome do arquivo da sua extensão atual
                basename, extension = os.path.splitext(file)
                
                # Concatena o novo nome do arquivo com a nova extensão
                new_filename = basename + new_extension
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_filename)
                
                # Renomeia o arquivo com a nova extensão
                os.rename(old_path, new_path)
                
                print(f"Arquivo renomeado de '{old_path}' para '{new_path}'.")

# Exemplo de uso
root_path = "C:/Users/Inforbyte/Downloads/Aprenda Power BI - Leonardo Karpinski/"
folder_name = "17-GRATUITO Playlist #aprendaPBI"
folder_path = root_path + folder_name
old_extension = ".ts"
new_extension = ".mp4"
change_file_extension(folder_path, old_extension, new_extension)