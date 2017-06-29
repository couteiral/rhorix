# Dr. Matthew J L Mills - Rhorix 1.0 - June 2017

#TopologyClasses Module
# This is a Python implementation of the class hierarchy needed to parse XML files
# adhering to the document model defined in Topology.dtd
# Should be loaded into Rhorix.py as needed

class Topology():
	
	def __init__(self,nuclei,critical_points,gradient_vector_field):
		self.nuclei                = nuclei
		self.critical_points       = critical_points
		self.gradient_vector_field = gradient_vector_field

	# Find the center of the distribution of critical points
	def findCenter():

		x_total = 0.0
		y_total = 0.0
 		z_total = 0.0

		for cp in critical_points:
			x_total += cp.position[0]
			y_total += cp.position[1]
			z_total += cp.position[2]

		N = len(critical_points)
		x_origin = x_total / N
		y_origin = y_total / N
		z_origin = z_total / N

		return mathutils.Vector((float(x_origin),float(y_origin),float(z_origin)))

	# Get the radius of a sphere containing all the critical point objects
	def computeRadius():

		max = -100000

		center = findCenter(critical_points)
		for cp in critical_points:
			position = cp.position - center
			r = math.sqrt(position[0]*position[0] + position[1]*position[1] + position[2]*position[2])

			if position[0] > max:
				max = position[0]

		return max

class Nucleus():
	def __init__(self,element,position_vector):
		self.element         = element
		self.position_vector = position_vector

class CriticalPoint(Point):
	def __init__(self,position_vector,scalar_properties,rank,signature):
		Point.__init__(self,position_vector,scalar_properties)
		self.rank      = rank
		self.signature = signature

class GradientVectorField():
	def __init__(self,molecular_graph,atomic_basins,envelopes,atomic_surfaces,ring_surfaces,rings,cages):
		self.molecular_graph = molecular_graph
		self.atomic_basins   = atomic_basins
		self.envelopes       = envelopes
		self.atomic_surfaces = atomic_surfaces
		self.ring_surfaces   = ring_surfaces
		self.rings           = rings
		self.cages           = cages

class MolecularGraph():
	def __init__(self,atomic_interaction_lines):
		self.atomic_interaction_lines = atomic_interaction_lines

class AtomicInteractionLine():
	def __init__(self,gradient_paths):
		self.gradient_paths = gradient_paths

class AtomicBasin():
	def __init__(self,gradient_paths):
		self.gradient_paths = gradient_paths

class Envelope():
	def __init__(self,isovalue,points,triangulation):
		self.isovalue      = isovalue
		self.points        = points
		self.triangulation = triangulation

class AtomicSurface():
	def __init__(self,interatomic_surfaces):
		self.interatomic_surfaces = interatomic_surfaces

class InteratomicSurface():
	def __init__(self,gradient_paths,triangulation):
		self.gradient_paths = gradient_paths
		self.triangulation  = triangulation

class RingSurface():
	def __init__(self,gradient_paths):
		self.gradient_paths = gradient_paths

class Ring():
	def __init__(self,atomic_interaction_lines):
		self.atomic_interaction_lines = atomic_interaction_lines

class Cage():
	def __init__(self,rings):
		self.rings = rings

class Point():
	def __init__(self,position_vector,scalar_properties):
		self.position_vector   = position_vector
		self.scalar_properties = scalar_properties

class Triangulation():
	def __init__(self,points,edges,faces):
		self.points = points
		self.edges  = edges
		self.faces  = faces

class Edge():
	def __init__(self,a,b):
		self.a = a
		self.b = b

class Face():
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

class GradientPath():
	def __init__(self,points):
		self.points = points