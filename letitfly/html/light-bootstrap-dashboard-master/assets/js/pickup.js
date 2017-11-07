function DisplayRoute(directionsService, directionsDisplay, currentPos, userAddr) {
  directionsService.route({
    origin: currentPos,
    destination: userAddr,
    travelMode: 'DRIVING'
  }, function(response, status) {
    if (status === 'OK') {
      console.log(response);
      directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}


pickup = {
  initGoogleMaps: function(ride){
    console.log("pickup.js is loaded");
    console.log(ride);

    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 7,
      center: {lat: 37.33542741901094, lng: -121.88427904493496}
    });

    directionsDisplay.setMap(map);

    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      console.log('Me: ' + pos);
      var marker = new google.maps.Marker({
        position: pos,
        title:"You are here!"
      });

      marker.setMap(map);
      map.setCenter(pos);
      map.setZoom(12);

      DisplayRoute(directionsService, directionsDisplay, pos, ride.start_location);
      
    });
    directionsDisplay.setMap(map);
  },
};


