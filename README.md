```zsh
mkdir data
mkdir data/mp3
```

```zsh
curl https://os.unil.cloud.switch.ch/fma/fma_small.zip --output fma_small.z
ip
```

```zsh
tar xvf fma_small.zip --directory=data
```

```zsh
find data/fma_small -mindepth 2 -type f -exec mv -i '{}' data/mp3 \;
```

```zsh
rm -rf data/fma_small
rm fma_small.zip
```

