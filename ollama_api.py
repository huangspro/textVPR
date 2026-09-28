import ollama

class OllamaAPI:
    def __init__(self, 
        model_name:str = '', 
        has_image:bool = False, 
        is_stream:bool = False, 
        has_memory:bool = False, 
        memory_length:int = 0,
        
    ):
        self.model_name = model_name
        self.has_image = has_image
        self.is_stream = is_stream
        self.has_memory = has_memory
        self.memory_length = memory_length
        
        self.messages = [] # store all the messages. If has_momery is True, this list will be appended, else, it will keep the latest message

    # geenrate a message, append it into the messages list
    def generate_message(self, prompt:str = '', role:str = 'user', image_paths:list = []):
        message={
                'role': role,
                'content': prompt,
                'images': image_paths if self.has_image else ''
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
    def send(self, is_to_file:str = False, file_path:str = '', save_mode:str = 'w'):
        # construct response
        # if the is_to_file is True, we shoule put the output of the model at once, not in stream
        if is_to_file==True:
            response = ollama.chat(model=self.model_name, messages=self.messages, stream = False)
        else:
            response = ollama.chat(model=self.model_name, messages=self.messages, stream = self.is_stream)
        
        # save to file
        if is_to_file:
            with open(file_path, save_mode) as f:
                f.write(response['message']['content'])
            
        # output the text output directly
        else:
            for chunk in stream:
                 print(chunk['message']['content'], end='', flush=True)
    
    def clear_context():
        self.message = []
        
tem = OllamaAPI('gemma3:4b', has_image = True)
tem.generate_message('describe the scene in the image', image_paths = ['/home/hhy/t.jpg'])
tem.send(True, './ok.txt', 'w')
