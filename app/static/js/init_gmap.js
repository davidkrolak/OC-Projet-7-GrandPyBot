function initMap() {
  var coordinates = {lat: 0, lng: 0};
  var map = new google.maps.Map(
      document.getElementById('mapid'), {zoom: 1, center: coordinates});
}

initMap();