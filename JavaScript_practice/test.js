let bikes = [
    {
      rackTotCnt: "7",
      stationName: "101. (구)합정동 주민센터",
      parkingBikeTotCnt: "4",
      shared: "14",
      stationLatitude: "37.54956055",
      stationLongitude: "126.90575409",
      stationId: "ST-3",
    },
    {
      rackTotCnt: "22",
      stationName: "102. 망원역 1번출구 앞",
      parkingBikeTotCnt: "17",
      shared: "5",
      stationLatitude: "37.55564880",
      stationLongitude: "126.91062927",
      stationId: "ST-4",
    },
    {
      rackTotCnt: "16",
      stationName: "103. 망원역 2번출구 앞",
      parkingBikeTotCnt: "11",
      shared: "13",
      stationLatitude: "37.55495071",
      stationLongitude: "126.91083527",
      stationId: "ST-5",
    },
    {
      rackTotCnt: "15",
      stationName: "104. 합정역 1번출구 앞",
      parkingBikeTotCnt: "11",
      shared: "0",
      stationLatitude: "37.55062866",
      stationLongitude: "126.91498566",
      stationId: "ST-6",
    },
    {
      rackTotCnt: "7",
      stationName: "105. 합정역 5번출구 앞",
      parkingBikeTotCnt: "1",
      shared: "0",
      stationLatitude: "37.55000687",
      stationLongitude: "126.91482544",
      stationId: "ST-7",
    },
    {
      rackTotCnt: "12",
      stationName: "106. 합정역 7번출구 앞",
      parkingBikeTotCnt: "8",
      shared: "8",
      stationLatitude: "37.54864502",
      stationLongitude: "126.91282654",
      stationId: "ST-8",
    }]

  function bike_func(bikes){
      for (let i = 0; i<bikes.length; i++){
          let bike_num = bikes[i]['parkingBikeTotCnt']
          if (bike_num <= 5){
              console.log(bikes[i]['stationName'])
          }
      }
  }

bike_func (bikes)