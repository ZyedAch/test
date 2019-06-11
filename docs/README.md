# Test

## Installation

The code has been tested in Python 3.6.5 & into a Linux environment.

Install requirements:

```bash
$ pip install -r requirements.txt
```

Install package from the package directory:
```bash
$ pip install .
```

## Generate documentation

Go to `test/docs` and execute the following code:

```bash
$ make html
```

You can check the html documentation if you open this file in an internet browser : 

`test/docs/build/html/index.html`


## Usage

Both of them need to be executed from the location of the ```Brisbane_CityBike.json``` or its location must be specified using the ```--out-dir``` argument.  

### build-clusters
Use it to generate output file.

```bash
usage: build-clusters [-h] 
                      [--out-dir OUTDIR]
                      [--input-file INPUT_FILE]


optional arguments:
  -h, --help                show this help message and exit
  --out-dir OUTDIR          directory where the result will be
  --input-file INPUT_FILE   json file containing input data
```

#### Output Description

The result (csv file) will be automatically uploaded to the output directory.

__Columns Description__
* ```id``` : bike id
* ```clusters``` : bike cluster