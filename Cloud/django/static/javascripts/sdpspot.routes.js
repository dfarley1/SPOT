(function () {
    'use strict';

    angular
        .module('sdpspot.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    /**
    * @name config
    * @desc Define valid application routes
    */
    function config($routeProvider) {
        $routeProvider.when('/register', {
            controller: 'RegisterController', 
            controllerAs: 'vm',
            templateUrl: '/static/templates/authentication/register.html'
        }).when('/login', {
            controller: 'LoginController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/authentication/login.html'
        }).when('/Lots', {
            controller: 'MonitorController',
            controllerAs: 'vm',
            templateUrl: 'static/templates/monitor/lots.html'
        }).when('/monitor', {
            controller: 'MonitorController',
            controllerAs: 'vm',
            templateUrl: 'monitor/templates/monitor.html'
        }).when('/payment_methods', {
            controller: 'PaymentMethodsController',
            controllerAs: 'vm',
            templateUrl: 'monitor/templates/payment_methods.html'
        }).when('/user', {
            controller: 'UserController',
            controllerAs: 'vm',
            templateUrl: 'user/templates/user.html'
        }).when('/edit_structures', {
            controller: 'StructuresController',
            controllerAs: 'vm',
            templateUrl: 'monitor/templates/edit_structures.html'
        })
        // .otherwise('/', {
        //     controller: 'MonitorController',
        //     controllerAs: 'vm',
        //     templateUrl: 'monitor/templates/monitor.html'
        // })
    }
})();
