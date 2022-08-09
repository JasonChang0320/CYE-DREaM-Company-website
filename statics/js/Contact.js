function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: new google.maps.LatLng(24.97084, 121.19495),
        mapTypeId: "terrain", //地形
    });

    const marker = new google.maps.Marker({
        position: new google.maps.LatLng(24.97084, 121.19495),
        map: map,
    });
}