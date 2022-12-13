# Sample Project
Change `sample` to the respective project name in
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

## Use Environment
before working on the project always make sure you have the environment activated:
```sh
$ conda activate sample
```
## Additional Information
See "About Readmes" on Github
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
