(function () {
    'use strict';

    angular
        .module('sdpspot.monitor.controllers')
        .controller('StructuresController', StructuresController);

    StructuresController.$inject = ['$location', '$scope', '$http', 'Monitor', 'ngDialog'];

    function StructuresController($location, $scope, $http, Monitor, ngDialog) {
        var vm = this;
        $scope.Math = window.Math;
        
        vm.get_rates = get_rates;
        vm.post_rates = post_rates;
        vm.save_rates = save_rates;

        vm.lot = 'West Core';
        vm.section = 'Level 1'; 
        vm.rates = [];

        get_rates()

        function save_rates() {
            console.log(vm.rates);
            post_rates();
        }

        function get_rates() {
            $http.get('/api/v1/monitor/edit_rates/', {params:{lot: vm.lot, section: vm.section}})
                .then(get_rates_OK, get_rates_ERR);

            function get_rates_OK(data, status, headers, config) {
                console.log(data.data);
                vm.rates = data.data;
            }
            function get_rates_ERR(data, status, headers, config) {
                console.log('structures_controller: get_rates ERROR');
            }
        }

        function post_rates() {
            $http.post('/api/v1/monitor/edit_rates/', {
                lot: vm.lot,
                section: vm.section,
                rates: vm.rates
            }).then(post_rates_OK, post_rates_ERR);

            function post_rates_OK(data, status, headers, config) {
                console.log('strctures controller: rates SAVED')
                get_rates();
            }
            function post_rates_ERR(data, status, headers, config) {
                console.log('structures controller: post_rates ERROR');
                get_rates();
            }
        }
    }
})();
