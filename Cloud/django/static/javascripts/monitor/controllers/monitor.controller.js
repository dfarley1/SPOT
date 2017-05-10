(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.controllers')
    .controller('MonitorController', MonitorController);

  MonitorController.$inject = ['$location', '$scope', 'Monitor'];

  function MonitorController($location, $scope, Monitor) {
    var vm = this;
    vm.create_lot = create_lot;
    vm.edit_rate = edit_rate;
    vm.update_lots = update_lots;
    vm.newLots = [];
  
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
  }
})();
