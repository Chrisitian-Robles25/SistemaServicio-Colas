var nodes = new vis.DataSet([
{id: 1, label: "1 bella vista"},
{id: 2, label: "2 El triunfo"},
{id: 3, label: "3 La paz"},
{id: 4, label: "4 El condominio"},
{id: 5, label: "5 Cinco esquinas"},
{id: 6, label: "6 CasaMIA"}]);

 var edges = new vis.DataSet([{
from: 1, to: 2, label: "0.81"},{
from: 1, to: 3, label: "0.52"},{
from: 1, to: 4, label: "0.67"},{
from: 2, to: 1, label: "0.81"},{
from: 2, to: 3, label: "0.75"},{
from: 2, to: 5, label: "2.13"},{
from: 3, to: 1, label: "0.52"},{
from: 3, to: 2, label: "0.75"},{
from: 3, to: 6, label: "91.21"},{
from: 4, to: 1, label: "0.67"},{
from: 5, to: 2, label: "2.13"},{
from: 6, to: 3, label: "91.21"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);