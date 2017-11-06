lookForDriver = {
  initGoogleMaps: function(){
    console.log("Looking for drivre js is loaded");
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 7,
      center: {lat: 37.33542741901094, lng: -121.88427904493496}
    });
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      console.log(pos)
      var marker = new google.maps.Marker({
        position: pos,
        title:"You are here!"
      });

      // To add the marker to the map, call setMap();
      // marker.setMap(map);
      map.setCenter(pos);
      map.setZoom(12);
    });
    directionsDisplay.setMap(map);
  },
}
