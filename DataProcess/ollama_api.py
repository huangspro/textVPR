import time

import ollama

class OllamaAPI:
    def __init__(self, 
        model_name:str = '', 
        has_image:bool = False, 
        is_stream:bool = False, 
        has_memory:bool = False, 
        memory_length:int = 10,
        is_think:bool = False
    ):
        self.model_name = model_name
        self.has_image = has_image
        self.is_stream = is_stream
        self.has_memory = has_memory
        self.memory_length = memory_length
        self.is_think = is_think

        self.messages = [] # store all the messages. If has_momery is True, this list will be appended, else, it will keep the latest message

    # generate a message, append it into the messages list
    def generate_message(self, prompt:str = '', role:str = 'user', image_paths:list = None):

        message={
                'role': role,
                'content': prompt,
                'images': image_paths if self.has_image is not None else ''
        }

        if self.has_memory is not True:
            self.messages = []
        while self.has_memory and len(self.messages) >= self.memory_length:
            self.messages.pop(0)
            
        self.messages.append(message)
        return message
        
    # send message and get reponse
    # user can choose wether to save the reponse to a file
    # save_mode: 'a'->append, 'w'->overwrite
    def send(self, is_to_file:bool = False, file_path:str = '', save_mode:str = 'w'):
        start = time.time()

        # construct response
        # if the is_to_file is True, we shoule put the output of the model at once, not in stream
        if is_to_file==True:
            response = ollama.chat(model=self.model_name, messages=self.messages, stream = False, think=self.is_think)
        else:
            response = ollama.chat(model=self.model_name, messages=self.messages, stream = self.is_stream, think = self.is_think)
        
        # save to file
        if is_to_file:
            print("Took ", time.time() - start, " to get output")
            with open(file_path, save_mode) as f:
                f.write(response['message']['content'])
            
        # output the text output directly
        else:
            for chunk in response:
                 print(chunk['message']['content'], end='', flush=True)
    
    def clear_context(self):
        self.message = []
        
