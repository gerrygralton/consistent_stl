# consistent_stl

## Dependencies
- [Gmsh](https://gmsh.info/#Download)

## Python
From the terminal run:

`python3 consistent_stl.py path/to/input_file path/to/output_file length_scale angle`

where length_scale is the desired element size and angle is the angle at which new surfaces are defined in degrees. For smooth geometries use 180 degrees, else use 45 degrees. 

## Julia
Inside a REPL run:

```
include("consistent_stl.jl")
constistent_stl(path/to/input_file, path/to/output_file, len_scale=1.)
```
