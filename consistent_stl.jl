using gmsh

function consistent_stl(input::String, output::String; len_scale::Real=1.)
    gmsh.initialize()
    gmsh.clear()

    gmsh.merge(input)

    gmsh.model.mesh.classifySurfaces(2, true, true)
    gmsh.model.mesh.createGeometry()

    gmsh.model.mesh.set_size(gmsh.model.getEntities(0), len_scale)
    gmsh.model.mesh.generate(2)

    gmsh.write(output)

    gmsh.clear()
end
