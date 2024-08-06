import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return
    lines = txt_importer(path_file)
    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    instance.enqueue(file_data)
    print(file_data)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        removed_item = instance.dequeue()
        print(
            f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data)
    except IndexError:
        print("Posição inválida", file=sys.stderr)