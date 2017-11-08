function pickupRider(riderAddr) {
  console.log('Picked up button is clicked');
  console.log('pickupRider param: ' + riderAddr);
  
  // Send the dirver location
  navigator.geolocation.getCurrentPosition(function(position) {
    var jsonData = {
      "lat": position.coords.latitude,
      "lng": position.coords.longitude,
    };

    $.ajax({
      method: "POST",
      url: "/pickup",
      data: JSON.stringify(jsonData),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
    })
    /*
     * Excecuted when success
     */
      .done(function (data) {
        console.log("Json from API server " + data.message);
        window.location.href = "drive";
      })
    /*
     * Excecuted when unsuccessful
     */
      .fail(function (jqXHR) {
        // Invoke error pop-up
        console.log(jqXHR.responseJSON);
      });
  });
}

function DisplayRoute(directionsService, directionsDisplay, currentPos, userAddr) {
  directionsService.route({
    origin: currentPos,
    destination: userAddr,
    travelMode: 'DRIVING'
  }, function(response, status) {
    if (status === 'OK') {
      console.log('Current POS');
      console.log(currentPos);
      console.log('User addr');
      console.log(userAddr);

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


