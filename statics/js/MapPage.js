function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 7,
        center: new google.maps.LatLng(23.5, 121),
        mapTypeId: "terrain", //地形
    });

    var controlDiv = document.getElementById('floating-panel'); //顯示圖層位置
    map.controls[google.maps.ControlPosition.LEFT].push(controlDiv);
    controlDiv.style.marginLeft = "10px";
    setTimeout(function () {
        controlDiv.style.display = "block";
    }, 700);

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

    // map.addListener('mouseover', function (e) {
    //     var coordinate = {
    //         lat: e.latLng.lat(),
    //         lng: e.latLng.lng()
    //     };
    //     console.log(coordinate.lat)
    // });

    var HazardCheckbox = document.getElementById("toggle-hazard");
    var FaultCheckbox = document.getElementById("toggle-fault");
    var counter = 0;
    var counter2 = 0;

    HazardLayer = new google.maps.Data();
    HazardCheckbox.addEventListener('change', function () {
        if (this.checked) {
            counter++;
            if (counter == 1) { //確保只載入一次
                HazardLayer.loadGeoJson('grid.geojson'); //載入10格子資料(用google api載)
            }
            HazardLayer.setStyle({ //設定框格屬性
                strokeWeight: 5,
                strokeOpacity: .3,
                strokeColor: '#000',
                fillColor: '#f00',
                fillOpacity: .3
            });

            HazardLayer.addListener('mouseover', function (event) { //設定滑鼠移入效果
                HazardLayer.revertStyle();
                HazardLayer.overrideStyle(event.feature, {
                    fillColor: '#000'
                });
            });

            HazardLayer.addListener('mouseout', function (event) { //設定滑鼠移出效果
                HazardLayer.revertStyle();
            });

            // var infowindow = new google.maps.InfoWindow(); //建立彈窗
            HazardLayer.addListener('click', function (e) {
                var feat = e.feature;
                var num = feat.getProperty('name');
                var img = document.getElementById('hazard');
                img.src = `../static/assets/map_image/hz_${num}.png`;
                console.log(img.src)
                // 點擊時獲取滑鼠的經緯度座標
                // var coordinate = {
                //     lat: e.latLng.lat(),
                //     lng: e.latLng.lng()
                // };
                // // 將資訊視窗的位置，設定為滑鼠的座標
                // infowindow.setPosition(coordinate);
                // // // 設定資訊視窗的內容為行政區名稱
                // infowindow.setContent(`<div style='float:left'>\
                //                 <img src='fakeimg${feat.getProperty('name')}.jpg' width=100px heigh=100px></div>\
                //                 <div style='float:right; padding: 10px;'><b>ID:${feat.getProperty('name')}</b><br/>\
                //                 <b>Hazard</b><br/>probability:50%<br/>conclude:dangerous</div>`);
                // // 將資訊視窗打開在地圖上
                // infowindow.open(map);
            });
            // HazardLayer.addListener('mouseout', function (e) {
            //     infowindow.close(map);
            // });

            HazardLayer.setMap(map);
        } else {
            HazardLayer.setMap(null);
        }
    });

    FalutLayer = new google.maps.Data();
    FaultCheckbox.addEventListener('change', function () {
        if (this.checked) {
            counter2++;
            if (counter2 == 1) { //確保只載入一次
                FalutLayer.loadGeoJson('fault.geojson'); //載入10格子資料(用google api載)
            }
            FalutLayer.setMap(map);
        } else {
            FalutLayer.setMap(null);
        }
    });
    // layer problem: https://cloud.tencent.com/developer/ask/sof/487546

    var SearchBtn = document.getElementById("search");
    var ClearBtn = document.getElementById("clear");
    var markers = [];
    SearchBtn.addEventListener('click', function () {
        var LonValue = parseFloat(document.getElementById("toggle-Lon").value);
        var LatValue = parseFloat(document.getElementById("toggle-Lat").value);
        if (isNaN(LonValue) || isNaN(LatValue)) {
            alert('Input value plz');
        } else if (LonValue > 180 || LonValue < -180) {
            alert('Input Longitude Value between -180-180');
        } else if (LatValue > 90 || LatValue < -90) {
            alert('Input Latitude Value between -90-90');
        } else {
            var position = {
                lat: LatValue,
                lng: LonValue
            };

            marker = new google.maps.Marker({ //注意這裡的marker不要使用var來呼叫，會變成local variable，正確應該是要global variable下面的EventListener才吃的到
                position: position,
                map: map,
                animation: google.maps.Animation.DROP
            });
            markers.push(marker);
        }
    });

    ClearBtn.addEventListener('click', function () {
        for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(null);
        }
        markers = [];
    });
}

function centerHandler() {
    /*設定置中的函式*/
    var scrollDist = $(window).scrollTop(); /*取得捲動長度*/
    var myTop = ($(window).height() - $("#popWindow").height()) / 2 + scrollDist;
    /*取得垂直中央位置*/
    var myLeft = ($(window).width() - $("#popWindow").width()) / 2;
    /*取得水平中央位置*/
    $("#popWindow").offset({
        top: myTop,
        left: myLeft
    });
    /*設定區塊於水平與垂直置中*/
    $('#subbmit').click(function () {
        $('#popWindow').hide();
    });
}

centerHandler(); /*呼叫置中函式，使廣告區塊置中*/
$(window).scroll(centerHandler); /*當網頁捲動時呼叫置中函式*/
$(window).resize(centerHandler); /*當視窗縮放時呼叫置中函式*/