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
		}).when('/test', {
      controller: 'MonitorController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/monitor/monitor.html'
    }).when('/home', {
			controller: 'MapController',
			controllerAs: 'vm',
			templateUrl: '/static/templates/home.html'
    }).when('/monitor', {
			controller: 'MonitorController',
			controllerAs: 'vm',
			templateUrl: 'monitor/templates/monitor.html'
		}).when('/mobile', {
      controller: 'MobileController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/mobile/insert.html'
    }).when('/', {
      controller: 'MonitorController',
      controllerAs: 'vm',
      templateUrl: 'monitor/templates/monitor.html'
    })
	// .otherwise('/', {
	// 		controller: 'MapController',
	// 		controllerAs: 'vm',
	// 		templateUrl: '/static/templates/home.html'});
	}
})();
