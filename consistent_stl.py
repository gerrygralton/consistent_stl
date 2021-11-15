import gmsh
import sys
import math

input = sys.argv[1]
output = sys.argv[2]
len_scale = float(sys.argv[3])

gmsh.initialize()
gmsh.clear()

gmsh.option.setNumber("General.NumThreads", 4)

gmsh.merge(input)

angle = math.pi * 0.3
gmsh.model.mesh.createTopology()
gmsh.model.mesh.classifySurfaces(angle, True, True)
gmsh.model.mesh.createGeometry()

gmsh.model.mesh.set_size(gmsh.model.getEntities(0), len_scale)
gmsh.model.mesh.generate(2)
gmsh.model.mesh.optimize("Netgen")

gmsh.write(output)

gmsh.clear()
