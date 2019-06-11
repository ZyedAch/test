#!/usr/bin/env python
import argparse
from project.clustering import build_clustering


def build_clusters():
    parser = argparse.ArgumentParser(description='Build clusters file')
    parser.add_argument('--out-dir', dest='outdir', default='./output/', type=str,
                        help='Directory where the result will be')
    parser.add_argument("--input-file", dest='input_file', default='Brisbane_CityBike.json',
                        type=str, help='json file containing input data')
    args = parser.parse_args()
    build_clustering(outdir=args.outdir,
                     input_file =args.input_file)
