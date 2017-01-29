var map;
var marker = false;
        
function initMap() {
    var centerOfMap = new google.maps.LatLng(44.93369638969468, -69.290771484375);
    var options = {
        center: centerOfMap,
        zoom: 7
    };
 
    map = new google.maps.Map(document.getElementById('map'), options);
    google.maps.event.addListener(map, 'click', function(event) {                
        var clickedLocation = event.latLng;
        if(marker === false){
            marker = new google.maps.Marker({
                position: clickedLocation,
                map: map,
                draggable: true
            });
            google.maps.event.addListener(marker, 'dragend', function(event){
                markerLocation();
            });
        } else{
            marker.setPosition(clickedLocation);
        }
        markerLocation();
    });
}
        
function markerLocation(){
    var currentLocation = marker.getPosition();
    document.getElementById('id_latitude').value = currentLocation.lat();
    document.getElementById('id_longitude').value = currentLocation.lng();
}
google.maps.event.addDomListener(window, 'load', initMap);
