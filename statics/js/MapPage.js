function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 7,
        center: new google.maps.LatLng(23.5, 121),
        mapTypeId: "terrain", //地形
    });

    var controlDiv = document.getElementById('floating-panel'); //顯示圖層位置
    map.controls[google.maps.ControlPosition.LEFT].push(controlDiv);
    controlDiv.style.marginLeft = "10px";
    setTimeout(function(){
        controlDiv.style.display= "block";
    },500);
    
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

    var HazardCheckbox = document.getElementById("toggle-hazard");
    var counter = 0;
    HazardCheckbox.addEventListener('change', function () {
        if (this.checked) {
            counter++;
            if (counter == 1) { //確保只載入一次
                map.data.loadGeoJson('grid.geojson'); //載入10格子資料(用google api載)
            }
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
            map.data.addListener('click', function (e) {
                var feat = e.feature;
                var num = feat.getProperty('name');
                var img = document.getElementById('hazard');
                img.src = `../static/assets/fakeimg${num}.jpg`;
                console.log(img.src)
                // // 點擊時獲取滑鼠的經緯度座標
                // var coordinate = {
                //     lat: e.latLng.lat(),
                //     lng: e.latLng.lng()
                // };
                // // 將資訊視窗的位置，設定為滑鼠的座標
                // infowindow.setPosition(coordinate);
                // // // 設定資訊視窗的內容為行政區名稱
                // infowindow.setContent(`<div style='float:left'>\
                //         <img src='fakeimg${feat.getProperty('name')}.jpg' width=100px heigh=100px></div>\
                //         <div style='float:right; padding: 10px;'><b>ID:${feat.getProperty('name')}</b><br/>\
                //         <b>Hazard</b><br/>probability:50%<br/>conclude:dangerous</div>`);
                // // 將資訊視窗打開在地圖上
                // infowindow.open(map);
            });

            map.data.addListener('mouseout', function (e) {
                infowindow.close(map);
            });
            map.data.setMap(map);
        } else {
            map.data.setMap(null);
        }
    });

}