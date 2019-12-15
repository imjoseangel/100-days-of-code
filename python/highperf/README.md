# Create and Visualize output.pstats

## Create

```bash
python -m cProfile -o output.pstats taylor.py
```

## Visualize

### Install gprof2dot

```bash
pip install gprof2dot
```

### Install graphviz on Mac

```bash
brew install graphviz
```

## Run gprof2dot

```bash
gprof2dot -f pstats output.pstats | dot -Tpng -o output.png
```
