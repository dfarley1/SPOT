(function () {
    'use strict';

    angular
        .module('sdpspot.user.controllers')
        .controller('UserController', UserController);

    UserController.$inject = ['$location', '$scope', '$http', 'User'];

    function UserController($location, $scope, $http, User) {
        // Variables
        var vm = this; 
        vm.curr_spot;
        vm.curr_status;
        vm.events;
        
        vm.curr_spot_text;
        //Functions
        vm.get_spot = get_spot;
        vm.get_status = get_status;
        vm.get_events = get_events;
        
        load_stuff();
        function load_stuff() {
            get_spot();
            get_status();
        }

        function get_spot() {
            $http.get('/api/v1/user/get_spot/',).then(get_spot_OK, get_spot_ERR);

            function get_spot_OK(data, status, headers, config) {
                console.log(data.data);
                vm.curr_spot = data.data;
                if (vm.curr_spot.occ_status > 0) {
                    vm.curr_spot_text = 'You are parked at SPOT';
                } else {
                    vm.curr_spot_text = 'You were last parked in SPOT';
                 }
            }
            function get_spot_ERR(data, status, headers, config) {
                console.log('user.controller: get_spot ERROR');
            }
        }

        function get_status() {
            $http.get('/api/v1/user/get_status/',).then(get_status_OK, get_status_ERR);

            function get_status_OK(data, status, headers, config) {
                console.log(data.data);
                vm.curr_status = data.data;
            }
            function get_status_ERR(data, status, headers, config) {
                console.log('user.controller: get_status ERROR');
            }
        }


        function get_events() {
            $http.get('/api/v1/user/get_events/',).then(get_OK, get_ERR);
            
            function get_OK(data, status, headers, config) {
                console.log(data.data);
                vm.events = data.data;
            }
            function get_ERR(data, status, headers, config) {
                console.log('user.controller: get_events ERROR');
            }
        }

    }

})();
