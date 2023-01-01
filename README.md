# Sample Project
Change `sample` to the respective project name in
* filename of .yml file
* environment name in .yml-file
* in the commands below
## Python Environment Setup and Management
**Install** conda environment:
```sh
$ conda env create -f sample.yml
```
**Update** the environment with new packages/versions:
1. modify template.yml
2. run `conda env update`:
```sh
$ conda env update --name sample --file sample.yml --prune
```
`prune` uninstalls dependencies which were removed from sample.yml

**Use** environment:
before working on the project always make sure you have the environment activated:
```sh
$ conda activate sample
```

**Remove** environment:
```sh
$ conda env remove -n sample
```

**List** all installed environments:
```sh
$ conda env list
```
## Additional Information
See "About Readmes" on Github
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
