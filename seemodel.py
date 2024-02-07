import argparse
import os

import paddle
import yaml

from medicalseg.cvlibs import Config
from medicalseg.utils import logger

model = paddle.load('D:\python\MedicalSeg\pretrained_model\model.pdparams')
print(model)