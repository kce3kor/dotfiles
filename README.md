## Generate ssh key and link to github

```zsh
ssh-keygen -t rsa -b 4096 -C "ayusk.kumar.shah@gmail.com"
eval "$(ssh-agent -s)"
gedit ~/.ssh/config
```

Add these lines:
```
Host *
  AddKeysToAgent yes
  IgnoreUnknown UseKeychain
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa
```

```zsh
ssh-add ~/.ssh/id_rsa
```

### Add the key to github

```zsh
alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'

cat ~/.ssh/id_rsa.pub | pbcopy
pbpaste
# Then paste to github
```


## Conda Commands


- create new environment
```bash
conda create -n myenv python=3.9
```

- remove a conda environment
```bash
conda remove --name myenv --all
```

- list all packages in the conda environment
```bash
conda list -n myenv
```

- list all conda environments
```bash
conda env list

or

conda info --envs
```

- Check how much space is occupied by the environment
```bash
du -h -s /home/kamal/miniconda3/
```

- create an environment file in conda 
```bash
conda env create -f environment.yml
```





