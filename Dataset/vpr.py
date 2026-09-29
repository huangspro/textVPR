"""
Haoyu Huang
The VPR/textVPR dataset has a different structure from other usual dataset
pitts30k
    ├── images
    │     ├── test
    │     │     ├── database/
    │     │     └── queries/
    │     ├── train
    │     │     ├── database/
    │     │     └── queries/
    │     └── val
    │         ├── database/
    │         └── queries/

images in database/ are used for training or searching
when training, the images are put into the models and do sth
when predicting, the search engine will use the images in query/ as queries and search results in the database/
"""

import torch
from torch.utils.data import Dataset
from pathlib import Path
from PIL import Image
from torchvision.transforms import v2

class VPRDataset(Dataset):
    def __init__(self, database_dir:str, query_dir:str, transform = None):
        self.database_dir = database_dir
        self.query_dir = query_dir
        self.transform = transform

        self.database = []
        self.queries = []

        self.load_database()
        self.load_queries()

    # load all the paths of images in the database/
    def load_database(self):
        database_folder = Path(self.database_dir)
        self.database = [str(file) for file in database_folder.iterdir() if file.is_file()]

    # load all the paths of images in the queries
    def load_queries(self):
        query_folder = Path(self.query_dir)
        self.queries = [str(file) for file in query_folder.iterdir() if file.is_file()]

    # return transformed image and its filename
    def get_item_from_database(self, idx:int):
        image = Image.open(self.database[idx]).convert("RGB")
        if self.transform is not None:
            image = self.transform(image)

        return (image, self.database[idx])

    # return transformed image and its filename
    def get_item_from_query(self, idx:int):
        image = Image.open(self.queries[idx]).convert("RGB")
        if self.transform is not None:
            image = self.transform(image)

        return (image, self.queries[idx])

    # here return the length of database, not queries
    def __len__(self):
        return len(self.database)

    # return (image, name)
    def __getitem__(self, idx):
        return self.get_item_from_database(idx)

transform = v2.Compose([
        v2.Resize((64, 64)),
        v2.ToImage(),
        v2.ToDtype(torch.float32, scale=True),
])
tem = VPRDataset("/home/hhy/Downloads/pitts30k/pitts30k/images/train/database", "/home/hhy/Downloads/pitts30k/pitts30k/images/train/queries", transform)
print(len(tem))
print(tem.get_item_from_query(0))
print(tem.get_item_from_query(0)[0].shape)
