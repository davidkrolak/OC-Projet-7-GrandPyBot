var mymap = L.map('mapid').setView([0, 0], 1);
var marker = L.marker([0, 0]).addTo(mymap);
marker.setOpacity(0);
L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    id: 'mapbox.streets',
}).addTo(mymap);
