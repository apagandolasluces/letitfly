search = {
  initGoogleMaps: function(data){
    console.log("Search.js is loaded");
    console.log(typeof data);
    console.log(data);

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
      console.log('Me: ' + pos);
      var marker = new google.maps.Marker({
        position: pos,
        title:"You are here!"
      });

      data.forEach(function(element) {
        console.log(element);
        var contentStr = "<p>Ride ID: " + element.ride_id + "</p>"
                          + "<p>" + element.start_location + "</p>";
        // Create info window
        var infowindow = new google.maps.InfoWindow({
          content: contentStr
        });

        var geocoder = new google.maps.Geocoder();
        geocoder.geocode({'address': element.start_location}, function(results, status) {
          if (status === 'OK') {
            // Create marker
            var marker = new google.maps.Marker({
              position: results[0].geometry.location,
              map: map,
              title: element.ride_id
            });
            marker.addListener('click', function() {
              infowindow.open(map, marker);
            });
          } else {
            alert('Geocode was not successful for the following reason: ' + status);
          }
        });
      });

      marker.setMap(map);
      map.setCenter(pos);
      map.setZoom(12);
    });
    directionsDisplay.setMap(map);
  },
};

