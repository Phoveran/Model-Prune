import numpy as np
import torch
import random

def set_seed(seed):
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    random.seed(seed) 
    torch.backends.cudnn.deterministic = True

def gen_folder_name(args):
    def get_attr(inst, arg):
        value = getattr(inst, arg)
        if isinstance(value, float):
            return f"{value:.4f}"
        else:
            return value
    folder_name = ''
    for arg in vars(args):
        folder_name += f'{arg}-{get_attr(args, arg)}~'
    return folder_name[:-1]
