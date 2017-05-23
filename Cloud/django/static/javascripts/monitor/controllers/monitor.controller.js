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
    vm.clear_info = clear_info;
    vm.show_editable = show_editable;
 
    vm.curr_info = {number: '0'};
    vm.currLots = [{name: 'Loading'}];
    vm.newLots = [];
    vm.currSpots = [{uuid: 'Loading Spots...'}];
    vm.spot_editable = false;
    vm.spot_edit_number = 0;
    vm.spot_edit_uuid = 0;
    vm.spot_edit_section = 0;
    vm.spot_edit_price = 0;
    
    // Load Server data
    load_lots();
    load_spots();
  
    vm.spot_info = spot_info;

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
        console.log(vm.currSpots);
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
      console.log(vm.spot_editable);
    }

  }
})();
