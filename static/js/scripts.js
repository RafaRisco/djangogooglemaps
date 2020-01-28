var watchId, startLat, startLong;
window.onload = function()
{
  if (navigator.geolocation)
  {
    watchId = navigator.geolocation.watchPosition(onSuccess, onError, {
      maximumAge: 60000,
      timeout: 5*60*1000,
      enableHighAccurady: true
    });
  }
}

function onSuccess(position)
{

  var currentLat = position.coords.latitude;
  var currentLong = position.coords.longitude;

var initMap = function() {
  var latlng = new google.maps.LatLng(currentLat, currentLong);
  var map = new google.maps.Map(document.getElementById('mapa'), {
  center: latlng,
  scrollwheel: true,
  zoom: 15,
  mapTypeId: google.maps.MapTypeId.ROADMAP,
});
var marker = new google.maps.Marker({
  position: latlng,
  map: map,
  draggable: true,
  title:"Arrastrame",
});

  google.maps.event.addListener(marker, 'position_changed', function(){
      getMarkerCoords(marker);
  });

  function getMarkerCoords(marker)
  {
      var markerCoords = marker.getPosition();
      document.getElementById("id_lat").value = markerCoords.lat();
      document.getElementById("id_long").value = markerCoords.lng();
  }

}
initMap()
}

function onError(error)
{
  switch(error.code)
  {
    case PERMISION_DENIED:
      alert("User denied permission");
      break;
    case TIMEOUT:
      alert("Geolocation timed out");
      break;
    case POSITION_UNAVAILABLE:
      alert("Geolocation information is not available")
      break;
    default:
      alert("Unknown error");
      break;
  }
}
