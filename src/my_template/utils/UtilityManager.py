import torch
import numpy as np
import random
import os

class UtilityManager:
  def __init__(self) -> None:
    self._get_root_path()

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

  def _get_root_path(self) -> None:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
      if os.path.exists(os.path.join(current_dir, '.git')):
        self._root_path = current_dir
        break
      parent_dir = os.path.dirname(current_dir)
      if parent_dir == current_dir:
        self._root_path = None
      current_dir = parent_dir
  
  @property
  def root_path(self) -> str:
    assert aelf._root_path is not None,"Root Path is Not valid"
    return self._root_path

  @property
  def config_path(self) -> str:
    
    return os.path.join(self.root_path,"config/config.yaml")