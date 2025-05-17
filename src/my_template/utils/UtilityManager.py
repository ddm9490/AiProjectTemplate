import torch
import numpy as np
import random
import os

class UtilityManager:
  def __init__(self) -> None:
    pass

  def set_seed(self,seed_value : int = 42) -> None:
    """Set seed for reproducibility."""
    np.random.seed(seed_value)
    torch.manual_seed(seed_value)
    torch.cuda.manual_seed(seed_value)
    torch.cuda.manual_seed_all(seed_value)  # if you are using multi-GPU.
    random.seed(seed_value)
    os.environ['PYTHONHASHSEED'] = str(seed_value)

    # The below two lines are for deterministic algorithm behavior in CUDA
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
  def get_root_path(self) -> str:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
      if os.path.exists(os.path.join(current_dir, '.git')):
        return current_dir
      parent_dir = os.path.dirname(current_dir)
      if parent_dir == current_dir:
        return None
      current_dir = parent_dir
