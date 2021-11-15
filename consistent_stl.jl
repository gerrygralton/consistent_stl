using gmsh

function consistent_stl(input::String, output::String; len_scale::Real=1., angle::Real=180.)
    gmsh.initialize()
    gmsh.clear()

    gmsh.merge(input)

    angle = angle * pi / 180
    gmsh.model.mesh.createTopology()
    gmsh.model.mesh.classifySurfaces(angle, true, true)
    gmsh.model.mesh.createGeometry()

    gmsh.model.mesh.set_size(gmsh.model.getEntities(0), len_scale)
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.optimize("Netgen")

    gmsh.write(output)

    gmsh.clear()
end
