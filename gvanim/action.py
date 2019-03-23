# Copyright 2016, Massimo Santini <santini@di.unimi.it>
#
# This file is part of "GraphvizAnim".
#
# "GraphvizAnim" is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# "GraphvizAnim" is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# "GraphvizAnim". If not, see <http://www.gnu.org/licenses/>.

class NextStep( object ):
	def __init__( self, clean = False ):
		self.clean = clean
	def __call__( self, steps ):
		from gvanim.animation import Step
		steps.append( Step( None if self.clean else steps[ -1 ] ) )

class AddNode( object ):
	def __init__( self, v ):
		self.v = v
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.v )

class HighlightNode( object ):
	def __init__( self, v, color = 'red' ):
		self.v = v
		self.color = color
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].hV[ self.v ] = self.color

class RemoveNode( object ):
	def __init__( self, v ):
		self.v = v
	def __call__( self, steps ):
		steps[ -1 ].V.discard( self.v )
		try:
			del steps[ -1 ].hV[ self.v ]
		except KeyError:
			pass
		dE = set( e for e in steps[ -1 ].E if self.v in e )
		steps[ -1 ].E -= dE
		for e in list(steps[ -1 ].hE.keys()):
			if self.v in e:
				del steps[ -1 ].hE[ e ]

class AddEdge( object ):
	def __init__( self, edge, **kwargs ):
		print("AddEdge: action: 56")
		self.u = edge.getFrom()
		self.v = edge.getTo()
		self.e = edge
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.u )
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].E.add( self.e )

class HighlightEdge( object ):
	def __init__( self, edge, color = 'red' ):
		print("HighlightEdge: action: 67")
		self.edge = edge
		self.color = color
	def __call__( self, steps ):
		print("HighlightEdge: action: 71")
		steps[ -1 ].E.add( self.edge )
		steps[ -1 ].hE[ self.edge ] = self.color

class RemoveEdge( object ):
	def __init__( self, edge ):
		self.edge = edge
	def __call__( self, steps ):
		steps[ -1 ].E.discard( self.edge )
		try:
			del steps[ -1 ].hE[ self.edge ]
		except KeyError:
			pass