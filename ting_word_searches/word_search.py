def exists_word(word, instance):
    result = []
    word_lower = word.lower()

    for index in range(len(instance)):
        file_data = instance.search(index)
        occurrences = []
        for index, line in enumerate(file_data['linhas_do_arquivo']):
            if word_lower in line.lower():
                occurrences.append({"linha": index + 1})
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return result


def search_by_word(word, instance):
    result = []
    word_lower = word.lower()

    for index in range(len(instance)):
        file_data = instance.search(index)
        occurrences = []
        for index, line in enumerate(file_data['linhas_do_arquivo']):
            if word_lower in line.lower():
                occurrences.append({"linha": index + 1, "conteudo": line})
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return result
