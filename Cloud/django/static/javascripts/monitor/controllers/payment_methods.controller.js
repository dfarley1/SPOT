(function () {
    'use strict';

    angular
        .module('sdpspot.monitor.controllers')
        .controller('PaymentMethodsController', PaymentMethodsController);

    PaymentMethodsController.$inject = ['$location', '$scope', '$http', 'Monitor', 'ngDialog'];

    function PaymentMethodsController($location, $scope, $http, Monitor, ngDialog) {
        var vm = this;
        vm.add_method = add_method;
        vm.remove_method = remove_method;
        vm.save_methods = save_methods;

        vm.payment_methods = [{
            id: '1',
            name: 'help',
            purchase_price: '0.00',
            rate_modifier: '0.0'
        }, {
            id: '2',
            name: 'me',
            purchase_price: '3.00',
            rate_modifier: '3.0'
        }];

        get_methods();

        function get_methods() {
            $http.get('/api/v1/monitor/payment_methods/',).then(get_methods_OK, get_methods_ERR);

            function get_methods_OK(data, status, headers, config) {
                console.log(data.data);
                vm.payment_methods = data.data;
            }
            function get_methods_ERR(data, status, headers, config) {
                console.log('monitor.controller: get_methods ERROR');
            }
        }

        function add_method() {
            vm.payment_methods.push({
                id: vm.payment_methods.length+1,
                name: 'New Payment Method',
                purchase_price: '50.00',
                rate_modifier: '0.0'
            });
        }

        function remove_method(index) {
            console.log('removing method: ' + index);
            vm.payment_methods.splice(index, 1);
        }

        function save_methods() {
            $http.post('/api/v1/monitor/payment_methods/', vm.payment_methods)
                .then(post_methods_OK, post_methods_ERR);

            function post_methods_OK(data, status, headers, config) {
                console.log('payment_methods.controller: SAVED')
                get_methods();
            }
            function post_methods_ERR(data, status, headers, config) {
                console.log('payment_methods.controller: post_methods ERROR');
                get_methods();
            }
        }
    }
})();
