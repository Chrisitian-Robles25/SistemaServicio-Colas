var nodes = new vis.DataSet([
{id: 1, label: "bella vista"},
{id: 2, label: "El triunfo"},
{id: 3, label: "La paz"},
{id: 4, label: "El condominio"},
{id: 5, label: "Cinco esquinas"},
{id: 6, label: "CasaMIA"},
{id: 7, label: "La esperanza"},
{id: 8, label: "Barrio nuevo"},
{id: 9, label: "La esquinera"},
{id: 10, label: "Puyango"},
{id: 11, label: "El limo"},
{id: 12, label: "El arenal"},
{id: 13, label: "Ciano"},
{id: 14, label: "Pindal"},
{id: 15, label: "Naipiraca"}]);

 var edges = new vis.DataSet([]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);