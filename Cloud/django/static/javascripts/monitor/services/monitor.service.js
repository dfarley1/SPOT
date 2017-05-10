(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.services')
    .factory('Monitor', Monitor);

  Monitor.$inject = ['$cookies', '$http'];

  // Returns factory
  function Monitor($cookies, $http) {
    var Monitor = {
      create_lot: create_lot,
      edit_rate: edit_rate,
      update_lots: update_lots
    }; 

    return Monitor;

    // Define factory functionality
    // Working POST example
    /*
    function create_lot(lot_name) {
      return $http.post('/api/v1/monitor/create_lot/', {
        lot_name: lot_name
        // old_info: old_lot_name,
        // new_info: new_lot_name
      }).then(create_lotSuccessFn, create_lotErrorFn);

      // Define Success and failure methods
      function create_lotSuccessFn(data, status, headers, config) {
        console.log('Successful POST to /monitor!');
      }
      function create_lotErrorFn(data, status, headers, config) {
        console.error('FAILED to POST to /monitor!');
      }
    }
    */
    function create_lot(newLots, lot_name) {
        newLots.push(lot_name);
        console.log(newLots);
    }

    function update_lots(newLot_array) {

      return $http.post('/api/v1/monitor/update_lots/', {
        lot_name: angular.toJson(newLot_array)
        // old_info: old_lot_name,
        // new_info: new_lot_name
      }).then(create_lotSuccessFn, create_lotErrorFn);

      // Define Success and failure methods
      function create_lotSuccessFn(data, status, headers, config) {
        console.log('Successful POST to /monitor!');
      }
      function create_lotErrorFn(data, status, headers, config) {
        console.error('FAILED to POST to /monitor!');
      }
    }


    function edit_rate(spot_number, spot_rate) {
      return $http.post('/api/v1/monitor/edit_rate/', {
        spot_number: spot_number,
        spot_rate: spot_rate
      }).then(create_lotSuccessFn, create_lotErrorFn);

      // Define Success and failure methods
      function create_lotSuccessFn(data, status, headers, config) {
        console.log('Successful POST to /api/v1/monitor/edit_rate!');
      }
      function create_lotErrorFn(data, status, headers, config) {
        console.error('FAILED to POST to /api/v1/monitor/edit_rate!');
      }
    }

  }
})();

// NOTE : add old_lot_name and new_lot_name for Dans soon to come changes
