function meterToMile(meter) {
  return meter/1609.344;
}

function calculatePrice (mile) {
  var chargedMile = mile - 2;
  var price = chargedMile * 10;

  if (price < 15) {
    return 15;
  } else {
    return price;
  }
}

function calculateAndDisplayRoute(directionsService, directionsDisplay, currentPos) {
  directionsService.route({
    // origin: document.getElementById('start').value,
    origin: currentPos,
    destination: document.getElementById('end').value,
    travelMode: 'DRIVING'
  }, function(response, status) {
    if (status === 'OK') {
      console.log(response);
      directionsDisplay.setDirections(response);
      // document.getElementById("duration").value = response.routes.
      var resultText = "Duration: " + response.routes[0].legs[0].duration.text +
        "<br>Distance: " + response.routes[0].legs[0].distance.text +
        "<br>$ " + meterToMile(calculatePrice(response.routes[0].legs[0].distance.value));
      document.getElementById("duration").innerHTML = resultText;
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}

$( document ).ready(function() {
    console.log( "ready!" );
});

usermap = {
  initGoogleMaps: function(){
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

    var onChangeHandler = function() {
      navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        calculateAndDisplayRoute(directionsService, directionsDisplay, pos);
      });
    };
    // document.getElementById('start').addEventListener('change', onChangeHandler);
    document.getElementById('end').addEventListener('change', onChangeHandler);
  },
}

