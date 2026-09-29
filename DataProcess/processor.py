from abc import ABC, abstractmethod
from ollama_api import OllamaAPI

class Processor(ABC):
    def __init__(self, prompt_path:str = '', images_paths:list = None):
        if images_paths is None:
            self.images_paths = []
        else:
            self.images_paths = images_paths
        self.prompt_path = prompt_path

    @abstractmethod
    def process(self):
        pass



class Processor1(Processor):
    def __init__(self, prompt_path:str = '', images_paths:list = None):
        super().__init__(prompt_path, images_paths)

    # define how to process images and save output
    def process(self):
        operator = OllamaAPI('qwen3-vl:8b')

        # read prompt from txt file
        prompt_text = ''
        with open(self.prompt_path, 'r') as f:
            prompt_text = f.read()

        # for each image, implement the process
        for i in self.images_paths:
            operator.generate_message(prompt_text, 'user', image_paths=[i])
            with open('test.txt', 'w') as f:
                pass
            operator.send(is_to_file=True, file_path= 'test.txt')



print("expe begin")
tem = Processor1("/home/hhy/hhy-data/Python/textVPR/DataProcess/prompt/prompt1.txt", ['/home/hhy/t.jpg'])
tem.process()