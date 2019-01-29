var coordinates = {lat: 0, lng: 0};
var gmap = new google.maps.Map(document.getElementById('gmap'), {
    zoom: 1,
    center: coordinates,
    fullscreenControl: false,
    streetViewControl: false,
    disableDefaultUI: true
});
var marker = new google.maps.Marker({
    position: coordinates,
    map: gmap,
    visible: false
});
