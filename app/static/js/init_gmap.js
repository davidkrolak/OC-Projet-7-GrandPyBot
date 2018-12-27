$("#mapid").hide();
var coordinates = {lat: 0, lng: 0};
var gmap = new google.maps.Map(document.getElementById('mapid'), {
    zoom: 1,
    center: coordinates,
    fullscreenControl: false,
    streetViewControl: false
});
var marker = new google.maps.Marker({
    position: coordinates,
    map: gmap,
    visible: false
});
