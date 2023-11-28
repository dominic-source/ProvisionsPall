
function initMap() {
    let options = {
        center: { lat: 7.7983, lng: 5.5145 },
        zoom: 16,
    }
    let map = new google.maps.Map(document.getElementById("map"), options);
}