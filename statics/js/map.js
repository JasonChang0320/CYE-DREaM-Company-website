function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: new google.maps.LatLng(23.5, 121.3),
        mapTypeId: "terrain", //地形
    });

    // fetch("./map.geojson") //讀入經緯json資料並在圖上作圖
    //     .then((res) => {
    //         return res.json();
    //     })
    //     .then((data) => {
    //         console.log("data", data);
    //         const latLng = new google.maps.LatLng(data.lat[1], data.lon[1]);
    //         new google.maps.Marker({
    //             position: latLng,
    //             map: map,
    //         });
    //     })

    // map.data.loadGeoJson('twCounty2010.topo.json'); //載入台灣行政區資料(用google api載)
    map.data.loadGeoJson('map.geojson'); //載入10格子資料(用google api載)

    map.data.setStyle({ //設定框格屬性
        strokeWeight: 5,
        strokeOpacity: .3,
        strokeColor: '#000',
        fillColor: '#f00',
        fillOpacity: .3
    });

    map.data.addListener('mouseover', function (event) { //設定滑鼠移入效果
        map.data.revertStyle();
        map.data.overrideStyle(event.feature, {
            fillColor: '#000'
        });
    });

    map.data.addListener('mouseout', function (event) { //設定滑鼠移出效果
        map.data.revertStyle();
    });

    var infowindow = new google.maps.InfoWindow(); //建立彈窗
    map.data.addListener('mouseover', function (e) {
        var feat = e.feature;
        console.log(feat.getProperty('name'))
        // 點擊時獲取滑鼠的經緯度座標
        var coordinate = {
            lat: e.latLng.lat(),
            lng: e.latLng.lng()
        };
        // 將資訊視窗的位置，設定為滑鼠的座標
        infowindow.setPosition(coordinate);
        // // 設定資訊視窗的內容為行政區名稱
        infowindow.setContent(`<div style='float:left'>\
                        <img src='fakeimg${feat.getProperty('name')}.jpg' width=100px heigh=100px>\
                        </div><div style='float:right; padding: 10px;'>\
                        <b>Hazard</b><br/>probability:50%<br/>conclude:dangerous</div>`);
        // 將資訊視窗打開在地圖上
        infowindow.open(map);
    });

    map.data.addListener('mouseout', function (e) {
        infowindow.close(map);
    });



    // $.getJSON('twCounty2010.topo.json', function (e) { //用jquery載入資料
    //     var features = e.features;
    //     console.log(features)
    //     // 載入資料後要做的事情.....
    // });

    // var polygonPathPoints = [{ // 地圖上畫愛心(多邊形作圖)
    //         lat: 25.032474,
    //         lng: 121.564714
    //     },
    //     {
    //         lat: 25.033018,
    //         lng: 121.563534
    //     },
    //     {
    //         lat: 25.034477,
    //         lng: 121.562954
    //     },
    //     {
    //         lat: 25.035157,
    //         lng: 121.563330
    //     },
    //     {
    //         lat: 25.035157,
    //         lng: 121.563941
    //     },
    //     {
    //         lat: 25.034622,
    //         lng: 121.564617
    //     },
    //     {
    //         lat: 25.035147,
    //         lng: 121.565390
    //     },
    //     {
    //         lat: 25.035021,
    //         lng: 121.565958
    //     },
    //     {
    //         lat: 25.034341,
    //         lng: 121.566237
    //     },
    //     {
    //         lat: 25.033252,
    //         lng: 121.565915
    //     }
    // ];

    // var polygonPath = new google.maps.Polygon({
    //     paths: polygonPathPoints,
    //     strokeColor: '#0c0',
    //     strokeOpacity: .5,
    //     strokeWeight: 20,
    //     strokePosition: google.maps.StrokePosition.CENTER,
    //     fillColor: '#f00',
    //     fillOpacity: 0.35,
    //     map: map
    // });
}