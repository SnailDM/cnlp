def get_common_vocab():
    with open("/tmp/cnlp/vocab.txt", "r", encoding="utf-8") as f_vocab:
        vocab_list = []
        for line in f_vocab:
            vocab_list.append(line.strip("\n"))
        return vocab_list
