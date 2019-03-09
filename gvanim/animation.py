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

from email.utils import quote
import shlex

from gvanim import action


class ParseException(Exception):
    pass


class Step(object):

    def __init__(self, step=None, copy_hV=True, copy_hE=False):
        if step:
            self.V = step.V.copy()
            self.E = step.E.copy()
            if copy_hV:
                self.hV = step.hV.copy()
            else:
                self.hV = dict()
            if copy_hE:
                self.hE = step.hE.copy()
            else:
                self.hE = dict()
        else:
            self.V = set()
            self.E = set()
            self.hV = dict()
            self.hE = dict()

    def node_format(self, v):
        fmt = []
        try:
            fmt.append('label="{}"'.format(v.label))
        except KeyError:
            pass
        if v in self.hV:
            fmt.append('color={}'.format(self.hV[v]))
        elif v not in self.V:
            fmt.append('style=invis')
        if fmt: return '[{}]'.format(','.join(fmt))
        return ''

    def edge_format(self, e):
        if e in self.hE:
            return '[color={}, label={}]'.format(self.hE[e], e.weight)
        elif e in self.E:
            return ''
        return '[style=invis]'

    def __repr__(self):
        return '{{ V = {}, E = {}, hV = {}, hE = {} }}'.format(self.V, self.E, self.hV, self.hE)


class Animation(object):

    def __init__(self):
        self._actions = []

    def next_step(self, clean=False):
        self._actions.append(action.NextStep(clean))

    def add_node(self, v):
        self._actions.append(action.AddNode(v))

    def highlight_node(self, v, color='red'):
        self._actions.append(action.HighlightNode(v, color=color))

    def label_node(self, v, label):
        self._actions.append(action.LabelNode(v, label))

    def unlabel_node(self, v):
        self._actions.append(action.UnlabelNode(v))

    def remove_node(self, v):
        self._actions.append(action.RemoveNode(v))

    def add_edge(self, edge, **kwargs):
        self._actions.append(action.AddEdge(edge, **kwargs))

    def highlight_edge(self, edge, color='red'):
        self._actions.append(action.HighlightEdge(edge, color=color))

    def remove_edge(self, u, v):
        self._actions.append(action.RemoveEdge(u, v))

    def parse(self, lines):
        action2method = {
            'ns': self.next_step,
            'an': self.add_node,
            'hn': self.highlight_node,
            'ln': self.label_node,
            'un': self.unlabel_node,
            'rn': self.remove_node,
            'ae': self.add_edge,
            'he': self.highlight_edge,
            're': self.remove_edge,
        }
        for line in lines:
            parts = shlex.split(line.strip(), True)
            if not parts: continue
            action, params = parts[0], parts[1:]
            try:
                action2method[action](*params)
            except KeyError:
                raise ParseException('unrecognized command: {}'.format(action))
            except TypeError:
                raise ParseException('wrong number of parameters: {}'.format(line.strip()))

    def steps(self):
        steps = [Step()]
        for action in self._actions:
            action(steps)
        return steps

    def graphs(self, layout='neato'):
        steps = self.steps()
        V, E = set(), set()
        for step in steps:
            V |= step.V
            E |= step.E
        graphs = []
        for n, s in enumerate(steps):
            graph = ['digraph G {']
            graph.append('layout="{}"'.format(layout))
            graph.append('ordering=out;')
            for v in V: graph.append('"{}" {};'.format(quote(str(v)), s.node_format(v)))
            for e in E: graph.append('"{}" -> "{}" {};'.format(quote(str(e[0])), quote(str(e[1])), s.edge_format(e)))
            graph.append('}')
            graphs.append('\n'.join(graph))
        return graphs
