import numpy as np
import torch
import argparse
parser = argparse.ArgumentParser(description='Point Cloud Registration')
parser.add_argument('--n', type=int, default=1024, metavar='N',
                        help='Num of subsampled points to use')
args = parser.parse_args()
n = args.n
a = torch.rand((n,1024,1024)).cuda()
while(1):
    a.matmul(a)