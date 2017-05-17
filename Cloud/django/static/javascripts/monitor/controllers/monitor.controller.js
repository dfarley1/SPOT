(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.controllers')
    .controller('MonitorController', MonitorController);

  MonitorController.$inject = ['$location', '$scope', '$http', 'Monitor', 'ngDialog'];

  function MonitorController($location, $scope, $http, Monitor, ngDialog) {
    // Initializations
    var vm = this;
    vm.create_lot = create_lot;
    vm.edit_rate = edit_rate;
    vm.update_lots = update_lots;
    vm.spot_info = spot_info;

    vm.newLots = [];
    vm.currSpots = [{uuid: 'Loading Spots...'}];
    
    // Load Server data
    load_spots();
  
    // API
    function create_lot() {
      Monitor.create_lot(vm.newLots, vm.lot_name);
    }

    function edit_rate() {
      Monitor.edit_rate(vm.spot_number, vm.spot_rate);
      window.location = '/monitor';
    }

    function update_lots() {
      Monitor.update_lots(vm.newLots);
    }

    function load_spots() {
      $http.get('/api/v1/monitor/list_spots/',
      ).then(loadSpotsSuccessFn, loadSpotsErrorFn);
   
      //Define Success and failure methods
      function loadSpotsSuccessFn(data, status, headers, config) {
        console.log(data.data);
        vm.currSpots = data.data;
      }

      function loadSpotsErrorFn(data, status, headers, config) {
        console.error('FAILED to GET directory');
      }
    }

    function spot_info(input) {
      console.log('Caffeinated' + input);
    }

    // function compare_spot(spot) {
    //   if(spot == 1) {
    //     return 1;
    //   } else return 0;
    // }

  }
})();
