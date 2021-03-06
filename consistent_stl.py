import gmsh
import argparse
import math

parser = argparse.ArgumentParser(description="Input arguments")
parser.add_argument("input", metavar="input", type=str,
                    help="Path to mesh")
parser.add_argument("output", metavar="output", type=str,
                    help="Output path")
parser.add_argument("length", metavar="length", type=float,
                    help="Characteristic length mesh")
parser.add_argument("angle", metavar="angle", type=float,
                    help="""Angle at which new surface is defined in degrees.
                    If geometry is smooth, use 180, else use 45.""")

args = parser.parse_args()

gmsh.initialize()
gmsh.clear()

gmsh.option.setNumber("General.NumThreads", 4)

gmsh.merge(args.input)

angle = args.angle * math.pi / 180
gmsh.model.mesh.createTopology()
gmsh.model.mesh.classifySurfaces(angle, True, True)
gmsh.model.mesh.createGeometry()

gmsh.model.mesh.set_size(gmsh.model.getEntities(0), args.length)
gmsh.model.mesh.generate(2)
gmsh.model.mesh.optimize("Netgen")

gmsh.write(args.output)

gmsh.clear()
