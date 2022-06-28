# Sample Project
Change `sample` to the reseptive project name in
* filename of .yml file
* environment name in .yml-file
* in the commands below
## Setup Environment
```sh
$ conda install -f sample.yml
```
## Update Environment from File
```sh
$ conda env update --name sample --file sample.yml --prune
```
`prune` uninstalls dependencies which were removed from sample.yml