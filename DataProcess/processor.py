from ollama_api import OllamaAPI


# define how to process images and save output
def processor1():
    model_name = ['qwen3-vl:8b', 'gemma3:4b']
    operator = OllamaAPI(model_name[1])
    prompt_path = "/home/hhy/hhy-data/Python/textVPR/DataProcess/prompt/prompt1.md"
    images_list = ['/home/hhy/t.jpg']

    # read prompt from txt file
    prompt_text = ''
    with open(prompt_path, 'r') as f:
        prompt_text = f.read()

    # for each image, implement the process
    for i in images_list:
        operator.generate_message(prompt_text, 'user', image_paths=[i])
        with open('test.txt', 'w') as f:
            pass
        operator.send(is_to_file = True, file_path = '/home/hhy/hhy-data/Python/textVPR/DataProcess/test.txt')


processor1()