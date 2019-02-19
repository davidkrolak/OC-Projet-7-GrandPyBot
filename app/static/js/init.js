const coordinates = {lat: 0, lng: 0};
const gmap = new google.maps.Map(document.getElementById('gmap'), {
    zoom: 1,
    center: coordinates,
    fullscreenControl: false,
    streetViewControl: false,
    disableDefaultUI: true
});
const marker = new google.maps.Marker({
    position: coordinates,
    map: gmap,
    visible: false
});
