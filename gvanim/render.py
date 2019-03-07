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

from __future__ import absolute_import
import itertools
from subprocess import Popen, PIPE, STDOUT, call
from multiprocessing import Pool, cpu_count

def _render( params ):
	path, fmt, size, graph = params
	with open( path , 'w' ) as out:
		pipe = Popen( [ 'dot', '-T', fmt ], stdout = out, stdin = PIPE, stderr = None )
		pipe.communicate( input = graph.encode() )
	return path

def render( graphs, basename, fmt = 'png', size = 800 ):
	try:
		_map = Pool( processes = cpu_count() ).map
	except NotImplementedError:
		_map = map
	return _map( _render, [ ( '{}_{:03}.{}'.format( basename, n, fmt ), fmt, size, graph ) for n, graph in enumerate( graphs ) ] )

def gif( files, basename, delay = 100 ):
	cmd = [ 'convert' ]
	for file in files:
		cmd.extend( ( '-delay', str( delay ), file ) )
	cmd.append( basename + '.gif' )
	call( cmd )

def addQueueState( queueStates, message=None):
    if message != None:
        text = "\n" + message + "\n"
    else:
        text = ""
    queueStates.append( text )

def slides( files1, files2, queueStates, basename, width=1920, height=1080):

	file = open(basename+".md","w")
	mdpre = "\n".join(
		[
		"---",
		"presentation:",
		"  theme: serif.css",
		"  width: {}".format(width),
	  	"  height: {}".format(height),
		"  transition: 'none'",
		"  transitionSpeed: 'fast'",
	  	"  backgroundTransition: 'none'",
		"  overview: true",
		"  progress: true",
		"  slideNumber: true",
		"---",
		""
		])

	file.write(mdpre)

	for file1,file2, queueState in itertools.izip(files1,files2,queueStates):
		md = [
			'',
			'<!-- slide -->',
		 	 "{}".format(queueState),
			'<div class="columns">',
			'   <div class="column" width="50%">',
			"![]({})".format(file1)+'{'+"width={0} height={1}".format(width*45/100,height*70/100)+'}',
			'   </div>',
			'   <div class="column" width="50%">',
			"![]({})".format(file2)+'{'+"width={0} height={1}".format(width*45/100,height*70/100)+'}',
			'   </div>',
			'</div>'
		]
		file.write("\n".join(md))
	file.close()
