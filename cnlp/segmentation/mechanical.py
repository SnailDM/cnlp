# 机械分词法
# 从文本中匹配字典中的文字，记录词语的位置（起点，终点），最后以 / 切分。

import re
import codecs


def get_char_dict(data_path):
    with codecs.open(data_path, "r", "utf-8") as f_dict:
        char_dict = f_dict.readlines()
    char_dict = [line.strip() for line in char_dict]
    return char_dict


def get_all_cut_postion(input_char, char_dict):
    # 遍历字典中的所有词，如果它存在于待分词文本中，就使用正则匹配它
    l_postions = []
    for char_item in char_dict:
        if char_item in input_char:
            # search 全局搜索，第一次就返回，所以使用这种方法会导致出现两次文本无法被匹配到，仅起到演示效果
            match_result = re.search(char_item, input_char)
            # 防御性判空
            if match_result:
                postion = match_result.span()
                # 保存分词位置
                l_postions.extend([p for p in postion])
                # 把匹配后的字符使用*替换，继续匹配
                input_char = input_char[:postion[0]] + "*"*len(char_item) + input_char[postion[1]:]

    # 将得到的切分位置列表去重后排序
    l_postions = list(sorted(set(l_postions)))
    # 这里的位置倒排是一个trick，可以解决迭代带来位置的变化的影响
    l_postions.reverse()
    return l_postions


def segmention(l_postions, input_char):
    # 使用位置对原待分词文本进行切分
    l_split_data = []
    for index in l_postions:
        l_split_data.append(input_char[index:])
        input_char = input_char[:index]
    l_split_data.reverse()
    return l_split_data


def run():
    input_char = "大家好，我是锅贴。什么是洗摸杯？张美丽人长得真好看！你好，欢迎来到南京市长江大桥参观。"
    copy_input_char = input_char[:]
    dict_path = "/tmp/cnlp/dict.txt"

    char_dict = get_char_dict(dict_path)
    postions = get_all_cut_postion(input_char, char_dict)
    l_split_data = segmention(postions, copy_input_char)
    # 最后用分隔符 / 连接文本列表
    result = " / ".join(l_split_data)
    print(result)


if __name__ == '__main__':
    run()
