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
    vm.clear_info = clear_info;
    vm.show_editable = show_editable;
    vm.save_editable = save_editable;
 
    vm.curr_info = {};
    vm.currLots = [{name: 'Loading'}];
    vm.newLots = [];
    vm.currSpots = [{uuid: 'Loading Spots...'}];
    vm.spot_editable = false;
    vm.spot_edit_number;
    vm.spot_edit_uuid;
    vm.spot_edit_section;
    vm.spot_edit_price;

    vm.lot_occupied = 0;
    
    // Load Server data
    load_lots();
    load_spots();
  
    vm.spot_info = spot_info;
    vm.lot_info = lot_info;

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

    function load_lots() {
      $http.get('/api/v1/monitor/list_lots/',
      ).then(getDirectorySuccessFn, getDirectoryErrorFn);
   
      //Define Success and failure methods
      function getDirectorySuccessFn(data, status, headers, config) {
        vm.currLots = data.data;
        console.log(vm.currLots);
      }

      function getDirectoryErrorFn(data, status, headers, config) {
        console.error('FAILED to GET directory');
      }
    }  

    function load_spots() {
      $http.get('/api/v1/monitor/list_spots/',
      ).then(loadSpotsSuccessFn, loadSpotsErrorFn);
   
      //Define Success and failure methods
      function loadSpotsSuccessFn(data, status, headers, config) {
        vm.currSpots = data.data;
      }

      function loadSpotsErrorFn(data, status, headers, config) {
        console.error('FAILED to GET directory');
      }
    }
    
    function spot_info(input) {
      vm.curr_info = vm.currSpots[input];
      console.log(vm.curr_info);
    }

    function clear_info() {
      vm.curr_info = {};
    }
    function show_editable() {
      vm.spot_editable = !vm.spot_editable;
      console.log('show edit = ' + vm.spot_editable);
    }

    function save_editable() {
      console.log('[save_editable()]: Sending: \n' + vm.spot_edit_number + '\n'
      + vm.spot_edit_active + '\n' + vm.spot_edit_uuid + '\n' + vm.spot_edit_section
      + '\n' + vm.spot_edit_price);
      return $http.post('/api/v1/monitor/edit_spot_info/', {
        spot_edit_number: vm.spot_edit_number,
        spot_edit_active: vm.spot_edit_active,
        spot_edit_uuid: vm.spot_edit_uuid,
        spot_edit_section: vm.spot_edit_section,
        spot_edit_rate: vm.spot_edit_price
      }).then(save_editableSuccess, save_editableError);
      function save_editableSuccess(data, status, headers, config) {
        console.log('Successful POST to /api/v1/monitor/edit_spot_info!');
      }
      function save_editableError(data, status, headers, config) {
        console.error('FAILED to POST to /api/v1/monitor/edit_spot_info!');
      }
    }

    function lot_info(lot_name) {
      var lot, spot;
      for (lot in vm.currLots) {
        // Sift for lot
        if (lot.name === lot_name) {
          // Get # if active spots
          var occupied = 0;
          for (spot in lot) {
            if (spot.active == 1) occupied++;
          }

          // Save to $scope
          return occupied;
        }
      }
    }

  }
})();
