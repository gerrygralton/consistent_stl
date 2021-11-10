import gmsh
import sys

input = sys.argv[1]
output = sys.argv[2]
len_scale = float(sys.argv[3])

gmsh.initialize()
gmsh.clear()

gmsh.option.setNumber("General.NumThreads", 4)

gmsh.merge(input)

gmsh.model.mesh.classifySurfaces(2, True, True)
gmsh.model.mesh.createGeometry()

gmsh.model.mesh.set_size(gmsh.model.getEntities(0), len_scale)
gmsh.model.mesh.generate(2)

gmsh.fltk.run()

gmsh.write(output)

gmsh.clear()
